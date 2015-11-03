#!/usr/local/bin/python
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
                        print '<td>3"+ Rainfall</td>'
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


def grade_winter(state, six_guess, twelve_guess, freeze_guess, caseNum):
	res_list = mydb.query("SELECT type from answerkey WHERE caseNum = '"+caseNum+"' and state = '"+state+"' ").getresult() 

	six_txt, twelve_txt, freeze_txt = "No", "No", "No"
	six_pts, twelve_pts, freeze_pts = 0, 0, 0
	six = 0
	twelve = 0
	freeze = 0

	for res in res_list:
		if res[0] == "S":
			six_txt = "Yes"
			if six_guess == res[0]:
				six = 1
				six_pts = 10
			else:
				six = 1
				six_pts = 0
		if res[0] == "T":
			twelve_txt = "Yes"
			if twelve_guess == res[0]:
				twelve = 1
				twelve_pts = 10
			else:
				twelve = 1
				twelve_pts = 0
		if res[0] == "F":
			freeze_txt = "Yes"
			if freeze_guess == res[0]:
				freeze = 1
				freeze_pts = 10
			else:
				freeze = 1
				freeze_pts = 0

	if not six:
		if six_guess == "N":
			six_pts = 10

	if not twelve:
		if twelve_guess == "N":
			twelve_pts = 10

	if not freeze:
		if freeze_guess == "N":
			freeze_pts = 10

	return six_txt, twelve_txt, freeze_txt, six_pts, twelve_pts, freeze_pts


def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()


	answers = mydb.query("SELECT * from users WHERE userKey = '"+str(userKey)+"' ").getresult()
	
	state = answers[0][3]	
	etime = answers[0][4]
	if caseNum[0] == "s":
		torn_txt, hail_txt, rain_txt = "No", "No", "No"
		rain_guess = answers[0][5]
		if rain_guess == "R":
			rain_guess_txt = "Yes"
		else:
			rain_guess_txt = "No"
		hail_guess = answers[0][6]
		if hail_guess == "H":
			hail_guess_txt = "Yes"
		else:
			hail_guess_txt = "No"
		torn_guess = answers[0][7]
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
		six_txt, twelve_txt, freeze_txt = "No", "No", "No"
		six_guess = answers[0][5]
		if six_guess == "S":
			six_guess_txt = "Yes"
		else:
			six_guess_txt = "No"
		twelve_guess = answers[0][6]
		if twelve_guess == "T":
			twelve_guess_txt = "Yes"
		else:
			twelve_guess_txt = "No"
		freeze_guess = answers[0][7]
		if freeze_guess == "F":
			freeze_guess_txt = "Yes"
		else:
			freeze_guess_txt = "No"

		state_pts = grade_state(state, caseNum)
		six_pts, twelve_pts, freeze_pts = 0,0,0
		if state_pts > 0:
			six_txt, twelve_txt, freeze_txt, six_pts, twelve_pts, freeze_pts = grade_winter(state, six_guess, twelve_guess, freeze_guess, caseNum)


	bonus_pts = answers[0][9]

	results = get_results(caseNum)

	style.header("Forecast Excercise Results", "white")	
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
		print '<TR><TH>Rain:</TH><TH>'+rain_guess_txt+'</TH><TH>'+rain_txt+'</TH><TH>',rain_pts,'</TH></TR>'
		print '<TR><TH>Hail:</TH><TH>'+hail_guess_txt+'</TH><TH>'+hail_txt+'</TH><TH>',hail_pts,'</TH></TR>'
		try:
			total = etime_pts + state_pts + torn_pts + rain_pts + hail_pts + int(bonus_pts)
		except:
			total = etime_pts + state_pts + torn_pts + rain_pts + hail_pts

	if caseNum[0] == "w":
		print '<TR><TH>Six Inch Snowfall:</TH><TH>'+six_guess_txt+'</TH><TH>'+six_txt+'</TH><TH>',six_pts,'</TH></TR>'
		print '<TR><TH>Twelve Inch Snowfall:</TH><TH>'+twelve_guess_txt+'</TH><TH>'+twelve_txt+'</TH><TH>',twelve_pts,'</TH></TR>'
		print '<TR><TH>Freezing Rain Event:</TH><TH>'+freeze_guess_txt+'</TH><TH>'+freeze_txt+'</TH><TH>',freeze_pts,'</TH></TR>'
		try:
			total = state_pts + six_pts + twelve_pts + freeze_pts + int(bonus_pts)
		except:
			total = state_pts + six_pts + twelve_pts + freeze_pts
	print '</TABLE>'	

	print '<BR><H3>Bonus Points:</H3>', bonus_pts , '<BR><HR>'
	print '<BR><H3>Total Points:</H3>', total , '<BR>'

	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

	print '<BR><a href="/svr_frcst/">Forecasting Exercise Homepage</a>'
	print '<BR><a href="http://www.pals.iastate.edu">PALS Homepage</a><BR>'
	print '</TD></TR>'

	print '</TABLE></BODY></HTML>'

#	mailresults.Main(secs, key)

	functs.updateUser(userKey, "userkey", "10")
	sys.exit(0)
