#!/usr/local/bin/python
# This is my attempt at a php like script
# Daryl Herzmann 9-21-99

import gd, cgi

base_pic = '/home/httpd/html/src/time.gif'

def Main():
	form = cgi.FormContent()
	label = form["label"][0]

	im = gd.image(base_pic)
#	im = mk_image(im)
	

	print 'Content-type: image/gif \n\n'
	print im

Main()
