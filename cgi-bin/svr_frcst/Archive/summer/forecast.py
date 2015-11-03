#!/usr/local/bin/python
# This program does the forecast thing
# Daryl Herzmann 5-20-1999
# UPDATED 7-12-99: Changed to the new format

import cgi, style, time, functs

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


def types():
	print '<CENTER>'
        print '<table width="100%" align="center"><tr>'
        print '<th><INPUT TYPE=checkbox NAME="T" VALUE="T"> Tornado</th>'
        print '<th><INPUT TYPE=checkbox NAME="H" VALUE="H"> Hail/Damaging Wind</th>'
        print '<th><INPUT TYPE=checkbox NAME="R" VALUE="R"> Greater Than 3 Inches of Rain</th>'
        print '</tr></table>'

def mk_sub_sec(string_title):   
        print '<TR><TD>&nbsp;</TD><TH align="left" colspan="2">'
        print '<font color="gold" size="4">'+string_title+'</FONT>'
        print '</TH></TR>'


def Main():
	style.header("Severe Forecasting Exercise","#0854a8")
	form = cgi.FormContent()
	secs = float(form["secs"][0])

	now = secs  	#
	now_tuple = time.localtime(now)	

	print '<form method="POST" action="hourly_pm.py">'
	print '<input type="hidden" name="secs" value="'+str(now)+'">'
	functs.setup_table() 

        functs.mk_sub_sec("Help Topics:")

        print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'
	print '<TD bgcolor="white" align="center" valign="center">'
        functs.mk_top(now_tuple)
        print '</TD></TR>' 

	functs.mk_sub_sec("Instructions:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	instructions()
	print '<BR>&nbsp;</TD></TR>'

	mk_sub_sec("1. Select a State:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2" align="center">'
	states()
	print '<BR>&nbsp;</TD></TR>'

	mk_sub_sec("2. Indicate the time frame when severe weather will occur:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2" align="center">'
	times()
	print '<BR>&nbsp;</TD></TR>'

	mk_sub_sec("3. Indicate what type(s) of severe weather will be occuring:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2" align="center">'
	types()
	print '<BR>&nbsp;</TD></TR>'


	functs.mk_sub_sec("4. Submit forecast:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2" align="center"><BR>'
	print '<input type="IMAGE" src="/icons/submit_forecast.gif" BORDER="0">'
	print '<BR>&nbsp;</TD></TR>'

	print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'




	print '</BODY></HTML>'

Main()
