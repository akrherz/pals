#!/usr/local/bin/python
# This program enters a day into the database system
# Daryl Herzmann	9-13-99

import pg, cgi, time, style

mydb = pg.connect('severe2','localhost', 5432)

def cases(typ):
        mydb.query("SET TIME ZONE 'GMT'")
	i = 100
	tester = 'hi'
	while (tester == 'hi'):
		i = i+1
		thisCase = typ+str(i)
		results = mydb.query("SELECT * from cases WHERE casenum = '"+thisCase+"' ").getresult()
		if len(results) > 0:
			tester = 'hi'
		else:
			tester = 'bye'

        return thisCase

def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	start_day = form["start_day"][0]
	start_month = form["start_month"][0]
	start_yeer = form["start_yeer"][0]
	start_ztime = form["start_ztime"][0]

	end_day = form["end_day"][0]
	end_month = form["end_month"][0]
	end_yeer = form["end_yeer"][0]
	end_ztime = form["end_ztime"][0]

	caseType = form["caseType"][0]

	caseNum = cases(caseType)

	startStr = start_yeer+"-"+start_month+"-"+start_day+" "+start_ztime+":00"
	endStr = end_yeer+"-"+end_month+"-"+end_day+" "+end_ztime+":00"

	mydb.query("SET TIME ZONE 'GMT'")
	mydb.query("INSERT into cases(casenum, starttime, endtime) values ('"+caseNum+"', '"+startStr+"', '"+endStr+"') ")

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=list.py">'
        print '</HEAD>'
        print '<body>'

#	print "INSERT into cases(casenum, starttime, endtime) values ('"+caseNum+"', '"+startStr+"', '"+endStr+"') "

        print '</HTML>'


Main()
