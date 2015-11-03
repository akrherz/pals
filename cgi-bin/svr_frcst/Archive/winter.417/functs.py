#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann
# UPDATED 8-9-99: Removed old changelog, Added more function variables

import time, os, sys, time, regsub, pg, string

admindb = pg.connect('archadmin')

def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def create_time(year, month, day, hour, minute):
        time_tuple = (year, month, day, hour, minute, 0, 0, 0, 0)       # Form the orig tuple
        return time.mktime(time_tuple)          # This is time_tuple in ticks

def setup_table():
	print '<CENTER>'
	print '<TABLE WIDTH="650" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">'
        
	print '<TR>'
	print '<TD colspan="3"><img src="/icons/svr_frcst-top.gif" HSPACE="0" VSPACE="0" BORDER="0"></TD></TR>'

	print '<TR valign="top" bgcolor="white">'
	print '<TD colspan="3"><img src="/icons/svr_frcst-upleft.gif" HSPACE="0" VSPACE="0" BORDER="0" HEIGHT="20"></TD>'
        print '</TR>'


def mk_help():
#	print '<B><U><font size="2" face="arial">Help Topics</font></U></B><BR>'
        print '<font size="2" face="arial">'
        print '<LI><a href="/svr_frcst/help/z.html">What is UTC time?</a></LI>'
        print '<LI><a href="/svr_frcst/help/text.html">Watches and Warnings Data</a></LI>'
        print '<LI><a href="/svr_frcst/help/temp.html">Surface Temperature Map</a></LI>'
        print '<LI><a href="/svr_frcst/help/sfcmap.html">Surface Map</a></LI>'
        print '<LI><a href="/svr_frcst/help/dewp.html">Surface Dew Points Map</a></LI>'
        print '<LI><a href="/svr_frcst/help/radar.html">Radar</a></LI>'
        print '</font><BR>&nbsp;'

def mk_data_link2(file, thumbnail, string_txt, i, hour_time):
#	print '/home/httpd/html/'+file
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/base/picture.py?file='+file+'"> '+hour_time+'</a><BR>'
	else:
		print "Missing"

def mk_data_link(file, thumbnail, string_txt):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/base/picture.py?file='+file+'">'+string_txt+'</a><BR>'

def mk_row_data(orig_secs, prefix, suffix, icon_ref, title):
	print '<TH>'+title+'</TH>'
	for i in range(4):
		print '<TD align="center">'
		this_secs = orig_secs - i*3600*3
		this_tuple = time.localtime(this_secs)
		if this_tuple[-1] == 1:
			this_secs = this_secs - 3600
			this_tuple = time.localtime(this_secs)
#		print this_tuple
		data_format = time.strftime("%y%m%d%H", this_tuple)
		hour_time = time.strftime("%H Z", this_tuple)
		dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
		mk_data_link2(dir_format+prefix+data_format+suffix , icon_ref , title, str(i), hour_time)
		print '</TD>'


def mk_data(gmt_tuple):
	orig_secs = time.mktime(gmt_tuple)
        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
        print '<font size="2" face="arial">'
	print '<BR>'
	print '<TABLE width="100%" border="1">'
	print '<TR><TH></TH><TH>Current:</TH><TH>- 3 hr:</TH><TH>- 6 hrs:</TH><TH>- 9 hrs:</TH></TR>'
	print '<TR>'
	mk_row_data(orig_secs, "sfc", ".gif", "/icons/sfc_thumb.gif", "Surface Chart")
	print '</TR><TR>'
	mk_row_data(orig_secs, "temp", ".gif", "/icons/temp_thumb.gif", "Surface Temps Chart")
	print '</TR><TR>'
	mk_row_data(orig_secs, "dew", ".gif", "/icons/temp_thumb.gif", "Surface DewPoint Chart")
	print '</TR><TR>'
	mk_row_data(orig_secs, "moist", ".gif", "/icons/moist_thumb.gif", "Moisture Divergence")
	print '</TR><TR>'
	mk_row_data(orig_secs, "NAT", ".gif", "/icons/NAT_thumb.gif", "National Radar Summary")
	print '</TR>'
	print '</TABLE>'

	print '<BR><b>Other data links:</b><BR>'
	print '<MULTICOL COLS="3">'
#	mk_data_link(dir_format+data_format+'.txt' , "/icons/NWS_thumb.gif" , "NWS Text Data")
	mk_data_link(dir_format+'cape'+data_format+'.gif' , "/icons/cape_thumb.gif" , "ETA Derived CAPE")
	mk_data_link(dir_format+'tpw'+data_format+'.gif' , "/icons/tpw_thumb.gif" , "Precipitable Water")
	mk_data_link(dir_format+'li'+data_format+'.gif' , "/icons/li_thumb.gif" , "Lifted Index")
	mk_data_link(dir_format+'light'+data_format+'.gif' , "/icons/light_thumb.gif" , "Lightning Data")
	mk_data_link(dir_format+'850mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "850 MB")
	mk_data_link(dir_format+'700mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "700 MB")
	mk_data_link(dir_format+'500VORT'+data_format+'.gif' , "/icons/temp_thumb.gif" , "500 MB Vorticity")
	mk_data_link(dir_format+'500mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "500 MB")
	mk_data_link(dir_format+'300mb'+data_format+'.gif' , "/icons/light_thumb.gif" , "300 MB")
	mk_data_link(dir_format+'200mb'+data_format+'.gif' , "/icons/light_thumb.gif" , "200 MB")
	mk_data_link(dir_format+'etaTHK'+data_format+'.gif' , "/icons/light_thumb.gif" , "ETA Thickness and Pressure")
	mk_data_link(dir_format+'etaVORT'+data_format+'.gif' , "/icons/light_thumb.gif" , "ETA Vorticity")
	mk_data_link(dir_format+'etaPREC'+data_format+'.gif' , "/icons/light_thumb.gif" , "ETA Precipation")
	mk_data_link(dir_format+'MPX'+data_format+'.gif' , "/icons/light_thumb.gif" , "Minneapolis Radar Reflectivity")
	mk_data_link(dir_format+'MPXVEL'+data_format+'.gif' , "/icons/light_thumb.gif" , "Minneapolis Velocity")
	mk_data_link(dir_format+'DMX'+data_format+'.gif' , "/icons/light_thumb.gif" , "Des Moines Radar Reflectivity")
	mk_data_link(dir_format+'1000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "1000 m Profiler")
	mk_data_link(dir_format+'3000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "3000 m Profiler")
	mk_data_link(dir_format+'5600m'+data_format+'.gif' , "/icons/light_thumb.gif" , "5600 m Profiler")
	mk_data_link(dir_format+'9000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "9000 m Profiler")
	mk_data_link(dir_format+'sat'+data_format+'.gif' , "/icons/light_thumb.gif" , "Satellite Image")

	print '</MULTICOL>'

def mk_top(now_tuple):
        date_str = time.strftime("%B %d, %Y", now_tuple)
        time_str = time.strftime("%I:%M %p [%Z]", now_tuple)

	print '<TABLE align="CENTER">'
	print '<TR WIDTH="100%"><TD>'
	print '<TABLE bgcolor="blue" border="1">'
	print '<TR><TD><font color="red" size="4" face="ARIAL"><B>Current Time:</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center"><B>'+time_str+'</B></TD></TR></TABLE>'
	print '</TD><TD>'
	print '<TABLE bgcolor="blue" border="1">'
	print '<TR><TD><font color="red" size="4" face="ARIAL"><B>Current Date:</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center"><B>'+date_str+'</B></TD></TR></TABLE>'
	print '</TD></TR></TABLE>'

def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'

