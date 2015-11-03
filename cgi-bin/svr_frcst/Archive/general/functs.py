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

def mk_data(gmt_tuple):
        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
        print '<font size="2" face="arial">'
	print '<TABLE ALIGN="CENTER" WIDTH="100%"><TR VALIGN="TOP">'

	if os.path.isfile('/home/httpd/html/'+dir_format+data_format+'.txt'):
	        print '<TH><a href="'+dir_format+data_format+'.txt">'
		print '<img src="/icons/NWS_thumb.gif" align="center" VSPACE="5"><BR>Weather Service Text</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'temp'+data_format+'.gif'):
	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'temp'+data_format+'.gif">'
		print '<img src="/icons/temp_thumb.gif" align="center" VSPACE="5"><BR>Surface Temps Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'sfc'+data_format+'.gif'):
        	print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'sfc'+data_format+'.gif">'
		print '<img src="/icons/sfc_thumb.gif" align="center" VSPACE="5"><BR>Surface Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'dew'+data_format+'.gif'):
	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'dew'+data_format+'.gif">'
		print '<img src="/icons/temp_thumb.gif" align="center" VSPACE="5"><BR>Surface Dew Point Chart</a></TH>'

	if os.path.isfile('/home/httpd/html/'+dir_format+'NAT'+data_format+'.gif'):
	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'NAT'+data_format+'.gif">'
		print '<img src="/icons/NAT_thumb.gif" align="center" VSPACE="5"><BR>NationalRadar</a></TH>'

#        print '</font></TR><TR valign="TOP">'

#	if os.path.isfile('/home/httpd/html/'+dir_format+'cape'+data_format+'.gif'):
#	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'cape'+data_format+'.gif">'
#		print '<img src="/icons/cape_thumb.gif" align="center" VSPACE="5"><BR>CAPE</a></TH>'
#
#	if os.path.isfile('/home/httpd/html/'+dir_format+'tpw'+data_format+'.gif'):
#	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'tpw'+data_format+'.gif">'
#		print '<img src="/icons/tpw_thumb.gif" align="center" VSPACE="5"><BR>Precipitale Water</a></TH>'
#
#	if os.path.isfile('/home/httpd/html/'+dir_format+'li'+data_format+'.gif'):
#	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'li'+data_format+'.gif">'
#		print '<img src="/icons/li_thumb.gif" align="center" VSPACE="5"><BR>Lifted Index</a></TH>'
#
#	if os.path.isfile('/home/httpd/html/'+dir_format+'moist'+data_format+'.gif'):
#	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'moist'+data_format+'.gif">'
#		print '<img src="/icons/moist_thumb.gif" align="center" VSPACE="5"><BR>Moisture Divergence</a></TH>'
#
#	if os.path.isfile('/home/httpd/html/'+dir_format+'light'+data_format+'.gif'):
#	        print '<TH><a href="/cgi-bin/svr_frcst/general/picture.py?file='+dir_format+'light'+data_format+'.gif">'
#		print '<img src="/icons/light_thumb.gif" align="center" VSPACE="5"><BR>Lightning Data</a></TH>'
	
	print '</TR></TABLE>'

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


def check_key(key, secs, refer):
	check_time = admindb.query("SELECT last_time from sessions WHERE key = '"+key+"' ").getresult()

	if float(check_time[0][0]) >= secs:
		been_here = 1	# They have been hear before

	else:
		update = admindb.query("UPDATE sessions set last_time = '"+str(secs)+"' WHERE key = '"+str(key)+"' ")
		check_ques = admindb.query("SELECT ticks from questions WHERE ticks = '"+str(int(secs))+"' ").getresult()
#		print check_time[0][0],  secs
		if len(check_ques) > 0:
			mk_question(key, secs, refer)
		update = admindb.query("UPDATE sessions SET last_time = "+str(secs)+" WHERE key = '"+str(key)+"' ")


def mk_question(key, secs, refer):
	query = admindb.query("SELECT * from questions WHERE ticks = '"+str(secs)+"' ").getresult()

	local = time.localtime(float(secs))
        anskey = "ans"+str(int(time.strftime("%I", local)))+string.lower(time.strftime("%p", local))
	test = admindb.query("SELECT "+anskey+" from sessions WHERE key = '"+str(key)+"' ").getresult()	

	if len(test[0][0]) > 0:
		temper = 'Allready done'
	else:
		ticks = query[0][0]
		question = query[0][1]
		type = query[0][2]
		if type == "M":
			optiona = query[0][3]
			optionb = query[0][4]	
			optionc = query[0][5]
			optiond = query[0][6]
			mk_multiple_choice(key, ticks, question, optiona,  optionb,  optionc,  optiond, refer)
		else:
			mk_text(key, ticks, question, refer)
		sys.exit(0)

def mk_multiple_choice(key, ticks, question, optiona,  optionb,  optionc,  optiond, refer):
	print '<TABLE bgcolor="WHITE" width="100%">'
	print '<TR><TD>'
	print "<H3>You get a Bonus Question !!</H3>"
	print '<form method="POST" action="question.py">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="secs" value="'+str(ticks)+'">'
	print '<input type="hidden" name="refer" value="'+refer+'">'

	print '<H3>Answer this Question:</H3>'
	print '<PRE>	'+question+'</PRE>'

	print '<BR><input type="radio" name="option" value="A">'
	print optiona

	print '<BR><input type="radio" name="option" value="B">'
	print optionb

	if optiona == "Yes" and optionb == "No":
		print '<BR>'
	else:
		print '<BR><input type="radio" name="option" value="C">'
		print optionc

		print '<BR><input type="radio" name="option" value="D">'
		print optiond


	print '<BR><BR><input type="submit">'

	print '</TD></TR></TABLE>'

def mk_text(key, ticks, question, refer):
	print '<TABLE bgcolor="WHITE" width="100%">'
	print '<TR><TD>'
	print "<H3>You get a Bonus Question !!</H3>"
	print '<form method="POST" action="question.py">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="secs" value="'+str(ticks)+'">'
	print '<input type="hidden" name="refer" value="'+refer+'">'

	print '<H3>Answer this Question:</H3>'
	print '<PRE>	'+question+'</PRE>'

	print '<TEXTAREA name="text" cols="80" rows="10"></TEXTAREA>'

	print '<BR><BR><input type="submit">'

	print '</TD></TR></TABLE>'

