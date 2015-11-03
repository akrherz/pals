#!/usr/bin/python
# This is the introduction into the case
# 12 May 2000  Daryl Herzmann

import functs, cgi, time, style, pg, pals

mydb = pg.connect('severe2', 'localhost', 5432)

def initUser(caseNum):
	userKey = int( float( time.time() ) )
	enter = mydb.query("INSERT into users (userkey, casenum, gradetime) values ("+str(userKey)+", '"+caseNum+"','1972-01-01 1:00:00-05') ")
	return userKey 

	
def Main():
	form = cgi.FormContent()
	try:
		caseNum = pals.formValue(form, "caseNum")
		userKey = initUser(caseNum)
	except:
		style.SendError("Case number parse error")

	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser(userKey)

	functs.setupPage("Welcome to the Severe Weather Forecasting Exercise")
	functs.printTime(startTime)
	
	functs.caseIntro(caseNum)
	
	functs.updateUser(userKey, "lasttime", startTime)
	print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">Navigation:</font></H2>'
	print '<CENTER><a href="/cgi-bin/severe2/intermediate/hour.py?userKey='+str(userKey)+'""><img src="/gen/hour.php3?label=Start%20Exercise&font_size=20" BORDER="0"></a></CENTER>'
	print '<BR><BR><BR>'
		
	functs.finishPage()

Main()
