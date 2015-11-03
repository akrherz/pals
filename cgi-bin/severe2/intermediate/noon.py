#!/usr/bin/python
# This program does the forecast thing
# Daryl Herzmann 4 June 2000

import cgi, style, time, sys, pg, functs

def instructions():
	print """<font color="#a0522d">
	<blockquote>Once you have successfully submitted your forecast, you will be given the afternoon's data in the same format as the mornings. So you can experience the
	developement of severe weather for the remainder of the day.  At the end of the day (midnight), you will be given your score and an explanation of the day's severe weather.
	There will be more than one correct answer, so if you are not working alone everyone's opinion may be correct.</blockquote></font><BR>"""

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
	print '<th><INPUT TYPE=checkbox NAME="R" VALUE="R"> Flash Flooding (warning issued)</th>'
	print '</tr></table>'

def win_types():
        print """
        <TABLE>
        <TR><TD align="left">
                <INPUT TYPE=radio NAME="S" VALUE="S"> Moderately heavy snowfall (max. storm total amount in state is 6-12")<BR>
                <INPUT TYPE=radio NAME="S" VALUE="T"> Extreme snowfall (max. storm total amount in state exceeds 12")<BR>
                <INPUT TYPE=checkbox NAME="F" VALUE="F"> Ice storm (advisory-criteria glaze)<BR>
                <INPUT TYPE=checkbox NAME="C" VALUE="C"> Dangerous wind chills (advisory or warning)<BR>
        </TD></TR></TABLE>"""



def Main(userKey, caseNum):
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()

	print '<form method="POST" action="/cgi-bin/severe2/intermediate/wrapper.py">'
	print '<input type="hidden" name="userKey" value="'+str(userKey)+'">'

	instructions()

	print """<font color="BLUE"><H2>Make Your Forecast:</H2></font>
	<font color="#a0522d"><blockquote>You are now asked to forecast a state where you believe severe weather will occur.  More 
	specifically, forecast during which time period this will occur and what type(s) of severe weather.  Your forecast will be validated at the end
	of the exercise.</blockquote></font>"""

	print '<TABLE align="CENTER" WIDTH="90%">'
	print '<TR><TH bgcolor="#EEEEEE">Select a state:</TH></TR>'
	print '<TR><TD align="center">'
	states()
	print '</TD></TR>'

        if caseNum[0] == "s":
                print '<TR><TH bgcolor="#EEEEEE">Select A Valid Time:</TH></TR>'
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
        print '<input type="IMAGE" src="/gen/hour.php3?label=Submit%20Forecast&font_size=20" BORDER="0">'
        print '</TD></TR>'

        print '</TABLE>'
        print '</BODY></HTML>'

	functs.finishPage()
	sys.exit(0)
