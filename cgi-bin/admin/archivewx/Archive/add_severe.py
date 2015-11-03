#!/usr/local/bin/python
# Adds entries into the answers database
# Daryl Herzmann 8/8/98
# New System added : 5-27-99

from cgi import *
from pg import *
import os, sys, regsub

mydb = connect("archresults")


def add_entry(day, state, type, time):
	insert = mydb.query("insert into t"+day+" values('"+state+"','"+type+"','"+time+"')")
	print 'DONE'

def Main():
	form = FormContent()
	day = form["day"][0]
	state = form["state"][0]
	type = form["type"][0]
	time = form["time"][0]

	print 'Content-type: text/html \n\n'
	add_entry(day, state, type, time)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=edit_severe.py?day='+day+'">'
        print '</HEAD></HTML>'
	sys.exit(0)
Main()

