#!/usr/local/bin/python 
# Takes search info and looks up database and spits out titles
# Daryl Herzmann 7/10/98

from pgext import * 
from cgi import * 
import os, string,sys, regsub, style

mydbase = connect("c2w") 

def Main():
	lresults = ""
	form = FormContent() 
        if not form.has_key("user"): style.SendError("You did not input a username")
        user = form["user"][0]

	lresults = mydbase.query("select * from users where user = '" + user + "'").getresult()
	if len(lresults) == 0: style.SendError("Username not found")
	if len(lresults) > 0:
		style.header("Previous Searches","/images/ISU_bkgrnd.gif")
		style.std_top("Titles of Saved Searches")
		print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
	        print '<a href="http://www.pals.iastate.edu/c2w/adm/access.html">Enter a different username</a>'
		print '<HR>'
		style.table_setter('650','Username','You Searched For:','In directories:','Entries Returned:','Click title to view search:')
		for i in range(len(lresults)):
			string = lresults[i][2]
			field = lresults[i][3]
			title = lresults[i][1]
			filename = lresults[i][4]
			total = lresults[i][5]
			print '<tr>'
			print '<form method="POST" action="http://www.pals.iastate.edu/cgi-bin/C2W/search2.py">'
			print '<INPUT TYPE=hidden NAME="string" VALUE="'+string+'">\n'
			print '<input type=hidden name="field" value="'+field+'">\n'
			print '<input type=hidden name="filename" value="'+filename+'">\n'
			print '<TD ALIGN="LEFT" VALIGN="CENTER">'+user+'</TD>'
			print '<TD ALIGN="LEFT" VALIGN="CENTER">'+string+'</TD>'
			if filename == "%": filename = "All Directories"
			print '<TD ALIGN="LEFT" VALIGN="CENTER">'+filename+'</TD>'
			print '<TD ALIGN="CENTER" VALIGN="CENTER">',total,'</TD>'
			print '<TD ALIGN="LEFT" VALIGN="CENTER"><input type=submit value="'+title+'"></TD>'
			print '</form>\n</TR>'
	print '</table>\n'
	print '<BR><BR><BR>'
	style.std_bot()

Main()
