#!/usr/local/bin/python

# A little program to fill a need
# Daryl Herzmann 7/30/98

import os, style
from pgext import *
from cgi import *

mydb = connect("archdays")

def Main():
	form = FormContent()
	ztime = form["ztime"][0]
	events = form["events"][0]
	updates = form["updates"][0]

	update = mydb.query("INSERT into jun181998 VALUES('"+ztime+"','"+events+"','"+updates+"')") 
	style.header("Worked","/images/ISU_bkgrnd.gif")
	style.std_top("Hello")

Main()
