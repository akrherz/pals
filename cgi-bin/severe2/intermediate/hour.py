#!/usr/bin/python
# This is the script that controls the morning hourly features
# Daryl Herzmann 9 May 2000

import functs, time, pals, mx.DateTime, question, sys, noon, cgi, results, SEVERE2

def navigation(userKey):
	print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d">Navigation:</font></H2>'
	print '<CENTER>'
	print '<a href="/cgi-bin/severe2/intermediate/hour.py?userKey='+str(userKey)+'"><img src="/gen/hour.php?label=Click%20To%20Continue&font_size=25" BORDER="0"></a>.'
	print '</CENTER>'


def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()

	if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) >= mx.DateTime.ISO.ParseDateTimeGMT(endTime)):
		results.Main()

	functs.setupPage()
	functs.printTime(lastTime)
	functs.makeHelp()
	
	# Check first if we have a question to display
	if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) > mx.DateTime.ISO.ParseDateTimeGMT(gradeTime)):
		question.Main(lastTime, userKey, caseNum, startTime)
	if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) == noonTime and not form.has_key("noon")):
		noon.Main(userKey, caseNum)
		
	
	print """<font color="#a0522d">
	<BLOCKQUOTE><P><FONT FACE="Britannic Bold">Check it out!</FONT> Click under the column titled 
	<FONT COLOR="#b0020f">Current,</FONT> and find out what is happening around the country at this hour. 
	<FONT COLOR="#b0020f" SIZE="+1">Hint</FONT>: If you need help understanding the charts, please review our help topics.</P></BLOCKQUOTE>	
	</font>	
	"""

	functs.dbComments(lastTime, "comments", "Hourly Notes:")
	
	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3)
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1)
		
	
	if (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) > noonTime):
		functs.dbComments(lastTime, "analysis", "Analysis:")
	
	if caseNum[0] == 's' and (mx.DateTime.ISO.ParseDateTimeGMT(lastTime) > noonTime) :
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+2)	
	elif caseNum[0] == 's':
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+1)	
	else:
		nextTime = mx.DateTime.ISO.ParseDateTimeGMT(lastTime) + mx.DateTime.RelativeDateTime(hours=+3)
		
	functs.updateUser(userKey, "lasttime", nextTime)

	navigation(userKey)
	
	functs.finishPage()


Main()
