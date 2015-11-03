#!/usr/local/bin/python
# This is the first page in the winter forecasting excercise
# Daryl Herzmann 8-12-99

import time, style, cgi, pg, functs

admindb = pg.connect('archadmin')
sessiondb = pg.connect('sessions_417')

def ask_for_info(start_secs, case_num, key):
	print '<font color="blue"><H1>Enter your information:</H1></font>'
	print 'Your email address and name will be sent to Dr. Gallus, along with your answers to the \
		excercise. So please use your real name and email address if you want to recieve credit for the \
		excercise'

	print '<form method="POST" action="index_2.py">'
	print '<input type="hidden" name="key" value="'+key+'">'		# These two values are key to the 
	print '<input type="hidden" name="case_num" value="'+case_num+'">'	# This is the case number that we are doing
	print '<input type="hidden" name="start_secs" value="'+start_secs+'">'	# This is the case number that we are doing

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

def find_secs(case_num):
	query = admindb.query("SELECT start_secs from winter_cases WHERE case_num = '"+case_num+"' ").getresult()
	
	return query[0][0]

def Main():
	form = cgi.FormContent()
	try:
		case_num = form["case_num"][0]		# These are the only values that we need in order
	except:
		style.SendError("The Link into the system is corrupt")

	start_secs = find_secs(case_num)

	key = mk_new_entry()

	style.header("Frontend to the Forecasting Excercise", "white")

	ask_for_info(start_secs, case_num, key)

        style.std_bot()

Main()
