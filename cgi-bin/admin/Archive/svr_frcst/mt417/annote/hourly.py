#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# UPDATED 6-25-99: Added the 7 am option, we want to annotate up the early morning
# UPDATED 7-27-99: Changed the entire way that this program stores data in the db

import style, os, time, std_form, cgi


def which_hours():
	print '<B>Select an Hour to edit: '
	std_form.ztimes()
	print '<BR>'

def which_days():
	print '<B>Select a day to edit: '
	std_form.days()
	print '<BR>'

def which_months():
	print '<B>Select a month to edit: '
	std_form.months()
	print '<BR>'

def Main():
	form = cgi.FormContent()
	try:
		case = form["case"][0]
	except:
		style.SendError("I need a case reference in order to start!!")

	style.header("Edit Hourly Reports","white")
	style.std_top("Edit Hourly Reports")


	print '<B>Information:</B> <dd>This is the date and time selection page for the Severe Forecasting Excercise.</dd><BR>'
	print '<B>Instruction:</B> <dd>Select the desired day and time and then click on "submit."</dd><BR>'
	print '<B>Scope of this program:</B> <dd>This edits the annotations specifically for Dr Gallus class.</dd><BR>'
	print '<B>NOTE:</b><dd>If you are wanting to edit the preview for a case, you will want to edit the first hour that the exercise runs for.</dd>'
	print '<HR>'
	if case == 'summer':
		print 'YOU ARE EDITING ANNOTATIONS FOR SUMMER CASES, BE WARE!!'
	if case == 'winter':
		print 'YOU ARE EDITING ANNOTATIONS FOR WINTER CASES, BE WARE!!'
	print '<HR>'
	print '<form method="post" action="edit_hourly.py">'
	print '<input type="hidden" name="case" value="'+case+'">'
	print '<B>Select a year</B>'	
	print '<SELECT name="yeer">'
	print '<option value="1996">1996'
	print '<option value="1997">1997'
	print '<option value="1998">1998'
	print '<option value="1999">1999'
	print '</SELECT>'
	print '<BR>'
	if case == "summer":
		which_hours()
	else:
		print '<B>Select an Hour to edit: '
		std_form.wintimes()
		print '<BR>'
	print '<BR>'
	which_days()
	print '<BR>'
	which_months()
	print '<input type="submit" value="submit">'

	print '<HR>Links outta here:<HR>'
	print '<BR><a href="/admin">Admin Page</a>'	

	style.std_bot()
Main()
