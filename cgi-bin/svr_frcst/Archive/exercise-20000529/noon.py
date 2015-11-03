#!/usr/local/bin/python
# This program does the forecast thing
# Daryl Herzmann 5-20-1999
# UPDATED 7-12-99: Changed to the new format
# UDPATED 7-17-99: Cleaned code

import cgi, style, time, functs, sys, pg
from functs import *

def instructions():
	print """
	<P>Once you have successfully submitted your forecast, you will be given the afternoon's data in the same format as the mornings. So you can experience the
	developement of severe weather for the remainder of the day.  At the end of the day (midnight), you will be given your score and an explanation of the day's severe weather.
	There will be more than one correct answer, so if you are not working alone everyone's opinion may be correct.<BR>"""

def states():
        print '<SELECT NAME="state"><OPTION> Alabama <OPTION> Arkansas <OPTION> Arizona<OPTION> California <OPTION> Colorado <OPTION> Connecticut <OPTION> Delaware <OPTION> Florida<OPTION> Georgia <OPTION> Idaho <OPTION> Illinois <OPTION> Indiana<OPTION> Iowa <OPTION> Kansas<OPTION> Kentucky <OPTION> Louisiana <OPTION> Maine <OPTION> Maryland'
        print '<OPTION> Massachusetts<OPTION> Michigan <OPTION> Minnesota <OPTION> Mississippi <OPTION> Missouri <OPTION> Montana<OPTION> Nebraska <OPTION> Nevada <OPTION> New_Hampshire <OPTION> New_Jersey <OPTION> New_Mexico'
        print '<OPTION> New_York <OPTION> North_Carolina <OPTION>North_Dakota <OPTION> Ohio <OPTION> Oklahoma<OPTION> Oregon <OPTION> Pennsylvania <OPTION> Rhode_Island <OPTION> South_Carolina <OPTION> South_Dakota'
        print '<OPTION> Tennessee <OPTION> Texas <OPTION> Utah <OPTION>Vermont <OPTION> Virginia <OPTION> Washington<OPTION> Wisconsin <OPTION> West_Virginia <OPTION> Wyoming </SELECT>'

def times():
        print """
	<SELECT NAME="etime">
		<OPTION VALUE="1"> Noon-3 PM 
		<OPTION VALUE="2"> 3-6 PM
		<OPTION VALUE="3"> 6-9 PM
		<OPTION VALUE="4"> 9-Midnight
	</SELECT>"""


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

def chk_allready(key, secs, caseNum):
	attempt = mydb.query("SELECT state from "+usersTable+" WHERE userid = '"+str(key)+"' ").getresult()

	if len(attempt[0][0]) > 0:
		print 'Content-type: text/html \n\n'
		print '<HTML><HEAD>'
	        print '<meta http-equiv="Refresh" content="1; URL=hourly_post.py?caseNum='+caseNum+'&secs='+str(secs)+'&key='+str(key)+'">'
		print '</HEAD>'
		print 'You have allready made a forecast!!, Too late to change it now'
		sys.exit(0)

def Main():
	form = cgi.FormContent()
	try:
	        key = form["key"][0]    
	        caseNum = form["caseNum"][0]
	        secs = int(float(form["secs"][0]))
	except:
		style.SendError("CGI Value Parse Error")

	if caseNum[0] == "w":
                now = secs  - 3*3600
                now_tuple = time.localtime(now) 
        else:
                now = secs  - 3600
                now_tuple = time.localtime(now) 

	chk_allready(key, now, caseNum)

	svrTop(now_tuple)
	mkHelp()

	print '<form method="POST" action="wrapper.py">'
	print '<input type="hidden" name="secs" value="'+str(now)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="caseNum" value="'+str(caseNum)+'">'

	instructions()

	print '<BR><BR><font color="BLUE"><H2>Make Your Forecast:</H2></font>'

        print '<TABLE align="CENTER" WIDTH="90%">'
        print '<TR><TH bgcolor="#EEEEEE">Select a state:</TH></TR>'
        print '<TR><TD align="center">'
        states()
        print '</TD></TR>'

        if caseNum[0] == "s":
                print '<TR><TH bgcolor="#EEEEEE">Select a state:</TH></TR>'
                print '<TR><TD align="CENTER">'
                times()
                print '</TD></TR>'

                print '<TR><TH bgcolor="#EEEEEE">Type of Severe Weather: (Check all that apply)</TH></TR>'
                print '<TR><TD align="CENTER">'
                sum_types()
                print '</TD></TR>'

        if caseNum[0] == "w":
                print '<TR><TH bgcolor="#EEEEEE">Type of Severe Weather: (Check all that apply)</TH></TR>'
                print '<TR><TD align="CENTER">'
                win_types()
                print '</TD></TR>'


        print '<TR><TH bgcolor="#EEEEEE">Submit Your Forecast:</TH></TR>'
        print '<TR><TD align="CENTER">'
        print '<input type="IMAGE" src="/icons/submit_forecast.gif" BORDER="0">'
        print '<input type="reset">'
        print '</TD></TR>'

        print '</TABLE>'
        print '</BODY></HTML>'

	svrBot()
Main()
