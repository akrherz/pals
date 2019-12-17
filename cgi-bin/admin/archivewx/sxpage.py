#!/usr/local/bin/python
# This program displays what a page would look like on the svr_frcst page...
# Daryl Herzmann 12-7-99

import os, pg, cgi, svr_frcst, style, time, functs, DateTime, sys, SEVERE2


def Main():
	form = cgi.FormContent()
	try:
		year = int(form["year"][0])
		day = int(form["day"][0])
		month = int(form["month"][0])
		ztime = int(form["ztime"][0])
		version = form["version"][0]
		zswitch = form["zswitch"][0]
	except:
		style.SendError("Bzz, give me a date please...")

	myDate = DateTime.mktime(year, month, day, ztime, 0, 0, '','','0')
	secs = myDate.ticks()
	time_tuple = myDate.tuple()
	myDateStr = DateTime.ISO.strGMT(myDate)

	SEVERE2.setupPage()
        SEVERE2.printTime(myDateStr)

	dir_format = myDate.strftime("/archivewx/data/%Y_%m_%d/")
	print '<BASE HREF="https://pals.agron.iastate.edu'+dir_format+'">'

	if version == "basic":
	        functs.dbComments(myDateStr, "comments", "News and Notes:", zswitch)
	else:
	        functs.db_comments_417(secs, time_tuple, "comments", "News and Notes:", "mt417")


        functs.mk_data(time_tuple, 1)

	if version == "basic":
	        functs.dbComments(myDateStr, "analysis", "Meteorological Analysis:", zswitch)
	else:
	        functs.db_comments_417(secs, time_tuple, "analysis", "Meteorological Analysis:", "mt417")
	

	functs.finishPage()

Main()
