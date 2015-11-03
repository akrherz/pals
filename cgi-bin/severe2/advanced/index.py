#!/usr/bin/env python
# This is the index file for the exercise. Gives the user an introduction to what will happen
# Daryl Herzmann 

import SEVERE2, cgi, pg, svrFrcst, style
startInterval = "1"
basedb = pg.connect('severe2', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)
tmpdb = pg.connect('severe2_tmp', 'localhost', 5432)


def update_db(userKey, name, email, className, startTime, answerQs, caseNum):
	update = advdb.query("UPDATE users SET casenum = '"+caseNum+"', className = '"+className+"', lasttime = '"+startTime+"', gradeTime = '1900/05/01', ans_ques = '"+answerQs+"', name = '"+name+"', email = '"+email+"', bonuspoints = 0  WHERE userKey = "+userKey+" ")

def Main():
	form = cgi.FormContent()
	if not form.has_key("email"): style.SendError("Please go back and enter your email address")
	email = form["email"][0]

	if not form.has_key("name"): style.SendError("Please go back and enter your name")
	name = form["name"][0]

	answerQs = form["answerQs"][0]
	userKey = form["userKey"][0]
	caseNum = form["caseNum"][0]
	className = form["className"][0]

	query = basedb.query("SELECT startTime from cases WHERE casenum = '"+caseNum+"' ").dictresult()
	startTime = query[0]["starttime"]

	update_db(userKey, name, email, className, startTime, answerQs, caseNum)

	SEVERE2.setupPage("Sx Wx Forecasting Exercise | Advanced Version")
	SEVERE2.printTime( startTime )

#	svrFrcst.svrTop(start_tuple, start_secs)


	print """
	This is a forecasting exercise for forecasting severe weather. You will be given hourly data for 6 hours and then asked to make some
decisions on where you believe severe weather will occur.  Then you will be guided  through the rest of the case and then given the results at the
end.  During this exercise, you may be asked  other case specific questions about the data that you are seeing.  Make sure to look at the maps, and
good luck!
	<BR><BR>"""

	svrFrcst.printIntro(caseNum, className)

	print '<CENTER>'
	cgiValues = 'userKey='+str(userKey)
	print '<a href="/cgi-bin/severe2/advanced/hour.py?'+cgiValues+'"><img src="/gen/hour.php3?label=Click%20To%20Start&font_size=25" border="0"></a>'
	print '</CENTER>'
	SEVERE2.finishPage("advanced")

Main()
