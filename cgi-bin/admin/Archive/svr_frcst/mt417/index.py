#!/usr/local/bin/python
# This program figures out what day they want to edit, or maybe add a new entry
# Daryl Herzmann 7-15-99

import style, time, std_form, pg

mydb = pg.connect("svr_frcst")
table_str = "questions_417"

def old_entries():
	entries = mydb.query("SELECT ticks from "+table_str).getresult()
	entries.sort()

	print '<form name="old" action="edit.py" method="POST">'
	print '<SELECT name="ticks">'
	for i in range(len(entries)):
		this_entry = float(entries[i][0])
		time_tuple = time.localtime(this_entry)
		date_str = time.strftime("%x -- %I %p", time_tuple)
		print '<OPTION value="'+str(this_entry)+'">'+date_str
	print '</SELECT>'
	print '<BR><input type="submit" value="Edit this entry">'
	print '</form>'

def new_entries():
	print '<form name="old" action="edit.py" method="POST">'
	print '<TABLE>'
	print '<TR><TH>Input a year in 4 digit format:'
	print '<Input type="text" MAXLENGTH="4" name="yeer"></TH>'
	print '<TH> Select a month:'
	std_form.months()
	print '</TH>'
	print '<TH> Enter a day:'
	std_form.days()
	print '</TH>'
	print '<TH> Enter a time:'
	std_form.times()
	print '</TH>'
	print '</TR>'
	print '<TR><TD>'
	print '<input type="submit" value="Add this time"></form>'
	print '</TD></TR></TABLE>'

def Main():
	style.header("Edit Questions for General class", "white")

	print '<H2 align="center">Editing and Adding questions to 417 excercise</H2>'

	print '<H3> Select a date to edit: </H3>'
	old_entries()
	print '<HR>'

	print '<H3> Or, create a new question </H3>'
	new_entries()
	print '<HR>'

Main()
