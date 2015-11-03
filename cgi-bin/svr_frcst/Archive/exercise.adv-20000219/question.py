#!/usr/local/bin/python
# This program with make the neccessary questions
# Daryl Herzmann 7-28-99

scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.adv-cvs"
specTable = "spec_questions"

import pg, time, sys, functs, style, string

mydb = pg.connect('svr_frcst')


def make_text_q(questions, i):
	question = questions[1]
	q_id = questions[0]
	thisq = "q"+i

	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
        
	print '<input type="hidden" name="'+thisq+'" value="YES">'
        
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
	print '<TR WIDTH="100%"><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question '+str(int(i)+1)+':</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="left">'

	print '<BR><dd>'+question+'</dd><BR>'
	print '<input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'q_id" value="'+q_id+'">'
	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
        print '<TEXTAREA name="'+thisq+'text" cols="70" rows="10" WRAP></TEXTAREA>'
	style.bot_box()

def make_option(letter, valu, thisq):
	if valu != "N":
		print '<BR><input type="radio" name="'+thisq+'option" value="'+letter+'">'
		print '<input type="hidden" name="'+thisq+'option_txt'+letter+'" value="'+letter+'. '+valu+'">'
		print "<b>"+letter+"</b>. "+valu

def make_other(generics, i):
	thisq = "q"+i
	try:
		q_id = generics[0]
		question = generics[1]
		optiona = generics[3]
		optionb = generics[4]
		optionc = generics[5]
		optiond = generics[6]
		optione = generics[7]
		optionf = generics[8]
		optiong = generics[9]
		optionh = generics[10]
	except:
		print

	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
	print '<input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'q_id" value="'+q_id+'">'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
	print '<TR WIDTH="100%"><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
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

def updatedb(ldb, key, secs, className):
        tableName = "users"
        update = ldb.query("UPDATE "+tableName+" set last_time = '"+str(secs)+"' WHERE userid = '"+str(key)+"' ")


def Main(interval, case_num, secs, key, refer, className, ldb):
	secs_tuple = time.localtime(secs)
	this_interval = case_num[0]+str(interval)
	ldb = pg.connect('svr_'+className)

	special = ldb.query("SELECT ticks, question, type, optiona, optionb, optionc, optiond, optione, optionf, optiong, optionh  from "+specTable+" WHERE ticks = '"+str(secs)+"' ").getresult()
	standard = mydb.query("SELECT q_id, question, type, optiona, optionb, optionc, optiond, optione, optionf, optiong, optionh from gen_417 WHERE interval_num = '"+this_interval+"' ").getresult()

	questions =  special + standard

	try:
		if len(questions[0]) == 0:
			updatedb(ldb, key, secs, className)
			return 1
	except:
		updatedb(ldb, key, secs, className)
		return 1

	print '<H1 align="CENTER">Bonus Question</H1>'

	print """<font color="#0854a8"><H2>Instructions:</H2></font>
	<P>You are now asked to answer the questions below.  Use the available weather maps and your 
	knowledge of this case so far, to answer the questions below...<BR><BR>"""
	


	if case_num[0] == 'w':
	        functs.mk_data(secs_tuple, 3)
	else:
	        functs.mk_data(secs_tuple, 1)

	print '<form method="POST" action="'+scriptBase+'/answer.py">'
	print '<input type="hidden" name="interval" value="'+interval+'">'
	print '<input type="hidden" name="className" value="'+className+'">'
	print '<input type="hidden" name="refer" value="'+refer+'">'
	print '<input type="hidden" name="secs" value="'+str(secs)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="case_num" value="'+str(case_num)+'">'

	for i in range(len(questions)):
		print '<TR><TD><BR></TD><TD colspan="2">'
		type = questions[i][2]
		if type == "T":
			make_text_q(questions[i], str(i))
		else:
			make_other(questions[i], str(i))
		print '</TD></TR>'

	print '<TR><TD>&nbsp;</TD><TD colspan="2">'

	print """
	<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">
	<TR WIDTH="100%"><TD>
		<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">
		<TR><TD><font color="blue" size="4" face="ARIAL"><B>Submit my answer:</B></font></TD></TR>
		<TR><TD bgcolor="white" align="center">
			<input type="submit" value="Submit my answers">
			<input type="reset">
		</TD></TR></TABLE>
	</TD></TR></TABLE>"""


        print '</TD></TR></TABLE>'

	functs.svr_bot()
	print '</form></body></html>'
	sys.exit(0)		# This is important
