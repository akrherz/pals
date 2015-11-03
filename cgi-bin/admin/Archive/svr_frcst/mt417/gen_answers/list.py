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

def print_cases(selected = "none"):
	print '<SELECT name="caseNum">'
	entries = mydb.query("SELECT * from cases").getresult()
	for i in range(len(entries)):
		caseNum = entries[i][0]
		start_secs = float(entries[i][1])
		start_tuple = time.localtime(start_secs)
		nice_date = time.strftime("%x", start_tuple)
		print '<option value="'+str(caseNum)+'" '
		if selected == caseNum:
			print 'SELECTED'
		print '>'+caseNum+' -- '+nice_date
	print '</SELECT>'

def Main():
	style.header("Choose time and question to edit", "white")

	form = cgi.FormContent()

	print '<font color="red"><H2>Edit Answer Keys for generic 417 questions</H2></font>'

	if form.has_key('caseNum'):
		caseNum = form["caseNum"][0]

		print '<form method="POST" action="list.py" name="switch">'
		print '<H3>Case:</H3>'
		print_cases(caseNum)
		print '<input type="SUBMIT" value="Switch Current Cases">'
		print '</form>'
		print '<HR><HR>'

		print '<form method="POST" action="edit.py">'
		print '<input type="hidden" name="caseNum" value="'+caseNum+'">'
		print '<H3>Pick Which Question for Case '+caseNum+':</H3>'
		print_questions(caseNum[0])
	else:
		print '<form method="POST" action="list.py">'
		print '<H3>Select which case: </H3>'
		print_cases()

	print '<H3>Submit:</H3>'
	print '<input type="submit">'

	print '</form>'

	print '<BR><BR><a href="/admin">Admin Page</a>'

Main()
