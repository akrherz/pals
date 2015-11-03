#!/usr/local/bin/python
# This will be the generic hourly generator
# Daryl Herzmann 9-13-99
scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.417"

import pg, cgi, time, svr_frcst, style, question, functs
mydb = pg.connect('svr_frcst')


def mk_before(ldb, case_num, key, this_interval, className):
	usersTable = "users"
	last_time = int( ldb.query("SELECT last_time from "+usersTable+" WHERE userid = '"+str(key)+"' ").getresult()[0][0] )
#	print time.localtime(last_time),"<BR>"
	case_boundry = mydb.query("SELECT start_secs, end_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float( case_boundry[0][0] ))
	end_secs   = int(float( case_boundry[0][1] ))

	if case_num[0] == "w":
		multi = 3
		noon_secs = start_secs + 21600
	if case_num[0] == "s":
		multi = 1
		start_secs = start_secs + 3600
		noon_secs = start_secs + 18000
	 

	next_secs = last_time + multi*3600
	noMore = 0

	for i in range(5):
		this_time = last_time - (3-i)*3600*multi
		now_tuple = time.localtime(this_time)
#		print "<BR>",this_time, start_secs, last_time, this_time- start_secs, now_tuple, "<BR>"
		if this_time >= start_secs and this_time <= last_time:
			icon_ref = int(time.strftime("%H", now_tuple ))
			icon_ref = str(icon_ref)+"%20Z"
			print '<a href="'+scriptBase+'/hourly_post.py?className='+className+'&interval='+this_interval+'&case_num='+case_num+'&secs='+str(this_time)+'&key='+str(key)+'">'
			print '<img src="/gen/hour.php3?label='+icon_ref+'&font_size=25" border="0"></a>'
		elif this_time == end_secs:
		        print '<a href="'+scriptBase+'/results.py?className='+className+'&key='+str(key)+'&case_num='+case_num+'&secs='+str(next_secs)+'">'
			print '<img src="/gen/hour.php3?label=View%20Results&font_size=25" border="0"></a>'
			noMore = 1
			break
	if not noMore:
	        print '<a href="'+scriptBase+'/hourly_post.py?className='+className+'&interval='+str(int(this_interval)+1)+'&key='+str(key)+'&case_num='+case_num+'&secs='+str(next_secs)+'">'
		print '<img src="/gen/hour.php3?label=Next%20Hour&font_size=25" BORDER="0"></a>'


def next_hour(case_num, secs):
	if case_num[0] == "s":
		interval = 1
	else:
		interval = 3

	return secs + interval*3600

def updatedb(ldb, key, secs, className):
	usersTable = "users"
	update = ldb.query("UPDATE "+usersTable+" set last_time = '"+str(secs)+"' WHERE userid = '"+str(key)+"' ")

def been_here(ldb, key, secs, className):
	usersTable = "users"
	update = ldb.query("SELECT last_time from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
	if int(float( update[0][0] )) >= secs:
		return 1
	else:
		updatedb(ldb, key, secs, className)			# This updates the session to know where we have been 
		return 0

def Main():
	form = cgi.FormContent()		# We start by getting neccessary values
	case_num = form["case_num"][0]		# Which case we are in
	key = form["key"][0]			# This session key
	secs = int(float(form["secs"][0]))	# The current time
	secs_tuple = time.localtime(secs)	# The tuple of the current time
	next_secs = next_hour(case_num, secs)	# What is the next time
	interval = form["interval"][0]
	className = form["className"][0]
	ldb = pg.connect('svr_'+className)

	svr_frcst.setup_page()			# Setup the page for the excercise

	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", time.localtime(secs))
        print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'

	if not been_here(ldb, key, secs, className):
		question.Main(interval, case_num, secs, key, "hourly_post.py", className) # Looks for generic and specific questions to give the user


	print '<TR><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'
        print '<TD align="center" valign="center">'
        svr_frcst.mk_top(secs_tuple, secs)
        print '</TD></TR>'


        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
        functs.db_comments_417(secs, secs_tuple, "comments", "News and Comments:", className)
        print '<BR></TD></TR>\n\n'

        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2">'

        print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Weather Data:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	if case_num[0] == 'w':
	        functs.mk_data(secs_tuple, 3)
	else:
		functs.mk_data(secs_tuple, 1)
        print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'

        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2">'
        functs.db_comments_417(secs, secs_tuple, "analysis", "Meteorological Analysis:", className)
        print '<BR></TD></TR>\n\n'

        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2">'
	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Navigation:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center" NOWRAP>'

	mk_before(ldb, case_num, key, interval, className)
	
        print '<BR></TD></TR></TABLE>'
	print '</TD></TR></TABLE>'
	print '</TD></TR></TABLE>'

	print '</body></html>'
Main()
