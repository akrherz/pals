#!/usr/local/bin/python
# This script will hand off to loop, which will generate a handy radar loop
# Daryl Herzmann 28 Feb 2001

import pg, cgi, DateTime, time

mydb = pg.connect('wx', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")

def setupHTML():
	print """<HTML>
<HEAD>  
        <TITLE>PALS | Radar Data Viewer</TITLE>
        <META name="author" content="Daryl Herzmann akrherz@iastate.edu">
        <link rel=stylesheet type=text/css href=/css/pals.css>
</HEAD>

<body BGCOLOR="#ffffff" LEFTMARGIN="0" MARGINWIDTH="5" MARGINHEIGHT="5" vlink="blue" alink="blue" link="blue">

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
</TABLE>

<B>Navigation:</B>
<a href="http://www.pals.iastate.edu/">PALS</a> &nbsp;>&nbsp;
<a href="http://www.pals.iastate.edu/archivewx/">Archived Weather Data</a> &nbsp;>&nbsp;
<B>Radar Looper</B> 


	"""


def listDays(mySite):
	rs = mydb.query("SELECT date(starttime) as starter, caseid from radardata WHERE site = '"+mySite+"' ORDER by starter").dictresult()

	print '<P>You have selected nexradID: '+mySite
	print ' ( <a href="index.py">change</a> )'

	print "<P>Please Select a Archive Date:"

	print '<SELECT name="caseid"><BR>'
	for i in range(len(rs)):
		starter = rs[i]["starter"]
		caseid = rs[i]["caseid"]
		print '<OPTION value="'+str(caseid)+'">'+starter
	print '</SELECT>'

def listSites(mySite = "Blah"):
	rs = mydb.query("SELECT site from radardata GROUP by site").dictresult()

	print "<P>Please Select a Site"

	print '<SELECT name="site"><BR>'
	for i in range(len(rs)):
		thisSite = rs[i]["site"]
		print '<OPTION value="'+thisSite+'">'+thisSite
	print '</SELECT>'

def listTimes(mySite, myCase):
	rs = mydb.query("SELECT starttime, stoptime from radardata WHERE caseid = "+myCase+" ").dictresult()

	print '<P>You have selected nexradID: '+mySite
	print ' ( <a href="index.py">change</a> )'

	print "<P>Please Select Loop Times:"

	print '<P><INPUT TYPE="checkbox" name="all" value="'+myCase+'">Loop All These Times'

	startDate = DateTime.ISO.ParseDateTimeGMT(rs[0]["starttime"])
	endDate = DateTime.ISO.ParseDateTimeGMT(rs[0]["stoptime"])
	startSecs = startDate.gmticks()
	endSecs = endDate.gmticks()

	now = startSecs
	print '<P><MULTICOL COLS="3">'
	while ( now <= endSecs):
		thisTuple = time.gmtime(now)
		timeString = time.strftime("%y%m%d%H%M", thisTuple)
                print '<BR><INPUT type="CHECKBOX" value="'+timeString+'" name="timeStamp">'+timeString
                now = now + 5*60
	print '</MULTICOL>'



def Main():
	print 'Content-type: text/html \n\n'
	setupHTML()

	form = cgi.FormContent()

	
	if form.has_key("caseid"):
		print '<FORM METHOD="GET" ACTION="genLoop.py">'
		caseid = form["caseid"][0]
		site = form["site"][0]
		print '<INPUT TYPE="HIDDEN" value="'+site+'" name="site">'
		listTimes(site, caseid)
		print '<BR><INPUT TYPE="SUBMIT" value="Continue">'
		print '<input type="RESET">'
	
	elif form.has_key("site"):
		print '<FORM METHOD="GET" ACTION="index.py">'
		site = form["site"][0]
		print '<INPUT TYPE="HIDDEN" value="'+site+'" name="site">'
		listDays(site)
		print '<BR><INPUT TYPE="SUBMIT" value="Continue">'
	
	else:
		print '<FORM METHOD="GET" ACTION="index.py">'
		listSites()
		print '<BR><INPUT TYPE="SUBMIT" value="Continue">'


	print '</FORM>'


Main()