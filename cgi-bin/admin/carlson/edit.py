#!/usr/local/bin/python
# This edits the file by given the users a bunch of options
# Daryl Herzmann 5-28-99

import cgi, style, os, string
from pgext import *

image_href = "https://pals.agron.iastate.edu/carlson/images/"
images_dir = "/home/www/pals/html/carlson/images/"
html_dir = "/home/www/pals/html/carlson"

mydb = connect('carlson')

def mk_option(file, searchingfor):
	print '<OPTION'
	if file == searchingfor:
		print 'SELECTED'
	print '>'+file

def Main():
	form = cgi.FormContent()
	file = form["file"][0]

	results = mydb.query("SELECT path, title, txt, next from images where file = '"+file+"'")
	results = results.getresult()
	try:
		orig_path = results[0][0] 
		orig_title = results[0][1] 
		orig_txt = results[0][2] 
		orig_next = results[0][3] 
	except IndexError:
		orig_path = ""
		orig_title = ""
		orig_txt = ""
		orig_next = ""

	style.header("Edit information for file "+file, "white")
	print '<H3>Edit information for file '+file+'</H3>'

	print '<form METHOD="post" action="change.py">'
	print '<IMG SRC="'+image_href+file+'.jpg" WIDTH="300">'
	print '<INPUT TYPE="hidden" name="file" value="'+file+'">'
	print '<H4>Enter directory path:</H4>'

	dirs = os.listdir(html_dir)
	dirs.sort()
	print '<SELECT name="path">'
	for dir in dirs:
		if (os.path.isdir(html_dir+"/"+dir)):
			more_dirs = os.listdir(html_dir+"/"+dir)
			for more in more_dirs:
				if (os.path.isdir(html_dir+"/"+dir+"/"+more)):
					mk_option(dir+"/"+more, orig_path)
			mk_option(dir, orig_path)
	print '</SELECT>'

	print '<H4>Enter the Title of the photo</H4><INPUT TYPE="text" name="title" SIZE="80" value="'+orig_title+'">'
	print '<H4>Select the next file:</H4>'
	print '<SELECT name="next">'
        filez = os.listdir(images_dir)
        filez.sort()
	for files in filez:
                files = string.split(files, ".")
                mk_option(files[0], orig_next)
	print '<option SELECTED>None'
        print '</SELECT>'

	print '<H4>Enter the text for the file:</H4>'
	print '<textarea name="txt" cols="60" rows="5" WRAP>'+orig_txt+'</textarea>'

	print '<INPUT type="submit">'

	print '</form></body></html>'

Main()
