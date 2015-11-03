#!/usr/local/bin/python
# This prompts for which day to edit it's severe forecast results
# Daryl Herzmann

import sys, style, os, posix
from pgext import *



def which_days():
	print '<H3>Which Day do you want to edit?</H3>'
	print '<select name="day">'
	files = posix.listdir('/home/httpd/html/archivewx/data_days')
	files.sort()
	for file in files:
		print '<option value="'+file+'">'+file+'\n'
	print '</select>'

def closing():
	print '<HR>'
	print '<input type="submit" value="submit">'


def Main():
	style.header("Edit Severe Forecast results","white")
	style.std_top("Which Day??")
	print '<form method="post" action="edit_severe.py">'
	print '<BR>'
	which_days()
	closing()
	style.std_bot()
	sys.exit()
Main()

