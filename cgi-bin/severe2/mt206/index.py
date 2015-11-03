#!/usr/bin/env python
# This is the index file for the exercise. Gives the user an introduction to what will happen
# Daryl Herzmann 

usersTable = "users206"
startInterval = "1"

import pg, cgi, style, time, functs, svrFrcst

mydb = pg.connect('svr_frcst')

def update_db(key, name, email, start_secs, caseNum, SSN):
	update = mydb.query("UPDATE "+usersTable+" SET ssn = '"+SSN+"', case_num = '"+caseNum+"', last_time = '"+str(start_secs)+"', realname = '"+name+"', email = '"+email+"', bonus_points = '0' WHERE userid = '"+key+"' ")

def Main():
	form = cgi.FormContent()

	if not form.has_key("email"):
		style.SendError("Please go back and enter your email address")
	email = form["email"][0]

	if not form.has_key("name"):
		style.SendError("Please go back and enter your name")
	name = form["name"][0]
	if not form.has_key("SSN"):
		style.SendError("Please go back and enter your social security number")
	SSN = form["SSN"][0]
	
	try:
		caseNum = form["caseNum"][0]
		key = form["key"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT start_secs from cases WHERE case_num = '"+caseNum+"' ").getresult()
	start_secs = int(float(secs[0][0]))
	start_tuple = time.localtime( start_secs )

	
	update_db(key, name, email, start_secs, caseNum, SSN)

	functs.svrTop(start_tuple, start_secs)

	print """
	<font color="blue"><H2>Introduction:</H2></font>
				This is a forecasting exercise for forecasting severe weather. You will be given hourly data for 6 hours
				and then asked to make some decisions on where you believe severe weather will occur.  Then you will be guided 
				through the rest of the case and then given the results at the end.  During this exercise, you may be asked 
				other case specific questions about the data that you are seeing.  Make sure to look at the maps, and good luck!
	<BR><BR>"""

	svrFrcst.printIntro(caseNum)


	print '<CENTER>'
	if caseNum[0] == "s":
		cgiValues = 'caseNum='+caseNum+'&secs='+str(int(start_secs)+3600)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" border="0"></a>'
	else:
		cgiValues = 'caseNum='+caseNum+'&secs='+str(start_secs)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'

	print '</CENTER>'
	functs.svrBot()
	print '</body></HTML>'


Main()
