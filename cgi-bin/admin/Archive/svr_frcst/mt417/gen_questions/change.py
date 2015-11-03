#!/usr/local/bin/python
# This program enters db stuff
# Daryl Herzmann 8-16-99
# 11-5-99: Lets make this work.....


import pg, cgi, time, style
mydb = pg.connect('svr_frcst')


def Main():
	form = cgi.FormContent()
	case_type = form["case_type"][0]
	question_num = form["question_num"][0]
	question = form["question"][0]
	optiona = form["optiona"][0]
	optionb = form["optionb"][0]
	optionc = form["optionc"][0]
	optiond = form["optiond"][0]
	optione = form["optione"][0]
	optionf = form["optionf"][0]
	optiong = form["optiong"][0]
	optionh = form["optionh"][0]


#	insert = mydb.query("DELETE from gen_417 WHERE q_id = '"+question_num+"'  ")
	insert = mydb.query("UPDATE gen_417 set question = '"+question+"', optiona = '"+optiona+"', optionb = '"+optionb+"', optionc = '"+optionc+"', optiond = '"+optiond+"' , optione = '"+optione+"', optionf = '"+optionf+"', optiong = '"+optiong+"', optionh = '"+optionh+"' WHERE q_id = '"+question_num+"' ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL=list.py?case_type='+case_type+'">'
        print '</HEAD>' 

Main()
