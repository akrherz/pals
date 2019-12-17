#!/usr/local/bin/python
# My attempt to "dominate" HTML code from other locations
# Daryl Herzmann 9/11/98

	# Python imports
import sys, re, regsub, os, urllib, urlparse, regex, string
from cgi import *

	# Define some constants used thoughout
dominator_href = "https://pals.agron.iastate.edu/cgi-bin/daryl_dev/dominator.py"

def gifGetter(url, file):
    if file != "none":
	    url = urlparse.urljoin(url,file)
    f = urllib.urlopen(url).read()
    print f


def html_getter(url, file):
		# Assigning the url to be the file + the url
	if file != "none":
		url = urlparse.urljoin(url,file)

		# Some priliminary variables, before begining the loop
		# Forms stuff, still needs work...
	hidden = "no"
	another = "no"

		# Opening up the file location
        f = urllib.urlopen(url) 
        page = f.readlines()

		# parsing through the html file 
        for i in range(len(page)): 

			# If the previous loop found something, I am attemping to master form pages
			# I still can not figure out how to do this.....
			# ________________________________________________________________________
                if another == "yes":
			another = "notyet"
			# I am in the middle of a <form> and a </form>, need to enter hidden values
		if hidden == "yes":
                        if another == "now":
				print '<input type="hidden" name="url" value="'+url+'">'
			elif another == "no":
				print '<input type="hidden" name="url" value="'+url+'">'
		if another != "notyet":
			hidden = "no"

			# ________________________________________________________________________
			# Simple replacing of <a href's>
		line = page[i]
		if string.find(line, 'href="') != -1: 
			line = regsub.gsub('href="','href="'+dominator_href+'?url='+url+'&file=',line)

		if string.find(line, 'HREF="') != -1: 
			line = regsub.gsub('HREF="','href="'+dominator_href+'?url='+url+'&file=',line)
		
		if string.find(line, 'ACTION="') != -1: 
                        line = regsub.gsub('ACTION="','ACTION="'+dominator_href+'"> <input type="hidden" name="cgifile" value="',line) 
                        first = line[:-3]
                        second = '?">'   
                        line = first+second

		if string.find(line, 'action="') != -1:
		      	line = regsub.gsub('action="','ACTION="'+dominator_href+'"> <input type="hidden" name="cgifile" value="',line) 
			first = line[:-3]
			second = '?">'
			line = first+second

			# Ridding of any other base refs in the html doc, changing them to font tages
		if string.find(line, 'BASE HREF') != -1: 
                        line = regsub.gsub('<BASE HREF=','<FONT=',line)

		if string.find(line, 'base href') != -1: 
                        line = regsub.gsub('<base href=','<FONT=',line)
		
		if string.find(line, 'BASE href') != -1: 
                        line = regsub.gsub('<BASE href=','<FONT=',line) 


			################################### Atempting Forms, work to be done ####################
		if string.find(line, '=POST') != -1: 
                	line = regsub.gsub('=POST','=GET',line)
			hidden = "yes"
			halves = string.split('=POST','line',1)
			if string.find(halves[1], '>') != -1:
				another = "no"
			else:
				another = "yes"
	
		if string.find(line, '="POST"') != -1: 
                        line = regsub.gsub('="POST"','="GET"',line)
			hidden = "yes"
			halves = string.split('="POST"','line',1)
                        if string.find(halves[0][1], '>') != -1:
                                another = "no"
                        else:
                                another = "yes"
		if string.find(line, '=post') != -1:
                        line = regsub.gsub('=post','="GET"',line)
                        hidden = "yes"
                        halves = string.split('=post','line',1)
                        if string.find(halves[0][1], '>') != -1:
                                another = "no"
                        else:
                                another = "yes"
		if string.find(line, '="post"') != -1:
                        line = regsub.gsub('="post""','="GET"',line)
                        hidden = "yes"
                        halves = string.split('="post"','line',1)
                        if string.find(halves[0][1], '>') != -1:
                                another = "no"
                        else:
                                another = "yes"

			# Cute little things, for when dominator screws up
		if string.find(line, '404 Not found') != -1: 
			print '<H1>Dominator is having trouble loading this page.</H1>'
			sys.exit()
		if string.find(line, 'moved path') != -1: 
                        print '<H1>Dominator is having trouble loading this page.</H1>'
                        sys.exit()		
			
			# finally print the line, after being modified
		print line

			# more forms stuff
		if another == "notyet":
			another = "now"	


def Main():
	# Set up some assignments
	# This page gets loaded to begin with, it has the info on Dominator
	url = "http://pals.agron.iastate.edu/home/dominator.html"
	file = "none"

	# Import forms values, assigns values
	form = FormContent()
	if form.has_key("url"): url = form["url"][0]
	if form.has_key("file"): file = form["file"][0]
	if form.has_key("cgifile"): file = form["cgifile"][0]

	if file[-3:] == "gif":
	    print "Content-type: image/gif\n\n"
	    gifGetter(url, file)   
	else:
	    print "Content-type: text/html\n\n"     		
	    print '<HTML><header>\n'
	    base = url
		
		
	    if file[0:3] == "htt":
	        base = file
		
	    # Or if the file is a refernce and not start with htt, then it must be a local ref
	    # then I need to join it's locate with the base ref
	    elif file != "none":
	        base = urlparse.urljoin(url,file)

	    # Need to make the base url trail with a /
	    base = urlparse.urlparse(base)

	    # If the second part is blank, then it is the home url address
	    if base[0][2] == '':
	        base[0][2] = '/'

	    # After fixing part two, I reassemble the url
	    base = urlparse.urlunparse(base)

	    # Adding the base ref to the head tag
	    print '<base href="'+base+'">'
    
	    # Adding my trademark to the page...
	    print '<title>Dominator</title>\n</header>\n'

	    # Actually getting the foriegn content of the page  
    	html_getter(url, file) 

Main()
