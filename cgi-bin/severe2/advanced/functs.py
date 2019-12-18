#!/usr/bin/env python2
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import pals, cgi, style, pg, time, mx.DateTime, os, regsub

basedb = pg.connect('severe2', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)
tmpdb = pg.connect('severe2_tmp', 'localhost', 5432)
advdb.query("SET TIME ZONE 'GMT'")

scriptBase = "https://pals.agron.iastate.edu/cgi-bin/severe2/advanced/"
usersTable = "users"

def updateUser(userKey, col, val):
	advdb.query("UPDATE users set "+col+" = '"+str(val)+"' WHERE userKey = "+str(userKey)+" ")

def retreiveUser(userKey = 'null'):
	if (userKey == 'null'):
		form = cgi.FormContent()
		userKey = pals.formValue(form, "userKey")
	try:
		lastTime, gradeTime, caseNum, className = advdb.query("SELECT lasttime, gradeTime, casenum, className from users WHERE userkey = '"+str(userKey)+"' ").getresult()[0]
		startTime, endTime = basedb.query("SELECT starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()[0]
	except:
		style.SendError("Can not locate your user info, sorry.")
	
	if caseNum[0] == 's':
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+5)
	else:
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+6)
                
	return userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum, className


def getQuestions(ldb, key, secs, className, interval):
	storAge = "s"+str(key)
	checker = ldb.query("SELECT * from "+storAge+" ").getresult()

	update = ldb.query("SELECT last_time, ans_ques from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
#        print update, secs, interval
	if ( int(float( update[0][0] )) < secs or (int(interval) == 1 and len(checker) == 0) )and update[0][1] == 't':
		return 1                                # WE have not been here
	else:
		return 0

def dbComments(lastTime, colName, secHead, className):
	select  = basedb.query("SELECT "+colName+" from annotations WHERE validTime = '"+lastTime+"' ").dictresult()
	select1 = advdb.query("SELECT "+colName+" from annotations WHERE validTime = '"+lastTime+"' ").dictresult()
	select2 = advdb.query("SELECT "+colName+" from annotations_custom WHERE validTime = '"+lastTime+"' and classname = '"+className+"' ").dictresult()

	if len( select2 ) > 0:
		select = select2
	elif len( select1 ) > 0:
		select = select1

	print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">'+secHead+'</font></H2>'
		
	if len( select ) == 0:
		print "None available for this hour..."
	else:
		print '<font size="6">'+select[0][colName][0]+'</font>'+select[0][colName][1:]      # Get the neat capital letter to start


def mk_help():
	SEVERE2.makeHelp()
	
	
def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def create_time(year, month, day, hour, minute):
	time_tuple = (year, month, day, hour, minute, 0, 0, 0, 0)       # Form the orig tuple
	return time.mktime(time_tuple)          # This is time_tuple in ticks


def mk_top(now_tuple):
	date_str = time.strftime("%B %d, %Y", now_tuple)
	time_str = time.strftime("%I:%M %p [%Z]", now_tuple)

	print '<font color="RED">Current Date & Time:</font>&nbsp;&nbsp;'
	print date_str+'&nbsp;&nbsp;'+time_str
	
	
def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'

