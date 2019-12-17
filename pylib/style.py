#!/usr/local/bin/python
# Sort of a cascade style sheet, but nicer to use!
# Daryl Herzmann 11/09/98
# UPDATED 1/17/99 : Corrected formatting errrors incountered with std_bot
# UPDATED 2/22/99 : Set up a standard page width
# UPDATED 6/2/99: Changed over to correct time feature
# UPDATED 9/12/99: Changed to a new style, nice...
# UPDATED 9/22/99: Changed the annoying part of style.SendError()
# UPDATED 10.1.99: Added style.box, neat little area maker...

import os, sys, posixpath, posix, time, re

def header(title, backround):
	print 'Content-type: text/html\n\n'
	print '<HTML>\n<HEAD>\n\t<TITLE>',
	print title,
	print '</TITLE>\n'
	print """
	<META name="keywords" content="PALS">
	<META name="author" content="Daryl Herzmann akrherz@iastate.edu">
	</HEAD>
	"""
	print '<body ',
	if backround[-14:] == "ISU_bkgrnd.gif":
		print 'bgcolor="white"', 
	if posixpath.isfile(backround):
		print 'background="'+backround+'">'
	elif backround[0:4] == "http":
		print 'background="'+backround+'">'
	elif backround[0] == "/":
		print 'background="'+backround+'">'
	else:
		print 'bgcolor="'+backround+'">'

def std_top(title):
	print """
<TABLE bgcolor="black" width="640" cellspacing="0" cellpadding="0" border="0">
<TR>
	<TD WIDTH="150">
		<TABLE border="0" cellspacing="2" cellpadding="2" WIDTH="100%">
		<TR>
			<TD bgcolor="blue" align="CENTER" valign="CENTER">
			<img src="/icons/pals_logo.gif"><BR>
			</TD></TR>
		</TABLE>
	</TD>

	<TD WIDTH="490" VALIGN="TOP">
		<TABLE border="0" cellspacing="2" cellpadding="2" WIDTH="100%">
		<TR>
			<TD bgcolor="white" align="CENTER" valign="TOP">
			<font size="3" face="ARIAL" color="red"><B>Partnerships to Advance Learning in Science</font></B>
			</TD></TR>
		<TR bgcolor="white">
			<TD align="CENTER" valign="BOTTOM">
			<font size="2">Developing, Implementing, and Sharing Constructivist Learning Reasources</font>
			</TD></TR>
		<TR bgcolor="white" align="center">
			<TD valign="BOTTOM">
			<BR>"""
	print '\t\t\t\t<H1>'+title+'</H1>'
	print '\t\t\t</TD></TR></TABLE>'
	print '\t</TD></TR></TABLE>'






def std_bot():
	now = time.time()
	now_tuple = time.localtime(now)
	date = time.strftime("%b %d, %Y", now_tuple)

	print '<BR><BR>'
	print '<TABLE bgcolor="black" width="640" cellspacing="0" cellpadding="0" border="0">\n'
	print '<TR><TD>'
	print '<TABLE border="0" cellspacing="3" cellpadding="3" WIDTH="100%">'
	print '\t<TR><TD bgcolor="white" align="CENTER" valign="TOP" colspan="2">'
	print '\t\t<a href="/index.html">PALS Homepage</a> | <a href="/home/email.html">Contact Us</a> | <A HREF="javascript:history.go(-1)">GO BACK</A>'
	print '\t\t</TD></TR>'
                        
	print '\t\t<TR bgcolor="white">'
	print '\t\t\t<TD align="CENTER" valign="CENTER">'
	print '\t\t\t<FONT SIZE="2" FACE="ARIAL,HELVETICA">'
	print '\t\t\t<B>Partnerships to Advance Learning in Science</B><BR>'
        print '\t\t\tDr. Doug Yarger - Program Coordinator'
        print '\t\t</FONT></TD>'
                                
        print '\t\t\t<TD bgcolor="red" align="CENTER" valign="CENTER">'
        print '\t\t\t<a href="http://www.iastate.edu" ALT="Iowa State University"><img src="/icons/isu.gif"></a>'
        print '\t\t<BR></TD>'

                        
        print '\t\t</TD></TR>'
        print '\t\t\t<TR bgcolor="white"><TD align="RIGHT" valign="BOTTOM" colspan="2">'
        print '\t\t\t<FONT SIZE="1" FACE="ARIAL,HELVETICA">'
        print '\t\t\t&#169; '+date+' PALS, all rights reserved<BR>'
        print '\t\t\tURL: <a href="https://pals.agron.iastate.edu">https://pals.agron.iastate.edu</a>'
        print '\t\t</TD></TR></TABLE>'
	print '\t</TD></TR></TABLE>'



def table_setter(width, *arguments):
	print '<table border="1" width='+width+'>'
	for arg in arguments:
		print '<th align="left" valign="top">'+arg+'</th>\n'		


def SendError(errmsg): 
        header("CGI ERROR","white") 
        std_top("PALS Script Execution Error")
	print '<BR><BR><BR>' 
        print "<H3><STRONG>" + errmsg + "</STRONG></H3>\n" 
	print '<BR><BR><BR>' 
        std_bot() 
        sys.exit(0)


def top_box(title_str, bgcolor, sec_color, fgcolor):
	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2">'
        print '<TABLE align="CENTER" bgcolor="'+bgcolor+'" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="'+fgcolor+'" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>'
	print title_str+'</B></font></TD></TR>'
        print '<TR><TD bgcolor="'+sec_color+'" align="center">'

def bot_box():
	print '<BR></TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

def jump_page(href):
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL='+href+'">'
	print '</HEAD></HTML>'

def clean_str(re_string):
	re_string = re.sub("'", "&#180;", re_string)
	return re_string

