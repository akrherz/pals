#!/usr/local/bin/python
# Standard file displayer
# Daryl Herzmann 7/10/98
# UPDATED 1/16/99 - Redid the former format that got deleted
# UPDATED 3/10/99 - The comments needed to be parsed for (')

from pgext import *
from cgi import * 
import os, string, sys, regsub, re, style

mydbase = connect("c2w") 

def Main():
	form = FormContent() 
	if not form.has_key("url"): style.SendError("CGI ERROR")	
	url = form["url"][0]
	
	if form.has_key("comment"):
		comment = form["comment"][0]
		comment = regsub.gsub("'","&#180;",comment)
		update = mydbase.query("update comments set comments = '"+comment+"' where url = '"+url+"'")

	cresults = mydbase.query(" select * from comments where url = '" + url + "'").getresult()
	if len(cresults) == 0: style.SendError("CGI ERROR")
	src = cresults[0][0]
	comments = cresults[0][1]

	lookup = mydbase.query("select * from movies where url = '" + url + "'").getresult()
	if len(lookup) == 0: style.SendError("CGI ERROR")
	filename = lookup[0][1]
	

 	style.header('c2w=>'+filename,'/images/ISU_bkgrnd.gif') 
        style.std_top("Viewing COMET® Video Files")
	print '<U><center><H1>'+filename+'</H1></center></U>'
	print '<BR><B>1) You can view this file:</B>' 
	print '<center><a href="'+src+'">View '+filename+'</a></center>'
	
	print """
	<blockquote>
	You can also download this file by either holding down the shift key and then clicking
on the link, or on some systems, you need to hold the option key down.

	</blockquote>
	"""

	print "<BR><BR><B>2) You can look at / edit this file's comments:</B><BR>"
	print "<center>You can add your comments about this file to the end of this section."
	print '<form name="form2" method="POST" action="https://pals.agron.iastate.edu/cgi-bin/C2W/file.py">'
	print '<textarea name="comment" cols="40" rows="10">'+comments+'</textarea>'
	print '<P>'
	print '<input type="hidden" name="url" value="'+url+'">'
	print '<input type="submit" value="Add my comment">'
	print '</form></center>'
	
	style.std_bot()

Main()		

