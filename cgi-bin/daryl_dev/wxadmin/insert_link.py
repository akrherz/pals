#!/usr/local/bin/python
# Inserts link into database
# Daryl Herzmann 9/19/98

import os, sys, regsub
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

	area = regsub.gsub(" ","_", area)
	spec = regsub.gsub(" ","_", spec)
	link = regsub.gsub(" ","_", link)
	url = regsub.gsub(" ","_", url)


	print 'Content-type: text/html \n\n'
	check = mydb.query("select * from mt101 where link = '"+url+"'").getresult()
	if len(check) > 0:
		delete = mydb.query("delete from mt101 where link = '"+url+"'")
		print "Deleted Old Entry"
	
	update = mydb.query("insert into mt101 values('"+area+"','"+spec+"','"+url+"','"+link+"')")		

	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="1; URL='+url+'">'
	print '</HEAD><BODY BGCOLOR="white">'
	print 'Successfully entered'
	
Main()
