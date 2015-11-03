#!/usr/local/bin/python
# This program edits the question and then submits it to enter.py
# Daryl Herzmann 7-15-99
# UPDATED 10-20-99: Changed the way that ticks gets made

import time, cgi, style, pg

mydb = pg.connect('svr_frcst')
table_str = "spec_questions"

def decide_date(yeer, month, day, tod):
	time_tuple = (yeer, month, day, tod, 0, 0, 0, 0, 0)
	if month > 5 and month < 11:
		time_tuple = (yeer, month, day, tod, 0, 0, 0, 0, 1)
	secs = time.mktime(time_tuple)
	return secs

def add_entry(ticks):
	tester = mydb.query("SELECT ticks from "+table_str+" where ticks = '"+ticks+"' ").getresult()
	if len(tester) == 0:
		create = mydb.query("INSERT into "+table_str+" values('"+ticks+"')")

def mk_question(question):
	print '<H4>Edit the Text of the Question:</H4>'
	print '<TEXTAREA cols="80" rows="3" name="quest" WRAP>'+question+'</TEXTAREA><BR>' 

def mk_type(type):
	print '<H4>Select the type of question:</H4>'
	print '<SELECT name="type">'
	print '		<option value="M">Multiple Choice'
	print '         <option value="T" '
	if type == "T":
		print "SELECTED"
	print '>Text Response'
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

def mk_answer(answer):
	print '<H4>Enter the answer if it applies, ex) A, B, C, or D: </H4>'
	print '<input type="text" size="2" MAXLENGTH="1" name="answer" value="'+answer+'"><BR>'

def mk_comments(comments):
	print '<H4>Enter comments to appear after the question gets answered (if applicable)</H4>'
	print '<TEXTAREA cols=80 rows=10 name="comments" WRAP>'+comments+'</TEXTAREA><BR>'

def Main():
	style.header("Edit Questions", "white")
	form = cgi.FormContent()

	if form.has_key("ticks"):
		ticks = form["ticks"][0]
	else:
		ticks = decide_date(int(form["yeer"][0]), int(form["month"][0]), int(form["day"][0]), int(form["ztime"][0]))

	ticks = int( float(ticks) )
	now_tuple = time.localtime(ticks)
	nice_date = time.strftime("%x %H  Z", now_tuple)

	print '<H2 align="CENTER">Edit Question for '+nice_date+':</H2>'
	print '<HR>'
	print '<a href="del.py?ticks='+str(ticks)+'">Delete this question from DB</a>'

	add_entry(str(ticks))
	
	entry = mydb.query("SELECT * from "+table_str+" WHERE ticks = '"+str(ticks)+"' ").getresult()
	question = entry[0][1]
	type = entry[0][2]
	optiona = entry[0][3]
	optionb = entry[0][4]
	optionc = entry[0][5]
	optiond = entry[0][6]
	answer = entry[0][7]
	comments = entry[0][8]

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" name="ticks" value="'+str(ticks)+'">'
	mk_question(question)
	mk_type(type)
	mk_optiona(optiona)	
	mk_optionb(optionb)	
	mk_optionc(optionc)	
	mk_optiond(optiond)	
	mk_answer(answer)
#	mk_comments(comments)

	print '<input type="SUBMIT" value="Make Changes">'

	print '</form></body></html>'

	
Main()
