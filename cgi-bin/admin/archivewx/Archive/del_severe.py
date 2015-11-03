#!/usr/local/bin/python
# Deletes entries for the Archive
# Daryl Herzmann 8/8/98
# New system: 5-27-99

from cgi import *
from pg import *
import os, sys, regsub

mydb = connect("archresults")


def add_entry(day, state, severe, time):
	print state, severe, time
	delete = mydb.query("delete from t"+day+" where state = '"+state+"' AND severe = '"+severe+"' AND date = '"+time+"'")
	print 'DONE'

def Main():
	form = FormContent()
	day = form["day"][0]
	num = form["num"][0]

	entries = mydb.query("Select * from t"+day).getresult()
	entries.sort()
	print 'Content-type: text/html \n\n'
	for i in range(len(entries)):
		if i == int(num):	
			state = entries[i][0]
			type = entries[i][1]
			time = entries[i][2]

	add_entry(day, state, type, time)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="1; URL=edit_severe.py?day='+day+'">'
        print '</HEAD></HTML>'
	sys.exit(0)
Main()

