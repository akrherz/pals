#!/usr/local/bin/python
# This will be the generic hourly generator
# Daryl Herzmann 9-13-99

import pg, cgi, time, svr_frcst, style, question
from functs import *
mydb = pg.connect('svr_frcst')

def islast(case_num, secs):
	tester = mydb.query("SELECT start_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float(tester[0][0]))

	span = int( ( int(secs) - start_secs ) / 3600 )

	if case_num[0] == "s" and span < 6:
		return 2

	if case_num[0] == "w" and span < 6:
		return 2

	return 0


def next_hour(case_num, secs):
	if case_num[0] == "s":
		interval = 1
	else:
		interval = 3

	return secs + interval*3600

def updatedb(key, secs):
	update = mydb.query("UPDATE users set last_time = '"+str(secs)+"' WHERE userid = '"+str(key)+"' ")

def mk_before(case_num, key):
        last_time = int( mydb.query("SELECT last_time from users WHERE userid = '"+str(key)+"' "). getresult()[0][0] )
#       print time.localtime(last_time),"<BR>"
        case_boundry = mydb.query("SELECT start_secs, end_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
        start_secs = int(float( case_boundry[0][0] ))
        end_secs   = int(float( case_boundry[0][1] ))

        if case_num[0] == "w":
                multi = 3
                noon_secs = start_secs + 32400
        if case_num[0] == "s":
                multi = 1
                start_secs = start_secs + 3600
                noon_secs = start_secs + 18000
         

        next_secs = last_time + multi*3600
        noMore = 0

        for i in range(5):
                this_time = last_time - (3-i)*3600*multi
                now_tuple = time.localtime(this_time)
#               print "<BR>",this_time, start_secs, noon_secs, this_time- start_secs, this_time - noon_secs, now_tuple, "<BR>"
                if this_time >= start_secs and this_time != noon_secs and this_time <= last_time:
                        icon_ref = int(time.strftime("%H", now_tuple ))
                        icon_ref = str(icon_ref)+"%20Z"
                        print '<a href="'+scriptBase+'/hourly_pre.py?case_num='+case_num+'&secs='+str(this_time)+'&key='+str(key)+'">'
                        print '<img src="/gen/hour.php3?label='+icon_ref+'&font_size=25" border="0"></a>'
                elif this_time == noon_secs:
                        print '<a href="'+scriptBase+'/noon.py?key='+str(key)+'&case_num='+case_num+'&secs='+str(next_secs)+'">'
                        print '<img src="/gen/hour.php3?label=Make%20Forecast&font_size=25" border="0"></a>'
                        noMore = 1
                        break
        if not noMore:
                print '<a href="'+scriptBase+'/hourly_pre.py?key='+str(key)+'&case_num='+case_num+'&secs='+str(next_secs)+'">'
                print '<img src="/gen/hour.php3?label=Next%20Hour&font_size=25" BORDER="0"></a>'


#def mk_before(case_num, secs, key):
#	start_secs = mydb.query("SELECT start_secs from cases WHERE case_num = '"+case_num+"' ").getresult()[0][0]
#
#	if case_num[0] == "w":
#		multi = 3
#	if case_num[0] == "s":
#		multi = 1
#	
#	intervals = ( int( secs ) - int(float( start_secs )) ) / (3600 *multi)
#	for i in range(intervals):
#		this_secs = int(float( start_secs ))+ i*3600*multi 
#		now_tuple = time.localtime(this_secs)
#		icon_ref = time.strftime("/icons/%HZ.gif", now_tuple )
#		print '<a href="'+scriptBase+'hourly_pre.py?case_num='+case_num+'&secs='+str(this_secs)+'&key='+str(key)+'"><img src="'+icon_ref+'" border="0"></a>'

def been_here(key, secs):
        update = mydb.query("SELECT last_time from users WHERE userid = '"+str(key)+"' "). getresult()
        if int(float( update[0][0] )) >= secs:
                return 1                                # WE have been here
        else:
                updatedb(key, secs)                     # This updates the session to know where we have been 
                return 0

def Main():
	form = cgi.FormContent()		# We start by getting neccessary values
	case_num = form["case_num"][0]		# Which case we are in
	key = form["key"][0]			# This session key
	secs = int(float(form["secs"][0]))	# The current time
	secs_tuple = time.localtime(secs)	# The tuple of the current time
	next_secs = next_hour(case_num, secs)	# What is the next time

	svr_frcst.setup_page()			# Setup the page for the excercise

	islaster = islast(case_num, secs)		# This will eventually be my grader

	
	if not been_here(key, secs):
		question.Main(case_num, secs, key, "hourly_pre.py")	# Looks for generic and specific questions to give the user

	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", time.localtime(secs))
        print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'

        print '<TR><TD>&nbsp;</TD><TD valign="top">'
        svr_frcst.mk_help()
        print '</TD>'

        print '<TD align="center" valign="center">'
        svr_frcst.mk_top(secs_tuple, secs)
        print '</TD></TR>'

        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'
        svr_frcst.db_comments(secs, secs_tuple, "comments", "News and Notes:")
        print '<BR></TD></TR>\n\n'


        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Weather Data:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
        mk_data(secs_tuple)
        print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '<BR></TD></TR>\n\n'


        print '<TR><TD>&nbsp;</TD>'
        print '<TD colspan="2"><BR>'

	print '<TABLE align="CENTER" bgcolor="black" cellpadding="2" border="0" width="100%">'
        print '<TR WIDTH="100%"><TD>'
        print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2" width="100%">'
        print '<TR><TD><font color="blue" size="4" face="ARIAL"><B>Navigation:</B></font></TD></TR>'
        print '<TR><TD bgcolor="white" align="center">'
	
	mk_before(case_num, key)
	
        print '</TD></TR></TABLE>'
        print '</TD></TR></TABLE>'

        print '</TD></TR></TABLE>'

Main()
