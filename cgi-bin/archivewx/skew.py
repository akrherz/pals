#!/usr/local/bin/python
# Generates HTML file's for todayand times for skewT maps
# Daryl Herzmann 7/22/98 

# Python imports
import posix, os, sys, re, time

# Base references for the program
data_path = '/home/httpd/html/archivewx/skew.map'
skew_path = 'http://www.pals.iastate.edu/archivewx/data/'
map_path = 'http://www.pals.iastate.edu/archivewx/skew.gif'


def imagemap():
	station_lines = []
        f = open(data_path, 'r') 
        comp = f.read() 
        f.close()
	lines = re.split('\012', comp) 
	return lines

def header():
	print 'Content-type: text/html\n\n'
	print '<HTML>\n<HEAD>\n<TITLE>Skew T chart</TITLE>\n</HEAD>\n'
	dirStr = time.strftime('/%Y_%m_%d/',time.gmtime(time.time()))
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

def get_time():
	geos = time.strftime('%y%m%d%H',time.gmtime(time.time())) 
        if int(geos[-2:]) > 12:
		end = "12.gif" 
        else:
                end = "00.gif"
	geos = time.strftime('%y%m%d',time.gmtime(time.time()))
	geos = geos+end
	return geos

def Main():
	station_lines = imagemap()

	now_date = get_time()
	header()
	make_imagemap(station_lines, now_date)

	body()
	sys.exit()
Main()
