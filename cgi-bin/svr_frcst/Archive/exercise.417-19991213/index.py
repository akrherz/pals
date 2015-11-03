#!/usr/local/bin/python
# This is the index file for the exercise. Gives the user an introduction to what will happen
# Daryl Herzmann 

import pg, cgi, style, svr_frcst, time, functs

mydb = pg.connect('svr_frcst')

def update_db(ldb, key, name, email, className):
	table_name = "users"
	update = ldb.query("UPDATE "+table_name+" SET last_time = '0', name = '"+name+"', email = '"+email+"', bonus_points = '0' WHERE userid = '"+key+"' ")

def Main():
	this_interval = "1"
	try:
		form = cgi.FormContent()
		case_num = form["case_num"][0]
		key = form["key"][0]
		email = form["email"][0]
		name = form["name"][0]
		className = form["className"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT start_secs, end_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float(secs[0][0]))
	start_tuple = time.localtime( start_secs )

	ldb = pg.connect('svr_'+className)
	update_db(ldb, key, name, email, className)

	svr_frcst.setup_page()

	print '<TR bgcolor="#0854a8"><TD>&nbsp;</TD><TD valign="center">'
        functs.mk_help()
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
        print 'This is a forecasting exercise for forecasting severe weather.  You will be given weather data for 6 hours into the forecast and then you \
	will be asked to make a decision on what you believe will happen.  At the end of this forecasting period, you will then be given your results.'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'

	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
	functs.db_comments_417(start_secs, start_tuple, "comments", "Preview:", className)
        print '<BR></TD></TR>\n\n'


	print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Navigation:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	if case_num[0] == "s":
		cgiValues = 'className='+className+'&interval='+this_interval+'&case_num='+case_num+'&secs='+str(int(start_secs)+3600)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/icons/start.gif" BORDER="0"></a>'
	else:
		cgiValues = 'className='+className+'&interval='+this_interval+'&case_num='+case_num+'&secs='+str(start_secs)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/icons/start.gif" BORDER="0"></a>'
	print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'

	print '</TABLE>'

Main()
