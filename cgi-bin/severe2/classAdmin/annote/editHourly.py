#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: With my new knowledge, I can do this correctly :)

import os, sys, regsub, style, posix, cgi, pg, time, DateTime, SEVERE2

mydb = pg.connect("severe2", 'localhost', 5432)
mydb1 = pg.connect("severe2_adv", 'localhost', 5432)
className = os.environ["REMOTE_USER"]

def adds(comment, analysis):
        print '<H3>Edit Comments ( These appear at the top of the pages )</H3>'
	print '<textarea name="comments" cols="80" rows="10" WRAP>'+comment+'</textarea>'
        print '<H3>Edit analysis ( These are the Meteorological comments for the hour )</H3>'
        print '<textarea name="analysis" cols="80" rows="10" WRAP>'+analysis+'</textarea>'

def get_entry(caseNum, ticks):
	thisDate = DateTime.gmtime(ticks)
	findDate = DateTime.ISO.strGMT(thisDate)

	entries1 = mydb.query("SELECT comments, analysis from annotations where ( validtime = '"+findDate+"' and casenum = '"+caseNum+"' )")
	entries2 = mydb1.query("SELECT comments, analysis from annotations where ( validtime = '"+findDate+"' and casenum = '"+caseNum+"' )")
	entries3 = mydb1.query("SELECT comments, analysis from annotations_custom where ( validtime = '"+findDate+"' and casenum = '"+caseNum+"' and className = '"+className+"')")

	entries1 = entries1.dictresult()
	entries2 = entries2.dictresult()
	entries3 = entries3.dictresult()
	if len(entries3) > 0:
		return entries3
	if len(entries2) > 0:
		return entries2
	return entries3


def Main():
	form = cgi.FormContent()
	try:
		caseNum = form["caseNum"][0]
		zticks = form["zticks"][0]
	except:
		style.SendError("CGI Parse Error")

	entry  = get_entry(caseNum,  float( zticks ) )

	try:
		comment = entry[0]["comments"]
	except IndexError:
		comment = "Write Something here"
	try:
		analysis = entry[0]["analysis"]
	except IndexError: 
                analysis = "Write Something here"

	localTuple = time.localtime( float(zticks) )
	nowStr = time.strftime("%b %d, %Y -- %HZ", localTuple)

	SEVERE2.setupPage("classAdmin for Sx Wx Activity")
	print '<H3 align="center">Edit annotation for '+nowStr+'</H3>'
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

	print '<P><a href="../index.py">Back to ClassAdmin</a>'

	SEVERE2.finishPage()	

Main()

