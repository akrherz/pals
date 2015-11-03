#!/usr/local/bin/python
# This program changes db stuff
# Daryl Herzmann 8-16-99

import cgi, pg, style, time, string

mydb = pg.connect('severe2_adv', 'localhost', 5432 )


def get_question(question_num):
	entry = mydb.query("SELECT * from questions WHERE q_id = '"+question_num+"' ").dictresult()
	return entry
	

def mk_option(letter, optionval):
	print '<BR><BR>Option '+letter+' '
#	print '<input type="text" size="100" name="option'+letter+'" value="'+optionval+'">'		
	print '<textarea cols="80" rows="2" name="option'+string.lower(letter)+'" WRAP>'+optionval+'</textarea>'		


def Main():
	form = cgi.FormContent()
	question_num = form["question_num"][0]

	style.header("Edit answer for Generic Question", "white")

	quest = get_question(question_num)

	print '<H3>This is Question number '+question_num+'</H3>'

	question = quest[0]["question"]
	optiona = quest[0]["optiona"]
	optionb = quest[0]["optionb"]
	optionc = quest[0]["optionc"]
	optiond = quest[0]["optiond"]
	optione = quest[0]["optione"]
	optionf = quest[0]["optionf"]
	optiong = quest[0]["optiong"]
	optionh = quest[0]["optionh"]

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" value="'+question_num+'" name="question_num">'

	print '<B>Edit this question:</B><BR>'
	print '<textarea name="question" WRAP cols="80" rows="3">'+question+'</textarea><BR>'

	print '<B>Enter the options:</B><BR>'
	mk_option("A", optiona)
	mk_option("B", optionb)
	mk_option("C", optionc)
	mk_option("D", optiond)
	mk_option("E", optione)
	mk_option("F", optionf)
	mk_option("G", optiong)
	mk_option("H", optionh)

	print '<BR><BR>'
	print '<input type="submit" value="SUBMIT ANSWER">'

	print '</form>'
	

Main()
