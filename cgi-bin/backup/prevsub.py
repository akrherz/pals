#!/usr/local/bin/python
#Takes the form data and enters to database
#Prints out what info was added to database
# Daryl Herzmann 7/10/98

from pgext import *
from cgi import *
import os, string,sys, regsub, style

mydbase = connect("c2w")

def SendError(str):
	errmsg = escape(str)
	style.header("CGI ERROR","white")
	style.std_top("CGI ERROR")
	print "<H3><STRONG>" + errmsg + "</STRONG></H3>\n"
	style.std_bot()
	sys.exit(0)

def Main():
	style.header("Saved Search","/images/ISU_bkgrnd.gif")
	form = FormContent()
	
	user = form["user"][0]
	title = form["title"][0]
	url = form["url"][0]
        mytime = form["mytime"][0]

	if not form.has_key("user"): SendError("You did not input a user name")
        if not form.has_key("title"): SendError("no search title")

	insert = mydbase.query("INSERT INTO saved VALUES ('" + user + "', '" + url + "','" + title + "', '" + mytime + "')")

        style.std_top('Your title: '+title+' has been saved')
	print '<P>\nYour title can now be accessed by going to <a href="https://pals.agron.iastate.edu/cgi-bin/places.py?user='+user+'">'
	print "Here</a>\n<BR>"
#	print "<P>Then enter your username and a list of your search titles will appear!"
	print '<BR>\n<BR>\n<HR>\n'
	print 'Write down your username and title of your search for future reference.<BR>'
	print '<B>Username =></B>'
	print user 
	print "<BR>"
	print '<B>File Title =></B>'
	print title
	print "<BR><B>"
	style.std_bot()

Main()
