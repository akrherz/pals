#!/usr/bin/python
# This generates the results and score for the user
# Revamped 9-21-99: To grade all users...
# 9-23-99: Lets get this working...

import cgi, style, time, string, pg, os, sys, functs

mydb = pg.connect('severe2', 'localhost', 5432)

def get_results(caseNum):
#	table_name = string.lower(time.strftime("%b%d%Y", now_tuple))
	results = mydb.query("select state, type, etime from answerkey WHERE caseNum = '"+caseNum+"'")
	results = results.getresult()
        results.sort()
	return results

def list_results(results, state, caseNum):
	if caseNum[0] == "s":
 	       style.table_setter("400","State","Severe Weather type","During time period")
	else:
 	       style.table_setter("400","State","Severe Weather type")

        for i in range(len(results)):
                state2 = results[i][0]
                type = results[i][1]
                time = results[i][2]
                if state == state2:
                        print '<tr><td><blink>'+state2+'</blink></td>'
                else:
                        print '<tr><td>'+state2+'</td>'
                if type == "T" and caseNum[0] == "s":
                        print '<td><B>Tornado</B></td>'
                elif type == "H":
                        print '<td>Hail</td>'
                elif type == "R":
                        print '<td>Flash Flooding</td>'
                elif type == "T":
                        print '<td>12"+ Snowfall</td>'
                elif type == "S":
                        print '<td>6"+ Snowfall</td>'
                elif type == "F":
                        print '<td>Freezing Rainfall Event</td>'
                elif type == "C":
                        print '<td>Dangerous Wind Chill Event</td>'
		if caseNum[0] == "s":
	                if time == "1":
	                        print '<td>12-3 PM (CDT)</td>'
	                elif time == "2":
	                        print '<td>3-6 PM (CDT)</td>'
	                elif time == "3":
	                        print '<td>6-9 PM (CDT)</td>'
	                elif time == "4":
	                        print '<td>9-Midnight PM (CDT)</td>'
                print '</tr>'
        print '</table>'

def realtime(time):
        if time == "1":
                return "12-3 PM (CDT)"
        elif time == "2":
                return "3-6 PM (CDT)"
        elif time == "3":
                return "6-9 PM (CDT)"
        elif time == "4":
                return "9 PM - Midnight (CDT)"

def grade_state(state, caseNum):
	states = mydb.query("SELECT * from answerkey WHERE state = '"+state+"' and caseNum = '"+caseNum+"' ").getresult()
	if len(states) > 0:
		return 10
	return 0

def grade_time(state, etime, caseNum):
	states = mydb.query("SELECT * from answerkey WHERE caseNum = '"+caseNum+"' and state = '"+state+"' and etime = '"+str(etime)+"' ").getresult()
	if len(states) > 0:
		return 10
	return 0


def grade_summer(state, torn_guess, hail_guess, rain_guess, caseNum, etime):
	res_list = mydb.query("SELECT type from answerkey WHERE caseNum = '"+caseNum+"' and state = '"+state+"' and etime = '"+str(etime)+"' ").getresult() 

	torn_txt, hail_txt, rain_txt = "No", "No", "No"
	torn_pts, hail_pts, rain_pts = 0, 0, 0
	torn = 0
	hail = 0
	rain = 0

	for res in res_list:
		if res[0] == "T":
			torn_txt = "Yes"
			if torn_guess == res[0]:
				torn = 1
				torn_pts = 10
			else:
				torn = 1
				torn_pts = 0
		if res[0] == "H":
			hail_txt = "Yes"
			if hail_guess == res[0]:
				hail = 1
				hail_pts = 10
			else:
				hail = 1
				hail_pts = 0
		if res[0] == "R":
			rain_txt = "Yes"
			if rain_guess == res[0]:
				rain = 1
				rain_pts = 10
			else:
				rain = 1
				rain_pts = 0

	if not torn:
		if torn_guess == "N":
			torn_pts = 10

	if not hail:
		if hail_guess == "N":
			hail_pts = 10

	if not rain:
		if rain_guess == "N":
			rain_pts = 10

	return torn_txt, hail_txt, rain_txt, torn_pts, hail_pts, rain_pts


