#!/usr/local/bin/python
# This program asks for a new spec for database
# Daryl Herzmann 9/19/98

import os, sys, regsub
from cgi import *

def html_content(area):
	print '<form method="POST" action="insert_spec.py">'
	print '<input type="hidden" value="'+area+'" name="area">'
	print '<H4> Enter a new topic under '+area+'  here:'
	print '<input type="text" name="spec">'
	print '<input type="submit" value="Add this topic">'
	print '</form>'

def Main():
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD></HEAD><BODY BGCOLOR="white">'

	form = FormContent()
	area = form["area"][0]
	
	area = regsub.gsub(" ","_", area)

	html_content(area)
Main()
