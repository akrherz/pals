#!/usr/local/bin/python
# This program makes the forecast page, thus automating the entire system
# Daryl Herzmann 8/14/98

import os, sys, posix, style, re
from cgi import *

form = FormContent()
day = form["day"][0]
month_name = form["month_name"][0]
month_num = form["month_num"][0]


data_path = '/home/httpd/html/archivewx/CGI_SRC/forecast.src'
title = month_name+' '+day[3:5]+', '+day[5:]

def hidden():
	print '<input type="hidden" name="month_name" value="'+month_name+'">'
	print '<input type="hidden" name="month_num" value="'+month_num+'">'
	
def Main(): 
	print 'Content-type: text/html\n\n'
	f = open(data_path, 'r')
        comp = f.read() 
        f.close() 
        lines = re.split('\012', comp)
	for line in lines:
		if line == "REPLACE":
			print day
		elif line == "TITLE":
			print title
		elif line == "NOW":
			hidden()
		else:
			print line
Main()


