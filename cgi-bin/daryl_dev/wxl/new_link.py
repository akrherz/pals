#!/usr/local/bin/python
# This program asks for a new link for database
# Daryl Herzmann 9/19/98

import os, sys
from cgi import *

def html_content(area, spec, user):
	print '<H3> Adding a new topic under '+area+'  '+spec+'</H3>' 
	print '<form method="POST" action="insert_link.py">'
	print '<input type="hidden" value="'+area+'" name="area">'
	print '<input type="hidden" value="'+user+'" name="user">'
	print '<input type="hidden" value="'+spec+'" name="spec">'
	print 'Enter the title of this link:'
	print '<input type="text" name="link">'
	print '<BR> Enter the URL of this file:'
	print '<input type="text" name="url">'
	print '<input type="submit" value="Submit your request">'
	print '</form>'

def Main():
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD></HEAD><BODY BGCOLOR="white">'

	form = FormContent()
	area = form["area"][0]
	spec = form["spec"][0]
	user = form["user"][0]
	
	html_content(area, spec, user)
Main()
