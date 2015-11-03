#!/usr/local/bin/python

import sys, posix

dir = "/home/httpd/html/archivewx/cases/"


print 'Content-type: text/html\n\n'
print '<HTML><HEAD><TITLE>'
print 'Brad & Jason Severe Weather Prompt' 
print '</TITLE><body bgcolor="white">' 
print '<center><H1>Select a days weather</H1></center>'

print '<form method="post" action="page_gen.html.py">'
print '<select name="date">'
dates = posix.listdir(dir)
dates.sort()
for date in dates:
	if date == "index.html":
		blah = "1"
	else:
		print '<option value="'+date+'">'+date

print '</select>'

print '<BR><input type="submit" value="Get This day Weather"></form></body></html>'

