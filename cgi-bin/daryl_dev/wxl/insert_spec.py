#!/usr/local/bin/python
# Inserts spec into database
# Daryl Herzmann 9/19/98

import os, sys
from cgi import *
from pg import *

mydb = connect("wx_areas")

def cgi_error():
	print 'The string you entered is allready in the database, please re-enter the data.'
	sys.exit()

def Main():
	form = FormContent()
	area = form["area"][0]
	spec = form["spec"][0]
	user = form["user"][0]

	print 'Content-type: text/html \n\n'

	check = mydb.query("select * from "+user+" where area = '"+area+"' and spec = '"+spec+"'").getresult()
	if len(check) > 0:
		cgi_error()
	update = mydb.query("insert into "+user+" values('"+area+"','"+spec+"')")		

	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="1; URL=top.py?user='+user+'&area='+area+'&spec='+spec+'&auth=yes">'
	print '</HEAD><BODY BGCOLOR="white">'
	print 'Added Successfully'
	
Main()
