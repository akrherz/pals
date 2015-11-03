#!/usr/local/bin/python
# This program does the forecast thing
# Daryl Herzmann 

import cgi, style, time, pg, sys
from functs import *

def instructions():
	print "<P>Once you have successfully submitted your forecast, you \
        will be given the data for the rest of the case in the same format as the \
        mornings. So you can experience the developement of severe \
        weather for the remainder of the day.  At the end of the day \
        , you will be given your score and an explanation of \
        the day's severe weather.<BR>"

def states():
        print '<SELECT NAME="state"><OPTION> Alabama <OPTION> Arkansas <OPTION> Arizona<OPTION> California <OPTION> Colorado <OPTION> Connecticut <OPTION> Delaware <OPTION> Florida<OPTION> Georgia <OPTION> Idaho <OPTION> Illinois <OPTION> Indiana<OPTION> Iowa <OPTION> Kansas<OPTION> Kentucky <OPTION> Louisiana <OPTION> Maine <OPTION> Maryland'
        print '<OPTION> Massachusetts<OPTION> Michigan <OPTION> Minnesota <OPTION> Mississippi <OPTION> Missouri <OPTION> Montana<OPTION> Nebraska <OPTION> Nevada <OPTION> New_Hampshire <OPTION> New_Jersey <OPTION> New_Mexico'
        print '<OPTION> New_York <OPTION> North_Carolina <OPTION>North_Dakota <OPTION> Ohio <OPTION> Oklahoma<OPTION> Oregon <OPTION> Pennsylvania <OPTION> Rhode_Island <OPTION> South_Carolina <OPTION> South_Dakota'
        print '<OPTION> Tennessee <OPTION> Texas <OPTION> Utah <OPTION>Vermont <OPTION> Virginia <OPTION> Washington<OPTION> Wisconsin <OPTION> West_Virginia <OPTION> Wyoming </SELECT>'

def times():
        print '<SELECT NAME="etime"><OPTION VALUE="1"> Noon-3 PM <OPTION VALUE="2"> 3-6 PM<OPTION VALUE="3"> 6-9 PM<OPTION VALUE="4"> 9-Midnight</SELECT>'


def sum_types():
	print """
	<TABLE>
	<TR><TD align="left">
		<INPUT TYPE=checkbox NAME="T" VALUE="T"> Tornado<BR>
		<INPUT TYPE=checkbox NAME="H" VALUE="H"> Hail/Damaging Wind<BR>
		<INPUT TYPE=checkbox NAME="R" VALUE="R"> Greater Than 3 Inches of Rain<BR>
	</TD></TR></TABLE>"""

def win_types():
	print """
	<TABLE>
	<TR><TD align="left">
		<INPUT TYPE=radio NAME="S" VALUE="S"> Moderately heavy snowfall (max. storm total amount in state is 6-12")<BR>
		<INPUT TYPE=radio NAME="S" VALUE="T"> Extreme snowfall (max. storm total amount in state exceeds 12")<BR>
		<INPUT TYPE=checkbox NAME="F" VALUE="F"> Ice storm (advisory-criteria glaze)<BR>
		<INPUT TYPE=checkbox NAME="C" VALUE="C"> Dangerous wind chills (advisory or warning)<BR>
	</TD></TR></TABLE>"""

def mk_sub_sec(string_title):   
        print '<TR><TD>&nbsp;</TD><TH align="left" colspan="2">'
        print '<font color="gold" size="4">'+string_title+'</FONT>'
        print '</TH></TR>'

def chk_allready(ldb, key, secs, interval, case_num, className):
	tableName = "users"
	attempt = ldb.query("SELECT state from "+tableName+" WHERE userid = '"+str(key)+"' ").getresult()

	if len(attempt[0][0]) > 0:
		print 'Content-type: text/html \n\n'
		print '<HTML><HEAD>'
	        print '<meta http-equiv="Refresh" content="1; URL=hourly_post.py?className='+className+'&case_num='+case_num+'&interval='+interval+'&secs='+str(secs)+'&key='+str(key)+'">'
		print '</HEAD>'
		print 'You have allready made a forecast!!, Too late to change it now'
		sys.exit(0)

def Main():
	form = cgi.FormContent()
	try:
	        key = form["key"][0]
	        case_num = form["case_num"][0]
	        secs = int(float(form["secs"][0]))
		interval = form["interval"][0]
		className = form["className"][0]
	except:
		style.SendError("CGI Value Parse Error")

	ldb = pg.connect('svr_'+className)

	if case_num[0] == "w":
		now = secs  - 3*3600
		now_tuple = time.localtime(now)	
	if case_num[0] == "s":
		now = secs  - 3600
		now_tuple = time.localtime(now)	

	chk_allready(ldb, key, secs, interval, case_num, className)
	
	secs_tuple = time.localtime(secs)

	svr_top(secs_tuple, secs)
        mk_help()

	print '<form method="POST" action="wrapper.py">'
	print '<input type="hidden" name="secs" value="'+str(secs)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="case_num" value="'+str(case_num)+'">'
	print '<input type="hidden" name="className" value="'+str(className)+'">'
	print '<input type="hidden" name="interval" value="'+str(interval)+'">'

	print '<font color="BLUE"><H2>Instructions:</H2></font>'
	instructions()

	print '<BR><BR><font color="BLUE"><H2>Make Your Forecast:</H2></font>'

	print '<TABLE align="CENTER">'
	print '<TR><TH bgcolor="#EEEEEE">Select a state:</TH></TR>'
	print '<TR><TD align="center">'
	states()
	print '</TD></TR>'

	if case_num[0] == "s":
		print '<TR><TH bgcolor="#EEEEEE">Select a state:</TH></TR>'
		print '<TR><TD align="CENTER">'
		times()
		print '</TD></TR>'

                print '<TR><TH bgcolor="#EEEEEE">Type of Severe Weather: (Check all that apply)</TH></TR>'
		print '<TR><TD align="CENTER">'
		sum_types()
		print '</TD></TR>'

	if case_num[0] == "w":
                print '<TR><TH bgcolor="#EEEEEE">Type of Severe Weather: (Check all that apply)</TH></TR>'
		print '<TR><TD align="CENTER">'
		win_types()
		print '</TD></TR>'


	print '<TR><TH bgcolor="#EEEEEE">Submit Your Forecast:</TH></TR>'
	print '<TR><TD align="CENTER">'
	print '<input type="IMAGE" src="/gen/hour.php3?label=Submit%20Forecast&font_size=25" BORDER="0">'
	print '<input type="reset">'
	print '</TD></TR>'

	print '</TABLE>'

	svr_bot()

Main()
