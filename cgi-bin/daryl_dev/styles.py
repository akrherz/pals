#!/usr/loca/bin/python
# Sort of a cascade style sheet, but nicer to use!
# Daryl Herzmann 7/9/98

import os, sys, posix

def header(title, backround):
	print '<HTML>\n<HEAD>\n<TITLE>\n'
	print title
	print '</TITLE>\n</HEAD>'
	print '<body '
	if posix.isfile(backround):
		print 'backround="'+backround+'">'
	elif backround[0:4] == "http":
		print 'backround="'+backround+'">'
	else:
		print 'bgcolor="'+backround+'">'

def std_top(title):
	print '<img src="/images/pals_logo.gif" align="left">'
	print '<spacer type="vertical" size="30">'
	print '<spacer type="horizontal" size="30">'
	print '<H1>'+title+'</H1>'
	print '<BR clear="all"><HR>'
