#!/usr/local/bin/python
# This will display the weather links on the top of the forms page
# Daryl Herzmann 9/19/98
# UPDATED 6-4-99: Gonna make this work....

import sys, os
from cgi import *
from pg import *

mydb = connect('wx_areas')
mydb2 = connect('wx_links')

def setup_html():
	print 'Content-type: text/html \n\n'
	print '<HTML>\n<HEAD></HEAD>\n<BODY BGCOLOR="red">'
	print '<form method="POST" action="top.py" name="weather">'
	print '<IMG SRC="/~akrherz/wxadmin/wx_title.gif" align="center">'


def area_loader(real_area):
	print '<SELECT name="area" onChange="location=this.form.area.options[this.form.area.selectedIndex].value">'
#	areas = mydb.query("Select area from mt101").getresult()
#	areas.sort()
	areas = ('Hemispheric','United_States','MidWest','Iowa','Local')
	test_4_rep = "no"
	selected = "no"
	for i in range(len(areas)):
		area = areas[i]
		if test_4_rep == area: 
			continue
		if area == real_area: 
			selected = "SELECTED"
		print '<option value="top.py?area='+area+'" '+selected+'>'+area
		test_4_rep = area
		selected = "no"
	print '</select>' 

def spec_loader(area, real_spec):
	print '<SELECT name="spec" onChange="location=this.form.spec.options[this.form.spec.selectedIndex].value">'
	specs = mydb.query("Select spec from mt101 WHERE area = '"+area+"'").getresult()
	specs.sort()
	test_4_rep = "no"
	selected = "no"
	print '<option value="top.py"> (Select Topic)' 
	for i in range(len(specs)):
		spec = specs[i][0]
		if test_4_rep == spec: 
			continue
		if spec == real_spec: 
			selected = "SELECTED"
		print '<option value="top.py?area='+area+'&spec='+spec+'" '+selected+'>'+spec
		test_4_rep = spec
		selected = "no"
	print '<option value="new_spec.py?area='+area+'">-- Add new --' 
	print '</select>' 
	
def link_loader(area, spec):
	print '<SELECT name="link" onChange="parent.display.location=this.form.link.options[this.form.link.selectedIndex].value">'
	links = mydb2.query("Select * from mt101 WHERE area = '"+area+"' AND spec = '"+spec+"'").getresult()
	links.sort()
	print '<option value="/~akrherz/wxadmin/bottom.html"> (Links) ' 
	for i in range(len(links)):
		link = links[i][3]
		url = links[i][2]
		print '<option value="'+url+'">'+link
	print '<option value="new_link.py?area='+area+'&spec='+spec+'">-- Add new --' 
	print '</select>' 
	

def Main():
	setup_html()

	area = "no"
	spec = "no"
	form = FormContent()
	if form.has_key("area"): area = form["area"][0]
	if form.has_key("spec"): spec = form["spec"][0]

	area_loader(area)
	if area != "no": spec_loader(area, spec)
	if spec != "no": link_loader(area, spec)

	print '</form></body></html>'
	sys.exit()
Main()

