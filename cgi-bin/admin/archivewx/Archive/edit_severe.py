#!/usr/local/bin/python
# Edits entries in the Archanswers database
# Daryl Herzmann 8/8/98

from cgi import *
from pg import *
import os, sys, regsub, style, string

mydb = connect("archresults")

form = FormContent()
day = form["day"][0]

def new_ones():
	print '<H3>Add a new Entry</H3>'
	print '<form method="post" name="new" action="add_severe.py">'
	print '<input type="hidden" name="day" value="'+day+'">'
	print '<select name="state">'
	state1 = 'Alabama Arkansas Arizona California Colorado Connecticut Delaware Florida Georgia Idaho Illinois Indiana Iowa Kansas Kentucky ' 
	state2 = 'Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada New_Hampshire New_Jersey '
	state3 = 'New_Mexico New_York North_Carolina North_Dakota Ohio Oklahoma Oregon Pennsylvania Rhode_Island South_Carolina South_Dakota Tennessee '
	state4 = 'Texas Utah Vermont Virginia Washington Wisconsin West_Virginia Wyoming'
	states = state1+state2+state3+state4
	states = string.split(states)
	for state in states:
		print '<option value="'+state+'" name="state">'+state
	print '</select>'

	print '<select name="type">'	
	print '<option value="T">Tornadic Event'	
	print '<option value="H">Hail Event'
	print '<option value="R">Rainfall over 3 inches Event'
	print '</select>'

	print '<select name="time">'
	print '<OPTION> (Select a time)' 
	print '<OPTION VALUE="1">12-3' 
	print '<OPTION VALUE="2"> 3-6' 
	print '<OPTION VALUE="3"> 6-9' 
	print '<OPTION VALUE="4"> 9-Midnight'
	print '</SELECT>'

	print '<input type="submit" value="Submit this">'
	print '</form>'

def cur_entry(entries):
	num = len(entries)
	if int(num) >= 1:
		if int(num) < 20:
			num = str(num)
		else:
			num = "20"
		print '<input type="hidden" name="day" value="'+day+'">'
		print '<Select name="num" size="'+num+'">'
		num = str(len(entries))
		spacer = '&nbsp;&nbsp;&nbsp;'
		for i in range(len(entries)):
			entry = entries[i][0]+spacer+entries[i][1]+spacer+entries[i][2]
			blah = str(i)
			print '<option value="'+blah+'">'+entry
		print '</select>'
	else:
		hello = "9"

def current(entries):
        print '<form method="post" action="del_severe.py" name="new">'
        print '<H3>Current Entries</H3>'
	cur_entry(entries)
	print '<input type="submit" value="Delete This Entry">'
	print '</form>'

def get_entry():
	entries = mydb.query("SELECT * from t"+day)
	entries = entries.getresult()
	entries.sort()
	return entries

def Main():
	style.header("Edit Entries","white")
	entries = get_entry()
	style.std_top('Edit Results for '+day)
	current(entries)
	print '<HR>'
	new_ones()
	style.std_bot()

	sys.exit(0)
Main()



