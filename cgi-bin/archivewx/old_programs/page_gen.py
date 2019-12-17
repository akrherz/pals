#!/usr/local/bin/python

# Takes the form prompt for a date and then generates a page to display
# That days data
# Daryl Herzmann 7/13/98

import sys, os, posix, style
from cgi import *

case_dir = "/home/httpd/html/archivewx/cases/"
case_ref = "https://pals.agron.iastate.edu/archivewx/cases/"


def table(title):
	print '</td></tr></table>'
	print '<HR><img src="/images/point_02.gif" align="left"><font size="4">'+title+'</font>'
	print '<table border="0" cellspacing="10"><tr>'

def lister(date):
	file_loc = case_dir+date
	files = posix.listdir(file_loc)
	files.sort()
	
	table("Temperatures and Winds")
	for file in files:
		if file[0:4] == "temp":
			if not file[4] == "9":
				if not int(file[4:6]) > 18:
					print '<td><a href="'+case_ref+date+'/'+file+'">'+file[4:6]+'Z Temps</a><BR>'
	
	table("Dewpoints and Winds")
	for file in files:
                if file[0:3] == "dew": 
			if not int(file[3:5]) > 18:
        	                print '<td><a href="'+case_ref+date+'/'+file+'">'+file[3:5]+'Z Dew Point</a><BR>'
	
	table("Upper Air at 0Z")
        for file in files: 
                if file[3:7] == "mb00":
			print '<td><a href="'+case_ref+date+'/'+file+'">'+file[0:5]+' Map</a><BR>'	
		elif file == "500vort00.gif":
			print '<td><a href="'+case_ref+date+'/'+file+'">'+file[0:3]+'mb Map with Vorticity</a><BR>'
	
	table("Upper Air at 12Z")
        for file in files:
                if file[3:7] == "mb12": 
                        print '<td><a href="'+case_ref+date+'/'+file+'">'+file[0:5]+' Map</a><BR>'
                elif file == "500vort12.gif": 
                        print '<td><a href="'+case_ref+date+'/'+file+'">'+file[0:3]+'mb Map with Vorticity</a><BR>'
	
	table("ETA run at 0Z for precip")
        for file in files: 
                if file[-5:] == "0.gif": phrase = "0-12 Hour ETA Precip"
		elif file[-5:] == "1.gif": phrase = "12-24 Hour ETA Precip"
		elif file[-5:] == "2.gif": phrase = "24-36 Hour ETA Precip"
		elif file[-5:] == "3.gif": phrase = "36-48 Hour ETA Precip"
		else: continue
		if file[0:9] == "etaprec12": 
                        print '<TD><a href="'+case_ref+date+'/'+file+'">'+phrase+'</a><BR>'
	
	table("ETA run at 0Z for vorticity")
        for file in files:
		if file[-5:] == "0.gif": phrase = "12 Hour ETA Vorticity"
		elif file[-5:] == "1.gif": phrase = "24 Hour ETA Vorticity"
		elif file[-5:] == "2.gif": phrase = "36 Hour ETA Vorticity"
 		elif file[-5:] == "3.gif": phrase = "48 Hour ETA Vorticity"
                else: continue
		if file[0:9] == "etavort12": 
                        print '<td><a href="'+case_ref+date+'/'+file+'">'+phrase+'</a><BR>'
	
	table("ETA run at 0Z for MSLP & Thickness")
        for file in files:
		if file[-5:] == "0.gif": phrase = "12 Hour ETA"
		elif file[-5:] == "1.gif": phrase = "24 Hour ETA"
		elif file[-5:] == "2.gif": phrase = "36 Hour ETA"
		elif file[-5:] == "3.gif": phrase = "48 Hour ETA "
                else: continue
		if file[0:8] == "etaTHK12": 
                        print '<td><a href="'+case_ref+date+'/'+file+'">'+phrase+'</a><BR>'
	print '</tr></table>'

def intro(date):
	print '<B>Help for forecasting: </B><BR>'
	print '<spacer type="horizontal" size="30"><a href="hints_gen.py?date='+date+'">Severe Weather Hints</a>'
	print '<spacer type="horizontal" size="30"><a href="/archivewx/files/zulu.html">What is Z time?</a>'

def ready(date):
	print '<HR><HR><H3>After looking at this data:<center><H2>'
	print '<a href="forecast_gen.py?date='+date+'">I am ready to forecast for this day</a>'
	print '</center></H2>'

def Main():
	form = FormContent()  
        date = form["date"][0]
	if not form.has_key("date"): style.SendError("CGI ERROR")
	style.header(date+' Weather','/images/ISU_bkgrnd.gif')
	style.std_top("U. S. Weather Observations on "+date)
	intro(date)
	lister(date)
	ready(date)

	style.std_bot()
Main()  


