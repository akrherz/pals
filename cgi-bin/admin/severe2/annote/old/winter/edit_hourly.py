#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: With my new knowledge, I can do this correctly :)

import os, sys, regsub, style, posix, cgi, pg, time

mydb = pg.connect("arch_hourly")

def adds(comment, analysis):
        print '<H3>Edit Comments ( These appear at the top of the pages )</H3>'
	print '<textarea name="comments" cols="80" rows="10" WRAP>'+comment+'</textarea>'
        print '<H3>Edit analysis ( These are the Meteorological comments for the hour )</H3>'
        print '<textarea name="analysis" cols="80" rows="10" WRAP>'+analysis+'</textarea>'

def get_entry(secs, table_name):
	entries = mydb.query("SELECT * from "+table_name+" where ticks = '"+secs+"' ").getresult()
	return entries

def avail(day):
	files = posix.listdir('/home/httpd/html/archivewx/data/'+day)
	files.sort()
	print '<H3>Available files to link in:</H3>'
	print '<form name="dummy">'
	print '<SELECT>'
	for file in files:
		print '<OPTION>'+file
	print '</SELECT></form><HR>'

def Main():
	style.header("Edit Annotation","white")

	form = cgi.FormContent()
	try:
		secs = int(float(form["secs"][0]))
	except:
		style.SendError("CGI Parse Error")

	this_tuple = time.localtime(secs)
	yeer = str( time.strftime("%Y", this_tuple) )
	day = str( time.strftime("%d", this_tuple) )
	month = str( time.strftime("%m", this_tuple) )

	std_day = yeer+"_"+month+"_"+day

	table_name = "t"+str(yeer)

	entry = get_entry(str(secs), table_name)
	try:
		comment = entry[0][1]
	except IndexError:
		comment = "Write Something here"
	try:
		analysis = entry[0][2]
	except IndexError: 
                analysis = "Write Something here"

	real = time.strftime("%I %p", this_tuple)

	style.std_top('Edit entry for '+std_day+' at '+real)

	avail(std_day)

        print '<form method="post" action="add_hourly.py">'
	print '<input type="hidden" name="ticks" value="'+str(secs)+'">'
	print '<input type="hidden" name="table_name" value="'+table_name+'">'
	adds(comment, analysis)
	print '<input type="submit" value="Click to Save this Entry">'
	print '</form>'

	
	style.std_bot()

Main()

