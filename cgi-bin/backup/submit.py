#!/usr/local/bin/python
#Takes the form data and enters to database
#Prints out what info was added to database

from pgext import *
from cgi import *
import os, string,sys, regsub, style

mydbase = connect("c2w")

def SendError(str):
	errmsg = escape(str)
	print "Content-type: text/html\n\n"
	print "<HEADER>\n<TITLE> CGI Error </TITLE>\n</HEADER>\n"
	print "<BODY bgcolor=#FFFFFF>\n"
	print "<H1>CGI Error</H1>\n"
	print "<H3><STRONG>" + errmsg + "</STRONG></H3>\n"
	print "</BODY>"
	sys.exit(0)

def Main():
	form = FormContent()
	
	user = form["user"][0]
	title = form["title"][0]
	string = form["string"][0]
        field = form["field"][0]
	filename = form["filename"][0]
	total = form["total"][0]	

	if not form.has_key("user"): SendError("You did not input a user name")
        if not form.has_key("title"): SendError("no search title")
	if not form.has_key("string"): SendError("You did not input a search string")
        if not form.has_key("field"): SendError("no search field found")

	insert = mydbase.query("INSERT INTO users VALUES ('" + user + "', '" + title + "','" + string + "', '" + field + "', '" + filename + "', '" + total + "')")
	
	style.header("Successful Search Saved","/images/ISU_bkgrnd.gif")
        style.std_top("Your search for "+string+" was saved")
        print '<H3>Save Information</H3>'
	print '<P>\nYour search can now be accessed by going to <a href="http://www.pals.iastate.edu/c2w/adm/access.html">'
	print "http://www.pals.iastate.edu/c2w/adm/access.html</a>\n<BR>"
	print "<P>Then enter your username and a list of your search titles will appear!"
	print '<BR>\n<BR>\n<HR>\n'
	print 'Write down your username and title of your search for future reference.<BR>'
	print '<B>Username =></B>'
	print user 
	print "<BR>"
	print '<B>Search Title =></B>'
	print title
	print "<BR><B>"
	print "<HR>"
	print '<form method=POST action="http://www.pals.iastate.edu/cgi-bin/search2.py">'
	print '<INPUT TYPE=hidden name="string" value="'+string+'">\n'
	print '<input type=hidden name="field" value="'+field+'">\n'
	print '<input type=hidden name="filename" value="'+filename+'">\n'
	print '<INPUT TYPE=submit value="Go back to my search list">\n'
	style.std_bot()
Main()
