#!/usr/bin/env python2
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99
# 29 Jan 2003	Fix a bug with SQL script

import cgi, pg, functs
from functs import *

admindb = pg.connect("svr_frcst")


def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	secs = int(float( form["secs"][0] ))
        key = form["key"][0]
        state = form["state"][0]

	if caseNum[0] == "s":
	        etime = form["etime"][0]
		T, H, R = "N", "N", "N"
	        if form.has_key("T"):   T = form["T"][0]
	        if form.has_key("H"):   H = form["H"][0]
	        if form.has_key("R"):   R = form["R"][0]
		sqlStr = "UPDATE "+usersTable+" set state = '"+state+"', etime = '"+etime+"', optiona = '"+R+"', optionb = '"+H+"', optionc = '"+T+"' WHERE userid = '"+str(key)+"' "
		try:
			update = admindb.query(sqlStr)
		except:
			print sqlStr
		multi = 1

	if caseNum[0] == "w":
		S, T, F = "N", "N", "N"
	        if form.has_key("S"):   S = form["S"][0]
	        if form.has_key("T"):   T = form["T"][0]
	        if form.has_key("F"):   F = form["F"][0]
		update = admindb.query("UPDATE "+usersTable+" set state = '"+state+"', optiona = '"+S+"', optionb = '"+T+"', optionc = '"+F+"' WHERE userid = '"+str(key)+"' ")
		multi = 3


	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly_post.py?secs='+str(secs + multi*3600)+'&key='+key+'&caseNum='+caseNum+'">'
        print '</HEAD>'


Main()


