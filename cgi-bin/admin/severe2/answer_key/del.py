#!/usr/local/bin/python
# This program deletes entries in the db system
# Daryl Herzmann 8-20-99

import cgi, pg, string

answerdb = pg.connect('severe2', 'localhost', 5432)

def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	entry = form["entry"][0]

	parts = string.split(entry)
	state = parts[0]
	type = parts[1]
	etime = ""
	if caseNum[0] == "s":
		etime = parts[2]

	delete = answerdb.query("DELETE from answerkey WHERE state = '"+state+"' AND type = '"+type+"' AND etime = '"+etime+"' AND casenum = '"+caseNum+"' ") 

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=edit.py?caseNum='+caseNum+'">'
        print '</HEAD></HTML>'

Main()
