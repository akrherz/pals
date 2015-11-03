#!/usr/local/bin/python
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99

import cgi, pg

admindb = pg.connect("svr_frcst")
scriptBase = 'http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.417'

def Main():
	form = cgi.FormContent()
	case_num = form["case_num"][0]
	secs = int(float( form["secs"][0] ))
        key = form["key"][0]
        state = form["state"][0]
	interval = form["interval"][0]

	if case_num[0] == "s":
	        etime = form["etime"][0]
		T, H, R = "No", "No", "No"
	        if form.has_key("T"):   T = form["T"][0]
	        if form.has_key("H"):   H = form["H"][0]
	        if form.has_key("R"):   R = form["R"][0]
		update = admindb.query("UPDATE users_417 set state = '"+state+"', etime = '"+etime+"', optiona = '"+R+"', optionb = '"+H+"', optionc = '"+T+"' WHERE userid = '"+str(key)+"' ")

	if case_num[0] == "w":
		S, T, F, C = "No", "No", "No", "No"
	        if form.has_key("S"):   S = form["S"][0]
	        if form.has_key("T"):   T = form["T"][0]
	        if form.has_key("F"):   F = form["F"][0]
	        if form.has_key("C"):   C = form["C"][0]
		update = admindb.query("UPDATE users_417 set state = '"+state+"', optiona = '"+S+"', optionb = '"+T+"', optionc = '"+F+"', optiond = '"+C+"' WHERE userid = '"+str(key)+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly_post.py?interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'">'
        print '</HEAD>'


Main()


