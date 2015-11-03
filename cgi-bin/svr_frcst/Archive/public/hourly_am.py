#!/usr/local/bin/python
# This will generate the hourly forecast excercise files to look at...
# Daryl Herzmann 5/20/99
#UPDATED 6-4-99: Moved the wxlinks to a different spot
#UPDATED 6-4-99: Gonna add hourly links in to help nav around
# UPDATED 6-30-99: Cleaned up code, looked for problems
# UPDATED 7-6-99: Brand new format for the layout
# UPDATED 7-14-99: Changed a border problem

import cgi, style, time, svr_frcst, functs

def mk_before_links(gmt_secs):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(gmt_secs)
	six_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 11, now_tuple[4], now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	six = time.mktime(six_tuple)
	intervals = (gmt_secs - six) / 3600

	for i in range(intervals):
		gmt_secs = six + i*3600
		if i == (intervals - 1):
			print '<img src="/icons/'+str(i+12)+'Z.gif" align="center" BORDER="0">'
		else:
			print '<a href="hourly_am.py?gmt_secs='+str(int(float(gmt_secs)))+'"><img src="/icons/'+str(i+12)+'Z.gif" align="center" BORDER="0"></a> '


def mk_after_links(gmt_secs):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(gmt_secs)
	twelve_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 17, now_tuple[4], now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	twelve = time.mktime(twelve_tuple)
	intervals = (twelve - gmt_secs) / 3600

	for i in range(intervals):
		secs = gmt_secs + i*3600
		if i == 0:
			print '<a href="hourly_am.py?gmt_secs='+str(secs)+'"><img src="/icons/next_hour.gif" BORDER="0" align="CENTER"></a>'
		else:
			print '<a href="hourly_am.py?gmt_secs='+str(secs)+'"><img src="/icons/'+str(now_tuple[3]+i+1)+'Z.gif" align="center" BORDER="0"></a>'


def content():
	print '<P>You should examine the charts linked below. And then navigate on to the next hour.'
	print '<P><B>Note:</B> Some data is missing.'


def Main():
	form = cgi.FormContent()
	gmt_secs = int(form["gmt_secs"][0])

	gmt_secs = gmt_secs + 3600 	# So that it is now the next hour
	gmt_tuple = time.localtime(gmt_secs)	

	if gmt_tuple[8] == 1:
		local_secs = gmt_secs - 18000
	else:
		local_secs = gmt_secs - 21600


	local_tuple = time.localtime(local_secs)	

	svr_frcst.setup_page()

	print gmt_tuple

        svr_frcst.mk_sub_sec("Help Topics:")
	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'

	print '<TD bgcolor="white" align="center" valign="center">'
        functs.mk_top(local_tuple)
        print '</TD></TR>'

	functs.mk_sub_sec("Instructions:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	content()
	print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Weather Data:")
	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        functs.mk_data(gmt_tuple)
        print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Navigation:")
	print '<TR><TD bgcolor="WHITE" colspan="3" align="center"><BR>'

	mk_before_links(gmt_secs)
	if local_tuple[3] == 12:
		print '<a href="forecast.py?gmt_secs='+str(gmt_secs)+'"><img src="/icons/make_forecast.gif" align="CENTER"></a>'
	else:
		mk_after_links(gmt_secs)
	print '</TD></TR>'

	print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'

        print '</BODY></HTML>'

Main()
