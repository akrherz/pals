#!/usr/local/bin/python
# This is the editor for the day's annotations
# Daryl Herzmann 8/9/98

import sys, style
from pg import *
from cgi import *

mydb = connect("archadmin")

form = FormContent()

def options():
	print '<center><H3><a href="new_annote.py">Add an Entry</a><BR>'
	print '</H3></center><HR>'

def selections():
	print '<center><H3>Avialable Entries to edit</H3>'
	print '<form method="post" action="edit_annote.py">'
	print '<select name="day">'
	entries = mydb.query("Select * from diary").getresult()
	for i in range(len(entries)):
		print '<option value="'+entries[i][0]+'">'+entries[i][0]
	print '</select>'
	print '<input type="submit" value="Edit entry">'


def Main():
	style.header("Annotation Editor","white")
	style.std_top("Edit Entries")

	options()	
	selections()
	
	style.std_bot()

Main()
