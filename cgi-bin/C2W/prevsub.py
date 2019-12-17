#!/usr/local/bin/python
#Takes the form data and enters to database
#Prints out what info was added to database
# Daryl Herzmann 7/13/98

from pgext import *
from cgi import *
import os, string,sys, regsub, style

mydbase = connect("c2w")

def Main():
	form = FormContent()
	
	if not form.has_key("user"): style.SendError("You did not input a user name")
        if not form.has_key("title"): style.SendError("no search title")
	
	user = form["user"][0]  
        title = form["title"][0]
        url = form["url"][0]
        mytime = form["mytime"][0]

	style.header("Saved Search","/images/ISU_bkgrnd.gif")

	insert = mydbase.query("INSERT INTO saved VALUES ('" + user + "', '" + url + "','" + title + "', '" + mytime + "')")

        style.std_top('Your title: '+title+' has been saved')
	print '<P>\nYour title can now be accessed by going to <a href="https://pals.agron.iastate.edu/cgi-bin/C2W/places.py?user='+user+'">'
	print "Here</a>\n<BR>"
	print '<BR>\n<BR>\n<HR>\n'
	print 'Write down your username and title of your search for future reference.<BR>'
	print '<B>Username =></B>'
	print user 
	print "<BR>"
	print '<B>File Title =></B>'
	print title
	print "<BR><BR>"
	style.std_bot()

Main()
