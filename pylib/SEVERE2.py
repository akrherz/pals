#!/usr/local/bin/python
# This is the global functions file for the forecasting exercise
# Daryl Herzmann 7 June 2000
# 25 Mar 2004	Fix a bug with profiler interaction

import mx.DateTime, time, os
	
def setupPage(title="Severe Wx Forecasting Exercise"):
	print 'Content-Type: text/html \n\n'
	
	print "<HTML>\n<HEAD>\n\t<TITLE>"+title+"</TITLE>\n"

	print """
	<SCRIPT LANGUAGE='JavaScript'>
	<!--
	// LaunchURL main function

	function launchURL(url,name,x,y) {
		window.name = "_wxdata";
		var ItsTheWindow;
		ItsTheWindow = window.open(url, name,
		"status=no,height="+y+",width="+x+",scrollbars=yes,resizable=yes,toolbar=no");
	}

	//-->
	</script>
	</HEAD>
	<body bgcolor="#ffffff" link="blue">
	<TABLE width="100%">
                <TR><TD background="/icons/sidebg.gif" align="CENTER" NOWRAP>
                        <font size="+3" color="white"><B>Severe Weather Forecasting Activity</b></font>
                </TD></TR>
	<TR><TD>
	"""
	
def printTime(thisDate = 0):
	import mx.DateTime, time
	
	if thisDate != 0:
		nowDate = mx.DateTime.ISO.ParseDateTimeGMT( thisDate )
		nowTuple = nowDate.tuple()
		localDate = mx.DateTime.gm2local(nowDate)
		localTuple = localDate.tuple()
#		dateStr = time.strftime("%B %d, %Y", localTuple )
#		timeStr = time.strftime("%I:%M %p [%Z]", localTuple )+'&nbsp;&nbsp; ( '+str(nowTuple[3])+' Z )'
		gmtStr = nowDate.strftime("%d %B %Y %H:%M UTC")
		localStr = localDate.strftime("%d %B %Y %I:%M %p")

		dir_format = nowDate.strftime("/archivewx/data/%Y_%m_%d/")
		print '<BASE HREF="http://www.pals.iastate.edu'+dir_format+'">'

	else:
		dateStr = " -- "
		timeStr = " -- "

#	print '<H2><CENTER><FONT COLOR="#000000">C</FONT><FONT SIZE="+1">urrent</FONT> <FONT COLOR="#000000">T</FONT><FONT SIZE="+1">ime</FONT>:'
#	print '<FONT COLOR="#b0020f">'+timeStr+'</FONT>'
#	print '&nbsp; &nbsp; &nbsp;'
#	print '<FONT COLOR="#000000">D</FONT><FONT SIZE="+1">ate</FONT>:'
#	print '<FONT COLOR="#b0020f">'+dateStr+'</FONT></CENTER></H2><BR>'


	print """
	<TABLE width="100%" border=0 cellpadding=3>
	<TR>
		<TD align="center">

		<TABLE bgcolor="#EEEEEE" cellspacing="0" border="0" cellpadding="1">
		<caption><font size=+1 color="black">Current UTC Time:</font></caption>
		<TR><TD>
			<TABLE bgcolor="black" cellspacing="0" border="0" cellpadding="3">
			<TR><TD>
				<font color="#7fff00" size=+2><B>"""
	print gmtStr
	print """</B></font>
			</TD></TR></TABLE>
		</TD></TR></TABLE>

		</TD>
        
		<TD align="center">
		<TABLE bgcolor="#EEEEEE" cellspacing="0" border="0" cellpadding="1">
		<caption><font size=+1 color="black">Current Central Time:</font></caption>
		<TR><TD>
			<TABLE bgcolor="black" cellspacing="0" border="0" cellpadding="3">
			<TR><TD>
				<font color="#7fff00" size=+2><B>"""
	print localStr
	print """</B></font>
			</TD></TR></TABLE>
		</TD></TR></TABLE>

		</TD>
	</TR>
	</TABLE>"""

	
	
