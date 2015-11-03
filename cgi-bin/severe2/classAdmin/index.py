#!/usr/local/bin/python
# This is the main page for class admin

import cgi, style, os, SEVERE2

def Main():
	form = cgi.FormContent()
	className = os.environ["REMOTE_USER"]

	SEVERE2.setupPage("classAdmin for Sx Wx Forecasting")
	
	print '<H3>Current ClassName: '+className+'</H3>'

	print """
	<blockquote>
	This is the main page showing you the options for editing within the Forecasting Activity.  The only required editing involves
	adding or releasing cases for use by your students.  The cases are basically pre-built and ready to use, but please review the case 
	first before adding it...
	</blockquote>
	"""

	print """
	<P><a href="spec_questions/index.py">Create / Edit Specific Questions</a>
	<dd>This option allows you to create specific questions that will appear when users in your class
work though the exercise.</dd>
	"""

	print """
	<P><a href="cases/release.py">Release / Revoke Cases to Class</a>
	<dd>This option releases and revokes cases for your class to work through.  Once a case is
released, it will appear on the main page that your students start the exercise from.</dd>
	"""

	print """
	<P><a href="annote/hourly.py">Edit Hourly Annotations</a>
	<dd>This option allows you to edit the hourly annotations that appear throughout the exercise.</dd>
	"""

#	print '<a href="intro/index.py">Edit The Case Introduction</a><BR>'

	SEVERE2.finishPage()
Main()
