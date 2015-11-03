#!/usr/local/bin/python
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99

from functs import *

def Main():
	secs = int(float( form["secs"][0] ))
        state = form["state"][0]
	interval = form["interval"][0]
	ldb = pg.connect('svr_'+className)

	if case_num[0] == "s":
	        etime = form["etime"][0]
		T, H, R = "No", "No", "No"
	        if form.has_key("T"):   T = form["T"][0]
	        if form.has_key("H"):   H = form["H"][0]
	        if form.has_key("R"):   R = form["R"][0]
		update = ldb.query("UPDATE "+usersTable+" set state = '"+state+"', etime = '"+etime+"', optiona = '"+R+"', optionb = '"+H+"', optionc = '"+T+"' WHERE userid = '"+str(key)+"' ")

	if case_num[0] == "w":
		S, T, F, C = "No", "No", "No", "No"
	        if form.has_key("S"):   
			S = form["S"][0]
			if S != "S":
				T = "T"		
				S = "N"
	        if form.has_key("F"):   F = form["F"][0]
	        if form.has_key("C"):   C = form["C"][0]
		update = ldb.query("UPDATE "+usersTable+" set state = '"+state+"', optiona = '"+S+"', optionb = '"+T+"', optionc = '"+F+"', optiond = '"+C+"' WHERE userid = '"+str(key)+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly_post.py?className='+className+'&interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'">'
        print '</HEAD>'


Main()


