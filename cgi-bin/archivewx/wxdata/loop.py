#!/usr/local/bin/python
# This program will be a frontend to the genloop.py
# Daryl Herzmann 2-24-2000

import time, std_form


def Main():
	print 'Content-type: text/html \n\n'
	print """
	<HTML>
		<HEAD><TITLE>PALS Weather Data Looper</TITLE></HEAD>
	<body bgcolor="white">
		<H2 align="center">PALS Weather Data Animator</H2>

	<P><b>Note:</b>I fixed the "Current Animations" so that indeed recent data is displayed.

	"""	

	now = time.time()
	now = time.gmtime(now - 3600)
	nowStr = time.strftime("%Y%m%d%H", now)

	print '<FORM METHOD="GET" action="genloop.py" target="_top">'
	print '<input type="hidden" name="dateStr" value="'+nowStr+'">'

	print """
	<font color="red"><h3>View Current Animations:</h3></font>
	<TABLE>
	<TR>
	<TH>Select a map type:</TH>
		<TD><SELECT name="mapType">
			<option value="sfc">Surface Analysis
			<option value="temp">Surface Temperatures
			<option value="moist">Moisture Divergence
			<option value="dew">Surface Dewpoint
			<option value="wvap">Water Vapor
			<option value="sat">IR Satelitte
		</SELECT></TD></TR>

	<TR>
	<TH>Select the time span of this loop:</TH>
		<TD><SELECT name="increment">
			<option value="-3">Past 3 Hours
			<option value="-4">Past 4 Hours
			<option value="-5">Past 5 Hours
			<option value="-6">Past 6 Hours
			<option value="-7">Past 7 Hours
			<option value="-8">Past 8 Hours
			<option value="-9">Past 9 Hours
			<option value="-10">Past 10 Hours
		</SELECT></TD></TR>

	<TR><TD colspan="2">
	<input type="SUBMIT">
	<input type="reset">
	</form></TD></TR></TABLE>
	<HR>
		<H2>Or...</H2>
	<HR>
	<font color="red"><h3>View an Archived Animation:</h3></font>
	<FORM METHOD="GET" name="archive" action="genloop.py" target="_top">
	<input type="hidden" value="yes" name="buildDate">
	<TABLE>
	<TR>
	<TH>Select a map type:</TH>
		<TD><SELECT name="mapType">
			<option value="sfc">Surface Analysis
			<option value="temp">Surface Temperatures
			<option value="moist">Moisture Divergence
			<option value="dew">Surface Dewpoint
			<option value="wvap">Water Vapor
			<option value="sat">IR Satelitte
			<option value="nowrad">NOWRAD
		</SELECT></TD></TR>
	<TR>
	<TH>Select a year:</TH>
		<TD><SELECT name="year">
			<option value="1998">1998
			<option value="1999">1999
			<option value="2000">2000
		</SELECT></TD></TR>
	<TR>
	<TH>Select a month:</TH>
	<TD>
	"""
	std_form.months()
	print '</TD></TR>'

	print '<TR><TH>Select A day:</TH><TD>'

	std_form.days()
	print '</TD></TR>'

	print '<TR><TH>Select A Start Hour:</TH><TD>'
	std_form.ztimes()
	print '</TD></TR>'

	print """
	<TR><TH>How Long a timeSpan:</TH>
		<TD><SELECT name="increment">
                        <option value="3">+3 Hours
                        <option value="4">+4 Hours
                        <option value="5">+5 Hours
                        <option value="6">+6 Hours
                        <option value="7">+7 Hours
                        <option value="8">+8 Hours
                        <option value="9">+9 Hours 
                        <option value="10">+10 Hours
                </SELECT></TD></TR>
	<TR><TD colspan="2">
	<input type="SUBMIT">
	<input type="reset">
	</TD></TR></TABLE>
	"""

Main()

