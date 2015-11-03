#!/usr/local/bin/python
# This program generates a listing of available days to make answer key for
# Daryl Herzmann 8-16-99

import pg, style, std_form, time, cgi

mydb = pg.connect('svr_frcst')

def print_questions(case_type):
	entries = mydb.query("SELECT q_id, question from gen_417 WHERE type = 'M' AND interval_num ~* '"+case_type+"' ").getresult()
	entries.sort()
	print '<SELECT name="question_num">'
	for i in range(len(entries)):
		tick = entries[i][0]
		question = entries[i][1]
		print '<option value="'+str(tick)+'">'+str(tick)+'. '+question[:70]
	print '</SELECT>'


def Main():
	style.header("Choose a question to edit", "white")

	form = cgi.FormContent()
	case_type = form["case_type"][0]

	print '<font color="red"><H2>Edit generic 417 questions</H2></font>'

	print '<form method="POST" action="edit.py">'
	print '<input type="hidden" value="'+case_type+'" name="case_type">'

	print '<H3>Which Question:</H3>'
	print_questions(case_type)

	print '<H3>Submit:</H3>'
	print '<input type="submit">'

	print '</form>'

	print '<BR><a href="/admin">Back to Admin page, please</a>'
	print '</body></html>'


Main()
