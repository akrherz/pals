#!/usr/local/bin/python
# Inserts link into database
# Daryl Herzmann 9/19/98

import os, sys
from cgi import *
from pg import *

mydb = connect("wx_links")

def cgi_error():
	print 'Your string is allready in the database, please go back and re-enter the correct data'
	sys.exit()

def Main():
	form = FormContent()
	area = form["area"][0]
	spec = form["spec"][0]
	link = form["link"][0]
	url = form["url"][0]
	user = form["user"][0]

	print 'Content-type: text/html \n\n'
	check = mydb.query("select * from "+user+" where link = '"+url+"'").getresult()
	if len(check) > 0:
		cgi_error()
	update = mydb.query("insert into "+user+" values('"+area+"','"+spec+"','"+url+"','"+link+"')")		

	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="1; URL='+url+'">'
	print '</HEAD><BODY BGCOLOR="white">'
	print 'Successfully entered'
	
Main()
