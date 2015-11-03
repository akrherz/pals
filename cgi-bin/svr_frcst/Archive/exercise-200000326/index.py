#!/usr/local/bin/python
# Ahh, this is the first program that will do all the general cases, winter and none...
# Daryl Herzmann 9-13-99

import pg, cgi, style, time, svrFrcst
from functs import *

def gen_key():
	key = int(float( time.time() ))

	enter = mydb.query("INSERT into "+usersTable+" values ('"+str(key)+"') ")
	update = mydb.query("UPDATE "+usersTable+" set bonus_points = '0', last_time = '10' WHERE userid = '"+str(key)+"' ")

	return str(key)

def Main():
	form = cgi.FormContent()
	try:
		caseNum = form["case_num"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT start_secs, end_secs from "+casesTable+" WHERE case_num = '"+caseNum+"' ").getresult()
	start_secs = int(float(secs[0][0]))
	end_secs = int(float(secs[0][0]))
	start_tuple = time.localtime( start_secs )
	end_tuple = time.localtime( end_secs )

	key = gen_key()

	svrTop(start_secs)

	print """
	<font color="blue"><H2>Introduction:</H2></font>
			This is an exerise in forecasting severe weather.  You will be given weather data for 6 hours into the forecast and then you  will be asked to make a
			decision on what you believe will happen.  Here is a look at the <a href="/svr_frcst/images/noonView.gif">forecasting page</a> you will
			encounter at 18z.  A few things you may want to keep an eye on in order to make an accurate forecast are:  the speed of the system to see how fast or
			slow it is moving, moisture supply out of the Gulf of Mexico to fuel storms, and any type of gradient(s) that exist (tempertatre, dew point, wind). At the end of this
			forecasting period, you will then be given your results.
	<BR><BR>"""

	svrFrcst.printIntro(caseNum)


	print '<CENTER>'
	if caseNum[0] == "s":
		print '<a href="hourly_pre.py?caseNum='+caseNum+'&secs='+str(int(start_secs) + 3600)+'&key='+str(key)+'">'
		print '<img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'
	else:
		print '<a href="hourly_pre.py?caseNum='+caseNum+'&secs='+str(start_secs)+'&key='+str(key)+'">'
		print '<img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'

	print '</CENTER>'

	svrBot()


Main()
