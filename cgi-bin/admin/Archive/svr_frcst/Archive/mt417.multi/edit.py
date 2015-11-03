#!/usr/local/bin/python
# This program edits the question and then submits it to enter.py
# Daryl Herzmann 7-15-99
# UPDATED 7-21-99: Added support for up to 3 questions per hour

import time, cgi, style, sys, posix
from pgext import *

mydb = connect('archadmin')

def decide_date(yeer, month, day, tod):
	time_tuple = (yeer, month, day, tod, 0, 0, 0, 0, 0)
	secs = time.mktime(time_tuple)
	return int(secs)

def add_entry(ticks):
	ticks_str = ticks
	test1 = mydb.query("SELECT ticks from questions_417 where ticks = '"+ticks_str+"' ").getresult()
	if len(test1) == 0 :		# This time is not in the db
		ticks_str = ticks[:-2]+"_1"	# So lets try number 1		
		test2 = mydb.query("SELECT ticks from questions_417 where ticks = '"+ticks_str+"' ").getresult()
		
		if len(test2) != 0:		# Number 1 is in the db
			ticks_str = ticks[:-2]+"_2"	# So lets try number 2
			test3 = mydb.query("SELECT ticks from questions_417 where ticks = '"+ticks_str+"' ").getresult()

			if len(test3) != 0:	# Numer 2 in in the db
				ticks_str = ticks[:-2]+"_3"      # So lets try number 3		
				test4 = mydb.query("SELECT ticks from questions_417 where ticks = '"+ticks_str+"' ").getresult()

				if len(test4) != 0:  # Numer 3 in in the db
					print "You allready have 3 entries in the db, no more are allowed"
					sys.exit(0)
				else:
					insert = mydb.query("INSERT into questions_417 VALUES ('"+ticks_str+"') ")
					return "3"
			else:
				insert = mydb.query("INSERT into questions_417 VALUES ('"+ticks_str+"') ")
				return "2"
		else:
			insert = mydb.query("INSERT into questions_417 VALUES ('"+ticks_str+"') ")
			return "1"
	else:
		return ticks_str[-1]


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

def mk_optione(optione):
	print '<H4>Enter Text for E Option (If applies):</H4>'
	print '<input type="text" size="80" name="optione" value="'+optione+'"><BR>'

def mk_optionf(optionf):
	print '<H4>Enter Text for F Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionf" value="'+optionf+'"><BR>'

def mk_optiong(optiong):
	print '<H4>Enter Text for G Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiong" value="'+optiong+'"><BR>'

def mk_optionh(optionh):
	print '<H4>Enter Text for H Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionh" value="'+optionh+'"><BR>'

def mk_answer(answer):
	print '<H4>Enter the answer if it applies, ex) A, B, C, D, E, F, G, or H: </H4>'
	print '<input type="text" size="2" MAXLENGTH="1" name="answer" value="'+answer+'"><BR>'

def mk_wro_comments(wro_comments):
	print '<H4>Enter comments to appear if the user gets the question wrong</H4>'
	print '<TEXTAREA cols=80 rows=10 name="wro_comments" WRAP>'+wro_comments+'</TEXTAREA><BR>'

def mk_cor_comments(cor_comments):
	print '<H4>Enter comments to appear if the user gets the question correct</H4>'
	print '<TEXTAREA cols=80 rows=10 name="cor_comments" WRAP>'+cor_comments+'</TEXTAREA><BR>'

def mk_links(dir_format, link):
	try:
		files = posix.listdir('/home/httpd/html/archivewx/data/'+dir_format)
        	files.sort()
	except:
		files = ["None"]
        print '<b>Available files to link in (Choose One):</b>'
        print '<SELECT name="link">'
	print '<option>None'
        for file in files:
                print '<OPTION '
		if file == link:
			print "SELECTED"
		print ' >'+file
        print '</SELECT><HR>'



def Main():
	style.header("Edit Questions for 417", "white")
	form = cgi.FormContent()

	if form.has_key("ticks"):
		ticks = form["ticks"][0]
	else:
		ticks = decide_date(int(form["yeer"][0]), int(form["month"][0]), int(form["day"][0]), int(form["tod"][0]))

	parts = re.split('_', str(ticks))
	time_part = int(parts[0])
	try:
		num = parts[1]
	except IndexError:
		num = 4

	now_tuple = time.localtime(time_part)
	gmt_tuple = time.gmtime(time_part)
	nice_date = time.strftime("%x %I:%M  %p", now_tuple)
	dir_format = time.strftime("%Y_%m_%d", gmt_tuple)

	ticks = str(time_part)+"_"+str(num)

	print '<H2 align="CENTER">Edit Question for '+nice_date+':</H2>'
	num = add_entry(str(ticks))

	ticks = str(time_part)+"_"+str(num)


	entry = mydb.query("SELECT * from questions_417 WHERE ticks = '"+str(ticks)+"' ").getresult()
	question = entry[0][1]
	type = entry[0][2]
	optiona = entry[0][3]
	optionb = entry[0][4]
	optionc = entry[0][5]
	optiond = entry[0][6]
	optione = entry[0][7]
	optionf = entry[0][8]
	optiong = entry[0][9]
	optionh = entry[0][10]
	answer = entry[0][11]
	cor_comments = entry[0][12]
	wro_comments = entry[0][13]
	link = entry[0][14]

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" name="ticks" value="'+str(ticks)+'">'
	print '<input type="hidden" name="multi" value="'+num+'">'
	mk_question(question)
	mk_links(dir_format, link)
	mk_type(type)
	mk_optiona(optiona)	
	mk_optionb(optionb)	
	mk_optionc(optionc)	
	mk_optiond(optiond)	
	mk_optione(optione)	
	mk_optionf(optionf)	
	mk_optiong(optiong)	
	mk_optionh(optionh)	
	mk_answer(answer)
	mk_cor_comments(cor_comments)
	mk_wro_comments(wro_comments)

	print '<input type="SUBMIT" value="Make Changes">'

	print '</form></body></html>'

	
Main()
