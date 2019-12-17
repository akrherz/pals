#!/usr/local/bin/python
# Takes search info and asks for more data
# Daryl Herzmann 7/13/98

from pgext import * 
from cgi import *
import os, string,sys, regsub, style

mydbase = connect("c2w")

def Main():
	form = FormContent()
	if not form.has_key("string"): style.SendError("search string not found")
	if not form.has_key("field"): style.SendError("field not found")
	if not form.has_key("filename"): style.SendError("CGI ERROR")
	if not form.has_key("total"): style.SendError("CGI ERROR")

	string = form["string"][0]
	field = form["field"][0]
	filename = form["filename"][0]
	total = form["total"][0]

	style.header("Save your search results","/images/ISU_bkgrnd.gif")
	style.std_top("Save your search for "+string)

	print '<P><H3>Enter a username and title for your search</H3>' 
	print '<BR CLEAR="all">\n'
	
	print '<FORM METHOD=POST action="https://pals.agron.iastate.edu/cgi-bin/C2W/submit.py">\n'
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
