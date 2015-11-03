#!/usr/local/bin/python
# The Script that will do all grading 
# Daryl Herzmann 7/30/98

from cgi import *
import style, pgext, os, posix

mydbase = pgext.connect("archanswers")

form = FormContent() 
state = form["state"][0]
time = form["time"][0]


def table(today): 
        results = mydbase.query("Select * from "+today+"") 
        results = results.getresult() 
        results.sort()
	for i in range(len(results)): 
                state2 = results[i][0]
                type = results[i][1]
                time = results[i][2]
                if state == state2:
			print '<tr><td><blink>'+state2+'</blink></td>'
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



def Main():
	form = FormContent()
	if time == "1": realtime = "12-3 PM (CDT)"
	if time == "2": realtime = "3-6 PM (CDT)"
	if time == "3": realtime = "6-9 PM (CDT)"
	if time == "4": realtime = "9-Midnight PM (CDT)"
	tornado = form["T"][0]
	today = form["day"][0]
	realtornado = "No"
	realrain = "No" 
	realhail = "No"
        if tornado == "T": realtornado = "Yes"
	rain = form["R"][0]
	if rain == "R": realrain = "Yes"
        hail = form["H"][0]
	if hail == "H": realhail = "Yes"
	month_name = form["month_name"][0]		

	style.header("Your Score for "+today,"/images/ISU_bkgrnd.gif") 
        print '<center><H1>'+month_name+' '+today[3:5]+', '+today[5:]+' forecast results</H1></center>'

	results = mydbase.query("Select * from "+today+" where state = '"+state+"' AND date = '"+time+"'") 
        results = results.getresult()
	
	statepoint = "-5"
	timepoint = "-5"
	actualtornado = "No"
	actualhail = "No"
	actualrain = "No"
	for i in range(len(results)):
		this = results[i][1]
		that = results[i][0]
		whatnot = results[i][2]
		if this == "T": actualtornado = "Yes"
		if this == "H": actualhail = "Yes"	
		if this == "R": actualrain = "Yes"
		if that == state: statepoint = "10"
		if whatnot == time: timepoint = "10"


	tornpoint = "-5"
	hailpoint = "-5"
	rainpoint = "-5"
	if realtornado == actualtornado: tornpoint = "10"
	if realhail == actualhail: hailpoint = "10"
	if realrain == actualrain: rainpoint = "10"

	print '<table><tr><td>'

	print '<center><H3>Severe Weather Reports:</H3></center>'

	style.table_setter("400","State","Severe Weather type","During time period")
	table(today)

	print '</td><td valign="top">'
	print '<center><H3>Here is a picture of what happened:</H3></center>'
	print '<img src="/archivewx/data_days/'+today+'/map.gif">'
	
	print '<center><H3>Here is a what you predicted:</H3></center>'
	style.table_setter("400"," ","PREDICTED","ACTUAL","POINTS") 
        print '<tr><th>State:</th><td>'
        print state+'</td><td>'+state+'</td><td>'+statepoint+'</td></tr>'
        print '<tr><th>Time:</th><td>'
        print realtime+'</td><td>'+realtime+'</td><td>'+timepoint+'</td></tr>'
        print '<tr><th>Tornado??:</th><td>'
        print realtornado+'</td><td>'+actualtornado+'</td>'
	print '<td>'+tornpoint+'</td></tr>'
        print '<tr><th>Hail??:</th><td>'
        print realhail+'</td><td>'+actualhail+'</td><td>'
	print hailpoint+'</td></tr>'
        print '<tr><th>Rain??:</th><td>'
        print realrain+'</td><td>'+actualrain+'</td><td>'
	print rainpoint+'</td></tr>'
        print '</table>'

	total = int(tornpoint)+int(hailpoint)+int(rainpoint)+int(statepoint)+int(timepoint)

	print '<center><H3>Here is your score:</H3></center>'
	print '<center><H1>',total,'</H1></center>'

	print '</td></tr></table>'
	style.std_bot()

Main()
