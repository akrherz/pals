#!/usr/local/bin/python
# This will be an unique script that will be able to browse data directories and show what's there
# Daryl Herzmann 9-14-99

import cgi, style, os, time

DATA_DIR = '/home/www/pals/html/archivewx/data/'
HREF = '/archivewx/data/'

vals = ("temp","dew", "NAT", "moist","cape",'tpw','li','light','850mb','700mb','500VORT','500mb','300mb','200mb','1000m','3000m','5600m','9000m','sat')
data_opts = {"temp": "Sfc Temps", "dew" : "Sfc Dew Points", "NAT": "National Radar", "moist": "Moisture Divergence", "cape" : "ETA Derived CAPE",
		'tpw' : "Precipitable Water" ,
		'li' : "Lifted Index" ,
		'light' : "Lightning Data" ,
		'850mb' : "850 MB" ,
		'700mb' : "700 MB" ,
		'500VORT' : "500 MB Vorticity",
		'500mb' : "500 MB" ,
		'300mb' : "300 MB" ,
		'200mb' : "200 MB" ,
		'1000m' : "1000 m Profiler",
		'3000m' : "3000 m Profiler",
		'5600m' : "5600 m Profiler",
		'9000m' : "9000 m Profiler",
		'sat' :	"Satellite Image",}

def mkoption(dirname):
	time_tuple = (int(dirname[:4]) , int(dirname[5:7]), int(dirname[8:]), 0, 0,0,0,0,0 )
	now = time.mktime(time_tuple)
	nice_date = time.strftime("%B %d, %Y", time_tuple)
	print '<option value="'+str(now)+'">'+nice_date 

def mkdata(secs):
	secs = int(float(secs))
	now_tuple = time.localtime(secs)
	nice_date = time.strftime("%B %d, %Y", now_tuple)
	print '<H3>Data For: '+nice_date+'</H3>'

	print '<TABLE><TR><TH>Data_Type:</TH>'
	for i in range(24):
		print '<TH>'+str(i)+'</TH>'
	print '</TR>'

	for val in vals:
		print '<TR><TH>'+data_opts[val]+'</TH>'
		for i in range(24):
			this_secs = secs + i*3600
			this_tuple = time.localtime(this_secs)
			data_pre = time.strftime("%Y_%m_%d", this_tuple)
			data_format = time.strftime("%y%m%d%H", this_tuple)		
			filename = DATA_DIR+data_pre+"/"+val+data_format+".gif"
			if os.path.isfile(filename):
		                print '<TH><a href="'+HREF+data_pre+'/'+val+data_format+'.gif">W</a></TH>'
			else:
				print '<TH bgcolor="red"><BR></TH>'
		print '</TR>'

		
	print '</TABLE>'

def Main():
	form = cgi.FormContent()
	try:
		secs = form["secs"][0]
	except:
		secs = "nill"
	
	style.header("Data Viewer","white")

	files = os.listdir(DATA_DIR)
	files.sort()

	print '<TABLE><TR><TD>'
	print '<H3>Pick Day:</H3>'
	print '<form method="POST" action="browser.py">'
	print '<SELECT name="secs" size="20">'
	for file in files:
		mkoption(file)
	print '</SELECT><BR>'
	print '<input type="SUBMIT">'
	print '</form></TD>'
	print '<TD>'
	if secs != "nill":	
		mkdata(secs)
	print '</TD>'
	print '</TR></TABLE>'

	print '<a href="/admin">Admin Page</a>'		

Main()
