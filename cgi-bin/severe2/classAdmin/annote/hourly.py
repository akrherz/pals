#!/usr/local/bin/python
# Edit each hours entries, another fascet of archivewx administration
# Daryl Herzmann
# REWROTE 2-1-2000

import style, os, cgi, SEVERE2

className = os.environ["REMOTE_USER"] 

def Main():
	form = cgi.FormContent()
	SEVERE2.setupPage("classAdmin for Sx Wx Forecasting")
	print """
	<H3>Edit Annotations for the Exercise.</H3>
	<blockquote>
	<B>Instructions:</B> The exercise comes pre-built with comments and annotations for each hour during the duration of each case.
	These annontations can be edited with this dialog, first select the case and then select the hour.  Your changes will imediately start
	appearing once you make the submissions.
	
	</blockquote>
	"""
	if form.has_key("caseNum"):
		print """
		<HR>
		<a href="hourly.py">Select a different Case</a><BR><HR>"""

		print '<form method="post" action="editHourly.py">'
		print '<input type="hidden" value="'+form["caseNum"][0]+'" name="caseNum">'
		SEVERE2.listHours( form["caseNum"][0] )
	else:
		print '<form method="post" action="hourly.py">'
		SEVERE2.listGoodCases()

	print '<input type="submit" value="submit">'

	print '<P>Back to <a href="../index.py">ClassAdmin Homepage</a>'

	SEVERE2.finishPage()
Main()
