#!/usr/local/bin/python

#EVER WONDER HOW MESSY A SCRIPT WRITTEN BY A 4 WEEK ROOKIE CAN BE????..
#SEE BELOW

from pgext import * 
from cgi import * 
import os, sys, regsub, re

mydbase = connect("c2w")

form = FormContent() 
user = form["user"][0]

home = "http://www.pals.iastate.edu/cgi-bin/daryl_dev/my.py?user="
home = home + user
base = "http://www.pals.iastate.edu/cgi-bin/daryl_dev/my.py"
point_image = '<img src="http://www.pals.iastate.edu/images/point_02.gif">'

def menuloader():
	print '<center>'
	print 'Archived Weather --'
	print '<a href="'+home+'&url=c2w">COMET Video</a>'
	print '<spacer type="horizontal" size="50">'
	print '<a href="'+home+'">Interactive Home</a>--'
	print '<a href="/index.html">Exit to PALS Home</a>'
	print '</center>'

def urlloader(target):
	prefix = "/home/www/pals/html/"
	if target == "c2w":
		ctwloader()
	else:	 
		myfile = prefix + target
		fp = open( myfile , 'r') 
		print fp.read()

def mysearches():
	results = mydbase.query("select * from users where user = '"+user+"'")
	results = results.getresult()
	print '<dl>'
	print '<HR><a href="'+home+'&saved=yes" style="color:black">Saved Searches</a>'
	for i in range(len(results)):
		print '<li>'
		newone = regsub.gsub(' ','_', results[i][1])
		print '<a href="'+home+'&titleA='+newone+'">'+newone+'</a>'
	print '</dl>'

def mylocales():
	bresults = mydbase.query("select * from saved where user = '"+user+"'")
        bresults = bresults.getresult() 
        print '<dl>'
	print '<HR><B><U>Saved Files</B></U>' 
        for i in range(len(bresults)): 
                print '<li>'
                newone = regsub.gsub(' ','_', bresults[i][2])
		print '<a href="'+home+'&titleB='+newone+'">'+newone+'</a>'
	print '</dl>'

def sloader(title):
	dresults = "" 
        fresults = "" 
        bresults = ""	

	form = FormContent()

	if form.has_key("titleA"):
		lookup = mydbase.query("select * from users where title = '" + title + "'")
		lookup = lookup.getresult()	
		mystring = lookup[0][2]
		field = lookup[0][3]
		filename = lookup[0][4]

	else:
		form = FormContent()
		mystring = form["string"][0]
		field = form["field"][0]
		filename = form["filename"][0]
		if filename == "all":
			filename = "%"
	
	print '<spacer type=vertical size="30">\n'
	print '<H3>Results of your search for "'+mystring+'"</H3>\n'
	
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
                        bresults = mydbase.query("select * from movies where description ~~ '%"+mystring+"%' OR filename ~~ '%"+filename+"%"+mystring+"%'") 
                        bresults = bresults.getresult()
	
	if len(dresults) == 0: total = 0
        if len(fresults) == 0: total = 0
        if len(bresults) == 0: total = 0

	if len(dresults) > 0: total = len(dresults) 
        if len(fresults) > 0: total = len(fresults) 
        if len(bresults) > 0: total = len(bresults)

	if form.has_key("search"):
		print '<form method="POST" action="'+home+'&searchloc=yes">\n'
        	print '<input type=hidden name="total" value="',total,'">\n'
        	print '<input type=hidden name="string" value="'+mystring+'">\n'
        	print '<input type=hidden name="field" value="'+field+'">\n'
        	print '<input type=hidden name="filename" value="'+filename+'">\n'
       		print 'Give your search a title:<input type="text" name="tile">'
		print '<input type=submit value="Save These Search Results">\n'
        	print '</form>\n'

	print '<HR>\n'
	print '<dl>\n'

	if len(dresults) > 0:
		for item in range(len(dresults)):
			print "<P>\n" 
                        print "<dt>\n" 
                        print item+1
                        print ")" 
                        print point_image
			print '<a href="'+home+'&titleD='+dresults[item][0]+'">'+dresults[item][0]+'</a>'
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
			print point_image
			print '<a href="'+home+'&titleD='+fresults[item][0]+'">'+fresults[item][0]+'</a>' 
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
			print point_image
			print '<a href="'+home+'&titleD='+bresults[item][0]+'">'+bresults[item][0]+'</a>'
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