def finishPage(version = 'null', className = 'null'):
	print """       
	</TD></TR>
                <TR><TD background="/icons/sidebg.gif" align="right" NOWRAP>
                        <font size="+1" color="white"><B>&copy; 2000 PALS</b></font>
		</TD></TR>
		<TR><TD align="right" NOWRAP>
			<a href="http://www.pals.iastate.edu">PALS Home</a> &nbsp; | &nbsp; 
			<a href="http://www.pals.iastate.edu/svr_frcst">Severe Wx Exercise</a> &nbsp; | &nbsp;"""
	if className == 'null' and version == 'null':
		print ""
	elif className == 'null':
		print '<a href="http://www.pals.iastate.edu/cgi-bin/severe2/'+version+'/list.py">Different Case</a> &nbsp; | &nbsp;'
	else:
		print '<a href="http://www.pals.iastate.edu/cgi-bin/severe2/'+version+'/list.py?className='+className+'">Different Case</a> &nbsp; | &nbsp;'
	print """
		</TD></TR>
	</TABLE>
	"""
	
def makeHelp():
	print """
        <TABLE border="0" cellpadding="2" align="right">
             
        <TR>
                <TD NOWRAP>
                        <font size="+1" face="GEORGIA">
                        <form method="POST" action=" " name="weather">
                        <SELECT name="area" onChange="location=this.form.area.options[this.form.area.selectedIndex].value">
						<option value="">Help Topics
						<option value="/svr_frcst/help/z.html">What are Z, UTC, GMT times?
						<option value="/svr_frcst/help/text.html">Watches and Warnings Data
						<option value="/svr_frcst/help/temp.html">Surface Temperature Map
						<option value="/svr_frcst/help/sfcmap.html">Surface Map
						<option value="/svr_frcst/help/dewp.html">Surface Dew Points Map
						<option value="/svr_frcst/help/radar.html">Radar
						<option value="/svr_frcst/help/skewt.html">Skew T 
						<option value="/svr_frcst/help/eta.html">ETA Forecast Maps
						<option value="/svr_frcst/help/animationhelp.html">Help with Annimations
                        </select>
                        </font>
                        </form>
                </TD></TR>
        </TABLE>
        """
        
def listAllCases(selected = 'null'):
	import pg, mx.DateTime
	advdb = pg.connect('severe2', 'localhost', 5432)
	
	cases = advdb.query("SELECT * from cases order by starttime").dictresult()

	print '<SELECT name="caseNum" size="10">'
	for i in range(len( cases )):
		thisCase = cases[i]["casenum"]
		thisStart  = cases[i]["starttime"]
		thisEnd   = cases[i]["endtime"]

		startDate = mx.DateTime.ISO.ParseDateTimeGMT(thisStart)
		print '<option value="'+thisCase+'">'+thisCase+' -- '+startDate.strftime("%d %B %Y")
	print '</SELECT>'

def listGoodCases(selected = 'null'):
	import pg, mx.DateTime
	advdb = pg.connect('severe2_adv', 'localhost', 5432)
	basedb = pg.connect('severe2', 'localhost', 5432)
	
	cases1 = advdb.query("SELECT * from basecases").dictresult()

	print '<SELECT name="caseNum" size="10">'
	for i in range(len( cases1 )):
		cases = basedb.query("SELECT * from cases WHERE casenum = '"+cases1[i]['casenum']+"' ").dictresult()
		thisCase = cases[0]["casenum"]
		thisStart  = cases[0]["starttime"]
		thisEnd   = cases[0]["endtime"]

		startDate = mx.DateTime.ISO.ParseDateTimeGMT(thisStart)
		print '<option value="'+thisCase+'">'+thisCase+' -- '+startDate.strftime("%d %B %Y")
	print '</SELECT>'
	
