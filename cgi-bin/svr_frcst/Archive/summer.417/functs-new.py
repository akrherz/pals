#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann
# UPDATED 6-4-99: Added picts into the data links
# UPDATED 6-4-99: Changed mk_top to a new style
# UPDATED 7-5-99: Changed functs in order to conform with new style
# UPDATED 7-14-99: Cleaned house and code
# UPDATED 7-21-99: Added Support for multiple q's per hour
	
import time, os, sys, time, regsub, pg, string

admindb = pg.connect('archadmin')

def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def create_time(year, month, day, hour, minute):
        time_tuple = (year, month, day, hour, minute, 0, 0, 0, 0)       # Form the orig tuple
        return time.mktime(time_tuple)          # This is time_tuple in ticks

def setup_table():
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

def mk_data_link(file, thumbnail, string_txt):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/mt417/picture.py?file='+file+'">'+string_txt+'</a><BR>'

def mk_row_data(orig_secs, prefix, suffix, icon_ref, title):
	for i in range(3):
		print '<TD>'
		this_secs = orig_secs - i*3600
		this_tuple = time.gmtime(this_secs)
		data_format = time.strftime("%y%m%d%H", this_tuple)
		dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
		mk_data_link(dir_format+prefix+data_format+suffix , "/icons/sfc_thumb.gif" , "Surface Chart")
		print '</TD>'


def mk_data(gmt_tuple):
	orig_secs = time.mktime(gmt_tuple)
        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
        print '<font size="2" face="arial">'
	print '<BR>'
	print '<TABLE><TR><TH>Minus 3 hours:</TH><TH>Minus 2 hours:</TH><TH>Minus 1 hour:</TH><TH>Current:</TH></TR>'
	print '<TR>'
	mk_row_data(orig_secs, "sfc", ".gif", "/icons/temp_thumb.gif", "Surface Temps Chart")
	print '</TR>'
	print '</TABLE>'

	print '<MULTICOL COLS="3">'
#	mk_data_link(dir_format+data_format+'.txt' , "/icons/NWS_thumb.gif" , "NWS Text Data")
	mk_data_link(dir_format+'temp'+data_format+'.gif' , "/icons/temp_thumb.gif" , "Surface Temps Chart")
	mk_data_link(dir_format+'sfc'+data_format+'.gif' , "/icons/sfc_thumb.gif" , "Surface Chart")
	mk_data_link(dir_format+'dew'+data_format+'.gif' , "/icons/temp_thumb.gif" , "Surface Dewpoints")
	mk_data_link(dir_format+'NAT'+data_format+'.gif' , "/icons/NAT_thumb.gif" , "National Radar Summary")
	mk_data_link(dir_format+'cape'+data_format+'.gif' , "/icons/cape_thumb.gif" , "CAPE")
	mk_data_link(dir_format+'tpw'+data_format+'.gif' , "/icons/tpw_thumb.gif" , "Precipitable Water")
	mk_data_link(dir_format+'li'+data_format+'.gif' , "/icons/li_thumb.gif" , "Lifted Index")
	mk_data_link(dir_format+'moist'+data_format+'.gif' , "/icons/moist_thumb.gif" , "Moisture Divergence")
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


