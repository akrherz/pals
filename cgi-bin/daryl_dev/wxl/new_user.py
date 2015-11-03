#!/usr/local/bin/python
# This will set up users for the weather link system
# Daryl Herzmann 10/10/98

import os, sys
from cgi import *
from pg import *

userdb = connect('wx_areas')
linksdb = connect('wx_links')

def html():
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD></HEAD><BODY BGCOLOR="white" text="blue">'

def adduser(user, passwd):
	update = userdb.query("insert into users values ('"+user+"','"+passwd+"')")
	print '<H2>Adding Username....</H2>'
	newtable = userdb.query("create table "+user+" (area varchar(50), spec varchar(50))")
	print '<H2>Creating Tables....</H2>'
	change = userdb.query("grant all on "+user+" to nobody")
	print '<H2>Granting Access via Web....</H2>'
	newlink = linksdb.query("create table "+user+" ( area varchar(50), spec varchar(50), link varchar(200), title varchar(40))")
	print '<H2>Setting up Links Database....</H2>'

	print '<a href="/wxl/index.html" target="_top">Click Here to start</a>'
	print '</HTML>'

def Main():
	form = FormContent()
	user = form["user"][0]
	passwd = form["passwd"][0]
	html()
	adduser(user, passwd)

Main()
