#!/usr/local/bin/python
# intro.py, its job is to introduce the case and get it going
# Daryl Herzmann 15 September 2000

import cityFX, cgi, style, pg
mydb = pg.connect('cityfx', 'localhost', 5432)

def Main():
	cityFX.setupPage()
	form = cgi.FormContent()
	try:
		userKey = form["userKey"][0]
		cityID = form["city"][0]
		day = form["day"][0]
		mydb.query("DELETE from users WHERE userID = "+userKey+" ")
		mydb.query("INSERT into users VALUES("+userKey+", "+day+", '"+cityID+"')")
	except:
		style.SendError("oops")
	
	
	print """<P>You are now ready to begin the Archived Forecasting Activity.  You will be presented with hourly
	data and asked to make some forecasts valid for your city. Good luck.
	"""
	
	print '<P>Lets go: <a href="hour.py">Start Exercise</a>'
	
	cityFX.finishPage()
Main()
