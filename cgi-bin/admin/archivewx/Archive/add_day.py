#!/usr/local/bin/python
# This sets up a new day into the system
# Daryl Herzmann 6-25-99

import os, cgi
from pg import *

mydb = connect('archresults')
mydb2 = connect('archdiary')

def create_table(day):
	try:
		make = mydb.query('CREATE TABLE "t'+day+'" (state varchar(40), severe varchar(5), date varchar(5))')
		make = mydb2.query('CREATE TABLE "t'+day+'" (ztime varchar(5), events varchar(4000), analysis varchar(4000))')


		make = mydb.query('grant all on "t'+day+'" to nobody')
		make = mydb2.query('grant all on "t'+day+'" to nobody')
		print day+' was successfully added'		

	except:
		print day+' has allready been added'
		sys.exit(0)

def Main():
	form = cgi.FormContent()
	yeer = form["yeer"][0]
	month = form["month"][0]
	day = form["day"][0]

	table_str = yeer+"_"+month+"_"+day

	print 'Content-type: text/html \n\n'
	
	print '<HTML><HEAD>'

	print '<meta http-equiv="Refresh" content="1; URL=/cgi-bin/svr_frcst/index.py?day='+day+'&month='+month+'&year='+yeer+'">'

	print '</HEAD><BODY>'

	create_table(table_str)

	print '</HTML>'
Main()

