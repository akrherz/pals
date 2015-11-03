#!/usr/local/bin/python
# This program simply displays a record from the database
# Daryl Herzmann 20 June 2000

import cgi, pg, regsub
mydb = pg.connect( 'nwstxt', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT' ")

def Main():
	print 'Content-type: text/html \n\n'
	form = cgi.FormContent()
	bNumber = form["bNumber"][0]
	bTime = regsub.gsub( " ", "+", form["bTime"][0])
	bTime = regsub.gsub( "_", " ", bTime)
	
	tableName = "t"+bTime[:4]+"_"+bTime[5:7]
	
	results = mydb.query("SELECT everything from "+tableName+" WHERE bTime = '"+bTime+"' and bNumber = '"+bNumber+"' ").dictresult()
	print '<PRE>'
	print regsub.gsub("\015\012", "", results[0]["everything"] )
	print '</PRE>'

Main()
