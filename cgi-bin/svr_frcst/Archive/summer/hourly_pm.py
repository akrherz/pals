#!/usr/local/bin/python
# This will generate the hourly forecast excercise files to look at and pass along the forecast
# Daryl Herzmann 5/20/99
#UPDATED 6-4-99: Moved the wx_links to the middle..
# UPDATED 6-30-99: Cleaned up code and widened out the page
# UPDATED 7-05-99: Brand New Style

import cgi, style, time, functs, string, pg

mydb = pg.connect('arch_hourly')

def mk_before_links(now, H, T, R, state, etime):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(now)
	noon_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 12, now_tuple[4], now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	noon = time.mktime(noon_tuple)
	intervals = (now - noon) / 3600

	for i in range(intervals):
		secs = noon + i*3600
#		if i == 6:
#			print '</TR></TABLE><TABLE><TR>'

		if i == (intervals -1):
			print '<TD valign="top"><img src="/icons/'+str(i+1)+'pm.gif" BORDER="0" valign="top"></TD>'
		else:
			print '<TD valign="top">'
			print '<form method="POST" action="/cgi-bin/svr_frcst/summer/hourly_pm.py" name="'+str(i)+'">'
			print '<input type="hidden" value="'+str(secs)+'" name="secs">'
			print '<input type="hidden" name="H" value="'+H+'">'
			print '<input type="hidden" name="T" value="'+T+'">'
		        print '<input type="hidden" name="R" value="'+R+'">'
		        print '<input type="hidden" name="state" value="'+state+'">'
		        print '<input type="hidden" name="etime" value="'+etime+'">'
			print '<input type="image" SRC="/icons/'+str(i+1)+'pm.gif" BORDER="0">'
			print '</form>'
			print '</TD>'


def mk_after_links(now, H, T, R, state, etime):
	# It is important to note that the time gets incremented automatically when first imported into code

	now_tuple = time.localtime(now)
	twelve_tuple = (now_tuple[0], now_tuple[1], now_tuple[2], 23, 59, now_tuple[5], now_tuple[6], now_tuple[7], now_tuple[8])
	twelve = time.mktime(twelve_tuple) + 60
	intervals = (twelve - now) / 3600

	for i in range(intervals):
		secs = now + i*3600
#		if (now_tuple[3]+i-11) == 6:
#			print '</TR></TABLE><TABLE><TR>'

		if i == 0:
#			if (now_tuple[3]+i-11) == 7:
#				print '</TR></TABLE><TABLE><TR>'
			print '<TD valign="top">'
			print '<form method="POST" action="/cgi-bin/svr_frcst/summer/hourly_pm.py">'
			print '<input type="hidden" value="'+str(secs)+'" name="secs">'
			print '<input type="hidden" name="H" value="'+H+'">'
			print '<input type="hidden" name="T" value="'+T+'">'
		        print '<input type="hidden" name="R" value="'+R+'">'
		        print '<input type="hidden" name="state" value="'+state+'">'
		        print '<input type="hidden" name="etime" value="'+etime+'">'
			print '<input type="image" SRC="/icons/next_hour.gif" BORDER="0">'
			print '</form>'
			print '</TD>'
		else:
			if (now_tuple[3]+i-11) != 12:
				print '<TD valign="top">'
				print '<form method="POST" action="/cgi-bin/svr_frcst/summer/hourly_pm.py">'
				print '<input type="hidden" value="'+str(secs)+'" name="secs">'
				print '<input type="hidden" name="H" value="'+H+'">'
				print '<input type="hidden" name="T" value="'+T+'">'
			        print '<input type="hidden" name="R" value="'+R+'">'
			        print '<input type="hidden" name="state" value="'+state+'">'
			        print '<input type="hidden" name="etime" value="'+etime+'">'
				print '<input type="image" SRC="/icons/'+str(now_tuple[3]+i-11)+'pm.gif" BORDER="0">'
				print '</form>'
				print '</TD>'

			else:
				print '<TD valign="top">'
				print '<form method="POST" action="/cgi-bin/svr_frcst/summer/hourly_pm.py">'
				print '<input type="hidden" value="'+str(secs)+'" name="secs">'
				print '<input type="hidden" name="H" value="'+H+'">'
				print '<input type="hidden" name="T" value="'+T+'">'
			        print '<input type="hidden" name="R" value="'+R+'">'
			        print '<input type="hidden" name="state" value="'+state+'">'
			        print '<input type="hidden" name="etime" value="'+etime+'">'
				print '<input type="image" SRC="/icons/'+str(now_tuple[3]+i-11)+'am.gif" BORDER="0">'
				print '</form>'
				print '</TD>'

def annote(now, now_tuple, col):
        table_str = time.strftime("t%Y", now_tuple)

        try:
                select = mydb.query("SELECT "+col+" from "+table_str+" where ticks = '"+str(now)+"'").getresult() 
        except ValueError:
                print "Needs to be written yet"
                select = [(" "),(" ")]

        if len(select) == 0:
                print "Needs to be written yet"
        else:
                print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '<BR>'



def Main():
	style.header("Severe Forecasting Exercise","#0854a8")

	form = cgi.FormContent()
	secs = float(form["secs"][0])
	T, H, R = "No", "No", "No"
	if form.has_key("T"):   T = form["T"][0]
        if form.has_key("H"):   H = form["H"][0]
        if form.has_key("R"):   R = form["R"][0]
	state = form["state"][0]
        etime = form["etime"][0]

	now = secs + 3600 	# So that it is now the next hour
	now_tuple = time.localtime(now)	

	if now_tuple[3] == 0:		# This is a special case for midnight
		now = now - 60
		now_tuple = time.localtime(now)	


	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", time.gmtime(now))
	print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'
	
	functs.setup_table()
	functs.mk_sub_sec("Help Topics:")

	print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'

        print '<TD bgcolor="white" align="center" valign="center">'
	functs.mk_top(now_tuple)
	print '</TD></TR>'

	functs.mk_sub_sec("Messenges for this hour:")

	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	annote(secs + 3600, now_tuple, "events")
	print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Weather Data:")

	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	functs.mk_data(time.gmtime(now))
	print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Analysis for this hour:")

	print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
	annote(secs + 3600, now_tuple, "analysis")
	print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Navigation:")

	print '<TR><TD bgcolor="WHITE" colspan="3">'

	if now_tuple[4] == 59:
#		print '<TABLE><TR>'
#		mk_before_links(now + 60, H, T, R, state, etime)
		print '<BR><CENTER>'
		print '<form method="POST" action="/cgi-bin/svr_frcst/summer/results.py">'
		print '<input type="hidden" value="'+str(now)+'" name="secs">'
		print '<input type="hidden" name="H" value="'+H+'">'
		print '<input type="hidden" name="T" value="'+T+'">'
	        print '<input type="hidden" name="R" value="'+R+'">'
	        print '<input type="hidden" name="state" value="'+state+'">'
	        print '<input type="hidden" name="etime" value="'+etime+'">'
		print '<input type="image" SRC="/icons/view_results.gif" BORDER="0">'
		print '</form></CENTER>'
#		print '</TD</TR></TABLE>'

	else:
		print '<TABLE><TR>'
		mk_before_links(now, H, T, R, state, etime)
		mk_after_links(now, H, T, R, state, etime)
		print '</TR></TABLE>'
	print '</TD></TR>'

	print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'

	print '</BODY></HTML>'

Main()



