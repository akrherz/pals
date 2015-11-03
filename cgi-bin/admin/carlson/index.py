#!/usr/local/bin/python
# This will give the option of which file they want to edit
# Daryl Herzmann 5-28-99

import os, cgi, style, string, pg

mydb = pg.connect('carlson')

base_fref = '/home/httpd/html/carlson/'
images_dir = base_fref+"images/"

def listFiles():
	print '<SELECT name="file" size="15">'
	files = mydb.query("SELECT file from images").getresult()
	files.sort()
	for i in range(len(files)):
		file = string.split(files[i][0], ".")
		print '<OPTION>'+file[0]
	print '</SELECT>'


def Main():
	style.header("Edit Carlson Picts","white")

	print '<H3> Select a file to edit info for: </H3>'

	print '<FORM method="POST" action="edit.py">'

	listFiles()

	print '<input type="SUBMIT" value="Edit">'

	print '</form></body></html>'

	style.std_bot()

Main()
