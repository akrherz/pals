#!/usr/local/bin/python
# This file checks for a question and then generates HTML for each question
# Daryl Herzmann 8-18-99

import cgi, pg, general

admindb = pg.connect('archadmin')
sessiondb = pg.connect('sessions_417')


def Main(case_num, secs, key, refer):
	start_secs = admindb.query("SELECT start_secs from winter_cases WHERE case_num = '"+case_num+"' ").getresult()
	start_secs = start_secs[0][0]

	intervals = ( int(float(secs)) - int(float(start_secs)) ) / 10800

	if intervals == 2:
		general.Main(case_num, secs, key, refer)

	entries = admindb.query("SELECT * from spec_winter_417 WHERE ticks = '"+str(secs)+"' ").getresult()

	for i in range(len(entries)):
		question = entries[i][1]

