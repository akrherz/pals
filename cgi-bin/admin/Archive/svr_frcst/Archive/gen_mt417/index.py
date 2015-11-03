#!/usr/local/bin/python
# This program figures out what day they want to edit, or maybe add a new entry
# Daryl Herzmann 7-15-99

import style, std_form, pg

mydb = connect("svr_frcst")
table_str = "questions"

def new_entries():
	print '<form name="old" action="edit.py" method="POST">'
	print '<TABLE>'
	print '<TR><TH> Enter a time:'
	std_form.times()
	print '</TH>'
	print '</TR>'
	print '<TR><TD>'
	print '<input type="submit" value="Add this time"></form>'
	print '</TD></TR></TABLE>'

def Main():
	style.header("Specific Hourly Questions", "white")

	print '<H2 align="center">Specific Hourly Questions</H2>'

	print '<H3> Select a date to edit: </H3>'
	print '<HR>'

	print '<H3> Or, create a new question </H3>'
	new_entries()
	print '<HR>'

Main()
