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

   form = FormContent() 
   
#   title = form["title"][0]
   description = form["description"][0]
#   runtime = form["runtime"][0]
#   keywords = form["keywords"][0]
   file = form["file"][0]

   title = 'null'
   runtime = 'null'
   keywords = 'null'

   #check and replace all 's
   description = regsub.gsub("'","&#180;",description)
   title = regsub.gsub("'","&#180;",title)
   keywords = regsub.gsub("'","&#180;",keywords)
   
   update = mydbase.query("UPDATE movies SET description ='"+description+"',title = '"+title+"', runtime='"+runtime+"',keywords='"+keywords+"' WHERE filename = '"+file+"'")   
   
   print "Content-type: text/html\n\n"
   print "<HEADER>\n<TITLE>C2W Update</TITLE>\n</HEADER>\n"
   print "<BODY bgcolor=#FFFFFF>\n"
   print "<h1>Update completed </h1><br>"
   print '<a href="https://pals.agron.iastate.edu/c2w/adm">Back to main menu'
   print '<br><br><a href="https://pals.agron.iastate.edu/c2w/adm/edit.html">'
   print 'Edit another entry</a> in:<br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=fire">'
   print 'fire</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=csm">'
   print 'csm</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=hydro">'
   print 'hydro</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=acsse">'
   print 'acsse</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=forecast">'
   print 'forecast</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=marine1">'
   print 'marine1</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=marine2">'
   print 'marine2</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=satellite1">'
   print 'satellite1</a><br>'
   print '<a href="https://pals.agron.iastate.edu/cgi-bin/c2w/list.py?dir=satellite2">'
   print 'satellite2</a><br>'
   print '</body></html>'

Main()
