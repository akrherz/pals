#!/usr/local/bin/python
# Finds previously saved file locations
# Daryl Herzmannn 7/10/98

from pgext import * 
from cgi import * 
import os, string, sys, regsub, re, style

mydbase = connect("c2w") 

def Main(): 
        presults = ""

        form = FormContent()  
	if not form.has_key("user"): style.SendError("Enter an Username")
        user = form["user"][0]
	
	style.header("Your saved file locations","white")
	style.std_top("Titles of saved files")
	print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
        print '<a href="http://www.pals.iastate.edu/c2w/adm/saves.html">Enter a different username</a>'
        print '<HR>'
        style.table_setter("650","Username:","Title:","Date:","Click to view file:")

        lresults = mydbase.query("select * from saved where user = '" + user + "'").getresult() 

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
			print '<TD ALIGN="LEFT" VALIGN="CENTER"><a href="http://www.pals.iastate.edu/cgi-bin/C2W/file.py?url='+url+'">'+filename+'</a></TD>'
        else: 
                print "Your username not found" 
        print '</table>\n'
	style.std_bot()
Main() 

