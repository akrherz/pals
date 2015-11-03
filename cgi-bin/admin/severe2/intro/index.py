#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# REWROTE 2-1-2000

import style, os, time, pg, std_form, cgi

mydb = pg.connect('severe2', 'localhost', 5432)

def listCases():
	cases = mydb.query("SELECT casenum, date(starttime) from cases order by starttime").getresult()

	print '<H3>Select A Case to Edit:</H3>'
	print '<SELECT name="caseNum" size="10">'
	for i in range(len(cases)):
		caseNum = cases[i][0]
		print '<option value="'+caseNum+'">'+caseNum+' --> '+cases[i][1]

	print '</SELECT>'

def Main():
	form = cgi.FormContent()
	style.header("Edit Introduction","white")
	style.std_top("Edit Case Introduction")

	print """
	<B>Instructions:</B><BR>This page edits the case introduction that appears immediately on the
	forecasting exercise.  This introduction is the basis for all of the versions of the exercise."""


	print '<form method="post" action="edit.py">'
	listCases()

	print '<BR><input type="submit" value="submit">'

	print '<HR>Links outta here:<HR>'
	print '<BR><a href="/admin">Admin Page</a>'	

Main()
