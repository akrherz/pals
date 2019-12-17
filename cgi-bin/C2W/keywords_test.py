#!/usr/local/bin/python
# This will load the keywoards database
# Daryl Herzmann 1/13/99

import sys, os, regsub, string, style
from pgext import *

mydbase = connect("c2w")

def links():
        print '<a href="/index.html">Go to PALS Homepage</a>--'
	print '<a href="/c2w/index.html">COMET mainpage</a>--'
        print '<a href="/c2w/adm/help.html">Get help on Searching</a>--'
        print '<a href="/home/email.html">Contact Us</a>--'
        print '<a href="/c2w/adm/access.html">Access previous search</a><HR>'

def words():
	print '<H3><center>Select a Keyword:</center></H3>'
	words = mydbase.query("select * from keywords")
	words = words.getresult()
	words.sort()

	print '<multicol cols="5">'

	for i in range(len(words)):
		word = words[i][0]
		print '<input type="radio" name="string" value="'+word+'">'+word
		print '<br>'	

	print '</multicol>'

def dirs():
	print '<H3><center>In directories:</center></H3>'
	print '<select name=filename>'
	print '<option value="all" selected>All directories'
	print '<option value="acsse">ACSSE'	
	print '<option value="csm">CSM'
	print '<option value="fire">Fire'
	print '<option value="forecast">Forecast'
	print '<option value="hydro">Hydro'
	print '<option value="marine1">Marine I'
	print '<option value="marine2">Marine 2'
	print '<option value="satellite1">Satellite I'
	print '<option value="satellite2">Satellite 2'
	print '</select>'
	
def fields():
	print '<H3><center>Search in:</center></H3>'
	print '<SELECT NAME="field">'
	print '<OPTION VALUE="description" SELECTED>Description only'
	print '<option value="filename">Filename only'
	print '<option value="both">Description and Filename'
	print '</select>'

def Main():
	style.header("Keywords for Database","white")
	style.std_top("COMET Keyword Searches")
	print '<form method="post" action="https://pals.agron.iastate.edu/cgi-bin/C2W/search.py">'
	words()
	print '<HR>'
	dirs()
	print '<HR>'
	fields()
	print '<HR>'
	print '<center><input type="submit" value="Search for keyword">'
	print '</form>'
	style.std_bot()
Main()
