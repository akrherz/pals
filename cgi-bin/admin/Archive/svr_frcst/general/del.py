#!/usr/local/bin/python
# This delete an entry outta the db system
# Daryl Herzmann 10-20-99

import pg, cgi, style

mydb = pg.connect('svr_frcst')


def Main():
	form = cgi.FormContent()
	ticks = str(form["ticks"][0])

	delete = mydb.query("DELETE from spec_questions WHERE ticks = '"+ticks+"' ")

	style.jump_page("index.py")

Main()
