#!/usr/local/bin/python
# This program enters db stuff
# Daryl Herzmann 8-16-99
# 11-5-99: Lets make this work.....


import pg, cgi, time, style
mydb = pg.connect('severe2', 'localhost', 5432)

def Main():
	form = cgi.FormContent()
	intval = form["intval"][0]
	question = form["question"][0]
	try:
		optiona = form["optiona"][0]
	except:
		optiona = ""

	try:
		optionb = form["optionb"][0]
	except:
		optionb = ""

	try:
		optionc = form["optionc"][0]
	except:
		optionc = ""

	try:
		optiond = form["optiond"][0]
	except:
		optiond = ""

	try:
		optione = form["optione"][0]
	except:
		optione = ""

	try:
		optionf = form["optionf"][0]
	except:
		optionf = ""

	try:
		optiong = form["optiong"][0]
	except:
		optiong = ""

	try:
		optionh = form["optionh"][0]
	except:
		optionh = ""



	insert = mydb.query("UPDATE intquestions set question = '"+question+"', optiona = '"+optiona+"', optionb = '"+optionb+"', optionc = '"+optionc+"', optiond = '"+optiond+"' , optione = '"+optione+"', optionf = '"+optionf+"', optiong = '"+optiong+"', optionh = '"+optionh+"' WHERE intval = '"+intval+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL=list.py">'
        print '</HEAD>' 

Main()
