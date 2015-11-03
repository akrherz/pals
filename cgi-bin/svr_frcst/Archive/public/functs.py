#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann
# UPDATED 6-4-99: Added picts into the data links
# UPDATED 6-4-99: Changed mk_top to a new style
# UPDATED 7-5-99: Changed functs in order to conform with new style
# UPDATED 7-14-99: Cleaned house and code
	
import time, os

picturepy = "/cgi-bin/svr_frcst/base/picture.py"

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

def mk_data(gmt_tuple):
        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
        print '<font size="2" face="arial">'
	print '<TABLE ALIGN="CENTER" WIDTH="100%"><TR VALIGN="TOP">'

	if os.path.isfile('/home/httpd/html/'+dir_format+data_format+'.txt'):
	        print '<TH><a href="'+dir_format+data_format+'.txt">'
		print '<img src="/icons/NWS_thumb.gif" align="center" VSPACE="5"><BR>Weather Service Text</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'temp'+data_format+'.gif'):
	        print '<TH><a href="'+picturepy+'?file='+dir_format+'temp'+data_format+'.gif">'
		print '<img src="/icons/temp_thumb.gif" align="center" VSPACE="5"><BR>Surface Temps Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'sfc'+data_format+'.gif'):
        	print '<TH><a href="'+picturepy+'?file='+dir_format+'sfc'+data_format+'.gif">'
		print '<img src="/icons/sfc_thumb.gif" align="center" VSPACE="5"><BR>Surface Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'dew'+data_format+'.gif'):
	        print '<TH><a href="'+picturepy+'?file='+dir_format+'dew'+data_format+'.gif">'
		print '<img src="/icons/temp_thumb.gif" align="center" VSPACE="5"><BR>Surface Dew Point Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'NAT'+data_format+'.gif'):
	        print '<TH><a href="'+picturepy+'?file='+dir_format+'NAT'+data_format+'.gif">'
		print '<img src="/icons/NAT_thumb.gif" align="center" VSPACE="5"><BR>NationalRadar</a></TH>'
        print '</font></TR></table>'

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


