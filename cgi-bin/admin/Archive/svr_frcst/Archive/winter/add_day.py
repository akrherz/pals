#!/usr/local/bin/python
# This program will prompt for a new case to add to the system
# Daryl Herzmann

import pg, std_form, style, time

mydb = pg.connect('archadmin')

def ztimes(title):
	print '<SELECT name="'+title+'">'
	print '<option value="0">0<option value="3">3<option value="6">6<option value="9">9<option value="12">12<option value="15">15<option value="18">18<option value="21">21'
	print '</SELECT>'

def oldcases():
	print '<H3>Allready created cases</H3>'
	print '<TABLE border="0" WIDTH="100%">'
	print '<TR><TH><font color="blue">Case Number:</TH><TH><font color="green">Start Time:</TH><TH><font color="red">End Time:</TH></TR>'

	entries = mydb.query("SELECT * from winter_cases").getresult()

	for i in range(len(entries)):
		casenum = str(entries[i][0])
		start_secs = float(entries[i][1])
		end_secs = float(entries[i][2])

		start_tuple = time.localtime(start_secs)
		end_tuple = time.localtime(end_secs)

		nice_start = time.strftime("%b %d, %Y - %I:%M %p", start_tuple)
		nice_end = time.strftime("%b %d, %Y - %I:%M %p", end_tuple)

		print '<TR><TH><font color="blue">'+casenum+'</TH><TH><font color="green">'+nice_start+'</TH><TH><font color="red">'+nice_end+'</TH></TR>'

	print '</TABLE>'

def findcase():
	entries = mydb.query("SELECT * from winter_cases").getresult()

	return int(entries[-1][0]) +1


def Main():
	style.header("Add a Winter weather case", "white")

	newcase = findcase()

	oldcases()

	print '<form method="POST" action="enter_day.py">'

	print '<input type="hidden" name="casenum" value="'+str(newcase)+'">'

	print '<H3>Enter the date of when you want this excercise to start:</H3>'
#	print '<BR>Pick A Time:'
#	ztimes("start_hour")

	print '<BR>Enter Day:'
	print '<input type="text" name="start_day" maxlength="2" size="2">'

	print '<BR>Select Month:'
	print '<SELECT name="start_month"><option value="1">January<option value="2">Feburary<option value="3">March<option value="4">April'
	print '<option value="5">May<option value="6">June<option value="7">July<option value="8">August<option value="9">September'
	print '<option value="10">October<option value="11">November<option value="12">December</SELECT>'

	print '<BR>Enter year (4 digits please):'
	print '<input name="start_year" type="text" maxlength="4" size="4">'

	print '<BR><BR>'

	print '<H3>Enter the last day of this winter forecasting case:</H3>'
#	print '<BR>Pick A Time:'
#	ztimes("end_hour")

	print '<BR>Enter Day:'
	print '<input type="text" name="end_day" maxlength="2" size="2">'

	print '<BR>Select Month:'
	print '<SELECT name="end_month"><option value="1">January<option value="2">Feburary<option value="3">March<option value="4">April'
	print '<option value="5">May<option value="6">June<option value="7">July<option value="8">August<option value="9">September'
	print '<option value="10">October<option value="11">November<option value="12">December</SELECT>'

	print '<BR>Enter year (4 digits please):'
	print '<input name="end_year" type="text" maxlength="4" size="4">'

	print '<BR><BR>'

	print '<input type="SUBMIT" value="Submit this case">'

	style.std_bot()

Main()
