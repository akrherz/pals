#!/usr/local/bin/python
# This will be the forecasting pages for mt417, it will use the same features as the main page,
# But there will be more of them
# Daryl Herzmann 7-14-99

import time, style, cgi, string, pg, svr_frcst

svrdb = pg.connect('svr_frcst')

def mk_top(local):
	date_str = time.strftime("%B %d, %Y", local)
        return '<BR><H1 align="left"><font color="red"> Forecasting Exercise for '+date_str+'</font></H1>'

def Main():
	form = cgi.FormContent()
	day = int(form["day"][0])
	month = int(form["month"][0])
 	year = int(form["year"][0])

	gmt_tuple = (year, month, day, 11, 0, 0, 0, 0, 0)       # Form the original tuple
        gmt_secs = time.mktime(gmt_tuple)                     # Convert it into seconds
        local_tuple = (year, month, day, 6, 0, 0, 0, 0, 0)                 # Local-time tuple
	local_secs = time.mktime(local_tuple)

	svr_frcst.setup_page()

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">&nbsp;</TD>'
        print '<TD bgcolor="white" align="center" valign="center">'
        print mk_top(local_tuple)
        print '</TD></TR>'


#	section("Date and Time:", mk_top(local) )
#	section("Information:", "This is an exercise in forecasting severe weather. You will be given weather data up until noon. Then you will make a forecast for when, where, and what type of \
#				        severe weather will occur. Then you can see if your forecast predictions happened, or nothing happened.<BR>")
#	section("Preview", mk_intro(time_secs, local) )
#	section("Navigation:", '<CENTER><a href="hourly_am.py?secs='+str(time_secs)+'"><img src="/icons/start.gif" BORDER="0"></a>')

	svr_frcst.mk_sub_sec("Preview")
	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD bgcolor="WHITE" colspan="2">'
        svr_frcst.db_comments(gmt_secs, gmt_tuple, "comments")
        print '<BR>&nbsp;</TD></TR>'

	svr_frcst.mk_sub_sec("Navigation")
	print '<TR bgcolor="white"><TD>&nbsp;</TD><TH bgcolor="WHITE" colspan="2">'
	print '<a href="hourly_am.py?gmt_secs='+str(int(float(gmt_secs)))+'"><img src="/icons/start.gif" BORDER="0"></a>'
        print '<BR>&nbsp;</TH></TR>'

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD bgcolor="WHITE" colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR>'

        print '</TABLE></BODY></HTML>'

Main()
