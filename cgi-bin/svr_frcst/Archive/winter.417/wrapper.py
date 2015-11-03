#!/usr/local/bin/python
# This program simply inputs data into the db system
# Daryl Herzmann 8-19-99

import cgi, pg

admindb = pg.connect("archadmin")


def Main():
        form = cgi.FormContent()
        secs = form["secs"][0]
        freeze, six, twelve = "N", "N", "N"
        if form.has_key("freeze"):   freeze = "Y"
        if form.has_key("six"):   six = "Y"
        if form.has_key("twelve"):   twelve = "Y"
        state = form["state"][0]
        key = form["key"][0]
	case_num = form["case_num"][0]
	refer = form["refer"][0]

        update = admindb.query("UPDATE win_sessions_417 set state = '"+state+"', freeze = '"+freeze+"',six = '"+six+"', twelve = '"+twelve+"' WHERE key = '"+str(key)+"' ")

        print 'Content-type: text/html \n\n'
        print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL='+refer+'?case_num='+str(case_num)+'&secs='+str(secs)+'&key='+key+'">'
        print '</HEAD>'


Main()

