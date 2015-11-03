#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: With my new knowledge, I can do this correctly :)

import os, sys, regsub, style, posix, cgi, pg, time, DateTime

mydb = pg.connect("severe2", 'localhost', 5432)

def adds(comment, analysis):
        print '<H3>Edit Comments ( These appear at the top of the pages )</H3>'
	print '<B>This is the only entry you need to make the Introduction</B>'
	print '<textarea name="comments" cols="80" rows="10" WRAP>'+comment+'</textarea>'
        print '<H3>Edit analysis ( These are the Meteorological comments for the hour )</H3>'
        print '<textarea name="analysis" cols="80" rows="10" WRAP>'+analysis+'</textarea>'

def get_entry(caseNum, ticks):
	thisDate = DateTime.gmtime(ticks)
	findDate = DateTime.ISO.strGMT(thisDate)

	entries = mydb.query("SELECT comments, analysis from annotations where ( validtime = '"+findDate+"' and casenum = '"+caseNum+"' )")

	entries = entries.getresult()
	return entries


def Main():
	style.header("Edit Annotation","white")

	form = cgi.FormContent()
	try:
		caseNum = form["caseNum"][0]
		zticks = form["zticks"][0]
	except:
		style.SendError("CGI Parse Error")

	entry  = get_entry(caseNum,  float( zticks ) )

	try:
		comment = entry[0][0]
	except IndexError:
		comment = "Write Something here"
	try:
		analysis = entry[0][1]
	except IndexError: 
                analysis = "Write Something here"

	localTuple = time.gmtime( float(zticks) )
	nowStr = time.strftime("%b %d, %Y -- %HZ", localTuple)

	style.std_top('Edit entry for '+nowStr)
	print """
	<HR>
		<a href="hourly.py">Select a different Case</a><BR>"""
	print '<a href="hourly.py?caseNum='+caseNum+'">Select a different Hour for this Case</a><BR><HR>'

        print '<form method="post" action="addHourly.py">'
	print '<input type="hidden" name="zticks" value="'+str(int(zticks))+'">'
	print '<input type="hidden" name="caseNum" value="'+str(caseNum)+'">'
	adds(comment, analysis)
	print '<BR><input type="submit" value="Click to Save this Entry">'
	print '</form>'

	
	style.std_bot()

Main()

