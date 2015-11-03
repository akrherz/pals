#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# REWROTE 2-1-2000

import style, os, time, pg, std_form, cgi

mydb = pg.connect('svr_frcst')

def listCases():
	cases = mydb.query("SELECT * from cases order by start_secs").getresult()

	print '<H3>Select A Case to Edit:</H3>'
	print '<SELECT name="caseNum" size="10">'
	for i in range(len(cases)):
		caseNum = cases[i][0]
		thisTuple = time.localtime( float(cases[i][1]) )
		print '<option value="'+caseNum+'">'+caseNum+' --> '+time.strftime("%b %d, %Y", thisTuple)

	print '</SELECT>'

def Main():
	form = cgi.FormContent()
	className = form["className"][0]
	style.header("Edit Introduction","white")
	style.std_top("Edit Case Introduction:")

	print '<form method="post" action="edit.py">'
	print '<input type="hidden" name="className" value="'+className+'">'
	listCases()

	print '<input type="submit" value="submit">'

	print '<HR>Links outta here:<HR>'
	print '<BR><a href="/admin">Admin Page</a>'	

Main()
