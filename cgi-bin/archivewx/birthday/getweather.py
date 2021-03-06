#!/usr/local/bin/python
# This is my script that will get the data for the birthday and display it
# Daryl Herzmann 11-8-99

import pg, cgi, time, re, sys

mydb = pg.connect('coop', 'meteor.geol.iastate.edu', 5432)

def mk_header():
	print 'Content-type: text/html \n\n'
	print """
	<HTML>
	<HEAD>  
        <TITLE>PALS | Weather On Your Birthday</TITLE>
        <META name="author" content="Daryl Herzmann akrherz@iastate.edu">
        <link rel=stylesheet type=text/css href=/css/pals.css>
	</HEAD>

	<body BGCOLOR="#ffffff" LEFTMARGIN="0" MARGINWIDTH="5" MARGINHEIGHT="5" vlink="blue" alink="blue" link="blue">

	<TABLE WIDTH="100%" BORDER="0" CELLSPACING="0" CELLPADDING="0"  BORDER="0" BGCOLOR="#99ccff">
	<TR>
        <TD WIDTH=150 VALIGN="CENTER">
        <img src="/icons/pals_logo.gif" vpsace="5" hspace="5" width="75">
        </TD>
        <TD WIDTH="90%" ALIGN="left" NOWRAP>
        <font color="#003366" size="+3">Partnerships to Advance Learning in Science</font><BR>
        <font color="blue" size="3">Developing, Implementing, and Sharing Constructivist Learning Resources</font>
        </TD>
	</TR>

	<TR>
        <TD colspan="2" bgcolor="black"><img src="/icons/blank.gif" height="1" width="3"></TD>
	</TR>
	</TABLE>
	
	<H3>The Weather on Your Birthday!!</H3>
	
	<a href="/archivewx/birthday">Try another date or city</a><BR>
	"""

def weather_logic(month, high, low, rain, snow):
	deltaT = high - low
	
	if month > 4 and month < 11:		# It is summer
		if deltaT >= 30:
			if rain == 0.00:
				return "Sunny!!"
			else:
				return "Mostly sunny w/ Rain!!"
		elif deltaT >= 15 and deltaT < 30:
			if rain == 0.00:
				return "Mostly Sunny!!"
			else:
				return "Partly Sunny w/ Rain!!"
		else:
			if rain == 0.00:
				return "Cloudy!!"
			else:
				return "Cloudy and rainy!!"
		
	else:					# It is winter
		if deltaT >= 20:
			if rain == 0.00:
				return "Sunny!!"
			elif rain > 0 and snow > 0:
				return "Snowy!!"
			else:
				return "Mostly sunny w/ Rain!!"
				
		elif deltaT >= 10 and deltaT < 20:
			if rain == 0.00:
				return "Mostly Sunny!!"
			elif rain > 0 and snow > 0:
				return "Snowy!!"
			else:
				return "Partly Sunny w/ Rain!!"
		else:
			if rain == 0.00:
				return "Cloudy!!"
			elif rain > 0 and snow > 0:
				return "Snowy!!"
			else:
				return "Cloudy and rainy!!"

def get_values(city, dateStr):
	query_str = "SELECT high, low, precip, snow from "+city+" WHERE day = '"+dateStr+"' "

	results =  mydb.query(query_str).getresult()
	rain = round(float(results[0][2]), 2)
	snow = round(float(results[0][3]), 2)
	
	if rain < 0:
		rain = 0
	if snow < 0:
		snow = 0
		
	return results[0][0], results[0][1], str(rain), str(snow)



def get_day(city, ticks):
	local_time = time.localtime(ticks)
	str_month = time.strftime("%B", local_time)
	yeer = str(local_time[0])
	month = str(local_time[1])
	day = str(local_time[2])
	dateStr = yeer+"-"+month+"-"+day
	high, low, rain, snow =  get_values(city, dateStr)
	
	cloud_type = weather_logic(int(month), int(high), int(low), round(float(rain), 2), round(float(snow), 2) )

	print '<TD WIDTH="120" VALIGN="TOP" BORDER="1" align="CENTER">'
	print '<img src="/content/date.php?yeer='+yeer+'&month='+str_month+'&day='+day+'"><BR>'
	print '<TABLE>'
	print "<TR><TH>HIGH </TH><TD> "+str(high)+"</TD></TR>"
	print "<TR><TH>LOW  </TH><TD> "+str(low)+"</TD></TR>"
	print "<TR><TH>RAIN </TH><TD> "+str(rain)+"</TD></TR>"
	print "<TR><TH>SNOW </TH><TD> "+str(snow)+"</TD></TR>"
	print "<TR><TH colspan='2' NOWRAP><font color='blue'>"+cloud_type+"</font></TH></TR>"
	print '</TABLE>'
	print '</TD>'
	
def now_get_day(city, ticks):
	local_time = time.localtime(ticks)
	str_month = time.strftime("%B", local_time)
	yeer = str(local_time[0])
	month = str(local_time[1])
	day = str(local_time[2])
	dateStr = yeer+"-"+month+"-"+day
	high, low, rain, snow =  get_values(city, dateStr)
	cloud_type = weather_logic(int(month), int(high), int(low), round(float(rain), 2), round(float(snow), 2) )

	print '<TD VALIGN="TOP" BORDER="1" bgcolor="#EEEEEE" rowspan="2" NOWRAP align="center">'
	print '<font color="BLUE">HAPPY BIRTHDAY!!</font><BR><BR>'
	print '<img src="/content/date.php?yeer='+yeer+'&month='+str_month+'&day='+day+'"><BR>'
	print '<TABLE>'
	print "<TR><TH>HIGH </TH><TD> "+str(high)+"</TD></TR>"
	print "<TR><TH>LOW  </TH><TD> "+str(low)+"</TD></TR>"
	print "<TR><TH>RAIN </TH><TD> "+str(rain)+"</TD></TR>"
	print "<TR><TH>SNOW </TH><TD> "+str(snow)+"</TD></TR>"
	print "<TR><TH colspan='2' NOWRAP><font color='blue'>"+cloud_type+"</font></TH></TR>"
	print '</TABLE>'
	print '</TD>'


def Main():
	mk_header()

	form = cgi.FormContent()
	try:
		yeer = form["year"][0]
		month = form["month"][0]
		day = form["day"][0]
		cityParts = re.split("__", form["city"][0])
	except:
		print "<P><P><B>Invalid Post:</B><BR>"
		print "Please use this URL <a href='https://pals.agron.iastate.edu/archivewx/birthday/'>https://pals.agron.iastate.edu/archivewx/birthday/</a>"
		sys.exit(0)	

	city = cityParts[0]
	cityName = cityParts[1]
	
	
	now = time.mktime( int(yeer), int(month), int(day), 12, 12, 0, 0, 0, 0)
	nowM2 = now - 86400*2
	nowM1 = now - 86400*1
	nowP1 = now + 86400*1
	nowP2 = now + 86400*2
	

	print '<BR><h4>Data valid for station: '+cityName+', Iowa</h4><BR>'
	
	print '<TABLE width="600">'
	print '<TR><TD><BR><BR><BR></TD><TD></TD>'
	now_get_day(city, now)
	print '<TD></TD><TD></TD></TR><TR>'
	
	get_day(city, nowM2)
	
	get_day(city, nowM1)
	
	get_day(city, nowP1)
	
	get_day(city, nowP2)
	
	
	print '</TR></TABLE>'

	print """
	<BR><BR><P>The weather type listed for each day above in blue is <B>not</b> official data.  A rather
	subjective logic scheme is used to guess the weather purely for entertainment purposes only. 

	"""
Main()
