#!/usr/local/bin/python
# This is the first program for the 417 exercise, prompts user for info..
# Daryl Herzmann 11-14-99
scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.417"

import time, style, cgi, pg, functs


def ask_for_info(case_num, key, className):
	print """
	<font color="blue"><H1>Enter your information:</H1></font>

	<P>Please fill out the appropiate information as follows.  This authentications you to the
	system and allows the instruction to know who is doing this exercise...<BR>
	It is important to use your <b>real name</b> and <b>email address</b> in order to receive credit working
	through this case...

	<form method="POST" action="index.py">"""
	
	print '<input type="hidden" name="className" value="'+className+'">'	
	print '<input type="hidden" name="case_num" value="'+case_num+'">'	
	print '<input type="hidden" name="key" value="'+str(key)+'">'

	print """
	<H3>Enter your Full Name:</H3>
	<input size="40" MAXLENGTH="40" type="text" name="name"><BR>
	
	<H3>Enter your Email Address:</H3>
	<input size="40" MAXLENGTH="40" type="text" name="email"><BR><BR>

	<input type="submit" value="Start Excercise">
	<input type="reset"> 
	</form>"""

def mk_new_entry(ldb, className):
	users_table = "users"
	key = str(int(float(time.time())))		# we generate the key that the user will be using for the day
	input = ldb.query("INSERT into "+users_table+" VALUES ("+key+") ")	# Create the entry in the db
	create = ldb.query("CREATE TABLE s"+key[:9]+" (ticks varchar(20), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
	return key


def Main():
	form = cgi.FormContent()
	try:
		case_num = form["case_num"][0]		
		className = form["className"][0]
	except:
		style.SendError("The link into this system is corrupt")

	style.header("Welcome to Dr Gallus's Forecasting Exercise", "white")

	sessiondb = pg.connect('svr_'+className)

	key = mk_new_entry(sessiondb, className)
	ask_for_info(case_num, key, className)
        style.std_bot()

Main()
