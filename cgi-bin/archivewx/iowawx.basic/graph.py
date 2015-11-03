#!/usr/local/bin/python
# This program will generate graphs of daily temperature data
# Daryl Herzmann 4-10-99

import gd, sys, functs, tempfile, style
from cgi import *
from pg import *

mydb = connect('iowawx')

def Main():
	form = FormContent()
	if form.has_key("city"):
		city = form["city"][0]
	else:
		style.SendError("Please Enter a City")
	if form.has_key("year"):
		year = str(form["year"][0])
	else:
		style.SendError("Please Enter a Valid Year")


	print 'Content-type: text/html \n\n'
	
	im = gd.image((800,500))        # Set up image object

	# Allocate Colors and Fonts
	red = im.colorAllocate((255,0,0))
	green = im.colorAllocate((0,255,0))
	blue = im.colorAllocate((0,0,255))
	black = im.colorAllocate((0,0,0))
	white = im.colorAllocate((255,255,255))
	lgreen = im.colorAllocate((127,125,85))
	test = im.colorAllocate((12,15,185))

	label = gd.gdFontMediumBold
	title = gd.gdFontGiant

	city_name = functs.convert_station(city)	

	results = mydb.query("SELECT high,low from "+city+" WHERE yeer = '"+year+"'")
	results = results.getresult()

	im.fill((10,10), black)

	im.string(title, (10, 5), "Temperature Mins / Maxs for "+city_name+" during "+year , white) 
	im.string(title, (350, 400), "Consecutive Days", white)
	im.stringUp(title, (0, 250), "Temperature ", white)

	highs = []
	lows = []

	im.origin((20,0),2,3)

	im.line((0,20),(380,20), lgreen)		# 100 degree line
	im.line((0,88),(380,88), lgreen)		# 32 degree line
	im.line((0,120),(380,120), lgreen)		# 0 degree line

	im.string(label, (0, 16), "100 F", lgreen)
	im.string(label, (0, 84), "32 F", lgreen)
	im.string(label, (0, 116), "0 F", lgreen)


	im.origin((50,0),2,3)

	im.line((90,83),(90,93), white)		# April degree line
	im.line((181,83),(181,93), white)	# July degree line
	im.line((273,83),(273,93), white)	# October degree line


	for i in range(len(results)):
		highdata = i+1, 120 - int(results[i][0])
		lowdata =  i+1, 120  - int(results[i][1])
		highs.append(highdata)
		lows.append(lowdata)

	highs = tuple(highs)
	lows = tuple(lows)

	im.lines(highs, red)
	im.lines(lows, blue)

	filename = tempfile.mktemp()
	filename = filename[-5:-2] + filename[-1:]


	im.writeGif("/home/httpd/html/archivewx/iowawx/graphs/"+filename+".gif")

	print '<HTML>'
	print '<img src="/archivewx/iowawx/graphs/'+filename+'.gif">'

	print '<H3>Options:</H3>'
	print '<P><a href="/archivewx/iowawx/graphs/'+filename+'.gif">Shift-Click to download this graph</a>'
	print '<P><a href="index.py?opt=graph_yearly">Try another query</a>'
Main()
