#!/usr/local/bin/python
# Prompts for a title to save a search by
# Daryl Herzmann 7/10/98

from pgext import * 
from cgi import * 
import os, string, sys, regsub, re, style

mydbase = connect("c2w") 

def SendError(str): 
	errmsg = escape(str) 
	style.header("CGI Error","White")    
	style.std_top("CGI Error")
	print "<H3><STRONG>" + errmsg + "</STRONG></H3>\n" 
	style.std_bot()
	sys.exit(0) 

def Main(): 
	style.header("Save Location","white")
	style.std_top("Save the file location")
        print '<a href="https://pals.agron.iastate.edu/c2w/adm/search.html">New Search</a>--'
        print '<a href="https://pals.agron.iastate.edu/c2w/adm/access.html">Enter a different username</a>'
        print '<HR>'

        mytime = os.popen('date', 'r').read()


	form = FormContent() 
        url = form["url"][0]

	print '<form method=POST action="https://pals.agron.iastate.edu/cgi-bin/prevsub.py">'
        print '<input type="hidden" name="url" value="'+url+'">'
	print '<table>'
	print '<tr>'
        print '<th align="right">Enter your username'
        print '<td><input type="text" name="user">'
	print '<tr>'
	print '<th align="right">Name the file for future reference:'
	print '<td><input type="text" name="title">'
	print '<tr>'
        print '<th align="right">'
        print '<td><input type="hidden" value="'+mytime+'" name="mytime">'
	print '<tr>'
	print '<th colspan=2 align="center">'
	print '<input type="submit" value="Submit">'
	print '</form>'	

        print '</table>\n'
	style.std_bot()

Main() 

