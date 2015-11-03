#!/usr/local/bin/python
# This program changes db stuff
# Daryl Herzmann 8-16-99

import cgi, pg, style, time

mydb = pg.connect('severe2_adv', 'localhost', 5432)

def get_question(question_num):
	entry = mydb.query("SELECT * from questions WHERE q_id = '"+question_num+"' ").dictresult()
	return entry
	
def get_old_answer(caseNum, q_id):
	select = mydb.query("SELECT answer, correct, wrong from answers WHERE casenum = '"+caseNum+"' and q_id = '"+q_id+"' ").getresult()
	if len(select) > 0:
		ans = select[0][0]
		cor_comments = select[0][1]
		wro_comments = select[0][2]
		return ans, cor_comments, wro_comments
	else:
		return "","",""

def mk_option(ans, letter, optionval):
	if letter == ans and optionval != 'N':
		print '<option value="'+letter+'" SELECTED>'+letter+'. '+optionval[:80]+' ...'
	elif optionval != 'N':
		print '<option value="'+letter+'">'+letter+'. '+optionval[:80]+' ...'		


def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	question_num = form["question_num"][0]

	style.header("Edit answer for Generic Question", "white")

	quest = get_question(question_num)

	print '<H3>This is Question number '+question_num+' from caseNum '+caseNum+' </H3>'

	question = quest[0]["question"]
	optiona = quest[0]["optiona"]
	optionb = quest[0]["optionb"]
	optionc = quest[0]["optionc"]
	optiond = quest[0]["optiond"]
	optione = quest[0]["optione"]
	optionf = quest[0]["optionf"]
	optiong = quest[0]["optiong"]
	optionh = quest[0]["optionh"]

	ans, cor_comments, wro_comments = get_old_answer(caseNum, question_num)

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" value="'+question_num+'" name="question_num">'
	print '<input type="hidden" value="'+caseNum+'" name="caseNum">'

	print '<B>Edit the answer for this question:</B><BR>'
	print '<dd>'+question+'</dd><BR>'

	print '<B>Select the correct answer:</B><BR>'
	print '<SELECT name="answer">'
	mk_option(ans, "A", optiona)
	mk_option(ans, "B", optionb)
	mk_option(ans, "C", optionc)
	mk_option(ans, "D", optiond)
	mk_option(ans, "E", optione)
	mk_option(ans, "F", optionf)
	mk_option(ans, "G", optiong)
	mk_option(ans, "H", optionh)
	print '</SELECT>'

	print '<BR><B>Input the correct comments</B>'
	print '<textarea name="cor_comments" cols="70" rows="10" WRAP>'+cor_comments+'</textarea>' 

	print '<BR><B>Input the wrong comments</B>'
	print '<textarea name="wro_comments" cols="70" rows="10" WRAP>'+wro_comments+'</textarea>' 

	print '<BR><BR>'
	print '<input type="submit" value="SUBMIT ANSWER">'

	print '</form>'
	style.std_bot()

Main()