def listHours(caseNum):
	import pg, mx.DateTime, time
	advdb = pg.connect('severe2', 'localhost', 5432)
	advdb.query("SET TIME ZONE 'GMT' ")
	cases = advdb.query("select date_part('hour', age(endtime, starttime)), starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()
	starttime = cases[0][1] 
	endtime = cases[0][2]

	startDate = mx.DateTime.ISO.ParseDateTime(starttime)
	startSecs = startDate.gmticks()

	endDate = mx.DateTime.ISO.ParseDateTime(endtime)
	endSecs = endDate.gmticks()

	multi = 1
        if caseNum[0] == "w":
                multi = 3

        now = startSecs

        print '<SELECT name="zticks" size="10">'
        while ( now < endSecs ):
                thisTuple = time.gmtime(now)
                print '<option value="'+str(int(float(now)))+'">'+time.strftime("%b %d, %Y %HZ", thisTuple)
                now = now + multi*3600
        print '</SELECT>'

def makeData(nowDate, userKey, caseNum = "s12" , multipler = 1, version = 'a'):

	nowDate = mx.DateTime.ISO.ParseDateTimeGMT(nowDate)
	gmt_tuple = nowDate.tuple()
	orig_secs = nowDate.ticks()

	currentHour = gmt_tuple[3]

	data_format = time.strftime("%y%m%d%H", gmt_tuple)
	dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
	biFormat = data_format

	if currentHour > 12:
		timeTag = "12 Z"
		biFormat = time.strftime("%y%m%d12", gmt_tuple)
	elif currentHour < 12 and currentHour > 0:
		timeTag = "0 Z"
		biFormat = time.strftime("%y%m%d00", gmt_tuple)
	elif currentHour == 0:
		timeTag = "0 Z"
	elif currentHour == 12:
		timeTag = "12 Z"

	print """
	<P><img src="/icons/ball.red.gif" align="bottom"><B><font color="#a0522d" size=+2>Recent Weather Data:</font></B>

	<!-- Begin Section for Upper Air Data -->
	<BR>
	<table BORDER=0 CELLPADDING=1 CELLSPACING=0 ROWSPACING=0 WIDTH="100%" bgcolor="WHITE">
	<tr>
		<th ALIGN=CENTER VALIGN=CENTER COLSPAN="7" NOWRAP bgcolor="#778899">
	"""
	print '<font color="white">Upper Air Data valid @ '+timeTag+'</font></th>'
	print """
		<td ROWSPAN="4" bgcolor="white"><img src="/icons/blank.gif" width="1"></td>
		<th ALIGN=CENTER VALIGN=CENTER COLSPAN="7" NOWRAP bgcolor="#778899">
	"""
	if version != 'b':
		print '<font color="white">ETA Model Forecast Data</font>'
	print '</th>'
	print """</tr>

	<tr>
		<th NOWRAP>
			<font color="#009900">Mandatory Levels:</font></th>
	"""

	mkTDlink(dir_format+'850mb'+biFormat+'.gif' ,  "850 MB", "eta1")
	mkTDlink(dir_format+'700mb'+biFormat+'.gif' ,  "700 MB", "eta2")
	mkTDlink(dir_format+'500VORT'+biFormat+'.gif', "500 MB Vorticity", "eta3")
	mkTDlink(dir_format+'500mb'+biFormat+'.gif', "500 MB", "eta4")
	mkTDlink(dir_format+'300mb'+biFormat+'.gif', "300 MB", "eta5")
	mkTDlink(dir_format+'200mb'+biFormat+'.gif', "200 MB", "eta6")


	print '<td ROWSPAN="4" BGCOLOR="#FFFFFF" align="CENTER">'

	if version != 'b':
		if caseNum[0] == 's':
			mk_data_link(dir_format+'etaHEL'+data_format+'F12.gif' , "12 HR ETA Helicity", "asdf342")
			mk_data_link(dir_format+'etaTEMP'+data_format+'F12.gif' , "12 HR ETA Model Temperatures", "43eta")
			mk_data_link(dir_format+'etaPREC'+data_format+'F12.gif' ,"12 HR ETA Precipitation", "54eta")
			mk_data_link(dir_format+'etaTHK'+data_format+'F12.gif' , "12 HR ETA Thickness and Pressure", "32aet")
			mk_data_link(dir_format+'etaVORT'+data_format+'F12.gif' , "12 HR ETA Vorticity", "eta23as")
		else:
			mk_data_link(dir_format+'etaTEMP'+data_format+'F00.gif' , "00 HR ETA Model Temperatures", "43eta")
			mk_data_link(dir_format+'etaPREC'+data_format+'F00.gif' ,"00 HR ETA Precipitation", "54eta")
			mk_data_link(dir_format+'etaTHK'+data_format+'F00.gif' , "00 HR ETA Thickness and Pressure", "32aet")
			mk_data_link(dir_format+'etaVORT'+data_format+'F00.gif' , "00 HR ETA Vorticity", "eta23as")

	print """
	</td>

	</tr>
	
	<tr>
        <th>
                <font color="#009900">Profiler:</font></th>
	"""


	mkTDlink(dir_format+'1000m'+biFormat+'.gif' , "1000 m", "prof3")
	mkTDlink(dir_format+'3000m'+biFormat+'.gif' , "3000 m", "prof4")
	mkTDlink(dir_format+'5600m'+biFormat+'.gif' , "5600 m", "prof5")
	mkTDlink(dir_format+'9000m'+biFormat+'.gif' , "9000 m", "prof6")


	print '<TD></TD><TD></TD>'

	print '</TR><TR><th NOWRAP  ><font color="#009900">SkewT Charts:</font></th>'

	print '<td COLSPAN="6" BGCOLOR="#FFFFFF"><a href="/cgi-bin/severe2/resource/skewT.py?userKey='+userKey+'&advanced=yes" target="_new">View SkewT</a></td>'
	print '</tr></table>'
	
	print '<!-- End of Upper Air Section -->'

	print """<!-- Begin Surface Part -->
	<br>&nbsp;

	<table BORDER=0 CELLPADDING=1 CELLSPACING=0 ROWSPACING=0 WIDTH="100%">
	<tr bgcolor="#778899">
		<th ALIGN=CENTER COLSPAN="6" NOWRAP >
			<font color="white">Current and Recent Surface Plots:</font></th>

	<td ROWSPAN="8" bgcolor="white"><img src="/icons/blank.gif" width="1"></td>

	<th NOWRAP><font color="white">Misc Current Data:</font></th>
	</tr>

	<tr>
	<td></td>"""

	print '<TH> Current: </TH>'        
	print '<TH>- '+str(1*multipler)+' hr:</TH>'
	print '<TH>- '+str(2*multipler)+' hrs:</TH>'
	print '<TH>- '+str(3*multipler)+' hrs:</TH>'
	print '<TH>Animation</TH>'

	print '<td ROWSPAN="7" BGCOLOR="#FFFFFF" align="CENTER">'

	if currentHour == 12:
		mk_data_link(dir_format+'cape'+data_format+'.gif' ,  "ETA Forecasted CAPE", "etaCAPE")
	else:
		mk_data_link(dir_format+'cape'+data_format+'.gif' ,  "Satellite Derived CAPE", "satCAPE")
	mk_data_link(dir_format+'tpw'+data_format+'.gif' ,  "Precipitable Water", "precW")
	mk_data_link(dir_format+'li'+data_format+'.gif' ,  "Lifted Index", "liI")
	mk_data_link(dir_format+'light'+data_format+'.gif' , "Lightning Data", "liD")
	mk_data_link(dir_format+'sat'+data_format+'.gif' ,  "Satellite Image", "dase")
	mk_data_link(dir_format+'sat'+data_format+'.jpg' ,  "Alt Satellite Image", "asegas")
	mk_data_link(dir_format+'sfcPlot'+data_format+'.jpg' ,  "US Station Plot", "asdewrt")
	mk_data_link(dir_format+'MPX'+data_format+'.gif' , "Minneapolis Radar Reflectivity", "mspX")
	mk_data_link(dir_format+'MPXVEL'+data_format+'.gif' , "Minneapolis Velocity", "sapC")
	mk_data_link(dir_format+'DMX'+data_format+'.gif' ,  "Des Moines Radar Reflectivity", "basd")
	mk_data_link(dir_format+'1000m'+data_format+'.gif' ,  "1000m Hourly Profiler", "9000m")
	mk_data_link(dir_format+'3000m'+data_format+'.gif' ,  "3000m Hourly Profiler", "9000m")
	mk_data_link(dir_format+'5600m'+data_format+'.gif' ,  "5600m Hourly Profiler", "9000m")
	mk_data_link(dir_format+'9000m'+data_format+'.gif' ,  "9000m Hourly Profiler", "9000m")
		
	print '</TD></TR>'


	mk_row_data(orig_secs, "sfc", ".gif",  "Surface Chart", multipler)


	mk_row_data(orig_secs, "temp", ".gif",  "Surface Temps Chart", multipler)


	mk_row_data(orig_secs, "dew", ".gif", "Surface Dew Point Chart", multipler)


	mk_row_data(orig_secs, "moist", ".gif",  "Moisture Divergence", multipler)


	mk_row_data(orig_secs, "nowrad", ".gif",  "National Radar Summary", multipler)
	print '</TR></TABLE>'


def mk_data_link2(file, string_txt, i, hour_time, randString):
	if os.path.isfile('/home/httpd/html/'+file):
		print '\t<a href="javascript:launchURL(\'/cgi-bin/severe2/resource/getPic.py?file='+file+'\', \'wxdata'+randString+'\', 720, 640)">'
		print '\t<img src="/icons/g.gif" border="0" hspace=0 vspace=0></a>'
		return 1
	else:
		print '\t<img src="/icons/b.gif" border="0" hspace=0 vspace=0 >'
		return 0

def mkTDlink(file,  string_txt, randString):
	print '<TD>'
	if os.path.isfile('/home/httpd/html/'+file):
		print '\t<a href="javascript:launchURL(\'/cgi-bin/severe2/resource/getPic.py?file='+file+'\', \'wxdata'+randString+'\', 720, 640)">'+string_txt+'</a>'
	else:
		print '\t'+string_txt
	print '</TD>'

def mk_data_link(file,  string_txt, randString):
	if os.path.isfile('/home/httpd/html/'+file):
		print '<BR><a href="javascript:launchURL(\'/cgi-bin/severe2/resource/getPic.py?file='+file+'\', \'wxdata'+randString+'\', 720, 640)">'+string_txt+'</a>'
                
                
def mk_row_data(orig_secs, prefix, suffix, title, multipler):
	animCount = 0
	print '<TR><TH><font color="green">'+title+'</a></TH>'
	for i in range(4):
		print '<TD align="center">'
		this_secs = orig_secs - i*3600*multipler
		this_tuple = time.localtime(this_secs)
		data_format = time.strftime("%y%m%d%H", this_tuple)
		hour_time = time.strftime("%H Z", this_tuple)
		dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
		randString = prefix[:-1]+data_format
		if ( mk_data_link2(dir_format+prefix+data_format+suffix , title, str(i), hour_time, randString) ):
			animCount = animCount +1
		print '</TD>'

	print '<TD align="center">'
	dateStr = time.strftime("%Y%m%d%H", time.localtime(orig_secs-3600*multipler) )
	if animCount > 1:
		print '\t<a href="/cgi-bin/severe2/resource/loop.py?dateStr='+dateStr+'&mapType='+prefix+'&timeSpan=-6" target="_new">'
		print '\t<img src="/icons/g.gif" border="0" hspace=0 vspace=0></a>'
	else:
		print '\t<img src="/icons/b.gif" border="0" hspace=0 vspace=0 >'
	print '</TD></TR>'
