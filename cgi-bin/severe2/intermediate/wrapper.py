#!/usr/bin/python
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99

import cgi, pg, functs

admindb = pg.connect("severe2", 'localhost', 5432)

def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()

	state = form["state"][0]

	if caseNum[0] == "s":
		etime = form["etime"][0]
		T, H, R = "N", "N", "N"
		if form.has_key("T"):   T = form["T"][0]
		if form.has_key("H"):   H = form["H"][0]
		if form.has_key("R"):   R = form["R"][0]
		update = admindb.query("UPDATE users set state = '"+state+"', etime = '"+etime+"', optiona = '"+R+"', optionb = '"+H+"', optionc = '"+T+"' WHERE userKey = '"+str(userKey)+"' ")


	if caseNum[0] == "w":
		S, F, C = "N", "N", "N"
		if form.has_key("S"):   S = form["S"][0]
		if form.has_key("F"):   F = form["F"][0]
		if form.has_key("C"):   C = form["C"][0]
		update = admindb.query("UPDATE users set state = '"+state+"', optiona = '"+S+"', optionb = '"+F+"', optionc = '"+C+"' WHERE userKey = '"+str(userKey)+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL=/cgi-bin/severe2/intermediate/hour.py?userKey='+str(userKey)+'&noon=yes">'
	print '</HEAD>'

	print '<body></body></HTML>'


Main()