def floader(title):
	lookup = mydbase.query("select * from saved where title = '" + title + "' OR url = '" + title + "'") 
        lookup = lookup.getresult() 
        url = lookup[0][1]
	title = lookup[0][2]

	cresults = mydbase.query(" select * from comments where url = '" + url + "'") 
        cresults = cresults.getresult()
	comments = cresults[0][1]
	src = cresults[0][0]

	blookup = mydbase.query("select * from movies where url = '" + url + "'") 
        blookup = blookup.getresult()

	filename = blookup[0][1]

	print '<spacer type=vertical size="30">'
        print '<spacer type=horizontal size="30">'
        print '<H1>'+filename+'</H1>\n'
	print '<BR clear="all">\n<HR>\n'
	print '<center>'
        print '<a href="'+src+'">View '+filename+'</a>'
        print '<br>'
        print '<br>'
        print "You can add your comments about this file to the end of this section." 
        print '<form method="POST" action="'+base+'">'
        print '<textarea name="comment" cols="60" rows="20">'+comments+'</textarea>'
        print '<P>'
        print '<input type="hidden" name="user" value="'+user+'">'
	print '<input type="hidden" name="titleC" value="'+url+'">'
        print '<input type="submit" value="Add my comment">'
        print '</form>'

def cloader(title):
	form = FormContent() 
        url = form["titleC"][0]
        if form.has_key("comment"):
		comment = form["comment"][0]
		update = mydbase.query("update comments set comments = '"+comment+"' where url = '"+url+"'")

	find = mydbase.query("select * from movies where url = '"+url+"'") 
        find = find.getresult()
	filename = find[0][1]
	floader(url)

	
def loadertwo(url):
	form = FormContent() 
        url = form["titleD"][0]
        if form.has_key("comment"):
		comment = form["comment"][0]
		update = mydbase.query("update comments set comments = '"+comment+"' where url = '"+url+"'")

	cresults = mydbase.query(" select * from comments where url = '" + url + "'") 
        cresults = cresults.getresult()
	comments = cresults[0][1]
	src = cresults[0][0]

	lookup = mydbase.query("select * from movies where url = '" + url + "'") 
        lookup = lookup.getresult()

	filename = lookup[0][1]

	print '<spacer type=vertical size="30">'
        print '<spacer type=horizontal size="30">'
	print '<H1>'+filename+'</H1>\n'
	print '<a href="'+home+'&titleE='+filename+'&Trl='+url+'">Save File Location</a>'
	print '<BR clear="all">\n<HR>\n'
	print '<center>'
        print '<a href="'+src+'">View '+filename+'</a>'
	print '<br>'
        print '<br>'
        print "You can add your comments about this file to the end of this section."
	print '<form method="POST" action="'+base+'">'
        print '<textarea name="comment" cols="60" rows="20">'+comments+'</textarea>'
        print '<P>'
        print '<input type="hidden" name="user" value="'+user+'">'
        print '<input type="hidden" name="titleD" value="'+url+'">'
        print '<input type="submit" value="Add my comment">'
        print '</form>'

def titler(bla):
	print "<H1>Save the location of file</H1>\n" 
        print '<BR clear="all">\n<HR>\n'
	form = FormContent() 
        url = form["Trl"][0]
	print '<form method=POST action="'+base+'">'
	print '<input type="hidden" name="Trl" value="'+url+'">'
	print '<input type="hidden" name="user" value="'+user+'">'
	print '<table>'
	print '<tr>'
	print '<th align="right">Name the file for future reference:'
        print '<td><input type="text" name="title">'
	print '<tr>'
        print '<th colspan=2 align="center">'
        print '<input type="submit" value="Submit">'
        print '</form>'
	print '</table>'

def titlertwo(bla):
	form = FormContent()
	url = form["Trl"][0]
	title = form["title"][0]
	mytime = os.popen('date', 'r').read()
	
	search = mydbase.query("select * from saved where title = '"+title+"'") 
        search = search.getresult()

	if len(search) > 0:
                print "<H3>Title is already taken.</H3> Please go back and chose a different title." 
                print '</td></tr></table></html>'
		sys.exit(0)

	insert = mydbase.query("INSERT INTO saved VALUES ('" + user + "', '" + url + "','" + title + "', '" + mytime + "')")
	floader(title)

def startmain():
	print '<center><img src="/images/pals_logo.gif">'
	print '<H3> PALS Interactive </H3></center>'
	print '<P>This page is a resource for accessing your previously saved searches and files'
	print '<P>Your saved resources will appear in the left menubar and can be accessed at anytime while in PALS Interactive'
	print '<HR>'
	print '<dl>Interactive areas'
	print '<li>Archived Weather'
        print '<li><a href="'+home+'&url=c2w">COMET Video</a>'
	print '</dl>'

def ctwloader():
	print '<center><H2>COMET VIDEO Library</H2></center>'
	print '<HR width="400">'
	newsearch()
	print '<td>'

