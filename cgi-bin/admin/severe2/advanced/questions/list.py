#!/usr/local/bin/python
# This program generates a listing of available days to make answer key for
# Daryl Herzmann 8-16-99

import pg, style, std_form, time, cgi

mydb = pg.connect('severe2_adv', 'localhost', 5432)

def print_questions():
	entries = mydb.query("SELECT q_id, question, intval from questions WHERE type = 'M' ").getresult()
	entries.sort()
	print '<SELECT name="question_num">'
	for i in range(len(entries)):
		tick = entries[i][0]
		question = entries[i][1]
		intval = entries[i][2]
		print '<option value="'+str(tick)+'">'+str(intval)+'. '+question[:70]
	print '</SELECT>'


def Main():
	style.header("Choose a question to edit", "white")

	form = cgi.FormContent()
	print '<font color="red"><H2>Edit generic questions</H2></font>'

	print '<form method="POST" action="edit.py">'

	print '<H3>Which Question:</H3>'
	print_questions()

	print '<H3>Submit:</H3>'
	print '<input type="submit">'

	print '</form>'

	print '<BR><a href="/admin">Back to Admin page, please</a>'
	print '</body></html>'


Main()
