#!/usr/local/bin/python
# This will allow instructors to release cases
# Daryl Herzmann 12-7-99

import pg, cgi, time

form = cgi.FormContent()
mydb = pg.connect('severe2','localhost', 5432)

def list_cases2():
	print '<SELECT name="caseNum" size="10">'
	cases2 = mydb.query("SELECT casenum from intcases").getresult()
        cases2.sort()
        for i in range(len(cases2)):
                thiscase = cases2[i][0]
		cases = mydb.query("SELECT date(startTime) from cases WHERE casenum = '"+thiscase+"' ").getresult()
		startTime = cases[0][0]
		print '<OPTION value="'+thiscase+'">'+thiscase+'  '+startTime
        print '</SELECT><BR>'


def list_cases():
	print '<SELECT name="caseNum" size="10">'
	
	cases = mydb.query("SELECT casenum, date(startTime) from cases").getresult()
	cases.sort()
	for i in range(len(cases)):
		thiscase = cases[i][0]
		startTime = cases[i][1]
		print '<OPTION value="'+thiscase+'">'+thiscase+'  '+startTime
	print '</SELECT><BR>'

def Main():
	if form.has_key("type"):
		caseNum = form["caseNum"][0]
		type = form["type"][0]
		if type == "add":
			delete = mydb.query("DELETE from intcases WHERE caseNum = '"+caseNum+"' ")
			hello = mydb.query("INSERT into intcases VALUES ('"+caseNum+"')")
		else:
			hello = mydb.query("DELETE from intcases WHERE caseNum = '"+caseNum+"' ")


	print 'Content-type: text/html \n\n'

	print '<H3 align="CENTER">Pick A Case</H3>'

	print '<P>Release or remove cases to your hearts content.'

	print '<TABLE WIDTH="100%"><TR><TD>'
	print '<H3>Cases available</H3>'
	print '<FORM name="add" METHOD="POST" ACTION="release.py">'
	print '<input type="hidden" name="type" value="add">'
	list_cases()
	print '<input type="submit" value="Add This Case">'
	print '</form><BR>'

	print '</TD><TD>'
	
	print '<H3>Cases allready released</H3>'
	print '<FORM name="del" METHOD="POST" ACTION="release.py">'
	print '<input type="hidden" name="type" value="del">'
	list_cases2()
	print '<input type="submit" value="Delete This Case">'
	print '</form><BR>'

	print '</TD></TR></TABLE>'

	print '<HR><a href="/admin/index.html">Back to Admin Page</a>'

Main()
