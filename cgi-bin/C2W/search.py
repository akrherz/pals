#!/usr/local/bin/python
# Main search engine for PALS C2W
# Daryl Herzmann 7/13/98

from pgext import *
from cgi import *
import os, string, sys, regsub, re, style, c2w2, std_table

mydbase = connect("c2w")

def Main():
	skip = 0
	form = FormContent()
	if not form.has_key("string"): style.SendError("You did not input a search string")
	if not form.has_key("field"): style.SendError("no search field found")
	mystring = form["string"][0]
	field = form["field"][0]
	filename = form["filename"][0]
	if form.has_key("skip"): skip = form["skip"][0]

	style.header("C2W Search Results","white")
	std_table.blue_top('Results of your search for: "'+mystring+'"')
	print '<TR><TD colspan="2">'
	c2w2.new_search(mystring,field,filename,skip)	
	print '</TD></TR>'
	print '<TR><TD colspan="2">'
	style.std_bot()	
	print '</TD></TR></TABLE>'
Main()
	
