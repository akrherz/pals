#!/usr/local/bin/python
# Adds entries into the hourly database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: "Finally, The Rock has come back to add_hourly", -Dwayne Johnson

import os, sys, regsub, cgi, pg, DateTime

mydb = pg.connect("severe2_adv", 'localhost', 5432)
className = os.environ["REMOTE_USER"]


def add_entry(ticks, comments, analysis, caseNum):
	comments = regsub.gsub("'","&#180;", comments)
	analysis = regsub.gsub("'","&#180;", analysis)

	thisDate = DateTime.gmtime(ticks)
        findDate = DateTime.ISO.strGMT(thisDate)

	delete = mydb.query("delete from annotations_custom WHERE validtime = '"+findDate+"' and casenum = '"+caseNum+"' and className = '"+className+"' ") 	
	insert = mydb.query("insert into annotations_custom (validtime, comments, analysis, casenum, className) values('"+findDate+"','"+comments+"','"+analysis+"','"+caseNum+"', '"+className+"')")
	print 'DONE'

def Main():
	form = cgi.FormContent()
	zticks = form["zticks"][0]
	comments = form["comments"][0]
	analysis = form["analysis"][0]
	caseNum = form["caseNum"][0]

	print 'Content-type: text/html \n\n'
	add_entry(zticks, comments, analysis, caseNum)
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly.py?caseNum='+caseNum+'">'
	print '</HEAD>'
	print '<body>'
	print '</HTML>'

Main()

