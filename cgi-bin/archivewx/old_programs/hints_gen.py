#!/usr/local/bin/python

from cgi import *

form = FormContent()
date = form["date"][0]

def header(title):
	print '<HTML><HEAD><TITLE>'
	print title
	print '</TITLE></HEAD><BODY BACKGROUND="/images/clouds.jpg">'
	
def top(title):
	print '<CENTER><H1>'
	print title
	print '</H1></center><br>'
	
def body():	
	print '<center><IMG SRC="/archivewx/files/tornadiccell9.JPG">'
	print '<BR>(Photo Courtesy of ISU <a href="http://www.public.iastate.edu/~wxintro/atmos.html">Meteorology Program)'	
	print '</a><H3>This Page Is Intended To Help High School '
	print 'Students Forecast Severe Weather</H3></CENTER><BR clear="all">'
	print '<P><B><FONT COLOR="#FF0000" SIZE=+2>'
	print 'Here Is Some Information You Should Know Before Forecasting</FONT></B>'
	print '<BR><UL><FONT SIZE=+1><LI>The surface map shows conditions at the surface.</LI>'
	print '<P><LI>The 850 mb map shows conditions at 5,000 feet above sea level.</LI>'
	print '<P><LI>The 500 mb map shows conditions at 18,000 feet above sea level.</LI>'
	print '<P><LI>An upper air sounding is data taken from a weather balloon sent up twice each day.</LI></UL></font>'
	
	print '<br><br><P><IMG SRC="/images/lightning2.gif"><br>'	
	print '<P><B><FONT COLOR="#FF0000" SIZE=+2>Steps</FONT></B>'

	print '<P><FONT COLOR="#000000" SIZE=+2>'
	print '1. Look at Surface Map For:</FONT><br>'
	print '<UL><FONT SIZE=+1><LI><A HREF="/archivewx/files/fronts.html">Fronts </A>in the Area</LI>'
	print '<BR><LI><A HREF="/archivewx/files/gradients.html">Temperature Gradients</A></LI>'
	print '<BR><LI><A HREF="/archivewx/files/dewpoints.html">Dew Point </A>Levels</LI>'
	print '<BR><LI><A HREF="/archivewx/files/wind.html">Wind Speed and Direction</A></FONT></LI></UL>'
	
	print '<P><FONT COLOR="#000000" SIZE=+2>'
	print '2. Look at 850 mb Map For:</FONT><br>'
	print '<UL><FONT SIZE=+1><LI><A HREF="/archivewx/files/advection.html">Advection of Moisture</A></FONT></LI></UL>'
	
	print '<P><FONT COLOR="#000000" SIZE=+2>'
	print '3. Look at 500 mb Map With Vorticity For:</FONT><BR>'
	print '<UL><FONT SIZE=+1><LI><A HREF="/archivewx/files/pva.html">Positive Vorticity Advection</A></FONT></LI></UL>'

	print '<P><FONT COLOR="#000000" SIZE=+2>'
	print '4. Look at Upper Air Soundings For:</FONT><BR>'
	print '<UL><FONT SIZE=+1><LI><A HREF="/archivewx/files/li.html">Lifted Index</A></LI>'
	print '<BR><LI><A HREF="/archivewx/files/cape.html">Cape</A></LI>'
	print '<BR><LI><A HREF="/archivewx/files/windshear.html">Wind Shear</A></LI></UL></font>'
	
	print '<FONT COLOR="#000000" SIZE=+2>'
	print '5. Complete Your <A HREF="forecast_gen.py?date='+date+'">Forecast</A></FONT><br>'
	
	print '<BR><BR>'
	print '<FONT COLOR="#FF0000" SIZE=+2>Here Are Some Helpful Weather Product Links</FONT>'
	print '<BR><UL><FONT SIZE=+1><LI><A HREF="page_gen.py?date='+date+'">Weather Products Page</A></FONT></LI></UL>'

def Main():
	print 'Content-type: text/html\n\n'
	header("Severe Weather Forecasting Tips")
	top("Here Are Some Helpful Tips For Forecasting Severe Weather")
	body()

	print '</body></html>'
Main()
