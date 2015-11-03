#!/usr/local/bin/python
# This program takes people through the archivewx forecast
# Daryl Herzmann 8/14/98

from cgi import *
import os, sys, posix, style, re
from pgext import *

mydb = connect('archanswers')

data_path = '/home/httpd/html/archivewx/CGI_SRC/hours.src'
form = FormContent()
day = form["day"][0]
month_num = form["month_num"][0]
month_name = form["month_name"][0]

hour = "07AM(CDT)12Z"
if form.has_key("hour"): hour = form["hour"][0]
hour = str(hour[:2]+' '+hour[2:4]+' '+hour[4:9]+' '+hour[9:])
realyez = day[-2:]+month_num+day[3:5]+hour[12:14]

real = month_name+' '+day[3:5]+', '+day[5:]

def next():
	aaa = str(int(hour[:2])+(1))
	if int(aaa) == 12:
		bbb = str(int(hour[-3:-1])+(1))
		nexthour = '12PM(CDT)17Z'
		condense = aaa+'PM'+hour[6:11]+bbb+'Z&month_num='+month_num+'&month_name='+month_name
	elif int(aaa) < 10:
		aaa = '0'+aaa
		bbb = str(int(hour[-3:-1])+(1))
		nexthour = aaa+hour[2:12]+bbb+'Z'
		condense = aaa+hour[3:5]+hour[6:11]+bbb+'Z&month_num='+month_num+'&month_name='+month_name
	else:
		bbb = str(int(hour[-3:-1])+(1))
		nexthour = aaa+hour[2:12]+bbb+'Z'
		condense = aaa+hour[3:5]+hour[6:11]+bbb+'Z&month_num='+month_num+'&month_name='+month_name
	return nexthour, condense

def closer():
	print '<center><H3>You have now seen all the data for Today</H3>'
	print '<a href="/cgi-bin/archivewx/HTML_SRC/make_forecast.py?day='+day+'&month_name='+month_name+'&month_num='+month_num+'">'
	print 'It is time to Forecast</a>'
	style.std_bot()
	sys.exit()

def Main():  
	style.header('Forecast Exercise for '+real,'white')
	nexthour, condense = next()
	f = open(data_path, 'r')
        comp = f.read() 
        f.close() 
        lines = re.split('\012', comp)
	for line in lines:
		if line == "REPLACE":
			print day
		elif line == "REALTIME":
			print hour
		elif line == "TIME":
			print realyez
		elif line == "NEXTHOUR":
			print condense
		elif line == "NEXTHOUR2":
			print condense[0:4]
		elif line == "DAY":
                        print day
		elif line == "REAL":
			print real
		elif line == "STOP":
			if hour[:2] == "12":
				closer()
			else:
				print '<BR>'
		else:
			print line
	style.std_bot()

Main()
