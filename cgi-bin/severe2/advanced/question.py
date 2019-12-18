#!/usr/bin/env python2
# This program with make the neccessary questions
# Daryl Herzmann 7-28-99

import style, pg, functs, SEVERE2, sys

basedb = pg.connect('severe2', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)

def make_text_q(questions, i):
	question = questions["question"]
	q_id = questions["q_id"]
	thisq = "q"+i

	print """
 	<BR><TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="3" cellspacing="0" border="0" width="100%">
                <TR WIDTH="100%"><TD>
                <TABLE bgcolor="#EEEEEE" border="0" cellpadding="3" cellspacing="0" width="100%">"""
	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question '+str(int(i)+1)+':</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'

	print '<BR><dd>'+question+'</dd><BR>'
	print '<input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'q_id" value="'+q_id+'">'
	print '<input type="hidden" name="'+thisq+'option" value="YES">'
	print '<TEXTAREA name="'+thisq+'text" cols="70" rows="10" WRAP></TEXTAREA><BR><BR>'
	style.bot_box()

def make_option(letter, valu, thisq):
	if valu != "N":
		print '<BR><input type="radio" name="'+thisq+'option" value="'+letter+'">'
		print '<b>'+letter+'</b>. '+valu

def make_other(generics, i):
	thisq = "q"+i
	try:
		q_id = generics["q_id"]
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

	print '<input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'q_id" value="'+q_id+'">'

	print """<BR>
        <TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="3" cellspacing="0" border="0" width="100%">
                <TR WIDTH="100%"><TD>
                <TABLE bgcolor="#EEEEEE" border="0" cellpadding="3" cellspacing="0" width="100%">"""
	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question '+str(int(i)+1)+':</B></font></TD></TR>'
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
	except:
		print

	style.bot_box()


def Main(lastTime, userKey, caseNum, startTime, className, startTime22):

	hours = advdb.query("SELECT date_part('hour', age(lastTime, '"+startTime+"')), ans_ques from users WHERE userKey = "+str(userKey)+" ").getresult()
	
	if hours[0][1] == "f":
		return 1


	intval = caseNum[0]+str(int(hours[0][0]))
	
	qOptions = "optiona, optionb, optionc, optiond, optione, optionf, optiong, optionh"

	standard = advdb.query("SELECT q_id, question, type, "+qOptions+" from questions WHERE intval = '"+intval+"' and question NOTNULL").dictresult()
	
	special = advdb.query("SELECT validTime as q_id, question, type,  "+qOptions+" from questions_custom WHERE validTime = '"+lastTime+"' and className = '"+className+"' and question NOTNULL").dictresult()

	questions =  special + standard

#	print "<H3>Hello</H3>"
#	print "SELECT q_id, question, type, "+qOptions+" from questions WHERE intval = '"+intval+"' "
#	print "SELECT validTime, question, type,  "+qOptions+" from questions_custom WHERE validTime = '"+lastTime+"' and className = '"+className+"' "
#	print questions

	try:
		if len(questions[0]) == 0:
			functs.updateUser(userKey, "gradeTime", lastTime)
			return 1
	except:
		functs.updateUser(userKey, "gradeTime", lastTime)
		return 1

	print '<H1 align="CENTER">Bonus Question!</H1>'

	print """
	<P>You are now asked to answer the questions below.  Use the available weather maps and your 
	knowledge of this case so far to answer the questions below...<BR><BR>"""
	

	print '<form method="POST" action="/cgi-bin/severe2/advanced/answer.py">'
	print '<input type="hidden" name="userKey" value="'+str(userKey)+'">'


	for i in range(len(questions)):
		type = questions[i]["type"]
		if type == "T":
			make_text_q(questions[i], str(i))
		else:
			make_other(questions[i], str(i))
		


	print """
			<input type="submit" value="Submit my answers">
			<input type="reset">
   <BR><BR>"""

	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3)
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1)

	
	print '</form>'
	SEVERE2.finishPage("advanced", className)
	sys.exit(0)		# This is important
