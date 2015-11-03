#!/usr/local/bin/python
# This program will make the changes in the database
# Daryl Herzmann 5-29-99

import cgi, style, regsub
from pgext import *

mydb = connect('carlson')


def Main():
	form = cgi.FormContent()
	file = form["file"][0]
	path = form["path"][0]
	title = form["title"][0]
	txt = form["txt"][0]
	next = form["next"][0]

	title = regsub.gsub("'","&#180;", title)
	txt = regsub.gsub("'","&#180;", txt)
	print 'Content-type: text/html \n\n'
	print file, path, title, txt,  next
	update = mydb.query("UPDATE images SET path = '"+path+"' , title = '"+title+"' , txt = '"+txt+"' , next = '"+next+"' WHERE (file = '"+file+"')") 

	print '<HTML><HEAD>'
	if next == "None":
		print '<meta http-equiv="Refresh" content="1; URL=index.py">'
	else:
	        print '<meta http-equiv="Refresh" content="1; URL=edit.py?file='+next+'">'
        print '</HEAD>'
        print '<body>'
	print '<H2> Update successful </H2>'
        print '</HTML>'



Main()
