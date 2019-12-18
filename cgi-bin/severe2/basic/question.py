#!/usr/bin/python2
# This program with make the neccessary questions
# Daryl Herzmann 7-28-99

import pg, time, sys, functs, style, string
from functs import *

mydb = pg.connect('severe2', 'localhost', 5432)

def make_text_q(question, i):
	thisq = "q"+i
	print "<BR><dd><b>"+str(int(i)+1)+"</b>. "+question+"</dd>"
	print '<BR><input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
	print '<TEXTAREA name="'+thisq+'text" cols="70" rows="10" WRAP></TEXTAREA>'

def make_option(letter, valu, thisq):
	if valu != "" and valu != "N":
		print '<BR><input type="radio" name="'+thisq+'option" value="'+letter+'">'
		print '<input type="hidden" name="'+thisq+'option_txt'+letter+'" value="'+letter+'. '+valu+'">'
		print "<b>"+letter+"</b>. "+valu

def make_other(generics, i):
	thisq = "q"+i
	try:
		question = generics[1]
		optiona = generics[3]
		optionb = generics[4]
		optionc = generics[5]
		optiond = generics[6]
		optione = generics[7]
		optionf = generics[8]
	except:
		print

#	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
	print '<input type="hidden" name="'+thisq+'" value="YES">'

	print """
 	<BR><TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="3" cellspacing="0" border="0" width="100%">
		<TR WIDTH="100%"><TD>
		<TABLE bgcolor="#EEEEEE" border="0" cellpadding="3" cellspacing="0" width="100%">
		<TR><TD><font color="blue" size="3" face="ARIAL"><B>Answer this question:</B></font></TD></TR>
		<TR><TD bgcolor="white" align="left">"""

	try:
		print question
		make_option("A", optiona, thisq)
		make_option("B", optionb, thisq)
		make_option("C", optionc, thisq)	
		make_option("D", optiond, thisq)
		make_option("E", optione, thisq)
		make_option("F", optionf, thisq)
	except:
		print

	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'


def Main(lastTime, userKey, caseNum, startTime):
	special = mydb.query("SELECT * from specquestions WHERE validTime = '"+lastTime+"' and question NOTNULL").getresult()

	generics =  special

	try:
		if len(generics[0]) == 0:
			return 1
	except:
		return 1

	multi = 1
	if caseNum[0] == "w":
		multi = 3


	print '<H1 align="CENTER">Bonus Question</H1>'

        print """
        <P>The following question is a bonus question for this case. Use your knowledge of this case so far
        and the weather data below to help you answer this question."""
        
	

	print '<form method="POST" action="'+scriptBase+'/answer.py">'
	print '<input type="hidden" name="userKey" value="'+str(userKey)+'">'
	for i in range(len(generics)):
		question = generics[i][1]
		type = generics[i][2]
		if len(question) > 0:
			if type == "T":
					make_text_q(question, str(i))
			else:
				make_other(generics[i], str(i))

	print """
	<CENTER>
                        <input type="submit" value="Submit my answers">
                        <input type="reset">
	</CENTER>
	"""


	print '</form>'
	
	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3, 'b')
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1, 'b')
	
	svrBot()
	sys.exit(0)


