#!/usr/local/bin/python
# This is the first program down the city forecasting exercise
# Daryl Herzmann 12 September 2000

import cgi, pg, time, cityFX
mydb = pg.connect('cityfx', 'localhost', 5432)

def initUser():
	newID = mydb.query("SELECT nextval('newuserid')").getresult()[0][0]
	
	return newID


def cityDialog(day, userKey):
	print '<form method="POST" action="intro.py" name="cityDialog">'
	print '<input type="hidden" value="'+userKey+'" name="userKey">'
	print '<input type="hidden" value="'+day+'" name="day">'
	print '<H3>Select a city:</H3>'

	cities = mydb.query("SELECT * from cities").dictresult()
	print '<SELECT name="city">'
	for i in range(len(cities)):
		print '<option value="'+cities[i]["citycode"]+'">'+cities[i]["cityname"]
	print '</SELECT>'

	print '<input type="SUBMIT">'
	print '</form>'

def dayDialog(userKey):
	print '<form method="POST" action="index.py" name="dayDialog">'
	print '<input type="HIDDEN" value="'+str(userKey)+'" name="userKey">'
	print '<H3>Select case date:</H3>'

	cities = mydb.query("SELECT caseid, starttime::date as start from cases WHERE released = 't'").dictresult()
	print '<SELECT name="day">'
	for i in range(len(cities)):
		print '<option value="',cities[i]["caseid"],'">'+cities[i]["start"]
	print '</SELECT>'

	print '<input type="SUBMIT">'
	print '</form>'


def Main():
	form = cgi.FormContent()

	cityFX.setupPage()

	print """<P><B>Welcome</b> to the Archived City Forecasting Activity. This activity presents weather
	data in an hourly format and you are asked to forecast the weather for a city of your choice.  In order 
	to start the exercise, you need to select a case date to work and a city to forecast for."""


	if form.has_key("day"):
		day = form["day"][0]
		userKey = form["userKey"][0]
		cityDialog(day, userKey)

	else:
		userKey = initUser()
		dayDialog(userKey)


	cityFX.finishPage()
Main()
