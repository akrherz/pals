#!/usr/bin/python
# Intermediate Exercise, checks out the db for generic question and then prompts for answer
# Daryl Herzmann -- 4 June 2000

import mx.DateTime, pg, time, functs, style, sys, SEVERE2

mydb = pg.connect('severe2', 'localhost', 5432)

def make_option(letter, valu, thisq):
	if valu != "":
		print '<BR><input type="radio" name="'+thisq+'option" value="'+letter+'">'
		print "<b>"+letter+"</b>. "+valu

def make_other(generics, i):
	thisq = "q"+i

	# Search Results for each option, if it errors, big deal
	try:
		question = generics["question"]
		optiona = generics["optiona"]
		optionb = generics["optionb"]
		optionc = generics["optionc"]
		optiond = generics["optiond"]
		optione = generics["optione"]
		optionf = generics["optionf"]
		optiong = generics["optiong"]
		optionh = generics["optionh"]
	except:
		print


	# Send along info that we indead have a question...	
	print '<input type="hidden" name="'+thisq+'" value="YES">'

	print """
	<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="3" cellspacing="0" border="0" width="100%">
		<TR WIDTH="100%"><TD>
		<TABLE bgcolor="#EEEEEE" border="0" cellpadding="3" cellspacing="0" width="100%">"""
	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question:</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="left">'

	try:
		print question
		make_option("A", optiona, thisq)
		make_option("B", optionb, thisq)
		make_option("C", optionc, thisq)	
		make_option("D", optiond, thisq)
		make_option("E", optione, thisq)
		make_option("F", optionf, thisq)
		make_option("G", optiong, thisq)
		make_option("H", optionh, thisq)
		make_option("N", "No data available", thisq)  #Give the option to pick no data
	except:
		print

	style.bot_box()


def Main(lastTime, userKey, caseNum, startTime):

	# First, decide what the interval value should be...	
	hours = mydb.query("SELECT date_part('hour', age(lastTime, '"+startTime+"')), \
		date_part('day', age(lastTime, '"+startTime+"')) from users WHERE userKey = "+str(userKey)+" ").getresult()

	hourVal = int( hours[0][0] )
	dayVal = int( hours[0][1] )
	if (dayVal > 0 ):
		hourVal = 24+hourVal

	# This is the value of the question in the db to look for
	intval = caseNum[0]+str( hourVal )

	questions = mydb.query("SELECT question, type, optiona, optionb, optionc, optiond, optione, optionf, optiong, optionh  from intquestions WHERE intval = '"+intval+"' ").dictresult()
	
	try:
		# If we do not find any questions, update the gradeTime and return
		if len(questions[0]) == 0:
			functs.updateUser(userKey,'gradetime', lastTime)
			return 1
	except:
		functs.updateUser(userKey,'gradetime', lastTime)
		return 1

	print '<H1 align="CENTER">Bonus Question!</H1>'

	print """<font color="#a0522d">
	<blockquote>You are now asked to answer the questions below.  Use the available weather maps and your 
	knowledge of this case so far to answer the questions below...</blockquote></font><BR><BR>"""
	

	print '<form method="POST" action="/cgi-bin/severe2/intermediate/answer.py">'
	print '<input type="hidden" name="userKey" value="'+str(userKey)+'">'
	print '<input type="hidden" name="intval" value="'+intval+'">'
	

	# For each question, loop 
	for i in range(len(questions)):
		
		type = questions[i]["type"]
		if type == "T":
			make_text_q(questions[i], str(i))
		else:
			make_other(questions[i], str(i))
		


	print """
		<input type="submit" value="Submit my answers">
		<input type="reset"></form><BR><BR>"""

	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3)
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1)
		
	functs.finishPage()

	
	sys.exit(0)
