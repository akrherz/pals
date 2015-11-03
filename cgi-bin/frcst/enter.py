#!/usr/local/bin/python
# This inputs data into the db
# Daryl Herzmann 8-30-99

import cgi, os, pg, style, time

mydb = pg.connect('frcst')

def upday(yeer, month, day):
        time_tuple = (int(yeer), int(month), int(day), 6,0,0,0,0,0)
        now = time.mktime(time_tuple) + 86400
        now_tuple = time.localtime(now)
        yeer = str(now_tuple[0])
        month = str(now_tuple[1])
        day = str(now_tuple[2])

        return yeer, month, day

def validate_passwd(userid, passwd):
	entry = mydb.query("SELECT passwd from users WHERE userid = '"+userid+"' ").getresult()
	try:
		passwd_db = entry[0][0]
		if passwd == passwd_db:
			print
		else:
			style.SendError("Invalid userid and password combo")
	except:
		style.SendError("Invalid userid and password combo")

def Main():
#	cgi.test()
	if os.environ.has_key('HTTP_REFERER'): 
                tester = os.environ['HTTP_REFERER']
	        if tester[-23:-12] == "forecast.py":
			print 'Content-type: text/html \n\n'
		else:
			style.SendError("Nice try, but that is not going to cut it...")
        else:
                style.SendError("You are not authenticated to the system")

	form = cgi.FormContent()
	try:
		userid = str(form["userid"][0])
		passwd = form["passwd"][0]
		class_name = str(form["class_name"][0])
#		yeer = str(form["yeer"][0])
#		month = str(form["month"][0])
#		day = str(form["day"][0])
		DMX_high = str(form["DMX_high"][0])
		DMX_low = str(form["DMX_low"][0])
		DMX_prec = str(form["DMX_prec"][0])
		DMX_snow = str(form["DMX_snow"][0])
		FLOATER_high = str(form["FLOATER_high"][0])
		FLOATER_low = str(form["FLOATER_low"][0])
		FLOATER_prec = str(form["FLOATER_prec"][0])
		FLOATER_snow = str(form["FLOATER_snow"][0])

		code = form["code"][0]
	except:
		style.SendError("CGI Parse Error, please go back.")

	if int(DMX_high) < int(DMX_low):
		style.SendError("Bzzzz, your high for Des Moines is too low")

	if int(FLOATER_high) < int(FLOATER_low):
		style.SendError("Bzzzz, your high for Floater is too low")


	if code != "try and hack this&":
		style.SendError("Ohhh, tring method get on me, eh??")

	now = time.time()
	now_tuple = time.localtime(now)
        yeer = str(now_tuple[0])
        month = str(now_tuple[1])
        day = str(now_tuple[2])

	validate_passwd(userid, passwd)
	year, month, day = upday(yeer, month, day)

	delete = mydb.query("DELETE from forecasts WHERE userid = '"+userid+"' and yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' ")

	insert = mydb.query("INSERT into forecasts VALUES ('"+userid+"','"+yeer+"','"+month+"','"+day+"','"+DMX_high+"','"+DMX_low+"','"+DMX_prec+"','"+DMX_snow+"','"+FLOATER_high+"','"+FLOATER_low+"','"+FLOATER_prec+"','"+FLOATER_snow+"')")

	# Print out something for everybody's own record...

	print "Copy of "+userid+" 's forecast<BR><BR>"

	print 'Des Moines Forecast<BR>'
	print DMX_high+' / '+DMX_low

	print '<BR><BR>'

	print 'Precip Cat: '+DMX_prec
	print 'Snowfall Cat: '+DMX_snow

	print '<BR><BR>'

	print 'Floater City Forecast<BR>'
	print FLOATER_high+' / '+FLOATER_low

	print '<BR><BR>'

	print 'Precip Cat: '+FLOATER_prec
	print 'Snowfall Cat: '+FLOATER_snow
	
	print '<BR><BR>'

	print '<a href="/frcst/">Return to forecasting front page</a>'

Main()
