#!/usr/local/bin/python
# This program starts people off down the road of archivewx
# Daryl Herzmann 9/14/98

from cgi import *
import os, sys, posix, style, re
from pgext import *

mydb = connect('archanswers')

data_path = '/home/httpd/html/archivewx/CGI_SRC/index.src'

def real_month(aaa):
	if aaa == 'jan': 
		month = '01'
		month2 = 'January'
	elif aaa == 'feb': 
		month = '02'
		month2 = 'February'
	elif aaa == 'mar': 
		month = '03'
		month2 = 'March'
	elif aaa == 'apr': 
		month = '04'
		month2 = 'April'
	elif aaa == 'may': 
		month = '05'
		month2 = 'May'
	elif aaa == 'jun': 
		month = '06'
		month2 = 'June'
	elif aaa == 'jul': 
		month = '07'
		month2 = 'July'
	elif aaa == 'aug': 
		month = '08'
		month2 = 'August'
	elif aaa == 'sep': 
		month = '09'
		month2 = 'September'
	elif aaa == 'oct': 
		month = '10'
		month2 = 'October'
	elif aaa == 'nov': 
		month = '11'
		month2 = 'November'
	elif aaa == 'dec': 
		month = '12'
		month2 = 'December'
	else:
		style.SendError('Invalid Month Entry')
	return month, month2

def Main():
	form = FormContent()
	day = form["day"][0]
	
	month_num, month_name = real_month(day[:3])

	real = month_name+' '+day[3:5]+', '+day[5:]
	style.header('Severe Weather Forecast Exercise','white')
	f = open(data_path, 'r')
        comp = f.read() 
        f.close() 
        lines = re.split('\012', comp)
	day = day+'&month_num='+month_num+'&month_name='+month_name

	for line in lines:
		if line == "REPLACE":
			print day
		elif line == "REAL":
			print real
		else:
			print line
Main()
