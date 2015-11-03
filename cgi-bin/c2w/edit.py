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
   print "<HEADER>\n<TITLE>C2W Edit Page</TITLE>\n</HEADER>\n"
   print "<BODY bgcolor=#FFFFFF>\n"

   form = FormContent()

   dir = form["dir"][0]
   filename = form["file"][0]
   file = dir + "/" + filename

   movies = mydbase.query("SELECT * from movies where filename = '"+file+"'")
   movies = movies.getresult()

   title = movies[0][2]
   description = movies[0][3]
   runtime = movies[0][5]
   keywords = movies[0][6]

   print '<h1>Edit entry for '+file+'</h1>'
   print 'Fill out this form to update the database <p>'
   print '<FORM METHOD="POST" ACTION="http://www.pals.iastate.edu/cgi-bin/c2w/update.py">'
   print 'Title:<INPUT NAME="title" VALUE="'+title+'"> <br>'
   print 'Keywords: <INPUT NAME="keywords" VALUE="'+keywords+'"> <br>'
   print 'Running Time: <INPUT size=10 NAME="runtime" VALUE="'+runtime+'">'
   print '<br><INPUT TYPE="hidden" NAME="file" value="'+file+'">'     
   print 'Description (Can be up to 4000 characters) :<br>'
   print '<TEXTAREA NAME="description" ROWS=20 COLS=70>'+description+'</TEXTAREA> '
   print '<p>'
   print '<INPUT TYPE="submit" VALUE="submit">'
   print '<INPUT TYPE="reset" VALUE="reset">'
   print '</FORM>'

   print "</body></html>"

Main()
