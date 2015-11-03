#!/usr/local/bin/python
# This program generates a listing of cases allready in the database
# Daryl Herzmann 8-26-99

import style, time, pg

casesdb = pg.connect('severe2', 'localhost', 5432)

def cases(typ):
	casesdb.query("SET TIME ZONE 'GMT'")
	entries = casesdb.query("SELECT date(starttime), date_part('hour', starttime), date(endtime), date_part('hour', endtime), casenum from cases WHERE casenum ~* '"+typ+"' ").getresult()
	entries.sort()

	print '<PRE>'
	for i in range(len(entries)):
		caseNum = entries[i][-1]
		print caseNum+" == "+entries[i][0]+" "+str(int(entries[i][1]))+"Z -- "+entries[i][2]+" "+str(int(entries[i][3]))+"Z"
	print '</PRE>'


def Main():
	style.header("Edit cases for the forecasting excercise", "white")
	style.std_top("Case Listing")

	print '<H3 align="CENTER">Case administration</H3>'
	print '<BR>'
	print '<TABLE cellpadding="3" border="1">'
	print '<TR><TH>Winter Cases</TH><TH>Summer Cases</TH></TR>'
	print '<TR><TD>'
	cases("w")
	print '</TD><TD>'
	cases("s")
	print '</TD></TR></TABLE>'

	print '<BR><BR><BR>'

	print '<a href="edit.py?caseType=w">Add a winter case</a><BR>'
	print '<a href="edit.py?caseType=s">Add a summer case</a><BR>'



Main()
