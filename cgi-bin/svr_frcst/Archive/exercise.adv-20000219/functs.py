#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import time, os, sys, time, regsub, string, style

scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.adv"
usersTable = "users"

def getQuestions(ldb, key, secs, className, interval):
	storAge = "s"+str(key)
	checker = ldb.query("SELECT * from "+storAge+" ").getresult()

	update = ldb.query("SELECT last_time, ans_ques from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
#        print update, secs, interval
        if ( int(float( update[0][0] )) < secs or (int(interval) == 1 and len(checker) == 0) )and update[0][1] == 't':
                return 1                                # WE have not been here
        else:
                return 0


def svr_top(secs_tuple, secs = 0):
	if secs != 0:
		if secs_tuple[-1] == 1:
	                secs = int(secs) - 5*3600
	        else:
	                secs = int(secs) - 6*3600
		now_tuple = time.localtime( secs )
		date_str = time.strftime("%B %d, %Y", now_tuple)
		time_str = time.strftime("%I:%M %p [%Z]", now_tuple)+'&nbsp;&nbsp; ( '+str(secs_tuple[3])+' Z )'
#		dateStr = date_str+'&nbsp;&nbsp;'+time_str+'&nbsp;&nbsp; ( '+str(secs_tuple[3])+' Z )'
	else:
		date_str = "Welcome!!"
		time_str = ""

	style.header("Severe Weather Forecasting Exercise", "white")
	
	print """
	<TABLE width="100%">
	<TR>
        <TD>
                <img src="/icons/svrTop.gif">
        </TD>
        <TD>
                <TABLE width="100%">
                <TR><TD background="/icons/sidebg.gif" align="CENTER" NOWRAP>
                        <font size="+3" color="white">Current Date & Time:</font>
                </TD></TR>
                <TR><TD bgcolor="white" align="CENTER" NOWRAP>
        """
	print '<font color="blue" size="+2">'+date_str+'</font><BR>'
        print '<font color="red" size="+2">'+time_str+'</font>'
	print """
                </TD></TR></TABLE>
        </TD></TR></TABLE>
	"""


#	print """
#	<TABLE WIDTH="100%" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">
#        <TR>
#	<TD bgcolor="#EEEEEE" align="right">
#		<font color="black">Partnerships to Advance Learning in Science</font>
#	</TD></TR>
#        <TR bgcolor="#0854a8">
#	<TD>
#		<img src="/icons/svr_frcst-top.gif" HSPACE="0" VSPACE="0" BORDER="0">
#	</TD></TR>
#	<TR bgcolor="yellow">
#	<TD align="center" NOWRAP valign="CENTER">
#		<h4><font color="RED">Current Exercise Date & Time:</font>&nbsp;&nbsp;
#        """
	
#	print dateStr
#	print '</H4></TD></TR></TABLE>'

def svr_bot(className = "test"):
	print """<BR clear="all"><BR>
	<TABLE WIDTH="100%" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">
        <TR>
        <TD bgcolor="#EEEEEE" align="right">                                                      
	© 2000, PALS, all rights reserved
	</TD></TR>
	<TR><TD bgcolor="#0854a8">
	<font color="#0854a8">Space Holder</font>
	</TD></TR>
	<TR><TD bgcolor="yellow">
	<a href="/">PALS Homepage</a> | <a href="/svr_frcst/index.html">Sx Frcst Exercise Homepage</a>
	</TD></TR></TABLE>"""	

def db_comments_417(now, now_tuple, col_name, sec_head, className):
        now = str(int(float(now)))
        table_str = time.strftime("annote_%Y", now_tuple)
	table_str2 = "annote"

	print '<BR clear="all">'
	if col_name == "comments":
	        print '<img src="/icons/comments.gif"><BR>'
	else:
	        print '<img src="/icons/analysis.gif"><BR>'

        try:
		import pg
		svrdb = pg.connect('svr_frcst')
		my417db = pg.connect('svr_'+className)
                select = svrdb.query("SELECT "+col_name+" from "+table_str+" where ztime = '"+str(int(float(now)))+"'").getresult() 
                select2 = my417db.query("SELECT "+col_name+" from "+table_str2+" where ztime = '"+str(int(float(now)))+"'").getresult() 

        except ValueError:
                print "None available for this hour..."
                select = [(" "),(" ")]
                select2 = ""

        if len(select2) > 0:
                select = select2

        if len(select) == 0:
                print "None available for this hour..."
        else:
                print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '<BR><BR>'


def mk_help():
	# This generates the help table that appears on many pages
	# CALLING:
	#	It is just a print function, so it needs nothing in...

        print """
        <TABLE border="0" cellpadding="2" align="right">
	<TR>
		<TD bgcolor="black" rowspan="2"><BR></TD>
		<TD align="CENTER" bgcolor="#EEEEEE">
			<font color="black"><B>Help Topics:</B></font></TD></TR>
	<TR bgcolor="WHITE">
		<TD NOWRAP>
		<form method="POST" action=" " name="weather">
                        <SELECT name="area" onChange="location=this.form.area.options[this.form.area.selectedIndex].value">
                                <option value="/svr_frcst/help/z.html">What are Z, UTC, GMT times?
                                <option value="/svr_frcst/help/text.html">Watches and Warnings Data
                                <option value="/svr_frcst/help/temp.html">Surface Temperature Map
                                <option value="/svr_frcst/help/sfcmap.html">Surface Map
                                <option value="/svr_frcst/help/dewp.html">Surface Dew Points Map
                                <option value="/svr_frcst/help/radar.html">Radar
                                <option value="/svr_frcst/help/eta.html">ETA Forecast Maps
                        </select>
                        </form>
		</TD></TR>
	</TABLE>
	"""
#			<LI><a href="/svr_frcst/help/z.html">What are Z, UTC, GMT times?</a></LI>
#			<LI><a href="/svr_frcst/help/text.html">Watches and Warnings Data</a></LI>
#			<LI><a href="/svr_frcst/help/temp.html">Surface Temperature Map</a></LI>
#			<LI><a href="/svr_frcst/help/sfcmap.html">Surface Map</a></LI>
#			<LI><a href="/svr_frcst/help/dewp.html">Surface Dew Points Map</a></LI>
#			<LI><a href="/svr_frcst/help/radar.html">Radar</a></LI>
#			<LI><a href="/svr_frcst/help/eta.html">ETA Forecast Maps</a></LI>


def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def create_time(year, month, day, hour, minute):
        time_tuple = (year, month, day, hour, minute, 0, 0, 0, 0)       # Form the orig tuple
        return time.mktime(time_tuple)          # This is time_tuple in ticks


def mk_data_link2(file, thumbnail, string_txt, i, hour_time):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/general/picture2.py?file='+file+'" target="_new"> '+hour_time+'</a><BR>'
	else:
		print "- -"

def mk_data_link(file, thumbnail, string_txt):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/general/picture2.py?file='+file+'" target="_new">'+string_txt+'</a><BR>'

def mk_row_data(orig_secs, prefix, suffix, icon_ref, title, multipler):
	print '<TH>'+title+'</TH>'
	for i in range(5):
		print '<TD align="center">'
		this_secs = orig_secs - i*3600*multipler
		this_tuple = time.localtime(this_secs)
		data_format = time.strftime("%y%m%d%H", this_tuple)
		hour_time = time.strftime("%H Z", this_tuple)
		dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
		mk_data_link2(dir_format+prefix+data_format+suffix , icon_ref , title, str(i), hour_time)
		print '</TD>'


def mk_data(gmt_tuple, multipler):
	orig_secs = time.mktime(gmt_tuple)

	currentHour = gmt_tuple[3]

        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)

	print '<BR>'
	print '<img src="/icons/wxdata.gif"><BR>'
	print '<TABLE width="100%" border="0">'
	print '<TR><TH></TH><TH>Current:</TH><TH>- '+str(1*multipler)+' hr:</TH><TH>- '+str(2*multipler)+' hrs:</TH><TH>- '+str(3*multipler)+' hrs:</TH><TH>- '+str(4*multipler)+' hrs:</TH></TR>'
	print '<TR>'
	mk_row_data(orig_secs, "sfc", ".gif", "/icons/sfc_thumb.gif", "Surface Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "temp", ".gif", "/icons/temp_thumb.gif", "Surface Temps Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "dew", ".gif", "/icons/temp_thumb.gif", "Surface Dew Point Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "moist", ".gif", "/icons/moist_thumb.gif", "Moisture Divergence", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "nowrad", ".gif", "/icons/NAT_thumb.gif", "National Radar Summary", multipler)
	print '</TR>'
	print '</TABLE>'

	print '<BR><b>This Hour Only Data:</b><BR>'
	print '<MULTICOL COLS="3">'
#	mk_data_link(dir_format+data_format+'.txt' , "/icons/NWS_thumb.gif" , "NWS Text Data")
	if currentHour == 12:
		mk_data_link(dir_format+'cape'+data_format+'.gif' , "/icons/cape_thumb.gif" , "ETA Forecasted CAPE")
	else:
		mk_data_link(dir_format+'cape'+data_format+'.gif' , "/icons/cape_thumb.gif" , "Satellite Derived CAPE")
	mk_data_link(dir_format+'tpw'+data_format+'.gif' , "/icons/tpw_thumb.gif" , "Precipitable Water")
	mk_data_link(dir_format+'li'+data_format+'.gif' , "/icons/li_thumb.gif" , "Lifted Index")
	mk_data_link(dir_format+'light'+data_format+'.gif' , "/icons/light_thumb.gif" , "Lightning Data")
	mk_data_link(dir_format+'MPX'+data_format+'.gif' , "/icons/light_thumb.gif" , "Minneapolis Radar Reflectivity")
	mk_data_link(dir_format+'MPXVEL'+data_format+'.gif' , "/icons/light_thumb.gif" , "Minneapolis Velocity")
	mk_data_link(dir_format+'DMX'+data_format+'.gif' , "/icons/light_thumb.gif" , "Des Moines Radar Reflectivity")
	mk_data_link(dir_format+'sat'+data_format+'.gif' , "/icons/light_thumb.gif" , "Satellite Image")
	mk_data_link(dir_format+'sat'+data_format+'.jpg' , "/icons/light_thumb.gif" , "Alt Satellite Image")

	print '</MULTICOL>'

	if currentHour > 12:
		timeTag = "12 Z"
	        data_format = time.strftime("%y%m%d12", gmt_tuple)
	elif currentHour < 12 and currentHour > 0:
		timeTag = "0 Z"
	        data_format = time.strftime("%y%m%d00", gmt_tuple)
	elif currentHour == 0:
		timeTag = "0 Z"
	elif currentHour == 12:
		timeTag = "12 Z"


	print '<TABLE><TR><TD>'

	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>Upper Air Data valid @ '+timeTag+' </B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'

	mk_data_link(dir_format+'850mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "850 MB")
	mk_data_link(dir_format+'700mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "700 MB")
	mk_data_link(dir_format+'500VORT'+data_format+'.gif' , "/icons/temp_thumb.gif" , "500 MB Vorticity")
	mk_data_link(dir_format+'500mb'+data_format+'.gif' , "/icons/temp_thumb.gif" , "500 MB")
	mk_data_link(dir_format+'300mb'+data_format+'.gif' , "/icons/light_thumb.gif" , "300 MB")
	mk_data_link(dir_format+'200mb'+data_format+'.gif' , "/icons/light_thumb.gif" , "200 MB")

	style.bot_box()

	print '</TD><TD>'

	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>Profiler Data valid @ '+timeTag+' </B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'

	mk_data_link(dir_format+'1000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "1000 m Profiler")
	mk_data_link(dir_format+'3000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "3000 m Profiler")
	mk_data_link(dir_format+'5600m'+data_format+'.gif' , "/icons/light_thumb.gif" , "5600 m Profiler")
	mk_data_link(dir_format+'9000m'+data_format+'.gif' , "/icons/light_thumb.gif" , "9000 m Profiler")

	style.bot_box()

	print '</TD><TD>'

	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>ETA 12-hr forecast, from '+timeTag+' run</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'
	
	mk_data_link(dir_format+'etaTEMP'+data_format+'F12.gif' , "/icons/light_thumb.gif" , "12 HR ETA Model Temperatures")
	mk_data_link(dir_format+'etaPREC'+data_format+'F12.gif' , "/icons/light_thumb.gif" , "12 HR ETA Precipation")
	mk_data_link(dir_format+'etaTHK'+data_format+'F12.gif' , "/icons/light_thumb.gif" , "12 HR ETA Thickness and Pressure")
	mk_data_link(dir_format+'etaVORT'+data_format+'F12.gif' , "/icons/light_thumb.gif" , "12 HR ETA Vorticity")
	mk_data_link(dir_format+'etaHEL'+data_format+'F12.gif' , "/icons/light_thumb.gif" , "12 HR ETA Helicity")

	style.bot_box()

	print '</TD></TR></TABLE>'

def mk_top(now_tuple):
        date_str = time.strftime("%B %d, %Y", now_tuple)
        time_str = time.strftime("%I:%M %p [%Z]", now_tuple)

	print '<font color="RED">Current Date & Time:</font>&nbsp;&nbsp;'
	print date_str+'&nbsp;&nbsp;'+time_str
	
	
def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'

