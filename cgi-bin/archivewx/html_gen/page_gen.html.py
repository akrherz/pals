#!/usr/local/bin/python

# Takes the form prompt for a date and then generates a page to display
# That days data
# Daryl Herzmann 7/8

import sys, os, posix
from cgi import *

case_dir = "/home/httpd/html/archivewx/cases/"
case_ref = "cases/"


def header(title):
	print '<head><title>'
	print title
	print '</title></head>'
	print '<body bgcolor="white">'

def lister(date):
	file_loc = case_dir+date
	files = posix.listdir(file_loc)
	files.sort()
	print '<HR><H3>Temperatures and Winds</H3>'
	for file in files:
		if file[0:4] == "temp":
			if not file[4] == "9":
				print '<a href="'+case_ref+date+'/'+file+'">'+file[4:6]+'Z Temps</a><BR>'
	print '<HR><H3>Dewpoints and Winds</H3>'
	for file in files:
                if file[0:3] == "dew": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file[3:5]+'Z Dew Point</a><BR>'
	print '<HR><H3>Upper Air at 0Z</H3>'
        for file in files: 
                if file[3:7] == "mb00":
			print '<a href="'+case_ref+date+'/'+file+'">'+file[0:5]+' Map</a><BR>'	
		elif file == "500vort00.gif":
			print '<a href="'+case_ref+date+'/'+file+'">'+file[0:3]+'mb Map with Vorticity</a><BR>'
	print '<HR><H3>Upper Air at 12Z</H3>'
        for file in files:
                if file[3:7] == "mb12": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file[0:5]+' Map</a><BR>'
                elif file == "500vort12.gif": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file[0:3]+'mb Map with Vorticity</a><BR>'
	print '<HR><H3>ETA run at 12Z for precip</H3>'
        for file in files: 
                if file[0:9] == "etaprec12": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file+'</a><BR>'
	print '<HR><H3>ETA run at 12Z for vorticity</H3>'
        for file in files: 
                if file[0:9] == "etavort12": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file+'</a><BR>'
	print '<HR><H3>ETA run at 12Z for THK</H3>'
        for file in files:
                if file[0:8] == "etaTHK12": 
                        print '<a href="'+case_ref+date+'/'+file+'">'+file+'</a><BR>'


def Main():
	print 'Content-type: text/html\n\n'
	form = FormContent()
	date = form["date"][0]
	header(''+date+' Weather')
	print '<H2 ALIGN=CENTER>Severe Weather Products</H2>'
	print '<HR><FONT COLOR=DARKBLUE><H2>U. S. Weather Observations on '+date+'</H2> </FONT>'
	lister(date)


Main()  


