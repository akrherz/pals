#!/usr/local/bin/python
# This will give the option of which file they want to edit
# Daryl Herzmann 5-28-99

import os, cgi, style, string, pg

mydb = pg.connect('carlson')

base_fref = '/home/httpd/html/carlson'
images_dir = base_fref+"/images"



def Main():
	style.header("Edit Carlson Picts","white")

	print '<H3> Select a file to edit info for: </H3>'

	print '<FORM method="POST" action="edit.py">'
	print '<SELECT name="file">'
	files = os.listdir(images_dir)
	files.sort()
	for file in files:
		file = string.split(file, ".")
		print '<OPTION>'+file[0]
	print '</SELECT>'

	print '<input type="SUBMIT" value="Edit">'

	print '</form></body></html>'

	style.std_bot()

Main()
