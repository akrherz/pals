#!/usr/local/bin/python

import sys, posix

dir = "/home/httpd/html/archivewx/cases/"


print 'Content-type: text/html\n\n'
print '<HTML><HEAD><TITLE>'
print 'Brad & Jason Severe Weather Prompt' 
print '</TITLE><body bgcolor="white">' 
print '<center><H1>Select a days weather</H1></center>'
print '<H3>Case data</H3>'
dates = posix.listdir(dir)
dates.sort()
for date in dates:
	if date == "index.html":
		blah = "1"
	else:
		print '<dd><a href="'+date+'main.html">'+date+'</a><BR></dd>'


print '<BR><input type="submit" value="Get This day Weather"></form></body></html>'

