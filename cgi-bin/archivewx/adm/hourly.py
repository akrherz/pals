#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann

import sys, style, os, posix
from pgext import *

mydb1 = connect("archdays")

def which_hours():
	print '<H3>Select an Hour to edit <spacer type="horizontal" size="50">'
	print '<select name="hour">'
	for i in range(12):
		z = str(i+(18))
		i = i+(1)
		print '<option value="'+z+'">',i,'PM\n'
	print '</select></H3>'


def which_days():
	print '<H3>on this day <spacer type="horizontal" size="50">'
	print '<select name="day">'
	files = posix.listdir('/home/httpd/html/archivewx/data_days')
	files.sort()
	for file in files:
		print '<option value="'+file+'">'+file+'\n'
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
