#!/usr/local/bin/python
# This program displays out the available entries
# Daryl Herzmann 2-17-2000

# select code, btype, istation from jun_1998 WHERE date(itime) = '6/18/1998';

import pg, cgi
mydb = pg.connect('nws_txt')
months = ['','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	year = form["year"][0]
	month = form["month"][0]
	day = form["day"][0]
	code = form["code"][0]

	tableName = months[int(month)]+"_"+year
	dateStr = month+"/"+day+"/"+year

	query = mydb.query("select btype, istationname, itime from "+tableName+" WHERE date(itime) = '"+dateStr+"' and code ~* '"+code+"' ").getresult()

	print """
	<TABLE width="100%">
	<TR>
		<TH>Bulletin Type:</TH>
		<TH>NWS Issue Station:</TH>
		<TH>Issue Time:</TH>
	</TR>
	"""
	for i in range(len(query)):
		print '<TR>'
		print '<TD NOWRAP>'+query[i][0]+'</TH>'
		print '<TD NOWRAP>'+query[i][1]+'</TH>'
		print '<TD NOWRAP>'+query[i][2]+'</TH>'
		print '</TR>'

	print '</TABLE>'
Main()
