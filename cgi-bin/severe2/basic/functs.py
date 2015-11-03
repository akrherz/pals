#!/usr/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import time, os, sys, time, regsub, pg, string, style, insText, mx.DateTime, cgi, pals, SEVERE2

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")
usersTable = "users"
casesTable = "cases"
annoteTable = "annotations"
scriptBase = "http://www.pals.iastate.edu/cgi-bin/severe2/basic/"

def getIntro(caseNum):
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

def updateUser(userKey, col, val):
        mydb.query("UPDATE users set "+col+" = '"+str(val)+"' WHERE userKey = "+str(userKey)+" ")

def retreiveUser(userKey = 'null'):
        if (userKey == 'null'):
                form = cgi.FormContent()
                userKey = pals.formValue(form, "userKey")
	try:
		lastTime, gradeTime, caseNum = mydb.query("SELECT lasttime, gradeTime, casenum from users WHERE userkey = '"+str(userKey)+"' ").getresult()[0]
		startTime, endTime = mydb.query("SELECT starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()[0]
	except:
		style.SendError("Your session info can not be found.<BR>You need to start <a href='list.py'>over</a>.")

	if caseNum[0] == 's':
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+5)
	else:
		noonTime = mx.DateTime.ISO.ParseDateTimeGMT(startTime) + mx.DateTime.RelativeDateTime(hours=+6)
	               
	return userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum

def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def svrTop( thisTime ):
	SEVERE2.setupPage()
	SEVERE2.printTime( thisTime )

	

def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'

def dbComments(nowDate, colName, secHead):
        print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">'+secHead+'</font></H2>'

 #      print "SELECT "+colName+" from "+annoteTable+" where validtime = "+nowDate
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

def svrBot():
       SEVERE2.finishPage("basic")



def mkHelp():
	SEVERE2.makeHelp()

