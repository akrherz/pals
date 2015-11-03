#!/usr/local/bin/python
# This will be the generic hourly generator
# Daryl Herzmann 9-13-99

from functs import *

def mk_before(ldb, case_num, key, this_interval, className):
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
	 

	next_secs = start_secs + int(this_interval)*multi*3600
	noMore = 0

	for i in range(6):
		this_time = next_secs - (4-i)*3600*multi
		now_tuple = time.localtime(this_time)
#		print "<BR>",this_time, start_secs, last_time, this_time- start_secs, now_tuple, "<BR>"
		if this_time >= start_secs and this_time < next_secs:
			icon_ref = int(time.strftime("%H", now_tuple ))
			icon_ref = str(icon_ref)+"%20Z"
			print '<a href="'+scriptBase+'/hourly_post.py?className='+className+'&interval='+this_interval+'&case_num='+case_num+'&secs='+str(this_time)+'&key='+str(key)+'">'
			print '<img src="/gen/hour.php3?label='+icon_ref+'&font_size=25" border="0"></a>'
		elif this_time == end_secs +multi*3600*2:
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

def Main():
	interval = form["interval"][0]
	secs = int(float(form["secs"][0]))	# The current time
	secs_tuple = time.localtime(secs)	# The tuple of the current time
	next_secs = next_hour(case_num, secs)	# What is the next time

	svrFrcst.svrTop(secs_tuple, secs)			# Setup the page for the excercise
        mk_help()

	if getQuestions(ldb, key, secs, className, interval):
		question.Main(interval, case_num, secs, key, "hourly_post.py", className, ldb) # Looks for generic and specific questions to give the user

	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", time.localtime(secs))
        print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'

        print """
        <P>Examine the data presented below and then continue on by using the time navigation on the bottom of this page.
        Consult the "Help Topics" to the left if you have any questions.
        <P>Listed below is all weather data available for this time.  In the case of the Upper Air data and ETA data, the most recent valid
        data is used..
        <BR><BR>"""

	db_comments_417(secs, secs_tuple, "comments", "News and Comments:", className)

	print '<BR clear="all">'
	
	if case_num[0] == 'w':
	        mk_data(secs_tuple, 3)
	else:
		mk_data(secs_tuple, 1)

	db_comments_417(secs, secs_tuple, "analysis", "Meteorological Analysis:", className)

	print '<BR><img src="/icons/navigation.gif"><BR><BR>'
	mk_before(ldb, case_num, key, interval, className)

	svrFrcst.svrBot()
	
	print '</body></html>'

Main()
