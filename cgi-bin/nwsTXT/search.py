#!/usr/local/bin/python
# This is the search engine for the NWS Text DB
# Daryl Herzmann 22 June 2000

import pg, cgi, regsub, DateTime, style, sys

mydb = pg.connect('nwstxt', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT' ")

def setupPage():
	print """
	<HTML>
	<HEAD>  
        <TITLE>PALS | NWS Text Products Search</TITLE>
        <META name="author" content="Daryl Herzmann akrherz@iastate.edu">
        <link rel=stylesheet type=text/css href=/css/pals.css>
	</HEAD>

	<body BGCOLOR="#ffffff" LEFTMARGIN="0" MARGINWIDTH="5" MARGINHEIGHT="5">

	<TABLE WIDTH="100%" BORDER="0" CELLSPACING="0" CELLPADDING="0"  BORDER="0" BGCOLOR="#99ccff">
	<TR>
        <TD WIDTH=150 VALIGN="CENTER">
	        <img src="/icons/pals_logo.gif" vpsace="5" hspace="5" width="75">
	        </TD>
	        <TD WIDTH="90%" ALIGN="left" NOWRAP>
	        <font color="#003366" size="+3">Partnerships to Advance Learning in Science</font><BR>
        <font color="blue" size="3">Developing, Implementing, and Sharing Constructivist Learning Resources</font>
        </TD>
	</TR>

	<TR>
        <TD colspan="2" bgcolor="black"><img src="/icons/blank.gif" height="1" width="3"></TD>
	</TR>
	</TABLE>"""


def cleanStr( myString ):
	return regsub.gsub("\015", "", myString)


def Main():
	form = cgi.FormContent()
	
	if form.has_key("bstation_PIL"):
		bstation = form["bstation_PIL"][0]
	else:
		bstation = form["bstation"][0]
	
	bType = form["bType"][0]
	year = form["year"][0]
	month = form["month"][0]

	try:
		day = form["day"][0]
	except:
		style.SendError("You need to enter a day into the 'Enter Valid Day:' prompt")
		sys.exit(0)

	if (int(year) == 1998 ):
		if (bType == "WFUS53"):	  bType = "WFUS1"
		elif (bType == "WUUS53"):	bType = "WUUS1"
		elif (bType == "WRUS53"):	bType = "WRUS1"
	
	dateStr = str(year)+"-"+str(month)+"-"+str(day)
	tableName = "t"+str(year)+"_"+str(month)	

	if bType == "all" and bstation != "all":
		searchStr = "SELECT * from "+tableName+" WHERE bstation = '"+bstation+"' and date(btime) = '"+dateStr+"' "
	elif bstation == "all" and bType != "all":
		searchStr = "SELECT * from "+tableName+" WHERE bType = '"+bType+"' and date(btime) = '"+dateStr+"'"
	elif bstation == "all" and bType == "all":
		searchStr = "SELECT * from "+tableName+" WHERE date(btime) = '"+dateStr+"'"
	else:
		searchStr = "SELECT * from "+tableName+" WHERE bstation = '"+bstation+"' and bType = '"+bType+"' and date(btime) = '"+dateStr+"'"
		
	try:
		results = mydb.query(searchStr).dictresult()
	except:
		results = ""
	
	print 'Content-type: text/html \n\n'

	setupPage()
	
	print '<BR><a href="/archivewx/nws_txt">NWS Text Mainpage</a> &nbsp; <a href="/archivewx/nws_txt/search.html">New Search</a><BR>'
	print '<h3>Query Results:</h3>'
	print '<TABLE width="100%" cellpadding="3" cellspacing="0" cellborder="0" border="0">'
	print '<TR><TD><B>WFO:</B></TD><TD><B>Issue:</B></TD><TD><B>Time:</B></TD><TD><B>View Issue:</B></TD></TR>'
	for i in range(len( results )):
		if (i%2 == 1):
			print '<TR>'
		else:
			print '\n<TR bgcolor="#EEEEEE">'
		print '<TD>'+results[i]["bstation"]+'</TD>'
		print '<TD>'+results[i]["bcodetxt"]+'</TD>'
		
		newTime = regsub.gsub(" ", "_", results[i]["btime"] )
		thisDate = DateTime.ISO.ParseDateTimeGMT( results[i]["btime"] )
		niceDate = thisDate.strftime("%d %B %Y | %H:%M Z")
		
		print '<TD>'+niceDate+'</TD>'
		print ' <TD><a href="record.py?bNumber='+str(results[i]["bnumber"])+'&bTime='+newTime+'">View</a></TD>'
		print '</TR>'
	print '</TABLE>'

	if len(results) == 0:
		print 'No results where found for your query'

	print '<BR><BR><HR><font color="red">DEBUGGING Information:</font><BR> '+searchStr
Main()
