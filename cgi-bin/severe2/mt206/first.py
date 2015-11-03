#!/usr/bin/env python
# This is the first program for the 417 exercise, prompts user for info..
# Daryl Herzmann 11-14-99


import time, style, cgi, pg, sys
from functs import *

def ask_for_info(caseNum, key):
	print """
	<font color="red"><h2>MT 206 Severe Weather Forecasting:</h2></font>
	<P>In order to get credit for working through this exercise, you will need to fill in the information
	below.  Please fill in your name as it appears on Classnet. ex) John Smith

	<form method="POST" action="index.py">"""
	
	print '<input type="hidden" name="caseNum" value="'+caseNum+'">'	
	print '<input type="hidden" name="key" value="'+str(key)+'">'

	print """
	<font color="red"><H2>Enter your information:</H2></font>
	<TABLE border="0">
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your Name:</font>
		</TH><TD>
			<input size="40" MAXLENGTH="60" type="text" name="name">
		</TD></TR>
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your ISU 9 digit ID<BR> (no spaces or dashes):</font>
		</TH><TD>
			<input size="20" MAXLENGTH="9" type="text" name="SSN">
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

def mk_new_entry():
	key = str(int(float(time.time())))		# we generate the key that the user will be using for the day
	input = mydb.query("INSERT into "+usersTable+" VALUES ("+key+") ")	# Create the entry in the db
	return key


def Main():
	form = cgi.FormContent()
	if not form.has_key("caseNum"):
		style.SendError("No case number was supplied to this script")

	case_num = form["caseNum"][0]	

	key = mk_new_entry()
	
	svrTop("Blah")
	ask_for_info(case_num, key)

	svrBot()

Main()
