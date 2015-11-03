#!/usr/local/bin/python

from cgi import *
import style

form = FormContent()
if not form.has_key("date"): style.SendError("CGI ERROR")
date = form["date"][0]

def top():
	print '<H2><IMG SRC="/images/weather.gif" HEIGHT=40 WIDTH=40>'
	print 'Forecast Severe Weather for '+date+'</H2>'
	print '<HR><font size="5">Help for your forecast:</font><BR><BR>'
	print '<img src="/images/point_02.gif">'
	print '<A HREF="hints_gen.py?date='+date+'">'
	print 'Severe Weather Hints</A><spacer type="horizontal" size="50">' 
	print '<img src="/images/point_02.gif">'
	print '<A HREF="page_gen.py?date='+date+'">'
	print 'Weather Products for this day</A><HR><BR><BR>'

def form():
	print '<font size="5">Complete your forecast:</font><BR><BR>'
	print '<FORM METHOD=POST ACTION="grader.py">'
	
	print '<P><B>1) Where will severe weather occur?</B><P>'
	print '<SELECT NAME="1.1"><OPTION> (Select a State)'
	print '<OPTION> ALABAMA <OPTION> ARKANSAS <OPTION> ARIZONA'
	print '<OPTION> CALIFORNIA <OPTION> COLORADO <OPTION> CONNECTICUT <OPTION> DELAWARE <OPTION> FLORIDA'
	print '<OPTION> GEORGIA <OPTION> IDAHO <OPTION> ILLINOIS <OPTION> INDIANA <OPTION> IOWA <OPTION> KANSAS'
	print '<OPTION> KENTUCKY <OPTION> LOUISIANA <OPTION> MAINE <OPTION> MARYLAND <OPTION> MASSACHUSETTS'
	print '<OPTION> MICHIGAN <OPTION> MINNESOTA <OPTION> MISSISSIPPI <OPTION> MISSOURI <OPTION> MONTANA'
	print '<OPTION> NEBRASKA <OPTION> NEVADA <OPTION> NEW HAMPSHIRE <OPTION> NEW JERSEY <OPTION> NEW MEXICO'
	print '<OPTION> NEW YORK <OPTION> NORTH CAROLINA <OPTION> NORTH DAKOTA <OPTION> OHIO <OPTION> OKLAHOMA'
	print '<OPTION> OREGON <OPTION> PENNSYLVANIA <OPTION> RHODE ISLAND <OPTION> SOUTH CAROLINA <OPTION> SOUTH DAKOTA'
	print '<OPTION> TENNESSEE <OPTION> TEXAS <OPTION> UTAH <OPTION> VERMONT <OPTION> VIRGINIA <OPTION> WASHINGTON'
	print '<OPTION> WISCONSIN <OPTION> WEST VIRGINIA <OPTION> WYOMING </SELECT><BR>'
	print '<spacer type="vertical" size="30">'
	
	print '<P><B>2) When do you think the severe weather will occur? (PM times)<P>'
	print '</B><SELECT NAME="2.1"> <OPTION> (Select a time) <OPTION>'
	print '12-3 <OPTION> 3-6 <OPTION> 6-9 <OPTION> 9-Midnight </SELECT><BR>'
	print '<spacer type="vertical" size="30">'

	print '<P><B>3) What type of severe weather will occur? (Choose all that apply)</B><P>'
	print '<table width="100%"><tr>'
	print '<td><INPUT TYPE=checkbox NAME=3.1> Tornado' 
	print '<td><INPUT TYPE=checkbox NAME=3.2> Hail/Damaging Wind'
	print '<td><INPUT TYPE=checkbox NAME=3.3> Greater Than 3 Inches of Rain'
	print '</tr></table>'
	print '<spacer type="vertical" size="30">'	

	print '<HR><BR><BR><font size="5">Submit your forecast:</font><BR><BR>'
	print '<CENTER><INPUT TYPE=submit Value="Submit my forecast">'
	print '<INPUT TYPE=reset></CENTER></FORM>'

def Main():
	style.header('Forecast for '+date,'/images/ISU_bkgrnd.gif')
	top()
	form()

	print '</body></html>'

Main()
