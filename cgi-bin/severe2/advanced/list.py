#!/usr/bin/env python2
# This program will generate a ClassNet like output...
# Daryl Herzmann 12-7-99

import pg, cgi, sys, time, SEVERE2, mx.DateTime, style

basedb = pg.connect('severe2', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)

def askForClass():
	print """
	<blockquote>Your link into this exercise did not specify a class to work this exercise as.  If you are using this exercise
	as a part of a class, then please select that class below.  If you are testing out this exercise, then use the "PALS Testing Class."
	</blockquote>
	<CENTER>
	<form method="POST" action="list.py">
	<SELECT name="className" size="5">"""

	classes = advdb.query("SELECT class_abv, classname from classes").dictresult()
	for i in range(len(classes)):
		class_abv = classes[i]["class_abv"]
		classname = classes[i]["classname"]
		print '<option value="'+class_abv+'">'+classname
	print '</SELECT><BR>'

	print '<input type="SUBMIT" value="Login"></form>'
	print '</CENTER>'

def list_cases2(className, caseType):

	if (className == "test"):
		cases2 = advdb.query("SELECT casenum from basecases WHERE caseNum ~* '"+caseType+"' ").dictresult()
	else:
		cases2 = advdb.query("SELECT casenum from basecases_custom WHERE className = '"+className+"' and caseNum ~* '"+caseType+"' ").dictresult()

#	print '<MULTICOL COLS="3">'
	cases2.sort()
	for i in range(len(cases2)):
		thisCase = cases2[i]["casenum"]
		cases = basedb.query("SELECT starttime  from cases WHERE casenum = '"+thisCase+"' ").dictresult()   
		startTime = cases[0]["starttime"]

		startDate = mx.DateTime.ISO.ParseDateTimeGMT( startTime )
		if className == "test":
			print '<a href="/cgi-bin/severe2/advanced/first.py?test=yes&className='+className+'&caseNum='+thisCase+'">'+startDate.strftime("%d %B %Y")+'</a>'
		else:
			print '<a href="/cgi-bin/severe2/advanced/first.py?className='+className+'&caseNum='+thisCase+'">'+startDate.strftime("%d %B %Y")+'</a>'
		print '&nbsp; &nbsp; &nbsp; &nbsp; '
		if (i%3 == 0 and i != 0):
			print '<BR>'
#	print '</MULTICOL>'


def makePage(className):
	SEVERE2.setupPage("Sx Wx Forecasting Activity | Advanced Version")
	
	print """<CENTER>
	<img src="/icons/svrTop.gif">
	</CENTER>
	<blockquote>
	The Severe Weather Forecasting Exercise is a web-based exercise that is designed to stimulate interest in severe weather. This
	exercise is being developed for use by all levels of meteorologists and K-12 students as well. Because of the wide range of skills
	among users, there are three versions of the forecasting exercise.

	<P>The exercise is worked by trying one of the cases below.  The case uses archived data and prepared questions to guide the user
	thoughout the cases duration.  Currently, we have two types of cases: the "Summer-like Events" contain questions that concern summer
	like severe weather (tornado, hail, heavy rain), and the "Winter-like Events" stress winter severe weather phenonema.

	<P>The advanced version of the exercise has been designed to allow any instructor administrative control over the exercise.  Once you 
	are an administrator, you can customize the questions that appear and allow your students to work through cases that you hand select.
	The results of your students work is then emailed back to you for your review.  More information on this feature can be found 
	<a href="/svr_frcst/advInstructor.html">here.</a>

	</blockquote>
	<H2><font color="#a0522d">Advanced Version:</font></H2>
			<dd>The advanced version of the forecasting exercise contains questions that are geared to upper-level meteorology students and prodessional meteorologists.
			</dd>
		"""

	print "<H3>Summer-like Events:</H3>"
	list_cases2(className, "s")

	print "<H3>Winter-like Events:</H3>"
	list_cases2(className, "w")
	SEVERE2.finishPage("advanced", className)
	sys.exit(0)


def Main():
	
	form = cgi.FormContent()
	if form.has_key("className"):
		className = form["className"][0]
		origPass = advdb.query("SELECT classpasswd from classes WHERE class_abv = '"+className+"' ").dictresult()[0]["classpasswd"]

		if form.has_key("classpasswd"):
			classpasswd = form["classpasswd"][0]					
			if classpasswd != origPass:
				style.SendError("The password you entered was incorrect, Try again.")
			makePage(className)
		elif origPass == "No" or form.has_key("sstr"):
			makePage(className)			

		elif origPass != "No":
			SEVERE2.setupPage("Class Authentification.")
			print '<H3>Password Required:</H3>'
			print '<P>This class requires a password, please enter it now.'
			print '<form method="POST" action="list.py">'
			print '<input type="hidden" name="className" value="'+className+'">'	
			print '<BR><B>Enter Password:</B> <input type="text" name="classpasswd">'
			print '<BR><input type="SUBMIT" value="Enter Exercise">'
			print '</form>'
			SEVERE2.finishPage("advanced")
			sys.exit(0)

		else:
			style.jump_page("first.py?className="+className+"&caseNum="+caseNum+"")

	else:
		SEVERE2.setupPage("Sx Wx Forecasting Activity | Advanced Version")
		askForClass()
		SEVERE2.finishPage("advanced")
		sys.exit(0)	


Main()
