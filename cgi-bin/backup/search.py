#!/usr/local/bin/python

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
	dresults = ""
	fresults = ""
	bresults = ""	

	form = FormContent()
	if not form.has_key("string"): SendError("You did not input a search string")
	if not form.has_key("field"): SendError("no search field found")
	mystring = form["string"][0]
	field = form["field"][0]
	filename = form["filename"][0]

	if filename == "all": filename = "%"

	style.header("C2W Search Results","white")
	style.std_top('Results of your search for "'+mystring+'"')
        print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
	print '<a href="http://www.pals.iastate.edu/c2w/adm/access.html">Access Saved Search</a>'
	
	addstring = re.split('AND', mystring)
	orstring = re.split('OR', mystring)
	
	
	if len(addstring) == 2:
		addone = addstring[0]		
		addtwo = addstring[1]
		addone = string.strip(addone)
		addtwo = string.strip(addtwo)
		
		if field == "description":
			dresults = mydbase.query("select * from movies where (description ~~ '%"+addone+"%' AND description ~~ '%"+addtwo+"%') AND filename ~~ '"+filename+"%'")
			dresults = dresults.getresult()	
		elif field == "filename":
			fresults = mydbase.query("select * from movies where filename ~~ '%"+filename+"%"+addone+"%' AND filename ~~ '%"+filename+"%"+addtwo+"%'")
			fresults = fresults.getresult()
		elif field == "both":
			bresults = mydbase.query("select * from movies where (description ~~ '%"+addone+"%' AND description ~~ '%"+addtwo+"%' AND filename ~~ '"+filename+"%') OR (filename ~~ '%"+filename+"%"+addone+"%' AND filename ~~ '%"+filename+"%"+addtwo+"%')")
			bresults = bresults.getresult()
	
	elif len(orstring) == 2:
		orone = orstring[0]
		ortwo = orstring[1]
		orone = string.strip(orone)		
		ortwo = string.strip(ortwo)

		if field == "description":
			dresults = mydbase.query("select * from movies where (filename ~~ '%"+filename+"%' AND description ~~ '%"+orone+"%') OR (filename ~~ '%"+filename+"%' AND description ~~ '%"+ortwo+"%')")
			dresults = dresults.getresult()
		elif field == "filename":
			fresults = mydbase.query("select * from movies where filename ~~ '%"+filename+"%"+orone+"%' OR filename ~~ '%"+filename+"%"+ortwo+"%'")
			fresults = fresults.getresult()
		elif field == "both":
			bresults = mydbase.query("select * from movies where (description ~~ '%"+orone+"%' OR filename ~~ '%"+orone+"%' OR description ~~ '%"+ortwo+"%' OR filename ~~ '%"+ortwo+"%') AND filename ~~ '%"+filename+"%'")	
			bresults = bresults.getresult()	
	
	else:
		if field == "description":
			dresults = mydbase.query("select * from movies where description ~~ '%"+mystring+"%' AND filename ~~ '"+filename+"%'")
			dresults = dresults.getresult()

		elif field == "filename":
			fresults = mydbase.query("select * from movies where filename ~~ '%"+filename+"%"+mystring+"%'")
			fresults = fresults.getresult()

		elif field == "both":
			bresults = mydbase.query("select * from movies where description ~~ '%"+mystring+"%' OR filename ~~ '%"+mystring+"%'")
			bresults = bresults.getresult()
	
	if len(dresults) == 0: total = 0	
	if len(fresults) == 0: total = 0
	if len(bresults) == 0: total = 0

  	if len(dresults) > 0: total = len(dresults) 
	if len(fresults) > 0: total = len(fresults) 
	if len(bresults) > 0: total = len(bresults)

	print '<BR CLEAR="all">\n<HR>\n'
	print '<form method=POST action="http://www.pals.iastate.edu/cgi-bin/enter.py">\n'
	print '<input type=hidden name="total" value="',total,'">\n'
        print '<input type=hidden name="string" value="'+mystring+'">\n'
        print '<input type=hidden name="field" value="'+field+'">\n'
        print '<input type=hidden name="filename" value="'+filename+'">\n'
        print '<input type=submit value="Save These Search Results">\n'
	print '</form>\n'
	print '<dl>\n'

	if len(dresults) > 0:
		for item in range(len(dresults)):
			print "<P>\n"
			print "<dt>\n"
			print item+1
			print ")"
			print '<IMG SRC="http://www.pals.iastate.edu/images/point_02.gif">'
			print '<a href="http://www.pals.iastate.edu/cgi-bin/file.py?url='+dresults[item][0]+'">'+dresults[item][0]+'</a>'
			size = int(dresults[item][4])
			if size >= 1024000:
				size = (size)/(1024000)
				tag = "MB"
			else:
				size = (size)/(1024)
				tag = "K"
			print '(size =',size,' '+tag+')<br>'
			print '<dd>(Filename = <b>'+dresults[item][1]+'</b>) -- '
	        	print dresults[item][3] + '<br>\n'  

	elif len(fresults) > 0:
		for item in range(len(fresults)):
			print "<P>\n" 
                	print "<dt>\n" 
                	print item+1
               		print ")" 
                	print '<IMG SRC="http://www.pals.iastate.edu/images/point_02.gif">'
			print '<a href="http://www.pals.iastate.edu/cgi-bin/file.py?url='+fresults[item][0]+'">'+fresults[item][0]+'</a>'
			size = int(fresults[item][4])
                        if size >= 1024000: 
                                size = (size)/(1024000) 
                                tag = "MB" 
                        else: 
                                size = (size)/(1024) 
                                tag = "K" 
                        print '(size =',size,' '+tag+')<br>'
                	print '<dd>(Filename = <b>'+fresults[item][1]+'</b>) -- '
                	print fresults[item][3] + '<br>\n'

	elif len(bresults) > 0:
		for item in range(len(bresults)):
			print "<P>\n" 
                	print "<dt>\n" 
                	print item+1
                	print ")" 
                	print '<IMG SRC="http://www.pals.iastate.edu/images/point_02.gif">'
			print '<a href="http://www.pals.iastate.edu/cgi-bin/file.py?url='+bresults[item][0]+'">'+bresults[item][0]+'</a>'
                	size = int(bresults[item][4]) 
                        if size >= 1024000: 
                                size = (size)/(1024000) 
                                tag = "MB" 
                        else: 
                                size = (size)/(1024) 
                                tag = "K" 
                        print '(size =',size,' '+tag+')<br>'
			print '<dd>(Filename = <b>'+bresults[item][1]+'</b>) -- '
                	print bresults[item][3] + '<br>\n'

	else:		
		print "No results were found"

	print '</dl>\n'
	style.std_bot()	
Main()
	
