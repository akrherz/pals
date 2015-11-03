#!/usr/local/bin/python
# This will generate the hourly forecast excercise files to look at...
# Daryl Herzmann 5/20/99
# UPDATED 6-4-99:  Moved the wxlinks to a different spot
# UPDATED 6-4-99:  Gonna add hourly links in to help nav around
# UPDATED 6-30-99: Cleaned up code, looked for problems
# UPDATED 7-6-99:  Brand new format for the layout
# UPDATED 7-14-99: Changed a border problem
# UPDATED 7-16-99: Going to an entirely auth core
# UPDATED 7-21-99: Multiple questions per hour :(
#	UPDATED 7-28-99: Now multiple generic question sessions :(

import cgi, style, time, functs, pg, question

admindb = pg.connect('archadmin')
table_str = "sessions_417"

def mk_before_links(now, key):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(now)
	six_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 6, now_tuple[4], now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	six = time.mktime(six_tuple)
	intervals = (now - six) / 3600

	for i in range(intervals):
		secs = six + i*3600
		if i == (intervals - 1):
			if i != 5:
				print '<img src="/icons/'+str(i+7)+'am.gif" align="center" BORDER="0">'
			else:
				print '<img src="/icons/12pm.gif" align="center" BORDER="0">'
		else:
			print '<a href="hourly_am.py?secs='+str(secs)+'&key='+str(key)+'"><img src="/icons/'+str(i+7)+'am.gif" align="center" BORDER="0"></a> '


def mk_after_links(now, key):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(now)
	twelve_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 12, now_tuple[4], now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	twelve = time.mktime(twelve_tuple)
	intervals = (twelve - now) / 3600

	for i in range(intervals):
		secs = now + i*3600
		if i == 0:
			print '<a href="hourly_am.py?secs='+str(now)+'&key='+str(key)+'"><img src="/icons/next_hour.gif" BORDER="0" align="CENTER"></a>'
		else:
#			if (now_tuple[3]+i+1) != 12:
#				print '<a href="hourly_am.py?secs='+str(secs)+'&key='+str(key)+'"><img src="/icons/'+str(now_tuple[3]+i+1)+'am.gif" align="center" BORDER="0"></a>'
			out = "null"
#			else:
#				print '<a href="hourly_am.py?secs='+str(secs)+'&key='+str(key)+'"><img src="/icons/12pm.gif" align="center" BORDER="0"></a>'


def content():
	print '<BR>'
	print '<dd>You should view the available data for this hour and then navigate onto the next hour...</dd><BR>'


def Main():
	form = cgi.FormContent()
	try:
		secs = float(form["secs"][0])
		key = form["key"][0]
	except:
		style.SendError("CGI Value parse error")

	style.header("Severe Forecasting Exercise","#0854a8")

	query = admindb.query("SELECT last_time from "+table_str+" WHERE key = '"+str(key)+"' ").getresult()

	if float(secs) > float(query[0][0]):
		question.Main(secs, key, "hourly_am.py")	# This function may not return, be ware

	now = secs + 3600 		# So that it is now the next hour
	now_tuple = time.localtime(now)	

	functs.setup_table()

#	functs.check_key(key, now, "hourly_am.py")

        functs.mk_sub_sec("Help Topics:")

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'

	print '<TD bgcolor="white" align="center" valign="center">'
        functs.mk_top(now_tuple)
        print '</TD></TR>'

	functs.mk_sub_sec("Instructions:")

	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	content()
	print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Weather Data:")

	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        functs.mk_data(time.gmtime(now))
        print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Navigation:")
        
        print '<TR><TD bgcolor="WHITE" colspan="3" align="center"><BR>'

	mk_before_links(now, key)
	if now_tuple[3] == 12:
		print '<a href="forecast.py?secs='+str(now)+'&key='+str(key)+'"><img src="/icons/make_forecast.gif" align="CENTER"></a>'
	else:
		mk_after_links(now, key)
	print '</TD></TR>'

	print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'

        print '</BODY></HTML>'

Main()
