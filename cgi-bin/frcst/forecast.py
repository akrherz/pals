#!/usr/local/bin/python
# Simple script to generate a forecast for students that need to enter one yet
# Whoo-hooo, this is going to work
# Daryl Herzmann 8-30-99

import pg, time, style, os, cgi, mk_forecast

START_HOUR = 0
END_HOUR = 19
mt311_day = 2
mt411_day1 = 1
mt411_day2 = 4

casesdb = pg.connect('frcst')

def valid_day(class_name):
#	now = time.time()
#	now_tuple = time.localtime(now)

	now = time.time() + 86400
	now_tuple = time.localtime(now)
	yeer = str(now_tuple[0])
	month = str(now_tuple[1])
	day = str(now_tuple[2])

	tester = casesdb.query("SELECT * from cases WHERE class_name = '"+class_name+"' and yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' ").getresult()

	if len(tester) > 0:
		return 1
	return 0

#	dow = int(time.strftime("%w", now_tuple))
#	if class_name == "mt311":
#		if dow == mt311_day :
#			return 1
#	elif class_name == "mt411":
#		if dow == mt411_day1 or dow == mt411_day2:
#			return 1 
#	else:
#		return 0

def valid_time():
	now = time.time()
        now_tuple = time.localtime(now)
        tod = int(time.strftime("%H", now_tuple))

	if tod >= START_HOUR and tod < END_HOUR:
		return 1
	else:
		return 0

def Main():
	form = cgi.FormContent()
	class_name = form['class'][0]

	if valid_day(class_name):
		noth = "Hello"
	else:
		style.SendError("This is not a "+class_name+" forecasting day...")

	if valid_time():
		style.header("Forecasting excercise", "white")
		mk_forecast.Main(class_name)
	else:
		style.SendError("You can not forecast at this time, sorry..")


	style.std_bot()

Main()

