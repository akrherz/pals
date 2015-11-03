#!/usr/local/bin/python
# This program pulls in a case_num value and then gives user the option about what to do...
# Daryl Herzmannn 9-13-99

import cgi, time, style

def win_times(title):
        print '<SELECT name="'+title+'">'
        print '<option value="0">0 Z'
	print '<option value="3">3 Z'
	print '<option value="6">6 Z'
	print '<option value="9">9 Z'
	print '<option value="12">12 Z'
	print '<option value="15">15 Z'
	print '<option value="18">18 Z'
	print '<option value="21">21 Z'
        print '</SELECT>'

def sum_times(title):
        print '<SELECT name="'+title+'">'
        print '<option value="0">0 Z'
        print '<option value="1">1 Z'
        print '<option value="2">2 Z'
	print '<option value="3">3 Z'
	print '<option value="4">4 Z'
	print '<option value="5">5 Z'
	print '<option value="6">6 Z'
	print '<option value="7">7 Z'
	print '<option value="8">8 Z'
	print '<option value="9">9 Z'
	print '<option value="10">10 Z'
	print '<option value="11">11 Z'
	print '<option value="12">12 Z'
	print '<option value="13">13 Z'
	print '<option value="14">14 Z'
	print '<option value="15">15 Z'
	print '<option value="16">16 Z'
	print '<option value="17">17 Z'
	print '<option value="18">18 Z'
	print '<option value="19">19 Z'
	print '<option value="20">20 Z'
	print '<option value="21">21 Z'
	print '<option value="22">22 Z'
	print '<option value="23">23 Z'
        print '</SELECT>'

def months(title):
        print '<SELECT name="'+title+'">'
	print '<option value="1">January'
	print '<option value="2">Feburary'
	print '<option value="3">March'
	print '<option value="4">April'
        print '<option value="5">May'
	print '<option value="6">June'
	print '<option value="7">July'
	print '<option value="8">August'
	print '<option value="9">September'
        print '<option value="10">October'
	print '<option value="11">November'
	print '<option value="12">December'
	print '</SELECT>'


def Main():
	style.header("Add a case to the system", "white")

	form = cgi.FormContent()
	caseType = form["caseType"][0]

	style.std_top("Add a case to the system")

	print '<form method="POST" action="addDay.py">'
	print '<input type="hidden" name="caseType" value="'+caseType+'">'
	print '<H3>Fill out the Form to add a case to the system:</H3>'

	print '<TABLE width="500">'
	print '<TR><TH></TH><TH>Year (4 digits):</TH><TH>Month:</TH><TH>Day:</TH><TH>Ztime:</TH></TR>'

	print '<TR><TH>Start At:</TH>'
	print '<TH><input type="text" MAXLENGTH="4" SIZE="5" name="start_yeer" value="20"></TH>'
	print '<TH>'
	months("start_month")
	print '</TH>'
	print '<TH><input type="text" name="start_day" maxlength="2" size="2"></TH>'
	print '<TH>'
	if caseType == "w":
		win_times("start_ztime")
	else:
		sum_times("start_ztime")
	print '</TH></TR>'

	print '<TR><TH>End At:</TH>'
	print '<TH><input type="text" MAXLENGTH="4" SIZE="5" name="end_yeer" value="20"></TH>'
	print '<TH>'
	months("end_month")
	print '</TH>'
	print '<TH><input type="text" name="end_day" maxlength="2" size="2"></TH>'
	print '<TH>'
	if caseType == "w":
		win_times("end_ztime")
	else:
		sum_times("end_ztime")
	print '</TH></TR></TABLE>'

	print '<input type="SUBMIT">'
	print '<input type="RESET">'

	print '</form>'

	style.std_bot()	

Main()
