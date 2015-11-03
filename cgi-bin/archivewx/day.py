#!/usr/local/bin/python
# This will prompt the form that will send them on
# Daryl Herzmann 8/25/98

import os, posix, re, style
from cgi import *

def determine_day():
	form = FormContent()
	day = form["day"][0]
	return day

def Main():
	day = determine_day()
	style.header('Access for '+day+' weather data','white')	
	style.std_top('Access '+day )
	print '<BR><TABLE><TR><TH align="right">'
	print 'Enter the password</TH>'
	print '<form method="post" action="adm/display.py">'
	print '<TD><input type="password" name="pass"></TD>'
	print '<input type="hidden" name="day" value="'+day+'">'
	print '</tr><tr><th colspan="2">'
	print '<input type="submit" value="Submit Request">'
	print '</form></td></tr></table>'
	style.std_bot()
Main()
