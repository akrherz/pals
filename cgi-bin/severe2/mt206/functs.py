#!/usr/bin/env python2
# Functions file for Severe Weather Forecasting Excercise
# Daryl Herzmann

import time, os, sys, time, regsub, pg, string, style

admindb = pg.connect('archadmin', 'localhost', 5555)
mydb = pg.connect('svr_frcst')
mydb2 = pg.connect('severe2', 'localhost', 5432)
usersTable = "users206"
casesTable = "cases"
scriptBase = "https://pals.agron.iastate.edu/cgi-bin/severe2/mt206/"

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


def mk_data_link2(file, thumbnail, string_txt, i, hour_time):
        if os.path.isfile('/home/www/pals/html/'+file):
                print '<a href="/cgi-bin/svr_frcst/general/picture2.py?file='+file+'" target="_new"> '+hour_time+'</a><BR>'
        else:
                print "- -"

def mk_data_link(file, thumbnail, string_txt):
        if os.path.isfile('/home/www/pals/html/'+file):
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


def mkData(gmt_tuple, multipler):
        orig_secs = time.mktime(gmt_tuple)

        currentHour = gmt_tuple[3]

        data_format = time.strftime("%y%m%d%H", gmt_tuple)
        dir_format = time.strftime("/archivewx/data/%Y_%m_%d/", gmt_tuple)
	print """
        <BR>
        <font color="blue"><H2>Available Weather Data:</H2></font>

        <TABLE width="100%" border="0" cellpadding="2">
        <TR><TH><font color="green"><U>Time Series Data:</U></font></TH>
        <TH rowspan="2" bgcolor="black"><img src="/icons/blank.gif" WIDTH=1 HEIGHT=1></TH>
        <TH><font color="green"><U>This Hour Only:</U></font></TH></TR>

        <TR><TD>

        <TABLE border="1" align="left" width="100%">
        <TR>
                <TH></TH>
                <TH>Current:</TH>"""
	print '<TH>- '+str(1*multipler)+' hr:</TH>'
	print '<TH>- '+str(2*multipler)+' hrs:</TH>'
	print '<TH>- '+str(3*multipler)+' hrs:</TH>'
	print '<TH>- '+str(4*multipler)+' hrs:</TH>'

	print '</TR><TR>'
        mk_row_data(orig_secs, "sfc", ".gif", "/icons/sfc_thumb.gif", "Surface Chart", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "temp", ".gif", "/icons/temp_thumb.gif", "Surface Temps Chart", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "dew", ".gif", "/icons/temp_thumb.gif", "Surface Dew Point Chart", multipler)

        print '</TR><TR>'
        mk_row_data(orig_secs, "nowrad", ".gif", "/icons/NAT_thumb.gif", "National Radar Summary", multipler)
        print '</TR></TABLE>'
	print '</TD><TD>'

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
	print '</TD></TR></TABLE>'
        





