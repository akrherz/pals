#!/usr/local/bin/python
# This program is the first attempt at modularizing svr_frcst
# Daryl Herzmann 8-24-99

import pg, cgi, style

casesdb = pg.connect('svr_frcst')

def determine_case_num(case_pre):
	entries = casesdb.query("SELECT case_num

def Main():
	form = cgi.FormContent()
	type = form["type"][0]
	try:
		start_day = int(form["start_day"][0])
		start_month = int(form["start_month"][0])
		start_year = int(form["start_year"][0])
		end_day = int(form["end_day"][0])
		end_month = int(form["end_month"][0])
		end_year = int(form["end_year"][0])
	except:
		style.SendError("CGI import value error")
	if type == "summer":
		start_time = (start_year, start_month, start_day, 12, 0, 0, 0, 0, 0)
		end_time = (end_year, end_month, end_day, 5, 0, 0, 0, 0, 0)
		case_pre = "s"
	if type == "winter":
		start_time = (start_year, start_month, start_day, 0, 0, 0, 0, 0, 0)
		end_time = (end_year, end_month, end_day, 0, 0, 0, 0, 0, 0)
		case_pre = "w"
	start_secs = time.localtime(start_time)
	end_secs = time.localtime(end_time)

	determine_case_num(case_pre)

Main()
