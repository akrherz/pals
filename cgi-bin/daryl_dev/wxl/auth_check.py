#!/usr/local/bin/python
# This checks for the correct password and then sets them down the road
# Daryl Herzmann 10/7/98

import os
from cgi import *
from pg import *

mydb = connect('wx_areas')

def Main():
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'

	form = FormContent()
	user = form["user"][0]
	pass_try = form["pass"][0]

	pass_real = mydb.query("select password from users where user = '"+user+"'").getresult()

	if pass_real[0][0] == pass_try:
		print '<meta http-equiv="Refresh" content="1; URL=top.py?user='+user+'&auth=yes">'
		print '</HEAD><BODY BGCOLOR="white" text="blue">'
		print "<H3>You are authenticated to use <B>"+user+"'s</B> database....</H3>"
	else:	
		print '<meta http-equiv="Refresh" content="1; URL=top.py?user='+user+'&auth=no">'
		print '</HEAD><BODY BGCOLOR="white" text="blue">'
		print '<H3> You did not authenticate: <BR> You will only have read access...</H3>'

Main()