def svrTop(secs_tuple, secs = 0):
        if secs != 0:
                if secs_tuple[-1] == 1:
                        secs = int(secs) - 5*3600
                else:
                        secs = int(secs) - 6*3600
                now_tuple = time.localtime( secs )
                date_str = time.strftime("%B %d, %Y", now_tuple)
                time_str = time.strftime("%I:%M %p [%Z]", now_tuple)+'&nbsp;&nbsp; ( '+str(secs_tuple[3])+' Z )'
        else:
                date_str = "Welcome!!"
                time_str = ""

	print 'Content-type: text/html \n\n'
	print """
<HTML>
<HEAD>
  <META NAME="GENERATOR" CONTENT="Adobe PageMill 3.0 Win">
  <TITLE>PALS | Severe Weather Forecasting Activity</TITLE>
<script language="JavaScript">

<!--
function MM_swapImgRestore() { //v2.0
  if (document.MM_swapImgData != null)
    for (var i=0; i<(document.MM_swapImgData.length-1); i+=2)
      document.MM_swapImgData[i].src = document.MM_swapImgData[i+1];
}

function MM_preloadImages() { //v2.0
  if (document.images) {
    var imgFiles = MM_preloadImages.arguments;
    if (document.preloadArray==null) document.preloadArray = new Array();
    var i = document.preloadArray.length;
    with (document) for (var j=0; j<imgFiles.length; j++) if (imgFiles[j].charAt(0)!="#"){
      preloadArray[i] = new Image;
      preloadArray[i++].src = imgFiles[j];
  } }
}

function MM_swapImage() { //v2.0
  var i,j=0,objStr,obj,swapArray=new Array,oldArray=document.MM_swapImgData;
  for (i=0; i < (MM_swapImage.arguments.length-2); i+=3) {
    objStr = MM_swapImage.arguments[(navigator.appName == 'Netscape')?i:i+1];
    if ((objStr.indexOf('document.layers[')==0 && document.layers==null) ||
        (objStr.indexOf('document.all[')   ==0 && document.all   ==null))
      objStr = 'document'+objStr.substring(objStr.lastIndexOf('.'),objStr.length);
    obj = eval(objStr);
    if (obj != null) {
      swapArray[j++] = obj;
      swapArray[j++] = (oldArray==null || oldArray[j-1]!=obj)?obj.src:oldArray[j];
      obj.src = MM_swapImage.arguments[i+2];
  } }
  document.MM_swapImgData = swapArray; //used for restore
}
//-->

</script>
</HEAD>
<BODY BGCOLOR="#ffffff" onLoad="MM_preloadImages('/btn/PALSLogoBall2.gif','#952697783900');MM_preloadImages(
'/btn/SevereTitle2a.gif','#952698953933')">

<table width="90%" border="0" cellspacing="0" cellpadding="12">
    <tr> 
      <td width="126" height="69"><a href="https://pals.agron.iastate.edu" onMouseOut="MM_swapImgRestore()" onMouseOver="MM_swapImage('document.Image1','document.Image1','/btn/PALSLogoBall2.gif','#952697783900')"><img name="Image1" border="0" src="/btn/PALSLogoBall.gif" width="126" height="94"></a></td>
      <td width="451" valign="CENTER"><a href="https://pals.agron.iastate.edu/svr_frcst/index.html" onMouseOut="MM_swapImgRestore()" onMouseOver="MM_swapImage('document.Image2','document.Image2','/btn/SevereTitle2a.gif','#952698953933')"><img name="Image2" border="0" src="/btn/SevereTitle2.gif" width="215" height="54"></a></td>
        <TD align="right">
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

       
       

def mk_sub_sec(string_title):   
	print '<TR><TD>&nbsp;</TD><TH align="left">'
	print '<font color="gold" size="4">'+string_title+'</FONT>'
	print '</TH><TD bgcolor="white">&nbsp;</TD></TR>'


def dbComments(now, now_tuple, col_name, sec_head):
        now = str(int(float(now)))
        table_str = time.strftime("annote_%Y", now_tuple)

	print '<font color="blue"><H2>'+sec_head+'</H2></font>'

	try:
		select = mydb2.query("SELECT "+col_name+" from annotations where date_part('epoch', validtime) = "+str(int(float(now)))+" - 18000").getresult() 
        except ValueError:
		print "SELECT "+col_name+" from "+table_str+" where ztime = '"+str(int(float(now)))+"'"
                print "None available for this hour..."
                select = [(" "),(" ")]

        if len(select) == 0:
                print "None available for this hour..."
        else:
                print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '<BR><BR>'

def svrBot():
	print """<BR clear="all"><BR>
        <TABLE WIDTH="100%" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">
        <TR>
        <TD align="right">                                                      
        � 2000, PALS, all rights reserved
        </TD></TR></TABLE>"""
  

def mkHelp():
#       print '<B><U><font size="2" face="arial">Help Topics</font></U></B><BR>'
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
                        </form></font>
                </TD></TR>
        </TABLE>
        """
