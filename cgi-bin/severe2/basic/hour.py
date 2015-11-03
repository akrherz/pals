#!/usr/bin/python
# This will be the generic hourly generator
# Daryl Herzmann 9-13-99

import pg, cgi, time, style, question, mx.DateTime, noon, results
from functs import *

def navigation(userKey):
	print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d">Navigation:</font></H2>'
	print '<CENTER>'
	print '<a href="'+scriptBase+'/hour.py?userKey='+str(userKey)+'"><img src="/gen/hour.php3?label=Next%20Hour&font_size=25" BORDER="0"></a>.'
	print '</CENTER>'

def next_hour(caseNum, secs):
	if caseNum[0] == "s":
		interval = 1
	else:
		interval = 3

	return secs + interval*3600


def been_here(key, secs):
        update = mydb.query("SELECT last_time from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
        if int(float( update[0][0] )) >= secs:
                return 1                                # WE have been here
        else:
                updatedb(key, secs)                     # This updates the session to know where we have been 
                return 0

def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = retreiveUser()


        if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) >= mx.DateTime.ISO.ParseDateTimeGMT(endTime)):
                results.Main()
                

	svrTop(lastTime)                        # Setup the page for the excercise
        mkHelp()
	
        if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) > mx.DateTime.ISO.ParseDateTimeGMT(gradeTime)):
		question.Main(lastTime, userKey, caseNum, startTime)

        if ( (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) == noonTime) and not form.has_key("noon") ):
                noon.Main(userKey, caseNum)

#	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", time.localtime(secs))
#        print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'

	# Check first if we have a question to display

	print """<BLOCKQUOTE>
  	<P><FONT FACE="Britannic Bold">Check it out!</FONT> Click under the column titled <FONT COLOR="#b0020f">Current,</FONT> and
find out what is happening around the country at this hour. <FONT COLOR="#b0020f" SIZE="+1">Hint</FONT>: If you need help
understanding the charts, please review our help topics.</P>
	</BLOCKQUOTE>"""

	dbComments(lastTime, "comments", "News and Notes:")
	print '<BR clear="all">'

	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3, 'b')
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1, 'b')

	if caseNum[0] == 's' and (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) > noonTime) :
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+2)
	elif caseNum[0] == 's':
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+1)        
	else:
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+3)

	if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) >= noonTime ):
		dbComments(lastTime, "analysis", "Meteorological Analysis:")

	print '<BR><BR>'
                
	navigation(userKey)

	updateUser(userKey, "lasttime", nextTime)

	svrBot()
Main()
