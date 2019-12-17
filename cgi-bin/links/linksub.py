#!/usr/local/bin/python 

from pgext import * 
from cgi import *
import os, sys, regsub

mydbase = connect("c2w")

def SendError(str): 
	errmsg = escape(str) 
	print "Content-type: text/html\n\n" 
	print "<HEADER>\n<TITLE> CGI Error </TITLE>\n</HEADER>\n" 
	print "<BODY bgcolor=#FFFFFF>\n" 
	print "<H1>CGI Error</H1>\n" 
	print '<H3>' + errmsg + '</H3>\n' 
	print "</BODY>" 
	sys.exit(0) 

def Main(): 
	print 'Content-type: text/html\n\n' 
	print '<HEADER>\n<TITLE>Saved links</TITLE>\n</HEADER>\n' 
	print '<BODY bgcolor="white">\n' 

	form = FormContent() 

	mylink = form["link"][0]
	mylink = regsub.gsub("'","&#180;",mylink)


	myURL = form["URL"][0]
	
	if form.has_key("kindA"):
		mykindA = form["kindA"][0]
	else: mykindA = "null"
	
	if form.has_key("kindB"):
		mykindB = form["kindB"][0]
	else: mykindB = "null"
	
	if form.has_key("kindC"):
		mykindC = form["kindC"][0]
	else: mykindC = "null"
	
	if form.has_key("kindD"):
		mykindD = form["kindD"][0]
	else: mykindD = "null"

	mydescription = form["description"][0]
	mydescription = regsub.gsub("'","&#180;",mydescription)	

	mytime = os.popen('date', 'r').read()
	
	if not form.has_key("link"): SendError("You need to enter a link") 
	if not form.has_key("URL"): SendError("You should enter a URL") 
	if not form.has_key("description"): SendError("What is it's description")

	search = mydbase.query("select * from linkex where url = '"+myURL+"'")
	search = search.getresult()
	
	if len(search) > 0:
		print "URL already taken."
		sys.exit(0)
	
	search2 = mydbase.query("select * from linkex where link = '"+mylink+"'") 
        search2 = search2.getresult()

	if len(search2) > 0:
		print "Link title aready taken."
		sys.exit(0)
	
	enter = mydbase.query("INSERT INTO linkex VALUES( ' " + mylink+"','"+myURL+"','"+mykindA+"','"+mykindB+"','"+mykindC+"','"+mykindD+"','"+mydescription+"', '"+mytime+"')")
	
	print '<img src="/images/pals_logo.gif" align=left>\n'
	print '<spacer type=vertical size="30">\n'
	print '<H3>Your link to "'+mylink+'" was saved!</H3>\n'
	print '<BR CLEAR="all">\n<HR>\n'
	print '<br><P>You can now:<ul>'
	print '<li><a href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/printout.py">View all the links</a>'
	print '<li><a href="https://pals.agron.iastate.edu/index.html">Go back to PALS Homepage</a>'
	print '</html>\n'

Main()
