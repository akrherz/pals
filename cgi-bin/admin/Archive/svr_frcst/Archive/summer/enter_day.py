#!/usr/local/bin/python
# This program enters a day into the database system
# Daryl Herzmann	8-12-99

import pg, cgi, time, style

mydb = pg.connect('archadmin')


def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	start_day = int(form["start_day"][0])
	start_month = int(form["start_month"][0])
	start_year = int(form["start_year"][0])

	casenum = form["casenum"][0]

	start_tuple = (start_year, start_month, start_day, 0, 0, 0, 0, 0, 0)
	end_tuple = (start_year, start_month, start_day, 24, 0, 0, 0, 0, 0)

	start_secs = time.mktime(start_tuple)
	end_secs = time.mktime(end_tuple)

	if end_secs < start_secs :
		style.SendError("Your end time is before your start time")

	mydb.query("INSERT into summer_cases values ('"+casenum+"', '"+str(start_secs)+"', '"+str(end_secs)+"') ")

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=add_day.py">'
        print '</HEAD>'
        print '<body>'
        print '</HTML>'


Main()
