#!/usr/local/bin/python
# This program changes db stuff
# Daryl Herzmann 8-16-99

import cgi, pg, style, time, string

mydb = pg.connect('severe2', 'localhost', 5432)

def get_question(question_num):
	entry = mydb.query("SELECT * from intquestions WHERE intval = '"+question_num+"' ").getresult()
	return entry
	
def get_old_answer(caseNum, q_id):
	select = mydb.query("SELECT answer, correct, wrong from intanswers WHERE casenum = '"+caseNum+"' and intval = '"+q_id+"' ").getresult()
#	print "SELECT answer, correct, wrong from intanswers WHERE casenum = '"+caseNum+"' and intval = '"+q_id+"' "
	if len(select) > 0:
		ans = select[0][0]
		cor_comments = select[0][1]
		wro_comments = select[0][2]
		return ans, cor_comments, wro_comments
	else:
		return "","",""

def mk_option(ans, letter, optionval):
	if letter == ans and optionval != '':
		print '<option value="'+letter+'" SELECTED>'+letter+'. '+optionval+' ...'		
	elif optionval != '':
		print '<option value="'+letter+'">'+letter+'. '+optionval+' ...'		


def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	question_num = form["question_num"][0]

	style.header("Edit answer for Generic Question", "white")

	quest = get_question(question_num)

	print '<H3>This is Question number '+question_num+' from caseNum '+caseNum+'</H3>'

	question = quest[0][1]
	optiona = quest[0][3]
	optionb = quest[0][4]
	optionc = quest[0][5]
	optiond = quest[0][6]
	optione = quest[0][7]
	optionf = quest[0][8]
	optiong = quest[0][9]
	optionh = quest[0][10]
	optionN = quest[0][11]

	ans, cor_comments, wro_comments = get_old_answer(caseNum, question_num)

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" value="'+string.strip(question_num)+'" name="question_num">'
	print '<input type="hidden" value="'+string.strip(caseNum)+'" name="caseNum">'

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
	mk_option(ans, "N", optionN)
	print '</SELECT>'

	print '<BR><B>INPUT THE CORRECT COMMENTS TO APPEAR</B><BR>'
	print '<textarea name="cor_comments" cols="80" rows="10" WRAP>'+cor_comments+'</textarea>' 

	print '<BR><B>INPUT THE WRONG COMMENTS TO APPEAR</B><BR>'
	print '<textarea name="wro_comments" cols="80" rows="10" WRAP>'+wro_comments+'</textarea>' 

	print '<BR><BR>'
	print '<input type="submit" value="SUBMIT ANSWER">'

	print '</form>'
	style.std_bot()

Main()
