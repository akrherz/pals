#!/usr/bin/env python
# Generates HTML file's for todayand times for skewT maps
# Daryl Herzmann 7/22/98 

# Python imports
import posix, os, sys, re, time, cgi, pg, mx.DateTime
mydb = pg.connect('severe2', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)

# Base references for the program
data_path = '/home/www/pals/html/archivewx/skew.map'
skew_path = 'https://pals.agron.iastate.edu/archivewx/data/'
map_path = 'https://pals.agron.iastate.edu/archivewx/skew.gif'


def imagemap():
	station_lines = []
        f = open(data_path, 'r') 
        comp = f.read() 
        f.close()
	lines = re.split('\012', comp) 
	return lines

def header(ticks):
	print 'Content-type: text/html\n\n'
	print '<HTML>\n<HEAD>\n<TITLE>Skew T chart</TITLE>\n</HEAD>\n'
	dirStr = time.strftime('/%Y_%m_%d/',time.gmtime(ticks))
	print '<BASE HREF="'+skew_path+dirStr+'skew/">\n'
	print '<BODY><MAP NAME="usa-2.map">\n'

def make_imagemap(station_lines, now_date):
	for line in station_lines:
		if line[0:3] != '<AR':
			break
		line = re.split('.gif', line)
		line = line[0]+now_date+line[1]
		print line+'\n'

def body():
	print '</MAP><P>\n'
	print '<A HREF="usa-2.map"><IMG SRC="'+map_path+'" ISMAP USEMAP="#usa-2.map"></A></P>\n'
	print '</BODY>\n</HTML>\n'

def get_time(myTicks):
	geos = time.strftime('%y%m%d%H',time.gmtime( myTicks )) 
        if int(geos[-2:]) > 12:
		end = "12.gif" 
        else:
                end = "00.gif"
	geos = time.strftime('%y%m%d',time.gmtime( myTicks ))
	geos = geos+end
	return geos

def Main():
	station_lines = imagemap()
	form = cgi.FormContent()
	userKey = form["userKey"][0]


	lastTime = advdb.query("SELECT lastTime from users WHERE userKey = "+userKey+" ").getresult()

	try:
		myDate = mx.DateTime.ISO.ParseDateTimeGMT(lastTime[0][0])
	except:
		lastTime = mydb.query("SELECT lastTime from users WHERE userKey = "+userKey+" ").getresult()
		myDate = mx.DateTime.ISO.ParseDateTimeGMT(lastTime[0][0])
	
	myTicks = myDate.ticks()

	now_date = get_time(myTicks)
	header(myTicks)
	make_imagemap(station_lines, now_date)

	body()
	sys.exit()
	
Main()
