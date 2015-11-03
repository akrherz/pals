#!/usr/local/bin/python

import os, posix

def Main():
	dir = "/home/httpd/cgi-bin/tmp/"
	filelist = posix.listdir(dir)
	print filelist


Main()
