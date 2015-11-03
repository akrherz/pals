#!/usr/local/bin/python 
#Takes search info and looks up database and spits out titles


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
	lresults = ""
	
	style.header("Previous Searches","white")
	style.std_top("Titles of Saved Searches")
	print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
	print '<a href="http://www.pals.iastate.edu/c2w/adm/access.html">Enter a different username</a>'
	print '<HR>'
	print '<TABLE BORDER="1" WIDTH="650">\n<TR>\n'
	print '<TH ALIGN="LEFT" VALIGN="TOP" WIDTH="125">Username:</TH>' 
	print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">You Searched For:</TH>'
	print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">In directories:</TH>'
	print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="50">Entries Returned:</TH>'
	print '<TH align="left" VALIGN="top" WIDTH="225">Click title to view search:</th></TR>'


	form = FormContent()
	user = form["user"][0]

	if not form.has_key("user"): SendError("You did not input a username")

	lresults = mydbase.query("select * from users where user = '" + user + "'")
	lresults = lresults.getresult()
	if len(lresults) > 0:
		for i in range(len(lresults)):
			string = lresults[i][2]
			field = lresults[i][3]
			title = lresults[i][1]
			filename = lresults[i][4]
			total = lresults[i][5]
			print '<tr>'
			print '<form method=POST action="http://www.pals.iastate.edu/cgi-bin/search2.py">'
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
	else:
		print "Your username not found"
	print '</table>\n'
	print '<BR><BR><BR>'
	style.std_bot()

Main()