def grade_winter(state, snowGuess,  freezeGuess, chillGuess, caseNum):
        res_list = mydb.query("SELECT type from answerkey WHERE caseNum = '"+caseNum+"' and state = '"+state+"' ").getresult() 

        snowTxt, freezeTxt, chillTxt = "No", "No", "No"
        snowPts, freezePts, chillPts = 0, 0, 0
        
        snow = 0
        freeze = 0
        chill = 0

        for res in res_list:
                if res[0] == "S":
                        snowTxt = "6-12 in"
                        if snowGuess == "S":
                                snow = 1
                                snowPts = 10
                        else:
                                snow = 1

                elif res[0] == "T":
                        snowTxt = "12+ in"
                        if snowGuess == "T":
                                snow = 1
                                snowPts = 10
                        else:
                                snow = 1
                
                elif res[0] == "F":
                        freezeTxt = "Yes"
                        if freezeGuess == "F":
                                freeze = 1
                                freezePts = 10
                        else:
                                freeze = 1
                                
                if res[0] == "C":
                        chillTxt = "Yes"
                        if chillGuess == "C":
                                chill = 1
                                chillPts = 10
                        else:
                                chill = 1
        if not snow:
                if snowGuess == "N":
                        snowPts = 10

        if not freeze:
                if freezeGuess == "N":
                        freezePts = 10

        if not chill:
                if chillGuess == "N":
                        chillPts = 10

        return snowTxt, freezeTxt, chillTxt, snowPts, freezePts, chillPts

def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()


	answers = mydb.query("SELECT * from users WHERE userKey = '"+str(userKey)+"' ").dictresult()
	
	state = answers[0]["state"]	
	etime = answers[0]["etime"]
	if caseNum[0] == "s":
		torn_txt, hail_txt, rain_txt = "No", "No", "No"
		rain_guess = answers[0]["optiona"]
		if rain_guess == "R":
			rain_guess_txt = "Yes"
		else:
			rain_guess_txt = "No"
		hail_guess = answers[0]["optionb"]
		if hail_guess == "H":
			hail_guess_txt = "Yes"
		else:
			hail_guess_txt = "No"
		torn_guess = answers[0]["optionc"]
		if torn_guess == "T":
			torn_guess_txt = "Yes"
		else:
			torn_guess_txt = "No"

		state_pts = grade_state(state, caseNum)
		etime_pts = grade_time(state, etime, caseNum)
		torn_pts, hail_pts, rain_pts = 0,0,0
		if state_pts > 0 and etime_pts > 0:
			torn_txt, hail_txt, rain_txt, torn_pts, hail_pts, rain_pts = grade_summer(state, torn_guess, hail_guess, rain_guess, caseNum, etime)

	else:
		snowTxt, freezeTxt, chillTxt = "No", "No", "No"
		snowGuessTxt = "No"
		freezeGuessTxt = "No"
		chillGuessTxt = "No"
                
		snowGuess = answers[0]["optiona"]
		if snowGuess == "S":
			snowGuessTxt = "6-12 in"
		elif snowGuess == "T":
			snowGuessTxt = "12+ in"

		freezeGuess = answers[0]["optionb"]
		if freezeGuess == "F":
			freezeGuessTxt = "Yes"
                

		chillGuess = answers[0]["optionc"]
		if chillGuess == "C":
			chillGuessTxt = "Yes"

		state_pts = grade_state(state, caseNum)
		snowPts, freezePts, chillPts = 0,0,0
		snowTxt, freezeTxt, chillText = "No", "No", "No"
		if state_pts > 0:
			snowTxt, freezeTxt, chillTxt, snowPts, freezePts, chillPts = grade_winter(state, snowGuess,  freezeGuess, chillGuess, caseNum)



	bonus_pts = answers[0]["bonuspoints"]

	results = get_results(caseNum)

	style.header("Forecast Exercise Results", "white")	
	print '<TABLE WIDTH="900" ALIGN="CENTER">'
	print '<caption><H1>Forecast Results for Case -> '+caseNum+'</H1></caption>'

	print '<TR>'
	print '<TD valign="top">'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Severe Weather Events:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	list_results(results, state, caseNum)
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'
	print '</TD>'

	print '<TD valign="top">'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Graphical Representation:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'

