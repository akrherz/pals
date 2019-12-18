#!/usr/bin/python2
# This program will generate a ClassNet like output...
# Daryl Herzmann 12-7-99

import pg, cgi, sys, time, functs, mx.DateTime

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")

def list_cases(caseType):
#	print '<SELECT name="caseNum" size="10">'
#	cases2 = mydb.query("SELECT casenum from intcases").getresult()
#	cases2.sort()
# 	for i in range(len(cases2)):
#		thiscase = cases2[i][0]
#		cases = mydb.query("SELECT date(starttime) from cases WHERE casenum = '"+thiscase+"' ").dictresult()
#		print '<OPTION value="'+thiscase+'">'+thiscase+'  '+cases[0]["starttime"][:10]
#	print '</SELECT><BR>'

	cases = mydb.query("SELECT casenum from intcases WHERE caseNum ~* '"+caseType+"' ").getresult()
	cases.sort()
#	print '<MULTICOL COLS="3">'
	for i in range(len(cases)):
		thisCase = cases[i][0]
		startTime = mydb.query("SELECT date(startTime) from cases WHERE caseNum = '"+thisCase+"' ").getresult()

		startDate = mx.DateTime.ISO.ParseDateTimeGMT(startTime[0][0])
		print '<a href="/cgi-bin/severe2/intermediate/intro.py?caseNum='+thisCase+'">'+startDate.strftime("%d %B %Y")+'</a>'
		print '&nbsp; &nbsp; &nbsp; &nbsp; '
		if (i%3 == 0 and i != 0):
			print '<BR>'
#	print '</MULTICOL>'

def Main():
	functs.setupPage()

	form = cgi.FormContent()

	print """<CENTER>
	<img src="/icons/svrTop.gif">
	</CENTER>

	<dd>The Severe Weather Forecasting Exercise is a web-based exercise that is designed to stimulate interest in severe weather. This
exercise is being developed for use by all levels of meteorologists and K-12 students as well. Because of the wide range of skills
among users, there are three versions of the forecasting exercise.</dd>

	<dd>The exercise is worked by trying one of the cases below.  The case uses archived data and prepared questions to guide the user
thoughout the cases duration.  Currently, we have two types of cases: the "Summer-like Events" contain questions that concern summer
like severe weather (tornado, hail, heavy rain), and the "Winter-like Events" stress winter severe weather phenonema.</dd>

	<H2><font color="#a0522d">Intermediate Version:</font></H2>	
	"""


	print "<H3>Summer-like Events:</H3>"
	list_cases("s")

	print "<H3>Winter-like Events:</H3>"
	list_cases("w")


	functs.finishPage()

Main()
