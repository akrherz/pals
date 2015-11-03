#!/usr/local/bin/python
# This is the index file for the exercise. Gives the user an introduction to what will happen
# Daryl Herzmann 

from functs import *
startInterval = "1"

def update_db(ldb, key, name, email, className, start_secs):
	update = ldb.query("UPDATE "+usersTable+" SET last_time = '"+str(start_secs)+"', name = '"+name+"', email = '"+email+"', bonus_points = '0', ans_ques = '"+answerQs+"' WHERE userid = '"+key+"' ")

def Main():
	if not form.has_key("email"):
		style.SendError("Please go back and enter your email address")
	email = form["email"][0]

	if not form.has_key("name"):
		style.SendError("Please go back and enter your name")
	name = form["name"][0]

	global answerQs
	answerQs = form["answerQs"][0]

	try:
		key = form["key"][0]
	except:
		style.SendError("Case number parse error")

	secs = mydb.query("SELECT start_secs from cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = int(float(secs[0][0]))
	start_tuple = time.localtime( start_secs )

	ldb = pg.connect('svr_'+className)
	update_db(ldb, key, name, email, className, start_secs)

	svrFrcst.svrTop(start_tuple, start_secs)

	print """
	This is a forecasting exercise for forecasting severe weather. You will be given hourly data for 6 hours and then asked to make some
decisions on where you believe severe weather will occur.  Then you will be guided  through the rest of the case and then given the results at the
end.  During this exercise, you may be asked  other case specific questions about the data that you are seeing.  Make sure to look at the maps, and
good luck!
	<BR><BR>"""

	svrFrcst.printIntro(case_num, className)

	print '<CENTER>'
	if case_num[0] == "s":
		cgiValues = 'className='+className+'&interval='+startInterval+'&case_num='+case_num+'&secs='+str(int(start_secs)+3600)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" border="0"></a>'
	else:
		cgiValues = 'className='+className+'&interval='+startInterval+'&case_num='+case_num+'&secs='+str(start_secs)+'&key='+str(key)
		print '<a href="hourly_pre.py?'+cgiValues+'"><img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" BORDER="0"></a>'

	print '</CENTER>'
	svrFrcst.svrBot()
	print '</body></HTML>'


Main()