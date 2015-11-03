#!/usr/local/bin/python
# This is the main program to show all the case data that we have
# 7/9/98 Daryl Herzmann

import sys, posix, style

dir = "/home/httpd/html/archivewx/cases/"


def body():
	print '<H2>Introduction:</H2>'
	print '<BR><B>In this activity, you are given the weather data up until noon for a certain day of your choice.'
	print '<P>Then after looking at the weather images, you will be asked for where you belive'
	print 'severe weather will happen.'
	print '<P>Then you can check your results.</B><HR>'
	print '<H2>Start by selecting a day to forecast for:</H2>'

def selector():
	print '<form method="post" action="/cgi-bin/archivewx/page_gen.py">'
	print '<select name="date">'
        dates = posix.listdir(dir)
        dates.sort()
	for date in dates:
                if date == "index.html":
			blah = "1"
                else:
                        print '<option value="'+date+'">'+date
	print '</select><HR><H2>And get started:</H2>'
	print '<input type="submit" value="Start exercise"></form>'

def Main():
	style.header("Archived Weather -- Cases","/images/ISU_bkgrnd.gif")
	style.std_top('Archived Weather Data -- Cases:<H3>Severe Weather Forecasting Activity</H3>')
	body()
	selector()
	style.std_bot()
Main()
