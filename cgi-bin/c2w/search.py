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
   dresults = ""
   kresults = ""
   tresults = ""

   form = FormContent()
   string = form["string"][0]
   field = form["field"][0]
   
   if not form.has_key("string"): SendError("You did not input a search string")
   if not form.has_key("field"): SendError("no search field found")

   print "Content-type: text/html\n\n"
   print "<HEADER>\n<TITLE>C2W Edit Page</TITLE>\n</HEADER>\n"
   print "<BODY bgcolor=#FFFFFF>\n"

   if field == "description" or field == "both":
	dresults = mydbase.query("select * from movies where description ~~ '%"+string+"%'")
	dresults = dresults.getresult()

   elif field == "keywords" or field == "both":
	kresults = mydbase.query("select * from movies where keywords ~~ '%"+string+"%'")
	kresults = kresults.getresult()

   elif field == "title" or field == "both":
	tresults = mydbase.query("select * from movies where title ~~ '%"+string+"%'")
	tresults = tresults.getresult()

  
   print "<h3>Results of the search</h3>"
   print '<TABLE BORDER="1"><TR><TH ALIGN="LEFT" VALIGN="TOP">Title</TH><TH'
   print 'ALIGN="LEFT" VALIGN="TOP">File Name</TH>'
   print '<th align="left" valign="top">Size</th>'
   print '<th ALIGN="LEFT" VALIGN="TOP">Description</TH>'
   print '<TH align="left" valign="top">URL</TH>'

   if len(dresults) > 0:
	for item in range(len(dresults)):
	#	print dresults[item][1] + '<br>'
	        print '<TR><TD ALIGN="LEFT" VALIGN="TOP">'+dresults[item][2]+'</TD>' 
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+dresults[item][1]+'</TD>'  
		print '<td align="left" valign="top">'+dresults[item][4]+'</td>'
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+dresults[item][3]+'</TD>'  
		print '<td align="left" valign="top"><a href="'+dresults[item][0]+'">'+dresults[item][0]+'</a></td>'
		print '</tr>'

   elif len(tresults) > 0:
	for item in range(len(tresults)):
#		print tresults[item][1] + '<br>'
	        print '<TR><TD ALIGN="LEFT" VALIGN="TOP">'+tresults[item][2]+'</TD>' 
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+tresults[item][1]+'</TD>'  
		print '<td align="left" valign="top">'+tresults[item][4]+'</td>'
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+tresults[item][3]+'</TD>'  
		print '<td align="left" valign="top"><a href="'+tresults[item][0]+'">'+tresults[item][0]+'</a></td>'
		print '</tr>'

   elif len(kresults) > 0:
	for item in range(len(kresults)):
#		print kresults[item][1] + '<br>'
	        print '<TR><TD ALIGN="LEFT" VALIGN="TOP">'+kresults[item][2]+'</TD>' 
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+kresults[item][1]+'</TD>'  
		print '<td align="left" valign="top">'+kresults[item][4]+'</td>'
 	        print '<TD ALIGN="LEFT" VALIGN="TOP">'+kresults[item][3]+'</TD>'  
		print '<td align="left" valign="top"><a href="'+kresults[item][0]+'">'+kresults[item][0]+'</a></td>'
		print '</tr>'

   else:		
	print "No results were found"
   
   print '</table>'

Main()
	
