#!/usr/local/bin/python
# Submits Comments and can cycle though endlessly
# Daryl Herzmann 7/10/98

from pgext import *
from cgi import * 
import os, string, sys, regsub, re, style

mydbase = connect("c2w") 

def SendError(str): 
	errmsg = escape(str) 
  	style.header("CGI ERROR","white")
	style.std_top("CGI ERROR")
	print "<H1>CGI Error</H1>\n" 
	print "<H3><STRONG>" + errmsg + "</STRONG></H3>\n" 
	style.std_bot()
	sys.exit(0)

def Main():
	form = FormContent()
	url = form["url"][0]
	comment = form["comment"][0]	

	update = mydbase.query("update comments set comments = '"+comment+"' where url = '"+url+"'")


	cresults = mydbase.query(" select * from comments where url = '" + url + "'")
	cresults = cresults.getresult() 

	src = cresults[0][0]
	comments = cresults[0][1]
	user = cresults[0][2]
	_timestamp = cresults[0][3]	

	lookup = mydbase.query("select * from movies where url = '" + url + "'")
	lookup = lookup.getresult()

	filename = lookup[0][1]

        style.header('c2w=>'+filename,'/images/ISU_bkgrnd.gif')
        style.std_top(filename)
	print '<form method="post" action="https://pals.agron.iastate.edu/cgi-bin/prev.py">'
        print '<input type="hidden" name="url" value="'+url+'">'
        print '<input type="submit" value="Save the file location">'
	print '</form>'
	print '<BR clear="all">\n<HR>\n'
	print '<center>'
	print '<a href="'+src+'">View '+filename+'</a>'
	print '<br>'
	print '<br>'
	print "You can add your comments about this file to the end of this section."
	print '<form method="POST" action="https://pals.agron.iastate.edu/cgi-bin/file2.py">'
	print '<textarea name="comment" cols="60" rows="20">'+comments+'</textarea>'
	print '<P>'
	print '<input type="hidden" name="url" value="'+url+'">'
	print '<input type="submit" value="Add my comment">'
	print '</form>'
	style.std_bot()

Main()		

