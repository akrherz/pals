#!/usr/local/bin/python
# Adds entries into the hourly database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: "Finally, The Rock has come back to add_hourly", -Dwayne Johnson

import os, sys, regsub, cgi, pg

mydb = pg.connect("severe2", 'localhost', 5432)

def add_entry(comments, caseNum):
	comments = regsub.gsub("'","&#180;", comments)
	delete = mydb.query("delete from intro WHERE casenum = '"+caseNum+"' ") 	
	insert = mydb.query("insert into intro (casenum, comments) values('"+caseNum+"','"+comments+"')")
	print 'DONE'

def Main():
	form = cgi.FormContent()
	comments = form["comments"][0]
	caseNum = form["caseNum"][0]

	print 'Content-type: text/html \n\n'
	add_entry(comments, caseNum)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=index.py">'
	print '</HEAD>'
	print '<body>'
	print '</HTML>'

Main()

