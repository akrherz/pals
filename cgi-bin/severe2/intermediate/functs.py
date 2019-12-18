#!/usr/bin/python2
# This will be the new functions file for the exercise
# Daryl Herzmann 9 May 2000

import pals, time, os, pg, cgi, style, mx.DateTime, SEVERE2

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")
annoteTable = "annotations"
global foundFile

def setupPage(title="Severe Wx Forecasting Exercise"):
	SEVERE2.setupPage(title)
	
def printTime(thisDate = 0):
	SEVERE2.printTime(thisDate)

def finishPage():
	SEVERE2.finishPage("intermediate")

def caseIntro(caseNum):
	print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">Case Introduction:</font></H2>'

	try:
		select = mydb.query("SELECT comments from intro where casenum = '"+caseNum+"' ").getresult() 
	except ValueError:
		print "No introduction has been written..."
		select = [(" "),(" ")]

	if len(select) == 0:
		print "No introduction has been written..."
	else:
		print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
		print '<BR><BR>'

def dbComments(nowDate, colName, secHead):
        print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">'+secHead+'</font></H2>'

        try:
                select = mydb.query("SELECT "+colName+" from "+annoteTable+" where validtime = '"+nowDate+"' ").getresult() 
        except ValueError:
                print "None available for this hour..."
                select = [(" "),(" ")]

        if len(select) == 0:
                print "None available for this hour..."
        else:
                print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '<BR><BR>'

def makeHelp():
	SEVERE2.makeHelp()
	
def retreiveUser(userKey = 'null'):
	if (userKey == 'null'):
		form = cgi.FormContent()
		userKey = pals.formValue(form, "userKey")
	try:
		lastTime, gradeTime, caseNum = mydb.query("SELECT lasttime, gradeTime, casenum from users WHERE userkey = '"+str(userKey)+"' ").getresult()[0]
		startTime, endTime = mydb.query("SELECT starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()[0]
	except:
		style.SendError("Can not locate your user info, sorry.")

	if caseNum[0] == 's':
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+5)
	else:
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+6)
		
	return userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum
	
def updateUser(userKey, col, val):
	mydb.query("UPDATE users set "+col+" = '"+str(val)+"' WHERE userKey = "+str(userKey)+" ")
