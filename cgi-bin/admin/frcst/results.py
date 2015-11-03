#!/usr/local/bin/python
# This will make the results for Catherine to print out
# Daryl Herzmann 9-1-99

import pg, cgi, style

mydb = pg.connect('frcst')

def mysort(list, field):
	res = []
	for x in list:
		i = 0
		for y in res:
			if x[field] <= y[field]:
				break
			i = i+1
		res[i:i] = [x]
	return res

def Main():
	style.header("Forecasting Results","white")
	form = cgi.FormContent()
	class_name = form["class_name"][0]
	yeer = form["yeer"][0]
	month = form["month"][0]
	day = form["day"][0]

	print '<H3>'+class_name+' : Forecasting Results</H3>'
	print '<BR>Year: '+yeer+'<BR>'
	print 'Month: '+month+'<BR>'
	print 'Day: '+day+'<BR>'

	entries = mydb.query("SELECT * from grades WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid ~* '"+class_name+"' or userid = 'mos' ").getresult()

	entries = mysort(entries, -1)
	print '<TABLE><TR>'
	print  '<TH>USERID</TH><TH>DM H:</TH><TH>DM L:</TH><TH>DM P:</TH><TH>DM S:</TH><TH>FL H:</TH><TH>FL L:</TH><TH>FL P:</TH><TH>FL S:</TH><TH>TOT:</TH></TR>'

	spacer = " "
        for i in range(len(entries)):
		print '<TR><TD>'
                this_entry = entries[i]
                print this_entry[0] +"</TD>"
                for j in range(len(this_entry)):
			thi = this_entry[j]
			entry = str(thi)
                        if entry[0] == "m" or j == 1 or j == 2 or j == 3:
                                doy = "nothing"
                        else:
                                print '<TD align="center">'+entry+'</TD>', 
                print '</TR>'
	print '</TABLE>'

Main()
