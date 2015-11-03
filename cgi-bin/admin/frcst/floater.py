#!/usr/local/bin/python
# This program simply asks for a floater city to add to the excercise...
# Daryl Herzmann 8-30-99

import pg, time, std_form, style, cgi

casesdb = pg.connect('frcst')

def previous(class_name):
	print '<PRE>'
	print 'Previous Floater cities for '+class_name
	select = casesdb.query("SELECT * from cases where class_name = '"+class_name+"' ").getresult()
	for i in range(len(select)):
		print select[i][0],'-',select[i][1],'-',select[i][2],'  ---- ',select[i][3]
	print '</PRE>'


def Main():
	form = cgi.FormContent()
	class_name = form["class_name"][0]

	style.header("Adding a floater city", "white")
	style.std_top("Adding a Floater City to the system")

	print '<P><b>Please</b>, fill out this form carefully.<BR>'
	print ' Note: Select the day that the forecast is for, not \
	the day that the forecast is made on. <BR>'

	print '<form method="POST" action="enter_floater.py">'
	print '<input type="hidden" value="'+class_name+'" name="class_name">'

	print '<TABLE><TR><TD>'
	print '<TABLE>'
	print '<TR><TH>Select Year:</TH><TH>Select Month:</TH><TH>Select Day:</TH></TR>'

	print '<TR><TD><SELECT name="yeer">'
	print '<option value="1999">1999'
	print '<option value="2000">2000'
	print '</SELECT></TD>'

	print '<TD>'
	std_form.months()
	print '</TD>'

	print '<TD>'
	std_form.days()
	print '</TD></TR></TABLE>'

	print '<H3>Input the station code:</H3>'
	print '<input type="text" size="20" MAXLENGTH="50" name="code">'
	print '<H3>Input the station name:</H3>'
	print '<input type="text" MAXLENGTH="50" name="station">'

	print '<BR><BR><BR>'
	print 'You are entering the floater city for '+class_name+'<BR>'
	print '<input type="submit" value="Add this floater city">'

	print '</TD><TD>'
	previous(class_name)
	print '</TD></TR></TABLE>'


	style.std_bot()
Main()
