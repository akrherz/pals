#!/usr/local/bin/python
# This program with make the neccessary questions
# Daryl Herzmann 7-28-99

import pg, time, sys, functs, style, string

mydb = pg.connect('archadmin')

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
	question = generics[1]
	optiona = generics[3]
	optionb = generics[4]
	optionc = generics[5]
	optiond = generics[6]
	optione = generics[7]
	optionf = generics[8]
	optiong = generics[9]
	optionh = generics[10]

	print '<input type="hidden" name="'+thisq+'question" value="'+question+'">'
	print '<input type="hidden" name="'+thisq+'" value="YES">'

	print "<BR><dd><b>"+str(int(i)+1)+"</b>. "+question+"</dd>"

	make_option("A", optiona, thisq)
	make_option("B", optionb, thisq)
	make_option("C", optionc, thisq)
	make_option("D", optiond, thisq)
	make_option("E", optione, thisq)
	make_option("F", optionf, thisq)
	make_option("G", optiong, thisq)
	make_option("H", optionh, thisq)
	

def Main(secs, key, refer):

	functs.setup_table()

	functs.mk_sub_sec("Help Topics:")
	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'
	print '<TD bgcolor="white" align="center" valign="center">'
        functs.mk_top( time.localtime(secs) )
        print '</TD></TR>'

	functs.mk_sub_sec("Weather Data:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        functs.mk_data( time.gmtime(secs) )
        print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Questions:")

	ztime = decide_time(float(secs))

	generics = mydb.query("SELECT * from gen_questions_417 WHERE ticks = "+ztime+" ").getresult()
	special = mydb.query("SELECT * from questions_417 WHERE ticks = "+str(secs)+" ").getresult()

	generics =  generics+special

	try:
		if len(generics[0]) == 0:
			return 1
	except:
		return 1

	print '<form method="POST" action="answer.py">'
	print '<input type="hidden" name="refer" value="'+refer+'">'
	print '<input type="hidden" name="secs" value="'+str(secs)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	for i in range(len(generics)):
		print '<TR bgcolor="white"><TD bgcolor="white"><BR></TD><TD colspan="2">'
		question = generics[i][1]
		type = generics[i][2]
		if type == "T":
			make_text_q(question, str(i))
		else:
			make_other(generics[i], str(i))
		print '</TD></TR>'

	print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
	print '<CENTER>'
	print '<input type="submit" value="Submit my answers">'
	print '</CENTER>'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'

	print '</form></body></html>'
	sys.exit(0)
