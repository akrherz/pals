#!/usr/local/bin/python
# This program does the forecast thing
# Daryl Herzmann 5-20-1999
# UPDATED 7-12-99: Changed to the new format
# UDPATED 7-17-99: Cleaned code

import cgi, style, time, functs, svr_frcst, sys
from pgext import *

admindb = connect('svr_frcst')

def instructions():
	print "<P>Once you have successfully submitted your forecast, you \
        will be given the afternoon's data in the same format as the \
        mornings. So you can experience the developement of severe \
        weather for the remainder of the day.  At the end of the day \
        (midnight), you will be given your score and an explanation of \
        the day's severe weather.<BR>"

def states():
        print '<SELECT NAME="state"><OPTION> Alabama <OPTION> Arkansas <OPTION> Arizona<OPTION> California <OPTION> Colorado <OPTION> Connecticut <OPTION> Delaware <OPTION> Florida<OPTION> Georgia <OPTION> Idaho <OPTION> Illinois <OPTION> Indiana<OPTION> Iowa <OPTION> Kansas<OPTION> Kentucky <OPTION> Louisiana <OPTION> Maine <OPTION> Maryland'
        print '<OPTION> Massachusetts<OPTION> Michigan <OPTION> Minnesota <OPTION> Mississippi <OPTION> Missouri <OPTION> Montana<OPTION> Nebraska <OPTION> Nevada <OPTION> New_Hampshire <OPTION> New_Jersey <OPTION> New_Mexico'
        print '<OPTION> New_York <OPTION> North_Carolina <OPTION>North_Dakota <OPTION> Ohio <OPTION> Oklahoma<OPTION> Oregon <OPTION> Pennsylvania <OPTION> Rhode_Island <OPTION> South_Carolina <OPTION> South_Dakota'
        print '<OPTION> Tennessee <OPTION> Texas <OPTION> Utah <OPTION>Vermont <OPTION> Virginia <OPTION> Washington<OPTION> Wisconsin <OPTION> West_Virginia <OPTION> Wyoming </SELECT>'

def times():
        print '<SELECT NAME="etime"><OPTION VALUE="1"> Noon-3 PM <OPTION VALUE="2"> 3-6 PM<OPTION VALUE="3"> 6-9 PM<OPTION VALUE="4"> 9-Midnight</SELECT>'


def sum_types():
	print '<CENTER>'
        print '<table width="100%" align="center"><tr>'
        print '<th><INPUT TYPE=checkbox NAME="T" VALUE="T"> Tornado</th>'
        print '<th><INPUT TYPE=checkbox NAME="H" VALUE="H"> Hail/Damaging Wind</th>'
        print '<th><INPUT TYPE=checkbox NAME="R" VALUE="R"> Greater Than 3 Inches of Rain</th>'
        print '</tr></table>'

def win_types():
        print '<CENTER>'
        print '<table width="100%" align="center"><tr>'
        print '<th><INPUT TYPE=checkbox NAME="S" VALUE="S"> 6 to 12 inches of Snow</th>'
        print '<th><INPUT TYPE=checkbox NAME="T" VALUE="T"> Greater than 12 inches of Snow</th>'
        print '<th><INPUT TYPE=checkbox NAME="F" VALUE="F"> Freezing Rain / Ice </th>'
#	print '<th><INPUT TYPE=checkbox NAME="C" VALUE="C"> Dangerous wind chills (advisory or warning)</th>'
        print '</tr></table>'

def mk_sub_sec(string_title):   
        print '<TR><TD>&nbsp;</TD><TH align="left" colspan="2">'
        print '<font color="gold" size="4">'+string_title+'</FONT>'
        print '</TH></TR>'

def chk_allready(key, secs, case_num):
	attempt = admindb.query("SELECT state from users WHERE userid = '"+str(key)+"' ").getresult()

	if len(attempt[0][0]) > 0:
		print 'Content-type: text/html \n\n'
		print '<HTML><HEAD>'
	        print '<meta http-equiv="Refresh" content="1; URL=hourly_post.py?case_num='+case_num+'&secs='+str(secs)+'&key='+str(key)+'">'
		print '</HEAD>'
		print 'You have allready made a forecast!!, Too late to change it now'
		sys.exit(0)

def Main():
	form = cgi.FormContent()
	try:
	        key = form["key"][0]    
	        case_num = form["case_num"][0]
	        secs = int(float(form["secs"][0]))
	except:
		style.SendError("CGI Value Parse Error")

	now = secs  - 3600
	now_tuple = time.localtime(now)	

	chk_allready(key, now, case_num)

	svr_frcst.setup_page()

	print '<form method="POST" action="wrapper.py">'
	print '<input type="hidden" name="secs" value="'+str(now)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="case_num" value="'+str(case_num)+'">'

	print '<TR><TD>&nbsp;</TD><TD valign="top">'
        svr_frcst.mk_help()
        print '</TD>'

        print '<TD align="center" valign="center">'
        svr_frcst.mk_top(now_tuple, now)
        print '</TD></TR>'

	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Instructions:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white">'
	instructions()
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'
        print '<BR></TD></TR>\n\n'


	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Select a State:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	states()
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'
        print '<BR></TD></TR>\n\n'

	if case_num[0] == "s":
		print '<TR><TD>&nbsp;</TD>'
        	print '<TD colspan="2"><BR>'
		print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        	print '<TR WIDTH="100%"><TD>'
        	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>2. Indicate the time frame when severe weather will occur:</B></font></TD></TR>'
        	print '<TR><TD bgcolor="white" align="center">'
		times()
		print '</TD></TR></TABLE>'
        	print '</TD></TR></TABLE>'
        	print '<BR></TD></TR>\n\n'

		print '<TR><TD>&nbsp;</TD>'
        	print '<TD colspan="2"><BR>'
		print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        	print '<TR WIDTH="100%"><TD>'
        	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        	print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>3. Indicate what type(s) of severe weather will be occuring:</B></font></TD></TR>'
        	print '<TR><TD bgcolor="white" align="center">'
		sum_types()
		print '</TD></TR></TABLE>'
        	print '</TD></TR></TABLE>'
        	print '<BR></TD></TR>\n\n'

	if case_num[0] == "w":
		print '<TR><TD>&nbsp;</TD>'
	        print '<TD colspan="2"><BR>'
		print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
	        print '<TR WIDTH="100%"><TD>'
	        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
	        print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>3. Indicate what type(s) of severe weather will be occuring::</B></font></TD></TR>'
	        print '<TR><TD bgcolor="white" align="center">'
		win_types()
		print '</TD></TR></TABLE>'
	        print '</TD></TR></TABLE>'
	        print '<BR></TD></TR>\n\n'

	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="3" face="ARIAL"><B>4. Submit your forecast:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	print '<input type="IMAGE" src="/icons/submit_forecast.gif" BORDER="0">'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'
        print '<BR></TD></TR>\n\n'

        print '</TD></TR></TABLE>'
	print '</BODY></HTML>'

Main()
