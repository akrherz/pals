#!/usr/local/bin/python
# This program enters the username info into the db
# Daryl Herzmann 8-31-99
# 9-1-99: Cleaned up the code dramatically

import cgi, pg, style, re
mydb = pg.connect('frcst')

def Main():
	form = cgi.FormContent()
	try:
		email = form["email"][0]
		full_name = form["full_name"][0]
		passwd1 = form["passwd1"][0]
		passwd2 = form["passwd2"][0]
		class_name = form["class_name"][0]
	except:
		style.SendError("CGI Parse Error")

	if passwd1 != passwd2:
		style.SendError("Your passwd is not valid, Try again.")

	email = re.split("@", email)
	userid = class_name+"_"+email[0]

	users = mydb.query("SELECT * from users WHERE userid = '"+userid+"' ").getresult()

	if len(users) > 0:
		style.SendError("Your username is allready taken")

	entre = mydb.query("INSERT into users values ('"+userid+"', '"+full_name+"', '"+passwd1+"' ) ")

	style.header("Username Results.", "white")

	print full_name +'<BR><BR>'
	print 'You have been assigned this userid : '+userid+' <BR><BR>'
	print 'You have been assigned this password : '+passwd1+' <BR><BR>'

	print '<P>You now have an account with the forecasting system, you are free to make forecasts.  Just remember your password :) '

	print '<BR><a href="/frcst/"> Go back to the Forecasting main page</a><BR>'

Main()
