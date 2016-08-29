#!/usr/bin/python
# Ahh, this is the first program that will do all the general cases, winter and none...
# Daryl Herzmann 9-13-99

import pg, cgi, style, time, svrFrcst
from functs import *

def gen_key():
	userKey = int(float( time.time() ))

	enter = mydb.query("INSERT into "+usersTable+" values ("+str(userKey)+") ")
	update = mydb.query("UPDATE "+usersTable+" set bonusPoints = '0', lastTime = '1900-01-01 01:00:00' WHERE userKey = "+str(userKey)+" ")

	return str(userKey)

def Main():
	form = cgi.FormContent()
	try:
		caseNum = form["caseNum"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT starttime, endtime from "+casesTable+" WHERE casenum = '"+caseNum+"' ").dictresult()
	startTime = secs[0]["starttime"]
	endTime = secs[0]["endtime"]

	userKey = gen_key()

	updateUser(userKey, "lasttime", startTime)
	updateUser(userKey, "gradetime", "1900-01-01 00:00:00-00")
	updateUser(userKey, "casenum", caseNum)

	svrTop(startTime)

	print """	This is an exercise in forecasting severe weather.  You will be given weather data for 6 hours into the forecast and then you  will be asked to make a
			decision on what you believe will happen.  Here is a look at the <a href="/svr_frcst/images/noonView.gif">forecasting page</a> you will
			encounter at 18z.  A few things you may want to keep an eye on in order to make an accurate forecast are:  the speed of the system to see how fast or
			slow it is moving, moisture supply out of the Gulf of Mexico to fuel storms, and any type of gradient(s) that exist (tempertatre, dew point, wind). At the end of this
			forecasting period, you will then be given your results.
	<BR><BR>"""

	getIntro(caseNum)


	print '<CENTER>'
	if caseNum[0] == "s":
		print '<a href="'+scriptBase+'/hour.py?userKey='+str(userKey)+'">'
		print '<img src="/gen/hour.php?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'
	else:
		print '<a href="'+scriptBase+'/hour.py?userKey='+str(userKey)+'">'
		print '<img src="/gen/hour.php?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'

	print '</CENTER>'

	svrBot()

Main()
