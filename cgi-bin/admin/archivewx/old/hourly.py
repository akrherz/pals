#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# UPDATED 6-25-99: Added the 7 am option, we want to annotate up the early morning

import sys, style, os, posix
from pgext import *

mydb1 = connect("archresults")

def which_hours():
	print '<H3>Select an Hour to edit <spacer type="horizontal" size="50">'
	print '<select name="hour">'
	print '<option value="0">Intro'
	for i in range(12):
		z = str(i+(18))
		i = i+(1)
		print '<option value="'+z+'">',i,'PM\n'
	print '</select></H3>'


def which_days():
	print '<H3>on this day <spacer type="horizontal" size="50">'
	print '<select name="day">'
	files = posix.listdir('/home/httpd/html/archivewx/data')
	files.sort()
	for file in files:
		try:
			tester = mydb1.query("SELECT * from t"+file+" ")
			print '<option value="'+file+'">'+file+'\n'
		except ValueError:
			continue

	print '</select></H3>'

def closing():
	print '<HR>'
	print '<input type="submit" value="submit">'


def Main():
	style.header("Edit Hourly Reports","white")
	style.std_top("Which Day and Hour??")
	print '<form method="post" action="edit_hourly.py">'
	which_hours()
	print '<BR>'
	which_days()
	closing()
	style.std_bot()
	sys.exit()
Main()
