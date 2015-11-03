#!/usr/local/bin/python
# THis program generates the forecasting excercise
# Daryl Herzmann 8-30-99

import time, pg

mydb = pg.connect('frcst')

def gettime():
	now = time.time()
	now_tuple = time.localtime(now)
	return now_tuple[0], now_tuple[1], now_tuple[2], now_tuple[3], now_tuple[4]

def find_float(yeer, month, day, class_name):
	time_tuple = (int(yeer), int(month), int(day), 6,0,0,0,0,0)
	now = time.mktime(time_tuple) + 86400
	now_tuple = time.localtime(now)
	yeer = str(now_tuple[0])
	month = str(now_tuple[1])
	day = str(now_tuple[2])

	entry = mydb.query("SELECT floater from cases WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ").getresult()
	try:
		return entry[0][0]
	except:
		return "Unknown"

def mk_prec(sec_head):
        print '<TD><SELECT name="'+sec_head+'">'
        print '<option value="0">CAT 0 &nbsp; | &nbsp; 0 - Trace'
        print '<option value="1">CAT 1 &nbsp; | &nbsp; Trace - 0.05'
        print '<option value="2">CAT 2 &nbsp; | &nbsp; 0.06 - 0.25'
        print '<option value="3">CAT 3 &nbsp; | &nbsp; 0.26 - 0.50'
        print '<option value="4">CAT 4 &nbsp; | &nbsp; 0.51 - 1.00'
        print '<option value="5">CAT 5 &nbsp; | &nbsp; 1.01 +'
        print '</SELECT></TD>'

def mk_snow(sec_head):
        print '<TD><SELECT name="'+sec_head+'">'
        print '<option value="0">CAT 0 &nbsp; | &nbsp; 0 - Trace'
        print '<option value="1">CAT 1 &nbsp; | &nbsp; Trace - 2"'
        print '<option value="2">CAT 2 &nbsp; | &nbsp; 2" - 4"'
        print '<option value="3">CAT 3 &nbsp; | &nbsp; 4" - 8"'
        print '<option value="4">CAT 4 &nbsp; | &nbsp; 8" +'
        print '</SELECT></TD>'


def Main(class_name):
	print '<H3 align="center">'+class_name+' Forecasting Exercise: Make your forecast</H3>'
	yeer, month, day, hour, minute = gettime()
	print '<H3 align="center"><font color="red">The Current Time is: ',hour,': ',minute,' | You have until 19:00</font></H3>'
	floater = find_float(str(yeer), str(month), str(day), class_name)
	code = "try and hack this&"

	print '<form method="POST" action="enter.py">'
	print '<input type="hidden" name="code" value="'+code+'">'
	print '<input type="hidden" name="yeer" value="'+str(yeer)+'">'
	print '<input type="hidden" name="month" value="'+str(month)+'">'
	print '<input type="hidden" name="day" value="'+str(day)+'">'
	print '<input type="hidden" name="class_name" value="'+str(class_name)+'">'

	print '<CENTER>'

	print '<TABLE>'
	print '<TR><TH valign="CENTER"><H4>Enter your userid: ex) mt311_akrherz</H4></TH>'
	print '<TD><input type="text" size="20" name="userid" value="'+class_name+'_"></TD></TR>'

	print '<TR><TH valign="CENTER"><H4>Enter your passwd: </H4></TH>'
	print '<TD><input type="password" size="10" MAXLENGTH="8" name="passwd"></TD>'
	print '</TR></TABLE>'

	print '<TABLE WIDTH="100%">'
	print '<TR><TH></TH><TH>High Temp:</TH><TH>Low Temp:</TH><TH>Precipitation:</TH><TH>Snow fall:</TH></TR>'

	print '<TR><TD>Des Moines:</TD>'
	print '<TD><input type="text" size="3" name="DMX_high" MAXLENGTH="3"></TD>'
	print '<TD><input type="text" size="3" name="DMX_low" MAXLENGTH="3"></TD>'
	mk_prec("DMX_prec")

	mk_snow("DMX_snow")

	print '<TR><TD>'+floater+':</TD>'
	print '<TD><input type="text" size="3" name="FLOATER_high" MAXLENGTH="3"></TD>'
	print '<TD><input type="text" size="3" name="FLOATER_low" MAXLENGTH="3"></TD>'

	mk_prec("FLOATER_prec")

	mk_snow("FLOATER_snow")

	print '</TR></TABLE>'

	print '<CENTER><BR><BR>'
	print '<input type="submit" value="submit my forecast">'

	print '</form></CENTER>'
