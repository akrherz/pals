#!/usr/local/bin/python
# This will be the generic hourly generator
# Daryl Herzmann 9-13-99

import pg, cgi, time, style, question
from functs import *

def next_hour(caseNum, secs):
	if caseNum[0] == "s":
		interval = 1
	else:
		interval = 3

	return secs + interval*3600

def updatedb(key, secs):
	update = mydb.query("UPDATE "+usersTable+" set last_time = '"+str(secs)+"' WHERE userid = '"+str(key)+"' ")

def mk_before(caseNum, key):
        last_time = int( mydb.query("SELECT last_time from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()[0][0] )

        case_boundry = mydb.query("SELECT start_secs, end_secs from "+casesTable+" WHERE case_num = '"+caseNum+"' ").getresult()
        start_secs = int(float( case_boundry[0][0] ))
        end_secs   = int(float( case_boundry[0][1] ))

        if caseNum[0] == "w":
                multi = 3
                noon_secs = start_secs + 32400
        if caseNum[0] == "s":
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
                        print '<a href="'+scriptBase+'/hourly_pre.py?caseNum='+caseNum+'&secs='+str(this_time)+'&key='+str(key)+'">'
                        print '<img src="/gen/hour.php3?label='+icon_ref+'&font_size=25" border="0"></a>'
                elif this_time == noon_secs:
                        print '<a href="'+scriptBase+'/noon.py?key='+str(key)+'&caseNum='+caseNum+'&secs='+str(next_secs)+'">'
                        print '<img src="/gen/hour.php3?label=Make%20Forecast&font_size=25" border="0"></a>'
                        noMore = 1
                        break
        if not noMore:
                print '<a href="'+scriptBase+'/hourly_pre.py?key='+str(key)+'&caseNum='+caseNum+'&secs='+str(next_secs)+'">'
                print '<img src="/gen/hour.php3?label=Next%20Hour&font_size=25" BORDER="0"></a>'


def been_here(key, secs):
        update = mydb.query("SELECT last_time from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
        if int(float( update[0][0] )) >= secs:
                return 1                                # WE have been here
        else:
                updatedb(key, secs)                     # This updates the session to know where we have been 
                return 0

def Main():
	form = cgi.FormContent()		# We start by getting neccessary values
	caseNum = form["caseNum"][0]		# Which case we are in
	key = form["key"][0]			# This session key
	secs = int(float(form["secs"][0]))	# The current time
	secs_tuple = time.localtime(secs)	# The tuple of the current time
	next_secs = next_hour(caseNum, secs)	# What is the next time

	svrTop(secs_tuple, secs)                        # Setup the page for the excercise
        mkHelp()
	
	if not been_here(key, secs):
		question.Main(caseNum, secs, key, "hourly_pre.py")	# Looks for generic and specific questions to give the user

	print """
        <font color="blue"><H2>Instructions:</H2></font>
        <P>Examine the data presented below and then continue on by using the time navigation on the bottom of this page.
        Consult the "Help Topics" to the left if you have any questions.
        <P>Listed below is all weather data available for this time.
        <BR><BR>"""

	dbComments(secs, secs_tuple, "comments", "News and Notes:")

	print '<BR clear="all">'


        if caseNum[0] == 'w':
                mkData(secs_tuple, 3)
        else:
                mkData(secs_tuple, 1)


	print '<BR clear="all"><P><font color="blue"><H2>Navigation:</H2></font>'
	mk_before(caseNum, key)

	svrBot()
Main()
