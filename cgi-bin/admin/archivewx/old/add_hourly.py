#!/usr/local/bin/python
# Adds entries into the hourly database
# Daryl Herzmann 8/8/98

from cgi import *
from pg import *
import os, sys, regsub

mydb = connect("archdiary")


def add_entry(day, hour, comments, analysis):
	comments = regsub.gsub("'","&#180;", comments)
	analysis = regsub.gsub("'","&#180;", analysis)
	delete = mydb.query("delete from t"+day+" where ztime = '"+hour[0:2]+"'")
	insert = mydb.query("insert into t"+day+" values('" + hour+"','"+comments+"','"+analysis+"')")
	print 'DONE'

def Main():
	form = FormContent()
	day = form["day"][0]
	hour = form["hour"][0]
	comments = form["comments"][0]
	analysis = form["analysis"][0]

	print 'Content-type: text/html \n\n'
	add_entry(day, hour, comments, analysis)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="1; URL=hourly.py">'
	print '</HEAD>'
	print '<body>'
	print '</HTML>'
	sys.exit(0)
Main()

