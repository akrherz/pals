#!/usr/local/bin/python
# This program will generate a plot of any asked for data
# Daryl Herzmann 6/20/99

import gd, time, tempfile, sys
from pg import *
from cgi import *

mydb = connect('campbell_daily')		# Where the Temp data is located

now = time.time()				# Return now
now_tuple = time.localtime(now)			# Find out when today is......

off = 17		# Offset on the chart
suth_pt = [135,129]	# Sutherland
char_pt = [275,333]	# Chariton
ceda_pt = [387,249]	# Cedar Rapids
ames_pt = [247,245]	# Ames
nash_pt = [315,194]	# Nashua
craw_pt = [384,314]	# Crawford
lewi_pt = [165,299]	# Lewis
cast_pt = [113,236]	# Castana
kana_pt = [250,173]	# Kanaswa
rhod_pt = [293,253]	# Rhodes

title = gd.gdFontGiant		# title type
label = gd.gdFontMediumBold	# label type

dirname = tempfile.mktemp()                     # Create a directory name via tempfile module
dirname = dirname[-5:-2] + dirname[-1:] 

iowa_gif_src = "/home/httpd/html/campbell/src/iowa.gif"
iowa_gif_out = "/home/httpd/html/campbell/hist/tmp/"+dirname+".gif"
iowa_gif_href = "/campbell/hist/tmp/"+dirname+".gif"

def mk_image(im):
	black = im.colorAllocate((0,0,0))	# Colors to use in the image
	red = im.colorAllocate((255,0,0))	#
	blue = im.colorAllocate((0,0,255))	#

	nice_date = time.strftime("%x %X", now_tuple)			# My Timestamp date format
	im.string(label, (290,490), "Generated on "+nice_date, black)	# My Timestamp label

	return im	# Return image container for others to fill

def plot_pt(im, first, second, location):
	red = im.colorAllocate((255,0,0))	# Colors to use in the image
	blue = im.colorAllocate((0,0,255))	#

	im.string(title, (location[0], location[1]), str(int(round(first))), red)		# High Temp.
	im.string(title, (location[0], location[1]+off), str(int(round(second))), blue)		# Low Temp.

	return im	# Return image container for others to fill

def Main():
	print 'Content-type: text/html \n\n'
	print '<HTML>'

	form = FormContent()
	yeer = form["yeer"][0]
	month = form["month"][0]
	day = form["day"][0]
	plot_str = form["plot_str"][0]

	im = gd.image(iowa_gif_src) 	# load image into a gd container
	im = mk_image(im)

	time_tuple = (int(yeer), int(month), int(day),  12, 36, 20, 4, 127, 1)
	nice_date = time.strftime("%B %d, %Y", time_tuple)			# Nice format for graph title

	black = im.colorAllocate((0,0,0))	# Colors to use in the image
	im.string(title, (15,15), "High & Low Air Temperatures "+nice_date , black) # The actual title

	stations = ('a130209','a131299','a131329','a131559','a131909','a134309','a134759','a135879','a138019','a136949') # Stations vector
	locations = [ames_pt, cast_pt, ceda_pt, char_pt, craw_pt, nash_pt, suth_pt, lewi_pt, kana_pt, rhod_pt] 		# Points array

	i = 0	# loop variable
	for station in stations:
		query = mydb.query("SELECT '+plot_str+' from "+station+"_"+yeer+" WHERE (month = "+month+" AND day = "+day+")").getresult()

		try:
			first = query[0][0]	# high air-temp
			second = query[0][1]	# low air-temp
			if first == second:
				first = -99
				second = -99

		except IndexError:
			first = -99	# high air-temp
			second = -99	# low air-temp

		im = plot_pt(im, first, second, locations[i]) # my ploting function
		i = i + 1		# Increment variable

	im.writeGif(iowa_gif_out)	# Write file out

	print '<img src="'+iowa_gif_href+'">'
	print '</HTML>'

Main()
