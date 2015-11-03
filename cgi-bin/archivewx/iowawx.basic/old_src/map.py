#!/usr/local/bin/python
# Program generates a page asking for birthdate
# Daryl Herzmann 8/1/98

import sys
from cgi import *
from pg import *

mydb2 = connect('supp')

form = FormContent()
stat = form["stat"][0]

def days(day):
	print '<option value="'+day+'">'+day+'\n'

def month(mon):
	print '<Option value="'+mon+'">'+mon+'\n'

def lookup(station): 
        query = mydb2.query("Select * from stations where code = '"+station+"'")  
	query = query.getresult() 
        station = query[0][1]
	ques = query[0][2]
        return station, ques

def Main():
	station, ques = lookup(stat)
	print 'Content-type: text/html\n\n'
	print '<HTML><HEAD><TITLE>Historical Data from '+station+'</TITLE>'
	print '<meta http-equiv="Refresh" content="60; URL=/index.html"></head>'
	print '<body bgcolor="#FFF0FF">'
	print '<CENTER>'
	print '<form method="post" action="result.py">'
	print '<input type="hidden" value="'+stat+'" name="stat">'
	print '<input type="hidden" value="'+station+'" name="station">'	
	if ques == "y":
		dates = "1900 to 1998"
	else: dates = "1951 to 1998"
	print '<table width="1250">'
	print '<tr><th colspan="2" bgcolor="blue"><font color="white" size="7"><BR>'
	print '<H2>Weather Archive of '+station+', Iowa<BR> from '+dates+'</font></H2>'

	print '<tr><th align="right"><font size="7">Select Month:</th><td width="400">'
	print '<Select name="month">'
	print '<option value="1">January\n'
	print '<option value="2">February\n'
	print '<option value="3">March\n'
	print '<option value="4">April\n'
	print '<option value="5">May\n'
	print '<option value="6">June\n'
	print '<option value="7">July\n'
	print '<option value="8">August\n'
	print '<option value="9">September\n'
	print '<option value="10">October\n'
	print '<option value="11">November\n'
	print '<option value="12">December\n'
	print '</SELECT></td></tr><tr>'
	print '<th align="right"><font size="8">Select Day:</font></th><td>'
	print '<Select name="day">'
	for i in range(31):
		day = str(i+(1))
		days(day)
	print '</SELECT></td></tr><tr>'
	print '<th align="right"><font size="7">Enter a year between '+dates+':</font></th><td>'
	print '<input name="year" type="text" size="10">'
	print '<spacer type="horizontal" size="100">'
	print '</td></tr><tr>'
	print '<th colspan="2">'
	print '<input type="submit" value="Give me the Weather for '+station+' on this day">'
	print '</th></tr></table>'
	print '</form>'
	print '<HR></center>'
	print '<H1>Select the month and day for the request and then enter the year.</H1>'
	print '</body></html>'
Main()
