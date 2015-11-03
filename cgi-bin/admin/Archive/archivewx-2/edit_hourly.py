#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98

from cgi import *
from pg import *
import os, sys, regsub, style

mydb = connect("archdays")

form = FormContent()
day = form["day"][0]
hour = form["hour"][0]

def adds(comment, analysis):
        print '<form method="post" action="add_hourly.py">'
        print '<H3>Edit Comments ( These appear at the top of the pages )</H3>'
	print '<textarea name="comments" cols="80" rows="10">'+comment+'</textarea>'
        print '<H3>Edit analysis ( These are the Meteorological comments for the hour )</H3>'
        print '<textarea name="analysis" cols="80" rows="10">'+analysis+'</textarea>'
        print '<input type="hidden" name="day" value="'+day+'">'
	print '<input type="hidden" name="hour" value="'+hour+'"><BR>'
	print '<input type="submit" value="Click to Save this Entry">'

def get_entry():
	entries = mydb.query("SELECT * from "+day+" where ztime = '" + hour+"'")
	entries = entries.getresult()
	return entries

def Main():
	style.header("Edit Annotation","white")
	entry = get_entry()
	try:
		comment = entry[0][1]
	except IndexError:
		comment = "Write Something here"
	try:
		analysis = entry[0][2]
	except IndexError: 
                analysis = "Write Something here"
	real = str(int(hour)-(17))
	style.std_top('Edit entry for '+day+' at '+real+' PM')

	adds(comment, analysis)
	
	style.std_bot()

	sys.exit(0)
Main()
