#!/usr/local/bin/python
# Simple program that outputs todays forecasts
# Daryl Herzmann 9-3-99

import pg, time, cgi

mydb = pg.connect('frcst')


def Main():
	form = cgi.FormContent()
	multi = int(form["multi"][0])
	class_name = form["class_name"][0]

	now = time.time() + multi*86400
	now_tuple = time.localtime(now)
	yeer = str(now_tuple[0])
	month = str(now_tuple[1])
	day = str(now_tuple[2])

	entries = mydb.query("SELECT * from forecasts WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid ~* '"+class_name+"' ").getresult()

	print 'Content-type: text/html \n\n'
	print '<PRE>'
	print 'USERID		YEAR   MONTH  DAY   DMX_HI DMX_LO DMX_PR DMX_SN FL_HI FL_LO FL_PR FL_SN'
	spacer = " "
	for i in range(len(entries)):
		this_entry = entries[i]
		print this_entry[0]+ (15 - len(this_entry[0]))*spacer ,
		for entry in this_entry:
			if entry[0] == "m":
				doy = "nothing"
			else:
				print entry+ (6 - len(entry))*spacer , 
		print 

	if len(entries) == 0:
		print '\n No forecasts were made for this particular day...\n'



Main()