#	fileRef = "/home/httpd/html/archivewx/data/"+std_date+"/svr"+std_date+".gif"
#        if os.path.isfile(fileRef):
#                print '<img src="http://www.pals.iastate.edu/archivewx/data/'+std_date+'/svr'+std_date+'.gif">'
#        else:
#               print fileRef+" Not found<BR>"
#                print 'Visual image for today is not available'

	fileRef = "/home/httpd/html/archivewx/cases/results/"+caseNum+".gif"
        if os.path.isfile(fileRef):
                print '<img src="http://www.pals.iastate.edu/archivewx/cases/results/'+caseNum+'.gif">'
        else:
#               print fileRef+" Not found<BR>"
                print 'Visual image for today is not available'

	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'


	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Your Forecast Score:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'

	print '<TABLE>'
	print '<TR><TD></TD><TH>You Predicted:</TH><TH>Actual:</TH><TH>Points:</TH></TR>'
	print '<TR><TH>State:</TH><TH>'+state+'</TH><TH>'+state+'</TH><TH>',state_pts,'</TH></TR>'
	if caseNum[0] == "s":
		print '<TR><TH>Time:</TH>'
		print '<TH>'+realtime(str(etime))+'</TH>'
		print '<TH>'+realtime(str(etime))+'</TH>'
		print '<TH>'+str(etime_pts)+'</TH></TR>'
		print '<TR><TH>Tornado:</TH><TH>'+torn_guess_txt+'</TH><TH>'+torn_txt+'</TH><TH>',torn_pts,'</TH></TR>'
		print '<TR><TH>Flash Flooding:</TH><TH>'+rain_guess_txt+'</TH><TH>'+rain_txt+'</TH><TH>',rain_pts,'</TH></TR>'
		print '<TR><TH>Hail:</TH><TH>'+hail_guess_txt+'</TH><TH>'+hail_txt+'</TH><TH>',hail_pts,'</TH></TR>'
		try:
			total = etime_pts + state_pts + torn_pts + rain_pts + hail_pts + int(bonus_pts)
		except:
			total = etime_pts + state_pts + torn_pts + rain_pts + hail_pts

	if caseNum[0] == "w":
                print '<TR><TH>Snowfall:</TH><TH>'+snowGuessTxt+'</TH><TH>'+snowTxt+'</TH><TH>',snowPts,'</TH></TR>'
                print '<TR><TH>Freezing Rain Event:</TH><TH>'+freezeGuessTxt+'</TH><TH>'+freezeTxt+'</TH><TH>',freezePts,'</TH></TR>'
                print '<TR><TH>Wind Chill:</TH><TH>'+chillGuessTxt+'</TH><TH>'+chillTxt+'</TH><TH>',chillPts,'</TH></TR>'
                try:
                        total = state_pts + snowPts + freezePts + chillPts + int(bonus_pts)
                except:
                        total = state_pts + snowPts + freezePts + chillPts
		
	print '</TABLE>'	

	print '<BR><H3>Bonus Points (from Bonus Questions):</H3>', bonus_pts , '<BR><HR>'
	print '<BR><H3>Total Points:</H3>', total , '<BR>'

	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

	print '<BR><a href="/svr_frcst/">Forecasting Exercise Homepage</a>'
	print '<BR><a href="http://www.pals.iastate.edu">PALS Homepage</a>'
	print '<BR><a href="http://www.pals.iastate.edu/cgi-bin/severe2/basic/list.py">Work a new case</a>'
	print '</TD></TR>'

	print '</TABLE></BODY></HTML>'

#	mailresults.Main(secs, key)

	functs.updateUser(userKey, "userkey", "10")
	sys.exit(0)
