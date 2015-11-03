#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: With my new knowledge, I can do this correctly :)

import os, sys, regsub, style, posix, cgi, pg, time

mydb = pg.connect("svr_mt417")
mydb2 = pg.connect("svr_frcst")

def adds(comment, analysis):
        print '<H3>Edit Comments ( aka News & Notes )</H3>'
	print '<B>This is the only entry you need to make for the 7am kick-start</B>'
	print '<textarea name="comments" cols="80" rows="10" WRAP>'+comment+'</textarea>'
        print '<H3>Edit analysis ( These are the Meteorological comments for the hour )</H3>'
        print '<textarea name="analysis" cols="80" rows="10" WRAP>'+analysis+'</textarea>'

def get_entry(ticks, yeer):
	entries = mydb.query("SELECT * from annote where ztime = '"+ticks+"' ").getresult()
	entries2 = mydb2.query("SELECT * from annote_"+yeer+" where ztime = '"+ticks+"' ").getresult()

	if len(entries) > 0:
		return entries
	else:
		return entries2

def Main():
	style.header("Edit Annotation","white")

	form = cgi.FormContent()
	try:
		day = int(form["day"][0])
		month = int(form["month"][0])
		yeer = int(form["yeer"][0])
		ztime = int(form["ztime"][0])
		case = form["case"][0]
	except:
		style.SendError("CGI Parse Error")
	print case

	time_tuple = (yeer, month, day, ztime, 0, 0, 0, 0, 0)
	if case == "summer":
		time_tuple = (yeer, month, day, ztime, 0, 0, 0, 0, 1)
	ticks = time.mktime(time_tuple)


	entry = get_entry(str(int(ticks)), str(yeer))
	try:
		comment = entry[0][1]
	except IndexError:
		comment = "Write Something here"
	try:
		analysis = entry[0][2]
	except IndexError: 
                analysis = "Write Something here"


	style.std_top('Edit entry for '+str(month)+'-'+str(day)+'-'+str(yeer)+' @'+str(ztime)+'Z ')

        print '<form method="post" action="add_hourly.py">'
	print '<input type="hidden" name="ticks" value="'+str(int(ticks))+'">'
	print '<input type="hidden" name="case" value="'+case+'">'
	print '<input type="hidden" name="table_name" value="annote">'
	adds(comment, analysis)
	print '<input type="submit" value="Click to Save this Entry">'
	print '</form>'

	
	style.std_bot()

Main()

