#!/usr/local/bin/python
# This generates the results and score for the user
# Daryl Herzmann 5-24-99
# 5-25-99 : Gonna finish this bad boy off...
# UPDATED 6-1-99: Got it going at the correct database
# UPDATED 7-14-99: Fixed a typo

from pgext import *
import cgi, style, time, string, mailresults

mydb2 = connect('archresults')
admindb = connect('archadmin')

def get_results(std_date):
#	table_name = string.lower(time.strftime("%b%d%Y", now_tuple))
	results = mydb2.query("Select * from t"+std_date+"")
	results = results.getresult()
        results.sort()
	return results

def list_results(results, state):
	flag = 0
        style.table_setter("400","State","Severe Weather type","During time period")
	print '<caption><H3>Severe Weather Events</H3></caption>'
        for i in range(len(results)):
                state2 = results[i][0]
                type = results[i][1]
                time = results[i][2]
                if state == state2:
                        print '<tr><td><blink>'+state2+'</blink></td>'
                        flag = 1
                else:
                        print '<tr><td>'+state2+'</td>'
                if type == "T":
                        print '<td><B>Tornado</B></td>'
                elif type == "H":
                        print '<td>Hail</td>'
                elif type == "R":
                        print '<td>3"+ Rainfall</td>'
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
        return flag

def realtime(time):
        if time == "1":
                return "12-3 PM (CDT)"
        elif time == "2":
                return "3-6 PM (CDT)"
        elif time == "3":
                return "6-9 PM (CDT)"
        elif time == "4":
                return "9 PM - Midnight (CDT)"


def Main():
	form = cgi.FormContent()
	secs = float(form["secs"][0])
	key = form["key"][0]
	answers = admindb.query("SELECT h,r,t,state,etime from sessions WHERE key = '"+str(key)+"' ").getresult()
	
	hail = answers[0][0]	
	rain = answers[0][1]
	tornado = answers[0][2]
	state = answers[0][3]
	etime = answers[0][4]

	now_tuple = time.localtime(secs)
	str_date = time.strftime("%B %d, %Y", now_tuple)
	std_date = time.strftime("%Y_%m_%d", now_tuple)
	table_name = string.lower(time.strftime("%Y_%m_%d", now_tuple))

	results = get_results(std_date)
	
	style.header("Forecast Excercise Results", "white")
	print '<TABLE WIDTH="100%" ALIGN="CENTER">'
	print '<caption><H1>Forecast Results for '+str_date+'</H1></caption>'

	print '<TR>'
	print '<TD valign="top">'
	state_flag = list_results(results, state)
	print '</TD>'

	print '<TD valign="top">'
	print '<H3>Graphical Represenation</H3>'
	print '<img src="/archivewx/data/'+std_date+'/svr'+std_date+'.gif">'
	print '<H3>Your forecast Score</H3>'	

	time_point = 0
	state_point = 0
	hail_point = 0
	rain_point = 0
	tornado_point = 0
	hail_txt = "No"
	tornado_txt = "No"
	rain_txt = "No"
	mytornado = "No"
	myrain = "No"
	myhail = "No"

	if state_flag != 1:
		total_score = 0
	else:
		state_point = 10
		ttimes = mydb2.query("Select date from t"+table_name+" where state ~~ '"+state+"'")
	        ttimes = ttimes.getresult()
        	for ttime in ttimes:
                	if ttime[0] == etime:
                	        time_point = 10
	if time_point == 10:
		types = mydb2.query("Select severe from t"+table_name+" where state ~~ '"+state+"'")
		types = types.getresult()
		for type in types:
			if type[0] == "H":
				hail_txt = "Yes"
			elif type[0] == "R":
				rain_txt = "Yes"
			elif type[0] == "T":
				tornado_txt = "Yes"
	if rain == "R":
		myrain = "Yes"
	if tornado == "T":
		mytornado = "Yes"
	if hail == "H":
		myhail = "Yes"
	if state_point == 10:
		if myhail == hail_txt:
			hail_point = 10
		if mytornado == tornado_txt:
			tornado_point = 10
		if myrain == rain_txt:
			rain_point = 10

	print '<TABLE align="center">'
	print '<TR><TH></TH><TH>Predicted:</TH><TH>Actual:</TH><TH>Points:</TH></TR>'
	print '<TR><TH>State:</TH><TD>'+state+'</TD><TD>'+state+'</TD><TD>',state_point,'</TD></TR>'
	print '<TR><TH>Time Period:</TH><TD>'+realtime(etime)+'</TD><TD>',realtime(etime),'</TD><TD>',time_point,'</TD></TR>'
	print '<TR><TH>Tornado Occurance:</TH><TD>'+mytornado+'</TD><TD>'+tornado_txt+'</TD><TD>',tornado_point,'</TD></TR>'
	print '<TR><TH>Hail Event:</TH><TD>'+myhail+'</TD><TD>'+hail_txt+'</TD><TD>',hail_point,'</TD></TR>'
	print '<TR><TH>Heavy Rainfall (3+ in):</TH><TD>'+myrain+'</TD><TD>'+rain_txt+'</TD><TD>',rain_point,'</TD></TR>'
	print '</TABLE>'

	total_score = rain_point + tornado_point + time_point + state_point + hail_point
	print '<U><H3>Your total score is ',total_score,' out of 50</H3></U>'

	print '<BR><a href="http://www.pals.iastate.edu">PALS Homepage</a><BR>'
	print '<a href="http://www.pals.iastate.edu/mt206/">Do another excercise!!</a><BR>'
	print '</TD></TR>'

	print '</TABLE></BODY></HTML>'

	mailresults.Main(secs, key)

Main()
