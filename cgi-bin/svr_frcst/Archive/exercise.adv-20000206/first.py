#!/usr/local/bin/python
# This is the first program for the 417 exercise, prompts user for info..
# Daryl Herzmann 11-14-99

scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.adv"
usersTable = "users"

import time, style, cgi, pg, functs

def ask_for_info(case_num, key, className):
	print """
	<font color="blue"><H2>Instructions:</H2></font>

	<P>Before you can begin this exercise, you need to enter your name and email address so that your
	instructor can grade your results.  It is therefore important to enter correct information below.

	<form method="POST" action="index.py">"""
	
	print '<input type="hidden" name="className" value="'+className+'">'	
	print '<input type="hidden" name="case_num" value="'+case_num+'">'	
	print '<input type="hidden" name="key" value="'+str(key)+'">'

	print """
	<font color="blue"><H2>Enter your information:</H2></font>
	<TABLE border="0">
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your Name:</font>
		</TH><TD>
			<input size="40" MAXLENGTH="40" type="text" name="name">
		</TD></TR>
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your Email Address:</font>
		</TH><TD>
			<input size="40" MAXLENGTH="40" type="text" name="email">
		</TD></TR>
	</TABLE>

	<input type="submit" value="Start Excercise">
	<input type="reset"> 
	</form>
	<BR>
	"""

def mk_new_entry(ldb, className):
	key = str(int(float(time.time())))		# we generate the key that the user will be using for the day
	input = ldb.query("INSERT into "+usersTable+" VALUES ("+key+") ")	# Create the entry in the db
	create = ldb.query("CREATE TABLE s"+key+" (ticks varchar(20), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
	return key


def Main():
	form = cgi.FormContent()
	if not form.has_key("case_num"):
		style.SendError("No case number was supplied to this script")
	if not form.has_key("className"):
		style.SendError("No class name specified")

	case_num = form["case_num"][0]	
	className = form["className"][0]

	functs.svr_top("Blah")

	sessiondb = pg.connect('svr_'+className)

	key = mk_new_entry(sessiondb, className)
	ask_for_info(case_num, key, className)

	functs.svr_bot()

Main()
