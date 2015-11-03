#!/usr/local/bin/python
# This program will output the results from the last forecast
# Daryl Herzmann

import pg, cgi, style, mk_table, time

mydb = pg.connect('frcst')

def Main():
	form = cgi.FormContent()
	class_name = form["class_name"][0]

	sort = -1
	if form.has_key('sort'):
		sort = int( form["sort"][0] )

	days = mydb.query("SELECT * from cases WHERE class_name = '"+class_name+"' ").getresult()
	day = str( days[-1][2] )
	month = str( days[-1][1] )
	yeer = str( days[-1][0] )
	floater = days[-1][3]

	tester = mydb.query("SELECT * from climo WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ").getresult()
	if len(tester) == 0:
		try:
			day = str( days[-2][2] )
		        month = str( days[-2][1] )
		        yeer = str( days[-2][0] )
		        floater = days[-2][3]
		except:
			style.SendError("It appears that no forecasts have been graded yet")

	time_tuple = (int(yeer), int(month), int(day), 12, 0, 0, 0, 0, 0)
	nice_date = time.strftime("%B %d, %Y", time_tuple)

	style.header("Last Forecast results", "white")
	print '<H3>Results of the last forecast for : '+nice_date+'</H3>'
	print '<HR>'
	print '<B>Validation:</B><BR>'
	print '<MULTICOL cols="2">'

	answers = mydb.query("SELECT * from answers WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' ").getresult()
	print 'Des Moines High: '+answers[0][3]
	print '<BR>Des Moines Low: '+answers[0][4]
	print '<BR>Des Moines Precip Category: '+answers[0][5]+' ( '+answers[0][11]+' in)'
	print '<BR>Des Moines Snow Category: '+answers[0][6]+' ( '+answers[0][12]+' in)'
	print '<BR><BR>'+floater+' High: '+answers[0][7]
	print '<BR>'+floater+' Low: '+answers[0][8]
	print '<BR>'+floater+' Precip Category: '+answers[0][9]+' ( '+answers[0][13]+' in)'
	print '<BR>'+floater+' Snow Category: '+answers[0][10]+' ( '+answers[0][14]+' in)'

	print '</MULTICOL>'
	mk_table.Main("grades", sort, class_name, "last.py", yeer, month, day, floater)


Main()
