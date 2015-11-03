#!/usr/local/bin/python

# This program takes the input data and enters it into the database system
# Daryl Herzmann 7-16-99

import cgi, regsub, pg

mydb = pg.connect('svr_frcst')
table_str = "spec_questions"


def enter_db(ticks, quest, type, optiona, optionb, optionc, optiond, answer, comments):
	verify = mydb.query("UPDATE "+table_str+" set question = '"+quest+"' , type = '"+type+"', optiona = '"+optiona+"', optionb = '"+optionb+"' , optionc = '"+optionc+"' , optiond = '"+optiond+"' , answer = '"+answer+"' , comments = '"+comments+"' WHERE ticks = '"+ticks+"' ")


def Main():
	form = cgi.FormContent()

	ticks = form["ticks"][0]
	
	quest = form["quest"][0]

	type = form["type"][0]

	if form.has_key("optiona"):
		optiona = form["optiona"][0]
	else:
		optiona = "N"

	if form.has_key("optionb"):
		optionb = form["optionb"][0]
	else:
		optionb = "N"
	if form.has_key("optionc"):
		optionc = form["optionc"][0]
	else:
		optionc = "N"
	if form.has_key("optiond"):
		optiond = form["optiond"][0]
	else:
		optiond = "N"
	if form.has_key("answer"):
		answer = form["answer"][0]
	else:
		answer = "N"
	if form.has_key("comments"):
		comments = form["comments"][0]
	else:
		comments = "N"

	quest = regsub.gsub("'","&#180;", quest)
	optiona = regsub.gsub("'","&#180;", optiona)
	optionb = regsub.gsub("'","&#180;", optionb)
	optionc = regsub.gsub("'","&#180;", optionc)
	optiond = regsub.gsub("'","&#180;", optiond)
	comments = regsub.gsub("'","&#180;", comments)

	print 'Content-type: text/html \n\n'

	ticks = str(ticks)
	enter_db(ticks, quest, type, optiona, optionb, optionc, optiond, answer, comments)

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=index.py?ticks='+ticks+'">'
        print '</HEAD>'


Main()
