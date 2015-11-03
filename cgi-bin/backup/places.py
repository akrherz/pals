#!/usr/local/bin/python
# Finds previously saved file locations
# Daryl Herzmannn 7/10/98

from pgext import * 
from cgi import * 
import os, string, sys, regsub, re, style

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
        presults = ""

        style.header("Your saved file locations","white")
	style.std_top("Titles of saved files")
	print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
        print '<a href="http://www.pals.iastate.edu/c2w/adm/saves.html">Enter a different username</a>'
        print '<HR>'
        print '<TABLE BORDER="1" WIDTH="650">\n<TR>\n'
        print '<TH ALIGN="LEFT" VALIGN="TOP" WIDTH="125">Username:</TH>'
        print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">Title:</TH>'
        print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">Date:</TH>'
        print '<TH align="left" VALIGN="top" WIDTH="225">Click to view file:</th></TR>'

        form = FormContent() 
        user = form["user"][0]


        lresults = mydbase.query("select * from saved where user = '" + user + "'") 
        lresults = lresults.getresult() 

        if len(lresults) > 0: 
                for i in range(len(lresults)): 
			url = lresults[i][1]
                        mytime = lresults[i][3]
                        title = lresults[i][2]
                        dresults = mydbase.query("select * from movies where url = '" + url + "'") 
                        dresults = dresults.getresult() 
                        filename = dresults[0][1]
			print '<tr>'
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+user+'</TD>'
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+title+'</TD>'
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+mytime[4:10]+mytime[22:27]+'</TD>'
			print '<TD ALIGN="LEFT" VALIGN="CENTER"><a href="http://www.pals.iastate.edu/cgi-bin/file.py?url='+url+'">'+filename+'</a></TD>'
        else: 
                print "Your username not found" 
        print '</table>\n'
	style.std_bot()
Main() 

