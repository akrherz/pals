#!/usr/local/bin/python
# The Script that will do all grading 
# Daryl Herzmann 7/27/98

from cgi import *
import style, pgext

mydbase = pgext.connect("archwx")


def table():
	results = mydbase.query("Select * from jun1898")
	results = results.getresult()
	results.sort()	

	for i in range(len(results)):
		state = results[i][0]
		type = results[i][1]
		time = results[i][2]
		print '<tr><td>'+state+'</td>'
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


def body():
	print '<a href="javascript:history.go(-1)">GO BACK</A><BR>'
#	print '<a href="answers.py">View the Answers</a><BR>'
#	print '<a href="/archivewx/jun181998/data1pm.html">Go to 1 PM</a>'
	bot()

def bot():
	style.std_bot()

def Main():
	style.header("7/18/98 Answers","/images/ISU_bkgrnd.gif")
	style.std_top("June 18, 1998 Answers")
	style.table_setter("400","State","Severe Weather type","During time period")
	table()
	body()	
	sys.exit(0)
Main()
