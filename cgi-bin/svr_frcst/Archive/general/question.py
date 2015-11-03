#!/usr/local/bin/python
# This program answers the question, if applicable and sends them back down that road
# Daryl Herzmann 7-16-99

import cgi, time, sys, string, style, functs
from pgext import *

admindb = connect("archadmin")

def grade_multi(secs, option, anskey, key):
	answer = admindb.query("SELECT answer from questions WHERE ticks = '"+str(secs)+"' ").getresult()
	answer = answer[0][0]

	test = admindb.query("SELECT "+anskey+" from sessions WHERE key = '"+str(key)+"' ").getresult()

	if len(test[0][0]) > 0:
		print 'You allready did this question!'
	else:
		if option == answer:
			res = "Correct"	
		else:
			res = "Wrong"
		update = admindb.query("UPDATE sessions set "+anskey+" = '"+res+"' WHERE key = '"+str(key)+"' ")
		
def enter_text(secs, option, anskey, key):
	test = admindb.query("SELECT "+anskey+" from sessions WHERE key = '"+str(key)+"' ").getresult()
#	print anskey, len(test), test
	if len(test[0][0]) > 0:
                print 'You allready did this question, Cheater!!'
        else:
		update = admindb.query("UPDATE sessions set "+anskey+" = '"+option+"' WHERE key = '"+str(key)+"' ")


def Main():
	print 'Content-type: text/html \n\n'
	form = cgi.FormContent()
	try:
		key = form["key"][0]
		secs = form["secs"][0]
		refer = form["refer"][0]
	except:
		style.SendError("CGI Value parse error")

	local = time.localtime(float(secs))
	anskey = "ans"+str(int(time.strftime("%I", local)))+string.lower(time.strftime("%p", local))
	
	if form.has_key("option"):
		option = form["option"][0]
		grade_multi(secs, option, anskey, key)
	else:
		text = form["text"][0]
		text = functs.clean_str(text)
		enter_text(secs, text, anskey, key)

	print '<HTML><HEAD>'
	secs = int(float(secs)) - 3600 
	print '<meta http-equiv="Refresh" content="0; URL='+refer+'?secs='+str(secs)+'&key='+str(key)+'">'
	print '</HEAD>'



Main()
