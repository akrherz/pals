#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98

from cgi import *
from pg import *
import os, sys, regsub, style

mydb = connect("archadmin")

form = FormContent()
day = form["day"][0]
month = form["month"][0]
year = form["year"][0]

if int(day) < 10:
	day = '0'+day
if int(month) < 10:
	month = '0'+month

day = month+'.'+day+'.'+year

def adds(descrip):
        print '<form method="post" action="add_annote.py">'
        print '<H3>Enter a day in the form mo.da.year (ex 06.09.1998)</H3>'
        print '<input type="text" name="day" value="'+day+'">'
        print '<H3>Enter description</H3>'
        print '<textarea name="descrip" cols="60" rows="20" WRAP>'+descrip+'</textarea>'
        print '<BR><input type="submit" value="Edit Entry">'

def get_entry():
	entries = mydb.query("SELECT * from diary where entry = '"+day+"'").getresult()
	if len(entries) == 0:
		entries = [("null","Not written yet")]
	return entries[0][1]

def Main():
	style.header("Edit Annotation","white")
	descrip = get_entry()
	style.std_top('Edit entry for '+day)

	adds(descrip)

	sys.exit(0)
Main()

