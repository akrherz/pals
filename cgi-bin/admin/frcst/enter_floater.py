#!/usr/local/bin/python
# This program enters the floater city info
# Daryl Herzmann

import pg, cgi

casesdb = pg.connect('frcst')

def Main():
	form = cgi.FormContent()
	yeer = form["yeer"][0]
	month = form["month"][0]
	day = form["day"][0]
	code = form["code"][0]
	station = form["station"][0]
	class_name = form["class_name"][0]

	delete = casesdb.query("DELETE from cases WHERE yeer =  '"+yeer+"' AND month = '"+month+"' AND day = '"+day+"' AND class_name = '"+class_name+"' ")

	insert = casesdb.query("INSERT into cases VALUES ('"+yeer+"','"+month+"','"+day+"','"+station+"','"+code+"','"+class_name+"') ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="1; URL=floater.py?class_name='+class_name+'">'
        print '</HEAD>'
        print '<body>'
        print '<H2> Update successful </H2>'
        print '</HTML>'


Main()
