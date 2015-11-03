#!/usr/local/bin/python
# This program starts the students down the forecasting excercise road...
# Daryl Herzmann 8-18-99

import os, style, time, pg, cgi, functs

admindb = pg.connect('archadmin')

def setup_html():
        print '<TABLE WIDTH="600" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">'
        
        print '<TR>' 
        print '<TD colspan="3"><img src="/icons/svr_frcst-top.gif" HSPACE="0" VSPACE="0" BORDER="0"></TD></TR>'
        
        print '<TR valign="top" bgcolor="white">'
        print '<TD colspan="3"><img src="/icons/svr_frcst-upleft.gif" HSPACE="0" VSPACE="0" BORDER="0" HEIGHT="20"></TD></TR>'

def mk_top(local, key):
        query = admindb.query("SELECT name from win_sessions_417 WHERE key = '"+key+"' ").getresult()
        date_str = time.strftime("%B %d, %Y", local)
        try:
                print '<H1 align="left"><font color="blue"> Welcome '+query[0][0]+'</font></H1>'
        except:
                print '<H1 align="left"><font color="blue"> Welcome</font></H1>'
                
        print '<H1 align="left"><font color="red"> Forecasting Excercise for '+date_str+'</font></H1>'

def update_db(key, name, email):
	update = admindb.query("UPDATE win_sessions_417 SET last_time = '0', name = '"+name+"', email = '"+email+"' WHERE key = '"+key+"' ")

def section(title_str, res):
        print '<TR><TD>&nbsp;</TD><TH align="left">'
        print '<font color="gold" size="4">'+title_str+'</FONT>'
        print '</TH><TD bgcolor="white"><BR></TD></TR>\n\n'

        print '<TR bgcolor="white"><TD>&nbsp;</TD>'
        print '<TD bgcolor="white" colspan="2"><BR>'
        print res
        print '<BR></TD></TR>\n\n'



def Main():
	style.header("Winter Weather Forecasting excercise", "#0854a8")

	form = cgi.FormContent()
        try:
                case_num = form["case_num"][0]
                start_secs = form["start_secs"][0]
                email = form["email"][0]
                name = form["name"][0]
                key = form["key"][0]
        except:
                style.SendError("CGI value parse Error")

	email = functs.clean_str(email)
        name = functs.clean_str(name)

	update_db(key, name, email)

	local = time.localtime(float(start_secs))

	setup_html()
	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">&nbsp;</TD>'
        print '<TD bgcolor="white" align="center" valign="center">'
        mk_top(local, key)
        print '</TD></TR>'
	
	section("Information:", "This is an exercise in forecasting severe weather. You will be given weather data up until noon. Then you will make a forecast for when, where, and what type of severe weather will occur. Then you can see if your forecast predictions happened, or nothing happened.<BR>")
        section("Navigation:", '<CENTER><a href="hourly.py?case_num='+case_num+'&secs='+str(start_secs)+'&key='+str(key)+'"><img src="/icons/start.gif" BORDER="0"></a>')

        print '<TR bgcolor="white"><TD>&nbsp;</TD><TD bgcolor="WHITE" colspan="2">'

	style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'
        print '</BODY></HTML>'


Main()
