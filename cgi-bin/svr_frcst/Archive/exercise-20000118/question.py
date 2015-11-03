#!/usr/local/bin/python
# This program with make the neccessary questions
# Daryl Herzmann 7-28-99

import pg, time, sys, functs, style, string, svr_frcst

mydb = pg.connect('svr_frcst')

def decide_time(secs):
        time_tuple = time.localtime(secs)
        return str(time_tuple[3])

def make_text_q(question, i):
	thisq = "q"+i
	print "<BR><dd><b>"+str(int(i)+1)+"</b>. "+question+"</dd>"
	print '<BR><input type="hidden" name="'+thisq+'" value="YES">'
	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
        print '<TEXTAREA name="'+thisq+'text" cols="70" rows="10" WRAP></TEXTAREA>'

def make_option(letter, valu, thisq):
	if valu != "N":
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
#		optione = generics[7]
#		optionf = generics[8]
#		optiong = generics[9]
#		optionh = generics[10]
	except:
		print

#	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
	print '<input type="hidden" name="'+thisq+'" value="YES">'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question:</B></font></TD></TR>'
#        print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>Question '+str(int(i)+1)+':</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="left">'
	try:
		print question
		make_option("A", optiona, thisq)
		make_option("B", optionb, thisq)
		make_option("C", optionc, thisq)	
		make_option("D", optiond, thisq)
#		make_option("E", optione, thisq)
#		make_option("F", optionf, thisq)
#		make_option("G", optiong, thisq)
#		make_option("H", optionh, thisq)
	except:
		print

	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'


def Main(case_num, secs, key, refer):
	secs_tuple = time.localtime(secs)
	special = mydb.query("SELECT * from spec_questions WHERE ticks = '"+str(secs)+"' ").getresult()

	generics =  special

	try:
		if len(generics[0]) == 0:
			return 1
	except:
		return 1

	print '<TR><TD>&nbsp;</TD><TD valign="top">'
        svr_frcst.mk_help()
        print '</TD>'
	print '<TD align="center" valign="center">'
        svr_frcst.mk_top( time.localtime(int(float(secs))) , secs)
        print '</TD></TR>'


	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2">'
        print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Weather Data:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
        functs.mk_data(secs_tuple)
        print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'
        print '<BR></TD></TR>\n\n'


	ztime = decide_time(float(secs))


	print '<form method="POST" action="/cgi-bin/svr_frcst/exercise/answer.py">'
	print '<input type="hidden" name="refer" value="'+refer+'">'
	print '<input type="hidden" name="secs" value="'+str(secs)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="case_num" value="'+str(case_num)+'">'
	for i in range(len(generics)):
		print '<TR><TD><BR></TD><TD colspan="2">'
		question = generics[i][1]
		type = generics[i][2]
		if type == "T":
			make_text_q(question, str(i))
		else:
			make_other(generics[i], str(i))
		print '</TD></TR>'

	print '<TR><TD>&nbsp;</TD><TD colspan="2">'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Submit my answer:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	print '<input type="submit" value="Submit my answers">'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'


        print '</TD></TR></TABLE>'

	print '</form></body></html>'
	sys.exit(0)
