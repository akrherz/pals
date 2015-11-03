#!/usr/local/bin/python
# This program edits the question and then submits it to enter.py
# Daryl Herzmann 7-15-99
# UPDATED 10-20-99: Changed the way that ticks gets made

import time, cgi, style, pg, DateTime

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")
table_str = "specquestions"

def add_entry(ticks):
	tester = mydb.query("SELECT validTime from "+table_str+" where validTime = '"+ticks+"' ").getresult()
	if len(tester) == 0:
		create = mydb.query("INSERT into "+table_str+" values('"+ticks+"')")

def mk_question(question):
	print '<H4>Edit the Text of the Question:</H4>'
	print '<TEXTAREA cols="80" rows="3" name="quest" WRAP>'+question+'</TEXTAREA><BR>' 

def mk_type(type):
	print '<H4>Select the type of question:</H4>'
	print '<SELECT name="type">'
	print '		<option value="M">Multiple Choice'
#	print '         <option value="T" '
#	if type == "T":
#		print "SELECTED"
#	print '>Text Response'
	print '</SELECT><BR>'

def mk_optiona(optiona):
	print '<H4>Enter Text for A Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiona" value="'+optiona+'"><BR>'

def mk_optionb(optionb):
	print '<H4>Enter Text for B Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionb" value="'+optionb+'"><BR>'

def mk_optionc(optionc):
	print '<H4>Enter Text for C Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionc" value="'+optionc+'"><BR>'

def mk_optiond(optiond):
	print '<H4>Enter Text for D Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiond" value="'+optiond+'"><BR>'

def mk_optione(optione):
	print '<H4>Enter Text for E Option (If applies):</H4>'
	print '<input type="text" size="80" name="optione" value="'+optione+'"><BR>'

def mk_optionf(optionf):
	print '<H4>Enter Text for F Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionf" value="'+optionf+'"><BR>'

def mk_answer(answer):
	print '<H4>Enter the answer if it applies, ex) A, B, C, D, E, F: </H4>'
	print '<input type="text" size="2" MAXLENGTH="1" name="answer" value="'+answer+'"><BR>'

def mk_cor_comments(cor_comments):
	print '<H4>Enter comments if the student answers correctly</H4>'
	print '<TEXTAREA cols=80 rows=10 name="cor_comments" WRAP>'+cor_comments+'</TEXTAREA><BR>'

def mk_wro_comments(wro_comments):
	print '<H4>Enter the comments if the student answers incorrectly</H4>'
	print '<TEXTAREA cols=80 rows=10 name="wro_comments" WRAP>'+wro_comments+'</TEXTAREA><BR>'

def Main():
	style.header("Edit Questions", "white")
	form = cgi.FormContent()

	zticks = form["zticks"][0]
	caseNum = form["caseNum"][0]

	zticks = int( float(zticks) )

	nowDate = DateTime.gmtime(zticks)

	nice_date = nowDate.strftime("%x %H  Z")
	strTicks = DateTime.ISO.strGMT(nowDate)
	add_entry( strTicks )
	
	print '<H2 align="CENTER">Edit Question for '+nice_date+':</H2>'
	print '<HR>'
	print '<a href="del.py?caseNum='+caseNum+'&zticks='+str(zticks)+'">Delete this question from DB</a>'

	
	entry = mydb.query("SELECT * from "+table_str+" WHERE validTime = '"+strTicks+"' ").dictresult()
	question = entry[0]["question"]
	type = entry[0]["type"]
	optiona = entry[0]["optiona"]
	optionb = entry[0]["optionb"]
	optionc = entry[0]["optionc"]
	optiond = entry[0]["optiond"]
	optione = entry[0]["optione"]
	optionf = entry[0]["optionf"]
	answer = entry[0]["answer"]
	cor_comments = entry[0]["correct"]
	wro_comments = entry[0]["wrong"]

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" name="validTime" value="'+strTicks+'">'
	print '<input type="hidden" name="caseNum" value="'+caseNum+'">'
	mk_question(question)
	mk_type(type)
	mk_optiona(optiona)	
	mk_optionb(optionb)	
	mk_optionc(optionc)
	mk_optiond(optiond)
	mk_optione(optione)
	mk_optionf(optionf)
	mk_answer(answer)
	mk_cor_comments(cor_comments)
	mk_wro_comments(wro_comments)

	print '<input type="SUBMIT" value="Make Changes">'

	print '</form></body></html>'

	
Main()
