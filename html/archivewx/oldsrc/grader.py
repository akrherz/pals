#!/usr/local/bin/python
# The Script that will do all grading 
# Daryl Herzmann 7/28/98

from cgi import *
import style, pgext

mydbase = pgext.connect("archwx")

def checker(severe, state, tornado, rain, hail):
	if severe == tornado:
		print "<H3>You correctly predicted a tornado in "+state+".</H3>"
#	elif tornado == "T":
#		print "<H3>You incorrectly predicted a tornado in "+state+".</H3>"

	elif severe == rain:
		print "<H3>You correctly predicted heavy rain in "+state+".</H3>"
	elif severe == hail:
		print "<H3>You correctly predicted hail in "+state+".</H3>"
	


def get_score():
	form = FormContent()
	state = form["state"][0]
	time = form["time"][0]
	tornado = "no"
	rain = "no"
	hail = "no"
	if form.has_key("T"): tornado = form["T"][0]
	if form.has_key("R"): rain = form["R"][0]
	if form.has_key("H"): hail = form["H"][0]

	results = mydbase.query("Select * from jun1898 where state = '"+state+"' AND date = '"+time+"'")
	results = results.getresult()
	
	if len(results) == 0:
		print '<center><H3>Your prediction was not correct</H3></center>'	
		body()
		sys.exit(0)

	for i in range(len(results)):
		severe = results[i][1]
		checker(severe, state, tornado, rain, hail)

def body():
#	print '<a href="javascript:history.go(-1)">go back and try again</A><BR>'
#	print '<a href="answers.py">View the Answers</a><BR>'
	print '<a href="/archivewx/jun181998/data1pm.html">Go to 1 PM</a>'
	bot()

def bot():
	style.std_bot()

def Main():
	form = FormContent()
	state = form["state"][0]	
	time = form["time"][0]	
	if state == "(Select a State)": style.SendError("Please enter a state")
	if time == "(Select a time)": style.SendError("Please choose a time")	
	style.header("Your Score","/images/ISU_bkgrnd.gif")
	style.std_top("June 18, 1998 Forecast Results")
	get_score()
	body()	
	sys.exit(0)
Main()
