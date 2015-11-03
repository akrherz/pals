#!/usr/local/bin/python
# Adds entries into the diary database
# Daryl Herzmann 8/8/98

from cgi import *
from pg import *
import os, sys, regsub

mydb = connect("archadmin")


def add_entry(day, descrip):
	descrip = regsub.gsub("'","&180;", descrip)
	delete = mydb.query("delete from diary where entry = '"+day+"'")
	insert = mydb.query("insert into diary values('"+day+"','"+descrip+"')")
	print 'DONE'

def Main():
	form = FormContent()
	day = form["day"][0]
	descrip = form["descrip"][0]
	print 'Content-type: text/html \n\n'
	add_entry(day, descrip)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="1; URL=annote.py">'
        print '</HEAD></HTML>'
	sys.exit(0)
Main()

