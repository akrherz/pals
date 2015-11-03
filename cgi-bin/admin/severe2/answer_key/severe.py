#!/usr/local/bin/python
# New graders for the cases...
# Daryl Herzmann 8-19-99

import sys, style, os, posix, pg, time

admindb = pg.connect('severe2', 'localhost', 5432)

def which_days():
	print '<H3>Which case do you want to create answers for?</H3>'

	cases = admindb.query("SELECT casenum from cases ").getresult()
	cases.sort()

	print '<select name="caseNum" size="10">'
	for i in range(len(cases)):
		caseNum = cases[i][0]
		print '<option value="'+caseNum+'">'+caseNum

	print '</select>'

def closing():
	print '<HR>'
	print '<input type="submit" value="submit">'


def Main():
	style.header("Edit Severe Forecast results","white")
	style.std_top("Edit answer key for what case??")
	print '<form method="post" action="edit.py">'
	print '<BR>'
	which_days()
	closing()
	style.std_bot()
Main()