def newsearch():
	print '<H5>New Search in database</H5>'
	print '<FORM METHOD="POST" ACTION="'+home+'&search=yes">'
	print '<table width="400" border="0"><tr><th align="right">Search For:</th>'
	print '<td><INPUT type=text NAME="string">'
	print '<tr><th align=right>In Directory:</th>'
	print '<td><select name=filename>'
	print '<option value="all" selected>All directories'
	print '<option value="acsse">ACSSE'
	print '<option value="csm">CSM'
	print '<option value="fire">Fire'
	print '<option value="forecast">Forecast'
	print '<option value="hydro">Hydro'
	print '<option value="marine1">Marine I'
	print '<option value="marine2">Marine 2'
	print '<option value="satellite1">Satellite I'
	print '<option value="satellite2">Satellite 2</select>'
	print '<tr><th align=right> Search In:</th>'
	print '<td><SELECT NAME=field>'
	print '<OPTION VALUE="description" SELECTED>Description only'
	print '<option value="filename">Filename only'
	print '<option value="both">Description and Filename</select>'
	print '<tr><th colspan="2" align=center><INPUT TYPE="submit" VALUE="Submit Query"><INPUT TYPE="reset" VALUE="Reset"></table></form>'
	
def save_search():
	form = FormContent()
	title = form["tile"][0]
	string = form["string"][0]
        field = form["field"][0]
        filename = form["filename"][0]
        total = form["total"][0]
	
	search = mydbase.query("select * from users where title = '"+title+"'") 
        search = search.getresult() 
        if len(search) > 0: 
                print "<H3>Title is already taken.</H3> Please go back and chose a different title." 
                print '</td></tr></table></html>'
                sys.exit(0)

	insert = mydbase.query("INSERT INTO users VALUES ('" + user + "', '" + title + "','" + string + "', '" + field + "', '" + filename + "', '"+ total + "')")	

	sloader(filename)

def saved():
	print "<H1>Titles of Previous Searches</H1>\n"
	print '<HR>'
        print '<TABLE BORDER="1">\n<TR>\n'
        print '<TH ALIGN="LEFT" VALIGN="TOP" WIDTH="125">Username:</TH>'
        print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">You Searched For:</TH>'
        print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="125">In directories:</TH>'
	print '<th ALIGN="LEFT" VALIGN="TOP" WIDTH="50">Entries Returned:</TH>'
        print '<TH align="left" VALIGN="top" WIDTH="225">Click title to view search:</th></TR>'
	form = FormContent() 
        user = form["user"][0]
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
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+user+'</TD>'
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+string+'</TD>'
                        if filename == "%": filename = "All Directories" 
                        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+filename+'</TD>'
                        print '<TD ALIGN="CENTER" VALIGN="CENTER">',total,'</TD>'
			title = regsub.gsub(' ','_', title)
                        print '<TD ALIGN="LEFT" VALIGN="CENTER"><a href="'+home+'&titleA='+title+'">'+title+'</a></TD>'
                        print '</TR>'
        else: 
                print "Your username not found" 
        print '</table>\n'


def viewer(): 
        if form.has_key("url"): 
                url = form["url"][0]
		urlloader(url)
	elif form.has_key("titleA"): 
                titleA = form["titleA"][0]
		titleA = regsub.gsub('_',' ', titleA)
		sloader(titleA)
	elif form.has_key("titleB"):
		titleB = form["titleB"][0]
		titleB = regsub.gsub('_',' ', titleB)
		floader(titleB)
	elif form.has_key("titleC"):
		titleC = form["titleC"][0]
		cloader(titleC)
	elif form.has_key("titleD"): 
		titleD = form["titleD"][0]
		loadertwo(titleD)
	elif form.has_key("titleE"): 
		titleE = form["titleE"][0]
		titler(titleE)
	elif form.has_key("title"):
		title = form["title"][0]
		titlertwo(title)
	elif form.has_key("search"): 
                blah = form["search"][0]
		sloader(blah)
	elif form.has_key("searchloc"): 
                save_search()
	elif form.has_key("saved"): 
                saved()

	else: 
		url = "/index.html"  
		startmain()

def Main(): 
	print 'Content-type: text/html\n\n'
        print '<HEADER>\n<TITLE>PALS Interactive</TITLE>\n</header>\n'
	
	# Set up the table	
        print '<BODY bgcolor="white" MARGINWIDTH="0" MARGINHEIGHT="0" vlink="blue" alink="blue" link="blue">\n'
	print '<table border="0" cellpadding="1" cellborder="0">'
	print '<tr height="50" width="550" bgcolor="#c0c0c0">'

	# Define the upper right corner	
	print '<td height="50" colspan="2" valign="left"><img src="/images/pals_logo.gif" height="50" width="60" align="left" hspace="10" vspace="0">'

	# Define the menu (static)	
	print '<H3><center>PALS Interactive for '+user+'</center></H3>'
	menuloader()
	print '</td>'
	print '</tr>'

	 # Define the user
        print '<tr height="0"><td height="0">'
	print '<b>USER=> '+user+'</b></td>'
	
	# Define the main viewer
	print '<td valign="top" rowspan="2">'
        viewer()
        print '</td></tr>'

	# Define the leftside index	
	print '<tr><td valign="top" width="160" bgcolor="#dfdfdf">'
	print '<spacer type="vertical" size="10">'
	print '<center><H5>COMET Files</H5></center>'
	print '<P>'
	mysearches()
	print '<P>'
	mylocales()
	print '</td></tr>'

	print '</table></html>'
Main()
