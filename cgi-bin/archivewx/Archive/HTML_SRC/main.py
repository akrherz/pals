#!/usr/local/bin/python
# This program makes the idex page for archive wx
# Daryl Herzmann 8/14/98

import os, sys, posix, style, re
from pgext import *

mydb = connect('archanswers')

data_path = '/home/httpd/html/archivewx/CGI_SRC/main.src'

def doer():
	print '<TR><td colspan="2">'
	print '<form method="post" action="/cgi-bin/archivewx/HTML_SRC/index.py">'
        print '<font color="white">Available Forecast Days<BR></font>'
	print '<select name="day">'
        dates = posix.listdir('/home/httpd/html/archivewx/data_days/') 
        dates.sort()  
        for date in dates:	
		if date == "index.html": 
                        blah = "1" 
                else:
			real = mydb.query("Select real from conversions where abbrev = '"+date+"' ").getresult()
			print '<option value="'+date+'">'+real[0][0]
	print '</select><BR><font color="white">And get started:</font>'
	print '<input type="submit" value="Start exercise"></form>'
	print '</form></td></tr>'


def Main(): 
	print 'Content-type: text/html\n\n'
	f = open(data_path, 'r')
        comp = f.read() 
        f.close() 
        lines = re.split('\012', comp)
	for line in lines:
		if line == "INSERTHERE":
			doer()
		else:
			print line
Main()


