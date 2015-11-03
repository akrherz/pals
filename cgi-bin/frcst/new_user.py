#!/usr/local/bin/python
# This creates a new account for the students
# Daryl Herzmann 8-31-99
# 9-1-99: Clean up Code

import cgi, style

def instructions():
	print '<H4>Instructions:</H4>'
	print '<P>This form is to create a new user account for the forecasting exercise. '
	print ' You should fill out the form and then click on the submit button.'


def Main():
	form = cgi.FormContent()
	try:
		class_name = form["class"][0]
	except:
		style.SendError("I do not know what class you are from")

	style.header("Create an Account", "white")

	print '<H3>Create account for the '+class_name+' forecasting exercise</H3>'

	instructions()

	print '<form method="POST" action="enter_user.py">'
	print '<input type="hidden" name="class_name" value="'+class_name+'">'

	print 'Enter your full name: <BR>'
	print '<input type="text" name="full_name" MAXLENGTH="50" size="30"><BR>'

	print 'Enter your ISU email address:<BR>'
	print '<input name="email" type="text" MAXLENGTH="50" size="30"><BR>'

	print 'Enter a password for your account: <BR>'
	print '<input name="passwd1" type="password" size="8" MAXLENGTH="8"><BR>'
	print 'Validate your password: <BR>'
	print '<input name="passwd2" type="password" size="8" MAXLENGTH="8"><BR>'

	print '<input type="submit" value="Submit">'
	print '<input type="reset">'
Main()
