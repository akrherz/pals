#!/usr/local/bin/python 
# Submits links
# Daryl Herzmann 7/14/98

from pgext import * 
from cgi import *
import os, sys, regsub, style

mydbase = connect("c2w")

def Main(): 
	form = FormContent()
	
	if not form.has_key("link"): style.SendError("Enter a Link")
	mylink = form["link"][0]
	mylink = regsub.gsub("'","&#180;",mylink)
	
	if not form.has_key("URL"): style.SendError("Enter an URL")
	myURL = form["URL"][0]

	if not form.has_key("description"): style.SendError("What is it's description")
	mydescription = form["description"][0]
	mydescription = regsub.gsub("'","&#180;",mydescription)

	style.header('Links Submitter','/images/ISU_bkgrnd.gif')

	mykindA = "null"
	mykindB = "null"
	mykindC = "null"
	mykindD = "null"

	if form.has_key("kindA"): mykindA = form["kindA"][0]
	if form.has_key("kindB"): mykindB = form["kindB"][0]
	if form.has_key("kindC"): mykindC = form["kindC"][0]
	if form.has_key("kindD"): mykindD = form["kindD"][0]

	mytime = os.popen('date', 'r').read()
	
	search = mydbase.query("select * from linkex where url = '"+myURL+"'")
	search = search.getresult()
	
	if len(search) > 0:
		style.std_top("URL already taken")
		sys.exit(0)
	
	search2 = mydbase.query("select * from linkex where link = '"+mylink+"'") 
        search2 = search2.getresult()

	if len(search2) > 0:
		style.std_top("Link title aready taken")
		sys.exit(0)
	
	enter = mydbase.query("INSERT INTO linkex VALUES( ' " + mylink+"','"+myURL+"','"+mykindA+"','"+mykindB+"','"+mykindC+"','"+mykindD+"','"+mydescription+"', '"+mytime+"')")
	
	style.std_top('Your link to "'+mylink+'" was saved!')
	print '<br><P>You can now:<ul>'
	print '<li><a href="http://www.pals.iastate.edu/cgi-bin/daryl_dev/printout.py">View all the links</a>'
	print '<li><a href="http://www.pals.iastate.edu/index.html">Go back to PALS Homepage</a>'	
	print '<spacer type="vertical" size="300">'
	style.std_bot()
Main()
