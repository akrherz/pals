#!/usr/local/bin/python
# Main search engine for PALS C2W
# Daryl Herzmann 7/13/98

from pgext import *
from cgi import *
import os, string, sys, regsub, re, style, c2w 

mydbase = connect("c2w")

def Main():
	form = FormContent()
	if not form.has_key("string"): style.SendError("You did not input a search string")
	if not form.has_key("field"): style.SendError("no search field found")
	mystring = form["string"][0]
	field = form["field"][0]
	filename = form["filename"][0]

	style.header("C2W Search Results","white")
	style.std_top('Results of your search for "'+mystring+'"')
        print '<a href="http://www.pals.iastate.edu/c2w/adm/search.html">New Search</a>--'
	print '<a href="http://www.pals.iastate.edu/c2w/adm/access.html">Access Saved Search</a>'

	c2w.old_search(mystring,field,filename)	
	style.std_bot()	
Main()
	
