#!/usr/local/bin/python
# This program lists out available hours to edit
# Daryl Herzmann 8-20-99

import pg, cgi, style, time

admindb = pg.connect('archadmin')

def list_options(case_num):
	print '<SELECT name="secs">'
	entry = admindb.query("SELECT start_secs, end_secs from winter_cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float(entry[0][0]))
	end_secs = int(float(entry[0][1]))

	intervals = int ((end_secs - start_secs) / 10800 )

	for i in range(intervals):
		this_secs = start_secs + (i*10800) 
		this_tuple = time.gmtime(this_secs) 
		nice_date = time.strftime("%H Z --  %x", this_tuple)
		print '<option value="'+str(this_secs)+'">'+nice_date

	print '</SELECT>'


def Main():
	form = cgi.FormContent()
	case_num = form["case_num"][0]

	style.header("Pick which hour", "white")

	print '<form method="POST" action="edit_hourly.py">'
	list_options(case_num)

	print '<input type="submit" name="Edit this annotation">'
	print '</form>'


Main()
