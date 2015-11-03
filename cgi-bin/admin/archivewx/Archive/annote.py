#!/usr/local/bin/python
# This is the editor for the day's annotations
# Daryl Herzmann 8/9/98
# UPDATE 1/17/99: Changed the Interface to the available entries

import style, std_form
from pg import *
from cgi import *

mydb = connect("archadmin")

form = FormContent()

def options():
	print '<center><H3>Add or Edit an Entry</H3></center>'
	print '<form method="post" action="edit_annote.py">'
	print '<table><tr><th>Select a day:</th><td>'
	std_form.days()
	print '</td></tr><tr><th>Select a month:</th><td>'
	std_form.months()	
	print '</td></tr><tr><th>Select a year:</th><td>'
	print '<SELECT name="year">'
	print '<option value="1998">1998'
	print '<option value="1999">1999'
	print '</SELECT>'
	print '</td></tr>'
	print '<TR><TH colspan="2"><input type="submit"></TH></TR></TABLE>'

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
#	selections()
	
	style.std_bot()

Main()
