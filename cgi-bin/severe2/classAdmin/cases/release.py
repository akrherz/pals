#!/usr/local/bin/python
# This will allow instructors to release cases
# Daryl Herzmann 12-7-99

import pg, cgi, time, SEVERE2, os

form = cgi.FormContent()
className = os.environ["REMOTE_USER"]


mydb = pg.connect('severe2','localhost', 5432)
mydb2 = pg.connect('severe2_adv','localhost', 5432)

def list_cases2(className):
	print '<SELECT name="caseNum" size="10">'
	cases2 = mydb2.query("SELECT casenum from basecases_custom WHERE className = '"+className+"' ").getresult()
        cases2.sort()
        for i in range(len(cases2)):
                thiscase = cases2[i][0]
		cases = mydb.query("SELECT date(startTime) from cases WHERE casenum = '"+thiscase+"' ").getresult()
		startTime = cases[0][0]
		print '<OPTION value="'+thiscase+'">'+thiscase+'  '+startTime
        print '</SELECT><BR>'


def Main():
	if form.has_key("type"):
		caseNum = form["caseNum"][0]
		type = form["type"][0]
		if type == "add":
			delete = mydb2.query("DELETE from basecases_custom WHERE caseNum = '"+caseNum+"' and className = '"+className+"' ")
			hello = mydb2.query("INSERT into basecases_custom(casenum, className) VALUES ('"+caseNum+"', '"+className+"')")
		else:
			hello = mydb2.query("DELETE from basecases_custom WHERE caseNum = '"+caseNum+"' and className = '"+className+"' ")


	SEVERE2.setupPage("Add/Revoke Cases to the System.")

	print """
	<blockquote>
	<B>Instructions:</B> This dialog releases and revokes which cases your students can work with.  When your students access the
	main page, they are presented with a listing of cases that you have released to them to work.  That listing is controled from 
	this dialog.  Removing or adding cases DOES NOT delete any work done on the specific questions nor the comments.
	</blockquote>
	"""

	print '<H3 align="CENTER">Pick A Case</H3>'

	print '<P>Release or remove cases to your hearts content.'

	print '<TABLE WIDTH="100%"><TR><TD>'
	print '<H3>Cases available</H3>'
	print '<FORM name="add" METHOD="POST" ACTION="release.py">'
	print '<input type="hidden" name="type" value="add">'
	print '<input type="hidden" name="className" value="'+className+'">'
	SEVERE2.listGoodCases()
	print '<input type="submit" value="Add This Case">'
	print '</form><BR>'

	print '</TD><TD>'
	
	print '<H3>Cases allready released</H3>'
	print '<FORM name="del" METHOD="POST" ACTION="release.py">'
	print '<input type="hidden" name="className" value="'+className+'">'
	print '<input type="hidden" name="type" value="del">'
	list_cases2(className)
	print '<input type="submit" value="Delete This Case">'
	print '</form><BR>'

	print '</TD></TR></TABLE>'

	print '<a href="../index.py">ClassAdmin Homepage</a>'

	SEVERE2.finishPage()

Main()
