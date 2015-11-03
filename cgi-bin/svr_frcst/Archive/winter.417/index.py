#!/usr/local/bin/python
# This program will be the index for the 417 winter excercise
# Daryl Herzmann 8-18-99

import os, cgi, pg, style, time

admindb = pg.connect('archadmin')
sessiondb = pg.connect('sessions_417')

def find_start(case_num):
	query = admindb.query("SELECT start_secs from winter_cases WHERE case_num = '"+case_num+"' ").getresult()
	return query[0][0]

def genkey():
	key = str(time.time())
	key = key[:9]
	input = admindb.query("INSERT into win_sessions_417 VALUES ("+key+") ")     # Create the entry in the db
        create = sessiondb.query("CREATE TABLE s"+key+" (ticks varchar(20), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
        return key


def make_form(start_secs, case_num, key):
	print '<font color="blue"><h3>Enter your Info for the excercise</h3></font>'
	print 'Your email address and name will be sent to Dr. Gallus, along with your answers to the \
                excercise. So please use your real name and email address if you want to recieve credit for the \
                excercise'

	print '<form method="POST" action="start.py">'
	print '<input type="hidden" name="key" value="'+key+'">'                # These two values are key to the 
        print '<input type="hidden" name="case_num" value="'+case_num+'">'      # This is the case number that we are doing
        print '<input type="hidden" name="start_secs" value="'+start_secs+'">'  # This is the case number that we are doing

        print '<H3>Enter your Name</H3>'
        print '<input size="40" MAXLENGTH="40" type="text" name="name"><BR>'

        print '<H3>Enter your Email Address:</H3>'
        print '<input size="40" MAXLENGTH="40" type="text" name="email"><BR><BR>'

        print '<input type="submit" value="Start Excercise">'
	print '</form>'


def Main():
	form = cgi.FormContent()
	try:
		case_num = form["case_num"][0]
	except:
		style.SendError("CGI import error")

	start_secs = find_start(case_num)
	key = genkey()

	style.header("Winter Weather Forecasting Excercise", "white")

	make_form(start_secs, case_num, key)

	style.std_bot()

Main()
