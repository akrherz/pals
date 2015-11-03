#!/usr/local/bin/python
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import time, os, sys, time, regsub, pg, string, style, insText, DateTime, cgi, pals

# admindb = pg.connect('archadmin')
mydb = pg.connect('severe2', 'localhost', 5555)
mydb.query("SET TIME ZONE 'GMT'")
usersTable = "users"
casesTable = "cases"
annoteTable = "annotations"
scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise/"
# scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise-cvs/"

def getIntro(caseNum):
        print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">Case Introduction:</font></H2>'

        try:
                select = mydb.query("SELECT comments from intro where casenum = '"+caseNum+"' ").getresult() 
        except ValueError:
                print "No introduction has been written..."
                select = [(" "),(" ")]

        if len(select) == 0:
                print "No introduction has been written..."
        else:
                print '<B><font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '</B><BR><BR>'

def updateUser(userKey, col, val):
        mydb.query("UPDATE users set "+col+" = '"+str(val)+"' WHERE userKey = "+str(userKey)+" ")

def retreiveUser(userKey = 'null'):
        if (userKey == 'null'):
                form = cgi.FormContent()
                userKey = pals.formValue(form, "userKey")
#        try:
	lastTime, gradeTime, caseNum = mydb.query("SELECT lasttime, gradeTime, casenum from users WHERE userkey = '"+str(userKey)+"' ").getresult()[0]
	startTime, endTime = mydb.query("SELECT starttime, endtime from cases WHERE casenum = '"+caseNum+"' ").getresult()[0]
#        except:
#                style.SendError("Can not locate your user info, sorry.")

        noonTime = DateTime.ISO.ParseDateTimeGMT(startTime) + DateTime.RelativeDateTime(hours=+5)
                
        return userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum

def clean_str(re_string):
	re_string = regsub.gsub("'", "&#180;", re_string)
	return re_string

def setup_table():
	print '<CENTER>'
	print '<TABLE WIDTH="650" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">'
        
	print '<TR>'
	print '<TD colspan="3"><img src="/icons/svr_frcst-top.gif" HSPACE="0" VSPACE="0" BORDER="0"></TD></TR>'

	print '<TR valign="top" bgcolor="white">'
	print '<TD colspan="3"><img src="/icons/svr_frcst-upleft.gif" HSPACE="0" VSPACE="0" BORDER="0" HEIGHT="20"></TD>'
        print '</TR>'


def mk_data_link2(file, thumbnail, string_txt, i, hour_time):
        if os.path.isfile('/home/httpd/html/'+file):
                print '<a href="/cgi-bin/severe2/resource/getPic.py?file='+file+'" target="_new"> '+hour_time+'</a><BR>'
        else:
                print "- -"

def mk_data_link(file, thumbnail, string_txt):
        if os.path.isfile('/home/httpd/html/'+file):
                print '<a href="/cgi-bin/severe2/resource/getPic.py?file='+file+'" target="_new">'+string_txt+'</a><BR>'

def mk_row_data(orig_secs, prefix, suffix, icon_ref, title, multipler):
        print '<TH><font color="green">'+title+'</a></TH>'
        for i in range(5):
                print '<TD align="center">'
                this_secs = orig_secs - i*3600*multipler
                this_tuple = time.localtime(this_secs)
                data_format = time.strftime("%y%m%d%H", this_tuple)
                hour_time = time.strftime("%H Z", this_tuple)
                dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", this_tuple)
                mk_data_link2(dir_format+prefix+data_format+suffix , icon_ref , title, str(i), hour_time)
                print '</TD>'
        print '<TD align="center">'
        dateStr = time.strftime("%Y%m%d%H", this_tuple)
        print '<a href="/cgi-bin/severe2/resource/loop.py?dateStr='+dateStr+'&mapType='+prefix+'&timeSpan=-6" target="_top">Loop</a>'
        print '</TD>'


def mkData(nowDate, multipler):
        nowDate = DateTime.ISO.ParseDateTimeGMT(nowDate)
        gmt_tuple = nowDate.tuple()
        orig_secs = nowDate.ticks()
        
        currentHour = gmt_tuple[3]

        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
        
        print """
        <BR>
        <H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d">Recent Weather Data:</font></H2>

        <font color="#551a8b"><i>Time Series Data:</i></font><BR>
        

        <TABLE border="1" align="center" width="100%">
        <TR>
                <TH></TH>
                <TH>Current:</TH>"""
        print '<TH>- '+str(1*multipler)+' hr:</TH>'
        print '<TH>- '+str(2*multipler)+' hrs:</TH>'
        print '<TH>- '+str(3*multipler)+' hrs:</TH>'
        print '<TH>- '+str(4*multipler)+' hrs:</TH>'
        print '<TH>Animation</TH>'

        print '</TR><TR>'
        mk_row_data(orig_secs, "sfc", ".gif", "/icons/sfc_thumb.gif", "Surface Chart", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "temp", ".gif", "/icons/temp_thumb.gif", "Surface Temps Chart", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "dew", ".gif", "/icons/temp_thumb.gif", "Surface Dew Point Chart", multipler)

