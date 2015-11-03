#!/usr/local/bin/python
# This is the index file for the exercise. Gives the user an introduction to what will happen
# Daryl Herzmann 11-14-99

import pg, cgi, style, svr_frcst, time, functs

mydb = pg.connect('svr_frcst')

def update_db(key, name, email):
	update = mydb.query("UPDATE users_417 SET last_time = '0', name = '"+name+"', email = '"+email+"', bonus_points = '0' WHERE userid = '"+key+"' ")

def Main():
	this_interval = "1"
	try:
		form = cgi.FormContent()
		case_num = form["case_num"][0]
		key = form["key"][0]
		email = form["email"][0]
		name = form["name"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT start_secs, end_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float(secs[0][0]))
	end_secs = int(float(secs[0][0]))
	start_tuple = time.localtime( start_secs )
	end_tuple = time.localtime( end_secs )

	update_db(key, name, email)


	svr_frcst.setup_page()

	print '<TR bgcolor="#0854a8"><TD>&nbsp;</TD><TD valign="center">'
        svr_frcst.mk_help()
        print '</TD>'

        print '<TD bgcolor="#0854a8" align="center" valign="center"><BR>'
        svr_frcst.mk_top(start_tuple, start_secs)
        print '<BR></TD></TR>'


	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Introduction:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white">'
        print 'This is forecasting excercise in forecasting severe weather.  You will be given weather data for 6 hours into the forecast and then you \
	will be asked to make a decision on what you believe will happen.  At the end of this forecasting period, you will then be given your results.'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'

	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
	svr_frcst.db_comments_417(start_secs, start_tuple, "comments", "Preview:")
        print '<BR></TD></TR>\n\n'


	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Navigation:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	if case_num[0] == "s":
		print '<a href="hourly_pre.py?interval='+this_interval+'&case_num='+case_num+'&secs='+str(int(start_secs)+3600)+'&key='+str(key)+'"><img src="/icons/start.gif" BORDER="0"></a>'
	else:
		print '<a href="hourly_pre.py?interval='+this_interval+'&case_num='+case_num+'&secs='+str(start_secs)+'&key='+str(key)+'"><img src="/icons/start.gif" BORDER="0"></a>'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'

	print '</TABLE>'

#        style.std_bot()

Main()
