#!/usr/local/bin/python

import sys, re, regsub, os, urllib, urlparse, regex, string
from cgi import *

def html_getter(url, file):
	if file != "none":
		url = urlparse.urljoin(url,file)
	 

        f = urllib.urlopen(url) 
        page = f.readlines() 

        for i in range(len(page)): 
                line = page[i]
		if string.find(line, 'href="') != -1: 
			line = regsub.gsub('href="','href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/dominator.py?url='+url+'&file=',line)

		if string.find(line, 'HREF="') != -1: 
			line = regsub.gsub('HREF="','href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/dominator.py?url='+url+'&file=',line)
		
		if string.find(line, 'ACTION="') != -1: 
                        line = regsub.gsub('ACTION="','ACTION="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/dominator.py?url='+url+'&file=',line) 

		if string.find(line, 'BASE HREF') != -1: 
                        line = regsub.gsub('<BASE HREF=','<FONT=',line)

		if string.find(line, 'base href') != -1: 
                        line = regsub.gsub('<base href=','<FONT=',line)
		
		if string.find(line, 'BASE href') != -1: 
                        line = regsub.gsub('<BASE href=','<FONT=',line) 

		if string.find(line, '=POST') != -1: 
                	#line = regsub.gsub('=POST','=GET',line)
			print '<H1>Dominator does not support forms yet.</H1>'
			sys.exit()
		if string.find(line, '="POST"') != -1: 
                        #line = regsub.gsub('="POST"','="GET"',line)
			print '<H1>Dominator does not support forms yet.</H1>'
                        sys.exit()		
		if string.find(line, '404 Not Found') != -1: 
			print '<H1>Dominator is having trouble loading this page.</H1>'
			sys.exit()
		if string.find(line, 'moved path') != -1: 
                        print '<H1>Dominator is having trouble loading this page.</H1>'
                        sys.exit()		
		print line

def Main():
	form = FormContent()
 	file = "none"
	url = "/home/dominator.html"
	if form.has_key("url"): url = form["url"][0]
        if form.has_key("file"): file = form["file"][0]
	print "Content-type: text/html\n\n"  
	print '<header>\n'
	base = url
	if file[0] == "h":
		base = file
	elif file[0] != "none":
		if file[0] != "h":
			base = urlparse.urljoin(url,file)

	## Need to make the base url trail with a /##
		
	base = urlparse.urlparse(base)
	if base[0][2] == '':
		base[0][2] = '/'
	base = urlparse.urlunparse(base)

	print '<base href="'+base+'">'
	print '<title>Dominator</title>\n</header>\n'  


	html_getter(url, file) 