#        print '</TR><TR>'
#        mk_row_data(orig_secs, "moist", ".gif", "/icons/moist_thumb.gif", "Moisture Divergence", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "nowrad", ".gif", "/icons/NAT_thumb.gif", "National Radar Summary", multipler)
        print '</TR></TABLE>'

        print '<BR><font color="#551a8b"><i>This Hour Only:</i></font><BR>'

         
        foundFile = 0

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

#       if not foundFile:
#               print "<dd>No further data was found for this time.</dd><BR>"




def svrTop(startTime):
        print 'Content-Type: text/html \n\n'
        
        print "<HTML>\n<HEAD>\n\t<TITLE>Severe Weather Forecasting Exercise</TITLE>\n</HEAD>\n"
        print '<body bgcolor="#ffffff" link="blue">'
#       print '<body bgcolor="#ffebcd" link="blue">'
        
        print """       
        <TABLE width="100%">
                <TR><TD background="/icons/sidebg.gif" align="CENTER" NOWRAP>
                        <font size="+3" color="white"><B>Severe Weather Forecasting Activity</b></font>
                </TD></TR>
        <TR><TD>
        """
	if startTime != 0:
                nowDate = DateTime.ISO.ParseDateTimeGMT(startTime)
                nowTuple = nowDate.tuple()
                localDate = DateTime.gm2local(nowDate)
                localTuple = localDate.tuple()
                dateStr = time.strftime("%B %d, %Y", localTuple )
                timeStr = time.strftime("%I:%M %p [%Z]", localTuple )+'&nbsp;&nbsp; ( '+str(nowTuple[3])+' Z )'
        else:
                dateStr = " -- "
                timeStr = " -- "

        print '<H2><CENTER><FONT COLOR="#000000">C</FONT><FONT SIZE="+1">urrent</FONT> <FONT COLOR="#000000">T</FONT><FONT SIZE="+1">ime</FONT>:'
        print '<FONT COLOR="#b0020f">'+timeStr+'</FONT>'
        print '&nbsp; &nbsp; &nbsp;'
        print '<FONT COLOR="#000000">D</FONT><FONT SIZE="+1">ate</FONT>:'
        print '<FONT COLOR="#b0020f">'+dateStr+'</FONT></CENTER></H2><BR>'

	

def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'

def dbComments(nowDate, colName, secHead):
        print '<H2><img src="/icons/ball.red.gif" align="bottom"><font color="#a0522d" size="+2">'+secHead+'</font></H2>'

 #      print "SELECT "+colName+" from "+annoteTable+" where validtime = "+nowDate
        try:
                select = mydb.query("SELECT "+colName+" from "+annoteTable+" where validtime = '"+nowDate+"' ").getresult() 
        except ValueError:
                print "None available for this hour..."
                select = [(" "),(" ")]

        if len(select) == 0:
                print "None available for this hour..."
        else:
                print '<B><font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '</B><BR><BR>'

def svrBot():
        print """       
        </TD></TR>
                <TR><TD background="/icons/sidebg.gif" align="right" NOWRAP>
                        <font size="+1" color="white"><B>&copy; 2000 PALS</b></font>
                </TD></TR>
                <TR><TD align="right" NOWRAP>
                        <a href="http://www.pals.iastate.edu">PALS Home</a> &nbsp; | &nbsp; 
                        <a href="http://www.pals.iastate.edu/svr_frcst">Severe Wx Exercise</a> &nbsp; | &nbsp;
                </TD></TR>
        </TABLE>
        """



def mkHelp():
        print """
        <TABLE border="0" cellpadding="2" align="right">
        <TR>
                <TD align="CENTER" bgcolor="#EEEEEE">
                        <font color="black"><B>Help Topics:</B></font></TD></TR>
        <TR bgcolor="WHITE">
                <TD NOWRAP>
			<font size="+1" face="GEORGIA">
                        <form method="POST" action=" " name="weather">
                        <SELECT name="area" onChange="location=this.form.area.options[this.form.area.selectedIndex].value">
                                <option value="/svr_frcst/help/z.html">What are Z, UTC, GMT times?
                                <option value="/svr_frcst/help/text.html">Watches and Warnings Data
                                <option value="/svr_frcst/help/temp.html">Surface Temperature Map
                                <option value="/svr_frcst/help/sfcmap.html">Surface Map
                                <option value="/svr_frcst/help/dewp.html">Surface Dew Points Map
                                <option value="/svr_frcst/help/radar.html">Radar
                                <option value="/svr_frcst/help/animationhelp.html">Help with Annimations
                        </select>
			</font>
                        </form>
                </TD></TR>
        </TABLE>
        """

