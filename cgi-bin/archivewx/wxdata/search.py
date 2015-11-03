#!/usr/local/bin/python
# This is the script that will show search data after search
# Daryl Herzmann 1/14/99
# UPDATED 2/25/99: Actually making this script work

import os, style, functs, string
from cgi import *

def setup_html():
	style.header("Archived Weather Data Search","white")
	print '<table border="0" cellspacing="0" rowspacing="0" width="600">'
	print '<tr><td width="150"></td><td width="450"></td></tr>'
	print '<tr><td bgcolor="#00fcf8" colspan="2">'
	print '<img src="/images/pals_logo.gif" align="left"><spacer type="vertical" size="30">'
	print '<H1>Archive Weather Data Search</H1></td></tr>'
	
def options():
	print '<table width="150" border="0" CELLSPACING="0">'
	print '<tr bgcolor="#FFCCCC"><td><B><font color="black">Other Search Options:</B></font></td></tr>'
	print '<TR><TD><IMG SRC="/images/point_02.gif">'
	print '<font size="3"><A HREF="/archivewx/search.html">New Search</A></font><spacer type="vertical" size="50"></TD></TR>'
	print '</table>'
	

def results():
	day = functs.get_content("day")
	month = functs.get_content("month")
	year = functs.get_content("year")
	
	str_month = functs.convert_month(month)
	std_date = str(year+'-'+month+'-'+day)
	str_date = str_month+' '+day+', '+year
	dir = '/home/httpd/html/archivewx/data/'+std_date

	print '<H4> Data for '+str_date+'</H4>'

	try:
		files = os.listdir(dir)
		files.sort()
		print '<MULTICOL cols="3">'
		for i in range(len(files)):
			file = files[i]
			print '<a href="/archivewx/data/'+std_date+'/'+file+'">'+file+'</a><BR>'
		print '</MULTICOL>'

	except:
		print 'There is currently no data available for this day<BR>'
		

def Main():
	setup_html()
	print '<tr><td bgcolor="#EEEEEE" valign="top">'
	options()
	print '</td><td align="top">'
	results()
	print '</td></tr>'
	print '<tr><td colspan="2">'
	style.std_bot()
	print '</td></tr></table>'
Main()



