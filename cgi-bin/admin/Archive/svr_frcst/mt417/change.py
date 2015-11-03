#!/usr/local/bin/python
# This program takes the input data and enters it into the database system
# Daryl Herzmann 7-16-99
# UPDATE 7-26-99: We are now back to having 1 question per hour

import cgi, regsub
from pgext import *

mydb = connect('archadmin')


def enter_db(ticks, quest, type, optiona, optionb, optionc, optiond,  optione, optionf, optiong, optionh, answer, cor_comments, wro_comments, link):
	verify = mydb.query("UPDATE questions_417 set question = '"+quest+"' , type = '"+type+"', optiona = '"+optiona+"', optione = '"+optione+"', optionf = '"+optionf+"', optiong = '"+optiong+"', optionh = '"+optionh+"', optionb = '"+optionb+"' , optionc = '"+optionc+"' , optiond = '"+optiond+"' , answer = '"+answer+"' , cor_comments = '"+cor_comments+"' , wro_comments = '"+wro_comments+"' , link = '"+link+"' WHERE ticks = '"+ticks+"' ")


def Main():
	form = cgi.FormContent()
	ticks = form["ticks"][0]
	quest = form["quest"][0]
	type = form["type"][0]
	link = form["link"][0]

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

	if form.has_key("optiong"):
		optiong = form["optiong"][0]
	else:
		optiong = "N"

	if form.has_key("optionh"):
		optionh = form["optionh"][0]
	else:
		optionh = "N"

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
	optiong = regsub.gsub("'","&#180;", optiong)
	optionh = regsub.gsub("'","&#180;", optionh)
	cor_comments = regsub.gsub("'","&#180;", cor_comments)
	wro_comments = regsub.gsub("'","&#180;", wro_comments)

	print 'Content-type: text/html \n\n'

	ticks = str(ticks)
	enter_db(ticks, quest, type, optiona, optionb, optionc, optiond,  optione, optionf, optiong, optionh, answer, cor_comments, wro_comments, link)

	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL=index.py">'
        print '</HEAD></HTML>'


Main()
