#!/usr/local/bin/python
# This program prompts for the password for athentication
# Daryl Herzmann 10/6/98

import os
from cgi import *

def Main():
	form = FormContent()
	user = form["user"][0]

	print 'Content-type: text/html \n\n'

	print '<HTML><HEAD></HEAD><BODY bgcolor="white" text="blue">'
	print '<form method="POST" action="auth_check.py">'
	print '<input type="hidden" name="user" value="'+user+'">'
	print 'Authentification for '+user+':<BR>'
	print 'Please Enter the password'
	print '<input type="password" name="pass">'
	print '<input type="submit" value="authenticate">' 

	print '<spacer type="horizontal" size="50">'
	print '<a href="top.py?user='+user+'&auth=no">Or just browse by clicking here</a>'

	print '</HTML>'

Main()
