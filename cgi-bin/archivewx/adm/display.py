#!/usr/local/bin/python
# This will display all the data for the day requested
# Daryl Herzmann 8/24/98

import os, posix, style
from cgi import *

data_src = '/home/httpd/html/archivewx/data/'
url_ref = 'https://pals.agron.iastate.edu/archivewx/data/'

def checker(passwd):
	if passwd != 'pals1998':
		style.SendError('Wrong password!')

def Main():
	form = FormContent()
	day = form["day"][0]
	passwd = form["pass"][0]
	checker(passwd)
	style.header('Data for '+day, 'white')
	style.std_top('Data for '+day)
	files = posix.listdir(data_src+day+'/data/')
	print '<multicol cols="3">'
	for file in files:
		print '<a href="'+url_ref+day+'/data/'+file+'">'
		print file+'</a><BR>'
	print '</multicol>'
	style.std_bot()

Main()
