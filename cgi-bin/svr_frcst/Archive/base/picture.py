#!/usr/local/bin/python
# This program displays the pict file
# Daryl Herzmann 6-2-99
#UPDATED 6-4-99: Made it so that the Help page appears on the page with the file

import os, cgi, style, re


def Main():
	form = cgi.FormContent()
	file = form["file"][0]

	style.header(file, "white")

	test = os.path.split(file)
	
	if test[1][:3] == "dew":
		print '<H3 align="center">Dewpoint Chart</H3>'
		print '<a href="/archivewx/help/dewp.html">Click for help with this Map</a><BR><BR>'

	elif test[1][:3] == "sfc":
		print '<H3 align="center">Surface Chart</H3>'
		print '<a href="/archivewx/help/sfcmap.html">Click for help with this Map</a><BR><BR>'		

	elif test[1][:4] == "temp":
		print '<H3 align="center">Surface Temperature Chart</H3>'
		print '<a href="/archivewx/help/temp.html">Click for help with this Map</a><BR><BR>'

	elif test[1][:3] == "NAT":
		print '<H3 align="center">National Radar</H3>'
		print '<a href="/archivewx/help/radar.html">Click for help with this Map</a><BR><BR>'

	print '<a href="javascript:history.go(-1)">Go Back..</a><BR><BR>'

	print '<IMG SRC="'+file+'">'

	style.std_bot()


Main()
