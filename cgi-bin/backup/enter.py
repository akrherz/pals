#!/usr/local/bin/python
#Takes search info and asks for more data

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
	string = form["string"][0]
	field = form["field"][0]
	filename = form["filename"][0]
	total = form["total"][0]

	if not form.has_key("string"): SendError("You did not input a search string")
	if not form.has_key("field"): SendError("no search field found") 

	style.header("Save your search results","/images/ISU_bkgrnd.gif")
	style.std_top("Save your search for "+string)

	print '<P><H3>Enter a username and title for your search</H3>' 
	print '<BR CLEAR="all">\n'
	
	print '<FORM METHOD=POST action="https://pals.agron.iastate.edu/cgi-bin/submit.py">\n'
	print '<table>\n<tr>\n'
	print '<th align=right>Enter a Username:'
	print '<td>\n'
	print '<INPUT TYPE=text name="user">\n'
	print '<tr>\n<th align=right>Title of your search:'
	print '<td>\n'
	print '<INPUT TYPE=text name="title">\n'
	print '<INPUT TYPE=hidden name="string" value="'+string+'">\n'
	print '<input type=hidden name="field" value="'+field+'">\n'
	print '<input type=hidden name="filename" value="'+filename+'">\n'
	print '<input type=hidden name="total" value="'+total+'">'
	print '<tr>\n<th colspan="2" align=center>\n'
	print '<INPUT TYPE=submit value="Submit">\n'
	print '</FORM>\n'
	print '</table><BR><BR>'
	style.std_bot()
Main()
