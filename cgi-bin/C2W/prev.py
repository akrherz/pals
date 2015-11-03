#!/usr/local/bin/python
# Prompts for a title to save a search by
# Daryl Herzmann 7/13/98

from pgext import * 
from cgi import * 
import os, string, sys, regsub, re, style

mydbase = connect("c2w") 

def Main(): 
	form = FormContent()
 	if not form.has_key("url"): style.SendError("CGI ERROR")
	url = form["url"][0]


	style.header("Save Location","white")
	style.std_top("Save the file location")
        print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
        print '<a href="http://www.pals.iastate.edu/c2w/adm/access.html">Enter a different username</a>'
        print '<HR>'

        mytime = os.popen('date', 'r').read()

	print '<form method=POST action="http://www.pals.iastate.edu/cgi-bin/C2W/prevsub.py">'
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

