#!/usr/local/bin/python

from pgext import *
from cgi import *
import os, string,sys, regsub

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
   
   print "Content-type: text/html\n\n"
   print "<HEADER>\n<TITLE>Directory listing </TITLE>\n</HEADER>\n"
   print "<BODY bgcolor=#FFFFFF>\n"

   form = FormContent()
   dir = form["dir"][0]

   movies = mydbase.query("SELECT * from movies where filename ~~ '"+dir+"%'")
   movies = movies.getresult()

   print '<TABLE BORDER="1"><TR><TH ALIGN="LEFT" VALIGN="TOP">Directory</TH><TH'
   print 'ALIGN="LEFT" VALIGN="TOP">File Name</TH>'
   print '<th ALIGN="LEFT" VALIGN="TOP">Description</TH>'
   print '<TH align="left" valign="top">Click to edit</th></TR>'

   for item in range(len(movies)):
	file = movies[item][1]
	cut = len(dir)
	file = file[cut+1:]

	print '<TR><TD ALIGN="LEFT" VALIGN="TOP">'+dir+'</TD>'
	print '<TD ALIGN="LEFT" VALIGN="TOP">'+file+'</TD>'
	
	#test for description
	if len(movies[item][3]) > 1: 
	   print '<TD ALIGN="LEFT" VALIGN="TOP">YES</TD>'
	else:
	   print '<TD ALIGN="LEFT" VALIGN="TOP">NONE</TD>'
	
	print '<TD ALIGN="LEFT" VALIGN="TOP">'
	print '<a href="http://www.pals.iastate.edu/cgi-bin/c2w/edit.py?dir='+dir+'&file='+file+'">'
	print 'edit</a>'

	print '<tr>'

   print '</Table>'	

Main()
