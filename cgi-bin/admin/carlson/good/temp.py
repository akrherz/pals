#!/usr/local/bin/python
# This will give the option of which file they want to edit
# Daryl Herzmann 5-28-99

import os, cgi, style, string
from pgext import *

mydb = connect('carlson')

base_fref = '/home/httpd/html/carlson'
images_dir = base_fref+"/images"



def Main():
	files = os.listdir(images_dir)
	for file in files:
		file = string.split(file, ".")
		thisfile = file[0]

		insert = mydb.query("INSERT into images values('"+thisfile+"')")

		print thisfile

Main()
