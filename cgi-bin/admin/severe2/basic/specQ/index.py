#!/usr/local/bin/python
# This program figures out what day they want to edit, or maybe add a new entry
# Daryl Herzmann 7-15-99

import style, time, std_form, pg, SEVERE2, cgi

mydb = pg.connect("severe2", 'localhost', 5432)

def Main():
	style.header("Edit Specific Questions", "white")

	print '<H2 align="center">Editing and Adding questions to Basic excercise</H2>'

	print '<B>Info:</B><HR>'
	print 'This program creates specific questions for the Basic forecasting exercise.'

	form = cgi.FormContent()
	if not form.has_key("caseNum"):
		print '<form method="POST" action="index.py">'
		print '<H3>Select Case to Edit Questions for:</H3>'
		SEVERE2.listAllCases()
		print '<BR><input type="submit" value="Select Case">'
		print '</form>'
	else:
		caseNum = form["caseNum"][0]
		print '<form method="POST" action="edit.py">'
		print '<input type="hidden" value="'+caseNum+'" name="caseNum">'
		print '<H3>Select Hour to Add/Delete/Edit Specific Question For:</H3>'
		SEVERE2.listHours(caseNum)
		print '<BR><input type="submit" value="Select Specific Time">'
		print '</form>'


	print '<P>Links outta here:'
	print '<HR>'
	print '<a href="/admin">Admin page</a>'

Main()
