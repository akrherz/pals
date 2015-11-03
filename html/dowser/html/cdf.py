#!/usr/local/bin/python

import posix, os, sys, posixpath, string

def Main():
	localfile = open('/home/httpd/html/dowser/html/cdf.txt','w')
	comp = localfile.read()
	files = posix.listdir('/home/httpd/html/dowser/')
	os.chdir('/home/httpd/html/dowser/')
	dirs = []
	paths = []
	for i in range(len(files)):
		file = files[i]
		if posixpath.isdir(file):
			os.chdir('/home/httpd/html/dowser/'+file+'/')		
			hello = posix.getcwd()
			refs = posix.listdir(hello)
			for it in range(len(refs)):
				ref = refs[it]
				paths.append(hello+"/"+ref)
			os.chdir('/home/httpd/html/dowser/')	
	
	
	print comp
	for i in range(len(paths)):
		path = paths[i]
		localfile.write(path+"\n")
	localfile.close()
	print "Files in dowser updated"

Main()
	
