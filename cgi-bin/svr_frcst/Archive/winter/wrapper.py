#!/usr/local/bin/python
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99

import cgi
from pgext import *

admindb = connect("archadmin")


def Main():
	form = cgi.FormContent()
	secs = form["secs"][0]
	T, H, R = "No", "No", "No"
        if form.has_key("T"):   T = form["T"][0]
        if form.has_key("H"):   H = form["H"][0]
        if form.has_key("R"):   R = form["R"][0]
        state = form["state"][0]
        etime = form["etime"][0]
        key = form["key"][0]

	update = admindb.query("UPDATE sessions_417 set state = '"+state+"', etime = '"+etime+"', r = '"+R+"',h = '"+H+"', t = '"+T+"' WHERE key = '"+str(key)+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=hourly_pm.py?secs='+str(secs)+'&key='+key+'">'
        print '</HEAD>'


Main()


