#!/usr/local/bin/python
# This will be the forecasting pages for mt417, it will use the same features as the main page,
# But there will be more of them
# Daryl Herzmann 7-14-99

import time, style, cgi, string, pg

mydb = pg.connect('arch_hourly')

def setup_html():
	style.header("Severe Weather Forecasting Exercise", "#0854a8")
	print '<TABLE WIDTH="600" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">'
	
	print '<TR>' 
	print '<TD colspan="3"><img src="/icons/svr_frcst-top.gif" HSPACE="0" VSPACE="0" BORDER="0"></TD></TR>'
	
	print '<TR valign="top" bgcolor="white">'
        print '<TD colspan="3"><img src="/icons/svr_frcst-upleft.gif" HSPACE="0" VSPACE="0" BORDER="0" HEIGHT="20"></TD></TR>'

def mk_top(local):
	date_str = time.strftime("%B %d, %Y", local)
        return '<BR><H1 align="left"><font color="red"> Forecasting Exercise for '+date_str+'</font></H1>'


def section(title_str, res):
	print '<TR><TD>&nbsp;</TD><TH align="left">'
        print '<font color="gold" size="4">'+title_str+'</FONT>'
        print '</TH><TD bgcolor="white"><BR></TD></TR>\n\n'

	print '<TR bgcolor="white"><TD>&nbsp;</TD>'
	print '<TD bgcolor="white" colspan="2"><BR>'
	print res
	print '<BR></TD></TR>\n\n'

def mk_intro(ticks, local):
        table_name = string.lower(time.strftime("t%Y", local))
        test = time.localtime(int(float(ticks)))
        try:
                select = mydb.query("SELECT events from "+table_name+" where ticks = '"+str(ticks)+"' ").getresult() 
        except ValueError:
                return "Needs to be written yet<BR>"
                select = [(" "),(" ")]

        if len(select) == 0:
                print "Needs to be written yet<BR>"
        else:
                return select[0][0]+"<BR>"

def Main():
	form = cgi.FormContent()
	day = int(form["day"][0])
	month = int(form["month"][0])
 	year = int(form["year"][0])

	time_tuple = (year, month, day, 6, 0, 0, 0, 0, 0)       # Form the original tuple
        time_secs = time.mktime(time_tuple)                     # Convert it into seconds
        local = time.localtime(time_secs)                       # Local-time tuple

	setup_html()

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">&nbsp;</TD>'
        print '<TD bgcolor="white" align="center" valign="center">'
        print mk_top(local)
        print '</TD></TR>'


#	section("Date and Time:", mk_top(local) )
	section("Information:", "This is an exercise in forecasting severe weather. You will be given weather data up until noon. Then you will make a forecast for when, where, and what type of \
				        severe weather will occur. Then you can see if your forecast predictions happened, or nothing happened.<BR>")
	section("Preview", mk_intro(time_secs, local) )
	section("Navigation:", '<CENTER><a href="hourly_am.py?secs='+str(time_secs)+'"><img src="/icons/start.gif" BORDER="0"></a>')

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD bgcolor="WHITE" colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'
        print '</BODY></HTML>'

Main()
