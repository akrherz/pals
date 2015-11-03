#!/usr/local/bin/python
# Main search engine for PALS C2W
# Daryl Herzmann 7/13/98

from pgext import *
from cgi import *
import os, string, sys, regsub, re, style, c2w 

mydbase = connect("archadmin", "localhost", 5555)

def Main():
	form = FormContent()
	if not form.has_key("string"): style.SendError("You did not input a search string")
	mystring = form["string"][0]

	style.header("ArchiveWx Search Results","white")
	style.std_top('Results of your search for "'+mystring+'"')
        print '<a href="http://www.pals.iastate.edu/archivewx/search.html">New Search</a>--'

	results = ""

	addstring = re.split('AND', mystring)
	orstring = re.split('OR', mystring)
	
	
	if len(addstring) == 2:
		addone = addstring[0]		
		addtwo = addstring[1]
		addone = string.strip(addone)
		addtwo = string.strip(addtwo)
		
		results = mydbase.query("select * from diary where (descript ~~ '%"+addone+"%' AND descript ~~ '%"+addtwo+"%')")
		results = results.getresult()	
	
	elif len(orstring) == 2:
		orone = orstring[0]
		ortwo = orstring[1]
		orone = string.strip(orone)		
		ortwo = string.strip(ortwo)

		results = mydbase.query("select * from diary where (descript ~~ '%"+ortwo+"%' OR descript ~~ '%"+orone+"%')")
		results = results.getresult()
	
	else:
		results = mydbase.query("select * from diary where descript ~~ '%"+mystring+"%'")
		results = results.getresult()

	
	if len(results) == 0: total = 0	

  	if len(results) > 0: total = len(results) 

	print '<BR CLEAR="all">\n<HR>\n'

	if len(results) > 0:
		for item in range(len(results)):
			print "<P>\n"
			print "<dt>\n"
			print item+1
			print ")"
			print '<IMG SRC="/images/point_02.gif">'
			temp = results[item][0]
			day = temp[3:5]
			month = temp[0:2]
			year = temp[6:]
			std_date = year+'-'+month+'-'+day
			print '<a href="/cgi-bin/archivewx/wxdata/search.py?day='+day+'&month='+month+'&year='+year+'">'+std_date+'</a>'
	        	print '<BR>'+results[item][1] + '<br>\n'  


	else:		
		print "No results were found"

	print '</dl>\n'

	print '</html>'
	style.std_bot()
Main()
