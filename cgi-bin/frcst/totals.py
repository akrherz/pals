#!/usr/local/bin/python
# This will make the total results for Catherine to print out
# Daryl Herzmann 9-1-99
# 9-6-99: Clean up code, document, clean up appearance

import pg, cgi, style, time, mk_table
mydb = pg.connect('frcst')


def Main():
	now = time.time()
	now_tuple = time.localtime(now)
	nice_date = time.strftime("%B %d, %Y", now_tuple)

	style.header("Forecasting Results","white")
	form = cgi.FormContent()
	class_name = form["class_name"][0]
	sort = -1
	if form.has_key("sort"):
		sort = int(form["sort"][0])

	print '<H3>Cumulative forecasting results for -- '+class_name+'</H3>'
	print 'Valid thru '+nice_date

	entries = mydb.query("SELECT * from totals WHERE userid ~* '"+class_name+"'").getresult()

	mk_table.Main("totals", sort, class_name, "totals.py", 5, 5, 5, "Floater City")
Main()
