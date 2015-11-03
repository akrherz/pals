#!/usr/local/bin/python
# Adds entries into the hourly database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: "Finally, The Rock has come back to add_hourly", -Dwayne Johnson

import os, sys, regsub, cgi, pg

mydb = pg.connect("arch_hourly")

def add_entry(ticks, comments, analysis, table_name):
	comments = regsub.gsub("'","&#180;", comments)
	analysis = regsub.gsub("'","&#180;", analysis)
	delete = mydb.query("delete from "+table_name+" WHERE ticks = '"+ticks+"' ") 	
	insert = mydb.query("insert into "+table_name+" values('"+ticks+"','"+comments+"','"+analysis+"')")
	print 'DONE'

def Main():
	form = cgi.FormContent()
	ticks = form["ticks"][0]
	comments = form["comments"][0]
	analysis = form["analysis"][0]
	table_name = form["table_name"][0]

	print 'Content-type: text/html \n\n'
	add_entry(ticks, comments, analysis, table_name)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly.py">'
	print '</HEAD>'
	print '<body>'
	print '</HTML>'
	sys.exit(0)
Main()

