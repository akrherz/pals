#!/usr/local/bin/python
# This will be the forecasting pages for mt417, it will use the same features as the main page,
# But there will be more of them
# Daryl Herzmann 7-14-99
# UDPATED 7-16-99: We are going to be authentication the sessions, now :)
# UPDATED 7-21-99: Fine tunning the system

import time, style, cgi, pg, functs

admindb = pg.connect('archadmin')
sessiondb = pg.connect('sessions_417')

def ask_for_info(secs, key):
	print '<font color="blue"><H1>Enter your information:</H1></font>'
	print 'Your email address and name will be sent to Dr. Gallus, along with your answers to the \
		excercise. So please use your real name and email address if you want to recieve credit for the \
		excercise'

	print '<form method="POST" action="index_2.py">'
	print '<input type="hidden" name="key" value="'+key+'">'	# These two values are key to the 
	print '<input type="hidden" name="secs" value="'+str(secs)+'">' # forecasting excercise

	print '<H3>Enter your Name</H3>'
	print '<input size="40" MAXLENGTH="40" type="text" name="name"><BR>'
	
	print '<H3>Enter your Email Address:</H3>'
	print '<input size="40" MAXLENGTH="40" type="text" name="email"><BR><BR>'

	print '<input type="submit" value="Start Excercise">'
	print '</form>'

def mk_new_entry():
	key = str(time.time())		# we generate the key that the user will be using for the day
	input = admindb.query("INSERT into sessions_417 VALUES ("+key+") ")	# Create the entry in the db
	create = sessiondb.query("CREATE TABLE s"+key[:9]+" (ticks varchar(20), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
	return key

def Main():
	form = cgi.FormContent()
	try:
		day = int(form["day"][0])		# These are the only values that we need in order
		month = int(form["month"][0])		# To start the excercise
	 	year = int(form["year"][0])
	except:
		style.SendError("The Link into the system is corrupt")

	secs = functs.create_time(year, month, day, 6, 0)
	key = mk_new_entry()

	style.header("Frontend to the Forecasting Excercise", "white")

	ask_for_info(secs, key)

        style.std_bot()

Main()
