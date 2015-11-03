#!/usr/local/bin/python
# This starts people into editing the archivewx databases
# Daryl Herzmann 8/8/98

from cgi import *
import sys, os, style

form = FormContent()
which_page = form["page"][0]
password = form["password"][0]


def checker():
	real_pass = "pals1998"
	if real_pass != password:
		style.SendError("Go back and enter a different password!")

def Main():
	checker()
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL='+which_page+'">'
	print '</HEAD></HTML>'
	sys.exit(0)

Main()
