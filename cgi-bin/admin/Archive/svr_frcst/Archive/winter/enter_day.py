#!/usr/local/bin/python
# This program enters a day into the database system
# Daryl Herzmann	8-12-99

import pg, cgi, time, style

mydb = pg.connect('archadmin')
resultsdb = pg.connect('archresults')

def fix_secs(secs):
	gmt_tuple = time.gmtime(secs)
	if gmt_tuple[3] != 0 and gmt_tuple[3] != 3 and gmt_tuple[3] != 6 and gmt_tuple[3] != 9 and gmt_tuple[3] != 12 and gmt_tuple[3] != 15 and gmt_tuple[3] != 18 and gmt_tuple[3] != 21:
		return secs + 3600
	else:
		return secs


def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	start_day = int(form["start_day"][0])
	start_month = int(form["start_month"][0])
	start_year = int(form["start_year"][0])
	end_day = int(form["end_day"][0])
	end_month = int(form["end_month"][0])
	end_year = int(form["end_year"][0])
#	end_hour = int(form["end_hour"][0])
#	start_hour = int(form["start_hour"][0])

	casenum = form["casenum"][0]

	start_tuple = (start_year, start_month, start_day, 0, 0, 0, 0, 0, 0)
	end_tuple = (end_year, end_month, end_day, 24, 0, 0, 0, 0, 0)

	start_secs = time.mktime(start_tuple)
	end_secs = time.mktime(end_tuple)

	start_secs = fix_secs(start_secs)
	end_secs = fix_secs(end_secs) 

	if end_secs < start_secs :
		style.SendError("Your end time is before your start time")

	resultsdb.query("CREATE table w"+casenum+" (state varchar(50), type varchar(20) )")
	mydb.query("INSERT into winter_cases values ('"+casenum+"', '"+str(start_secs)+"', '"+str(end_secs)+"') ")

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=add_day.py">'
        print '</HEAD>'
        print '<body>'
        print '</HTML>'


Main()
