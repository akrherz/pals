#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# REWROTE 2-1-2000

import style, os, time, pg, std_form, cgi, DateTime

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")

def listHours(caseNum):
	cases = mydb.query("select date_part('hour', age(endtime, starttime)), starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()
	starttime = cases[0][1]	
	endtime = cases[0][2]

	startDate = DateTime.ISO.ParseDateTime(starttime)
	startSecs = startDate.gmticks()

	endDate = DateTime.ISO.ParseDateTime(endtime)
	endSecs = endDate.gmticks()


	multi = 1
	if caseNum[0] == "w":
		multi = 3

	now = startSecs

	print '<H3>Select A Hour to Edit:</H3>'
	print '<SELECT name="zticks" onChange="parent.display.location=this.form.zticks.options[this.form.zticks.selectedIndex].value">'
	while ( now <= endSecs ):
		thisTuple = time.gmtime(now)
		print '<option value="'+str(int(float(now)))+'">'+time.strftime("%b %d, %Y %HZ", thisTuple)
		now = now + multi*3600
	print '</SELECT>'

def listCases():
	cases = mydb.query("SELECT casenum, starttime from cases order by starttime").getresult()

	print '<H3>Select A Case to Edit:</H3>'
	print '<SELECT name="caseNum" onChange="location=this.form.caseNum.options[this.form.caseNum.selectedIndex].value">

	for i in range(len(cases)):
		caseNum = cases[i][0]
		print '<option value="'+caseNum+'">'+caseNum+' --> '+cases[i][1][:13]+'Z'

	print '</SELECT>'

def Main():
	form = cgi.FormContent()
	style.header("Edit Hourly Reports","white")
	style.std_top("Edit Hourly Reports")


	print '<B>Information:</B> <dd>This is the date and time selection page for the Severe Forecasting Excercise.</dd><BR>'
	print '<B>Instruction:</B> <dd>Select the desired day and time and then click on "submit."</dd><BR>'
	print '<B>Scope of this program:</B> <dd>This set of programs modifies ALL of the hourly annotations available to ALL excercises.</dd><BR>'
	print '<B>NOTE:</b><dd>If you are wanting to edit the preview for a case, you will want to edit the first hour that the exercise runs for.</dd>'
	print '<HR>'

	if form.has_key("caseNum"):
		print """
		<HR>
		<a href="hourly.py">Select a different Case</a><BR><HR>"""

		print '<form method="post" action="editHourly.py">'
		print '<input type="hidden" value="'+form["caseNum"][0]+'" name="caseNum">'
		listHours( form["caseNum"][0] )
	else:
		print '<form method="post" action="hourly.py">'
		listCases()

	print '<input type="submit" value="submit">'

	print '<HR>Links outta here:<HR>'
	print '<BR><a href="/admin">Admin Page</a>'	

Main()
