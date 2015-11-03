#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import time, os, sys, time, regsub, string, style, pg, cgi, question, svrFrcst

#scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.adv/"
scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.adv-cvs/"
usersTable = "users"


form = cgi.FormContent()
if not form.has_key("case_num"):
	style.SendError("No case number was supplied to this script")
if not form.has_key("className"):
	style.SendError("No class name specified")
if not form.has_key("key"):
	style.SendError("I don't know who you are!")

case_num = form["case_num"][0]  
className = form["className"][0]
key = form["key"][0]

mydb = pg.connect('svr_frcst')
ldb = pg.connect('svr_'+className)


def getQuestions(ldb, key, secs, className, interval):
	storAge = "s"+str(key)
	checker = ldb.query("SELECT * from "+storAge+" ").getresult()

	update = ldb.query("SELECT last_time, ans_ques from "+usersTable+" WHERE userid = '"+str(key)+"' "). getresult()
#        print update, secs, interval
        if ( int(float( update[0][0] )) < secs or (int(interval) == 1 and len(checker) == 0) )and update[0][1] == 't':
                return 1                                # WE have not been here
        else:
                return 0



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
				<option value="/svr_frcst/help/animationhelp.html">Help with Annimations
			</select>
			</form>


		</TD></TR>
	</TABLE>
	"""
def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def create_time(year, month, day, hour, minute):
        time_tuple = (year, month, day, hour, minute, 0, 0, 0, 0)       # Form the orig tuple
        return time.mktime(time_tuple)          # This is time_tuple in ticks


def mk_data_link2(file, string_txt, i, hour_time):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/general/picture2.py?file='+file+'" target="_new"> '+hour_time+'</a><BR>'
	else:
		print "- -"

def mk_data_link(file, string_txt):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<a href="/cgi-bin/svr_frcst/general/picture2.py?file='+file+'" target="_new">'+string_txt+'</a><BR>'

def mk_row_data(orig_secs, prefix, suffix, title, multipler):
	print '<TH>'+title+'</TH>'
	for i in range(5):
		print '<TD align="center">'
		this_secs = orig_secs - i*3600*multipler
		this_tuple = time.localtime(this_secs)
		data_format = time.strftime("%y%m%d%H", this_tuple)
		hour_time = time.strftime("%H Z", this_tuple)
		dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
		mk_data_link2(dir_format+prefix+data_format+suffix , title, str(i), hour_time)
		print '</TD>'


def mk_data(gmt_tuple, multipler):
	orig_secs = time.mktime(gmt_tuple)

	currentHour = gmt_tuple[3]

        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)

	print '<BR>'
	print '<img src="/icons/wxdata.gif"><BR>'
	print '<font color="#0854a8"><H3>Hourly Data:</H3></font>'
	print '<TABLE width="100%" border="0">'
	print '<TR><TH></TH><TH>Current:</TH><TH>- '+str(1*multipler)+' hr:</TH><TH>- '+str(2*multipler)+' hrs:</TH><TH>- '+str(3*multipler)+' hrs:</TH><TH>- '+str(4*multipler)+' hrs:</TH></TR>'
	print '<TR>'
	mk_row_data(orig_secs, "sfc", ".gif", "Surface Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "temp", ".gif", "Surface Temps Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "dew", ".gif", "Surface Dew Point Chart", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "moist", ".gif", "Moisture Divergence", multipler)
	print '</TR><TR>'
	mk_row_data(orig_secs, "nowrad", ".gif", "National Radar Summary", multipler)
	print '</TR>'
	print '</TABLE>'

	print '<font color="#0854a8"><H3>Other Data for This Hour:</H3></font>'
	print '<MULTICOL COLS="3">'
#	mk_data_link(dir_format+data_format+'.txt' , "NWS Text Data")
	if currentHour == 12:
		mk_data_link(dir_format+'cape'+data_format+'.gif' ,  "ETA Forecasted CAPE")
	else:
		mk_data_link(dir_format+'cape'+data_format+'.gif' ,  "Satellite Derived CAPE")
	mk_data_link(dir_format+'tpw'+data_format+'.gif' ,  "Precipitable Water")
	mk_data_link(dir_format+'li'+data_format+'.gif' ,  "Lifted Index")
	mk_data_link(dir_format+'light'+data_format+'.gif' ,  "Lightning Data")
	mk_data_link(dir_format+'MPX'+data_format+'.gif' , "Minneapolis Radar Reflectivity")
	mk_data_link(dir_format+'MPXVEL'+data_format+'.gif' , "Minneapolis Velocity")
	mk_data_link(dir_format+'DMX'+data_format+'.gif' , "Des Moines Radar Reflectivity")
	mk_data_link(dir_format+'sat'+data_format+'.gif' , "Satellite Image")
	mk_data_link(dir_format+'sat'+data_format+'.jpg' , "Alt Satellite Image")

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


	print '<font color="#0854a8"><H3>Most Recent Data:</H3></font>'
	print '<TABLE><TR><TD>'
	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>Upper Air Data valid @ '+timeTag+' </B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'

	mk_data_link(dir_format+'850mb'+data_format+'.gif' , "850 MB")
	mk_data_link(dir_format+'700mb'+data_format+'.gif' , "700 MB")
	mk_data_link(dir_format+'500VORT'+data_format+'.gif' , "500 MB Vorticity")
	mk_data_link(dir_format+'500mb'+data_format+'.gif' , "500 MB")
	mk_data_link(dir_format+'300mb'+data_format+'.gif' , "300 MB")
	mk_data_link(dir_format+'200mb'+data_format+'.gif' , "200 MB")

	style.bot_box()

	print '</TD><TD>'

	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>Profiler Data valid @ '+timeTag+' </B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'

	mk_data_link(dir_format+'1000m'+data_format+'.gif' , "1000 m Profiler")
	mk_data_link(dir_format+'3000m'+data_format+'.gif' , "3000 m Profiler")
	mk_data_link(dir_format+'5600m'+data_format+'.gif' , "5600 m Profiler")
	mk_data_link(dir_format+'9000m'+data_format+'.gif' , "9000 m Profiler")

	style.bot_box()

	print '</TD><TD>'

	print '<TABLE align="CENTER" bgcolor="#EEEEEE" cellpadding="2" border="0">'
	print '<TR><TD>'
	print '<TABLE bgcolor="#EEEEEE" border="0" cellpadding="2">'
	print '<TR><TD><font color="black" size="4" face="ARIAL"><B>ETA 12-hr forecast, from '+timeTag+' run</B></font></TD></TR>'
	print '<TR><TD bgcolor="white" align="center">'
	
	mk_data_link(dir_format+'etaTEMP'+data_format+'F12.gif' , "12 HR ETA Model Temperatures")
	mk_data_link(dir_format+'etaPREC'+data_format+'F12.gif' ,"12 HR ETA Precipation")
	mk_data_link(dir_format+'etaTHK'+data_format+'F12.gif' , "12 HR ETA Thickness and Pressure")
	mk_data_link(dir_format+'etaVORT'+data_format+'F12.gif' , "12 HR ETA Vorticity")
	mk_data_link(dir_format+'etaHEL'+data_format+'F12.gif' , "12 HR ETA Helicity")

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

