#!/usr/local/bin/python
# This program enters the data into the db
# Daryl Herzmann 8-20-99

import pg, cgi, style

answersdb = pg.connect('severe2', 'localhost', 5432)

def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	state = form["state"][0]
	type = form["type"][0]
	etime = ""
	if caseNum[0] == "s":
		etime = form["etime"][0]
		if etime[0] == "(":
			style.SendError("Please Select a time:")	

	insert = answersdb.query("INSERT into answerkey(casenum, state, type, etime) VALUES ('"+caseNum+"','"+state+"', '"+type+"', '"+etime+"') ")

	print 'Content-type: text/html \n\n'
        print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=edit.py?caseNum='+caseNum+'">'
        print '</HEAD></HTML>'

Main()
