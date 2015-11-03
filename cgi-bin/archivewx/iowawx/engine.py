#!/usr/local/bin/python
# This file is the one that runs the search engine for the various files
# Daryl Herzmann 3/31/99
# UPDATE: 4/7/99 - Adding in allstations search

import functs, pg


mydb = pg.connect('coop', 'meteor.geol.iastate.edu', 5432)

def search(option, city, year, month, day):
	
	results = []
	dateStr = year+"-"+month+"-"+day

	if option == "yearly":

		print '<BR><a href="year_graph.py?city='+city+'&year='+year+'">Click Here for a graph of this data</a><BR>'

		results = mydb.query("SELECT * from "+city+" WHERE date_part('year', day) = "+year+" ")
		results = results.getresult()

	if option == "monthly":
		results = mydb.query("SELECT * from "+city+" WHERE date_part('year', day) = "+year+" AND date_part('month', day) = "+month+" ")
		results = results.getresult()

	if option == "daily":
		results = mydb.query("SELECT * from "+city+" WHERE day = '"+dateStr+"'")
		results = results.getresult()

	if option == "allstations_daily":
		stations = functs.stations()
#		for i in range(len(stations)):
		for i in range(10):
			code = stations[i][1]
			tmp_results = mydb.query("SELECT * from "+code+" WHERE day = '"+dateStr+"'")
			tmp_results = tmp_results.getresult()
			results = results + tmp_results

	return results
