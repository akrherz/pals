#!/usr/local/bin/python
# This program generates a listing of available days to make answer key for
# Daryl Herzmann 8-16-99

import pg, style, std_form, time, cgi, SEVERE2

mydb = pg.connect('severe2_adv', 'localhost', 5432)

def print_questions(case_type):
	entries = mydb.query("SELECT q_id, question from questions WHERE type = 'M' AND intval ~* '"+case_type+"' ").getresult()
	entries.sort()
	print '<SELECT name="question_num">'
	for i in range(len(entries)):
		tick = entries[i][0]
		question = entries[i][1]
		print '<option value="'+str(tick)+'">'+str(tick)+'. '+question[:70]
	print '</SELECT>'

def Main():
	style.header("Choose time and question to edit", "white")

	form = cgi.FormContent()

	print '<font color="red"><H2>Edit Answer Keys for generic questions</H2></font>'

	if form.has_key('caseNum'):
		caseNum = form["caseNum"][0]

		print '<a href="list.py">Change Current Case</a><BR><BR>'

		print '<form method="POST" action="list.py" name="switch">'
		print '</form>'
		print '<HR><HR>'

		print '<form method="POST" action="edit.py">'
		print '<input type="hidden" name="caseNum" value="'+caseNum+'">'
		print '<H3>Pick Which Question for Case '+caseNum+':</H3>'
		print_questions(caseNum[0])
	else:
		print '<form method="POST" action="list.py">'
		print '<H3>Select which case: </H3>'
		SEVERE2.listAllCases()

	print '<H3>Submit:</H3>'
	print '<input type="submit">'

	print '</form>'

	print '<BR><BR><a href="/admin">Admin Page</a>'

Main()
