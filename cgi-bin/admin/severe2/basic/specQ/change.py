#!/usr/local/bin/python

# This program takes the input data and enters it into the database system
# Daryl Herzmann 7-16-99

import cgi, regsub, pg

mydb = pg.connect('severe2', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT' ")
table_str = "specquestions"


def enter_db(ticks, quest, type, optiona, optionb, optionc, optiond, optione, optionf, answer, cor_comments, wro_comments):
	mydb.query("UPDATE "+table_str+" set question = '"+quest+"' , type = '"+type+"', optiona = '"+optiona+"', optionb = '"+optionb+"' , optionc = '"+optionc+"' , optiond = '"+optiond+"' , optione = '"+optione+"',optionf = '"+optionf+"', answer = '"+answer+"' , correct = '"+cor_comments+"',  wrong = '"+wro_comments+"' WHERE validTime = '"+ticks+"' ")


def Main():
	form = cgi.FormContent()

	validTime = form["validTime"][0]
	caseNum = form["caseNum"][0]
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

	if form.has_key("optione"):
		optione = form["optione"][0]
	else:
		optione = "N"

	if form.has_key("optionf"):
		optionf = form["optionf"][0]
	else:
		optionf = "N"

	if form.has_key("answer"):
		answer = form["answer"][0]
	else:
		answer = "N"

	if form.has_key("cor_comments"):
		cor_comments = form["cor_comments"][0]
	else:
		cor_comments = "N"

	if form.has_key("wro_comments"):
		wro_comments = form["wro_comments"][0]
	else:
		wro_comments = "N"

	quest = regsub.gsub("'","&#180;", quest)
	optiona = regsub.gsub("'","&#180;", optiona)
	optionb = regsub.gsub("'","&#180;", optionb)
	optionc = regsub.gsub("'","&#180;", optionc)
	optiond = regsub.gsub("'","&#180;", optiond)
	optione = regsub.gsub("'","&#180;", optione)
	optionf = regsub.gsub("'","&#180;", optionf)
	cor_comments = regsub.gsub("'","&#180;", cor_comments)
	wro_comments = regsub.gsub("'","&#180;", wro_comments)

	print 'Content-type: text/html \n\n'

	enter_db(validTime, quest, type, optiona, optionb, optionc, optiond, optione, optionf, answer, cor_comments, wro_comments)

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=index.py?caseNum='+caseNum+'">'
        print '</HEAD>'


Main()
