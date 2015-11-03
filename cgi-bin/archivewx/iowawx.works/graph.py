#!/usr/local/bin/python
# This program will generate graphs of daily temperature data
# Daryl Herzmann 4-10-99

import gd, sys, functs, tempfile, style, os
from cgi import *
from pg import *

mydb = connect('iowawx')

xwidth = 800
yheight = 500


def content():
	form = FormContent()
	if form.has_key("city"): city = form["city"][0]
	else:
		style.SendError("Please Enter a City")
	if form.has_key("year"): year = str(form["year"][0])
	else:
		style.SendError("Please Enter a Valid Year")
	if form.has_key("loop"): loop = str(form["loop"][0])
	else:
		loop = 1

	return city, year, loop

def query_station(city, year):
	results = mydb.query("SELECT high,low from "+city+" WHERE yeer = '"+year+"'")
	results = results.getresult()

	return results

def image(city_name, year):
	im = gd.image((xwidth,yheight))

	# Allocate Colors          
	red = im.colorAllocate((255,0,0))
	green = im.colorAllocate((0,255,0))
	blue = im.colorAllocate((0,0,255))
	black = im.colorAllocate((0,0,0))
	white = im.colorAllocate((255,255,255))
	lgreen = im.colorAllocate((127,125,85))

	label = gd.gdFontMediumBold
	title = gd.gdFontGiant

	im.fill((10,10), black)                 # Sets up backround of image

	im.string(title, (10, 5), "Temperature Mins / Maxs for "+city_name+" during "+year , white) 
	im.string(title, (xwidth - 450, yheight - 100), "Consecutive Days", white)
	im.stringUp(title, (0, yheight - 250), "Temperature ", white)

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

	return im

def parse_data(results):
	highs = []
	lows = []

	for i in range(len(results)):
		highdata = i+1, 120 - int(results[i][0])
		lowdata =  i+1, 120  - int(results[i][1])
		highs.append(highdata)
		lows.append(lowdata)

	return tuple(highs), tuple(lows)

def html_gif(filename):
	print '<HTML>'
	print '<img src="'+filename+'">'

	print '<H3>Options:</H3>'
	print '<P><a href="'+filename+'">Shift-Click to download this graph</a>'
	print '<P><a href="index.py?opt=graph_yearly">Try another query</a>'

def make_animate(dirname):
	os.chdir('/home/httpd/html/archivewx/iowawx/graphs/'+dirname+'/')
	os.popen('/usr/bin/gifsicle --delay=100 --loopcount=3 *.gif > anim.gif')

	return '/archivewx/iowawx/graphs/'+dirname+'/anim.gif'

def Main():
	city, year, loop = content()

	print 'Content-type: text/html \n\n'
	city_name = functs.convert_station(city)	# Convert code into string name


	im = []

	dirname = tempfile.mktemp()
	dirname = dirname[-5:-2] + dirname[-1:]

	os.mkdir("/home/httpd/html/archivewx/iowawx/graphs/"+dirname, 0777)

	for i in range(int(loop)):
		temp = image(city_name, year)
		im.append(temp)
		results = query_station(city, year)

		highs, lows = parse_data(results)

		red = im[i].colorAllocate((255,0,0))
		blue = im[i].colorAllocate((0,0,255))

		im[i].lines(highs, red)
		im[i].lines(lows, blue)

		this_i = str(i)

#		gif_file.append(filename)

		im[i].writeGif("/home/httpd/html/archivewx/iowawx/graphs/"+dirname+"/const"+this_i+".gif")

		year = str(int(year)+ 1)
	
	if loop > 0:
		gif_file = make_animate(dirname)
	else:
		gif_file = "/home/httpd/html/archivewx/iowawx/graphs/"+dirname+"/const0.gif"

	html_gif(gif_file)

Main()
