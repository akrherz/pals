#!/usr/bin/env python

# We can not use the functs file, it is too different
import cgi, pg, time, svrFrcst, sys, style, SEVERE2
advdb = pg.connect('severe2_adv', 'localhost', 5432)
tmpdb = pg.connect('severe2_tmp', 'localhost', 5432)

def ask_for_info(caseNum, userKey, className):
	print """
	<font color="blue"><H2>Instructions:</H2></font>

	<P>Before you can begin this exercise, you need to enter your name and email address so that your
	instructor can grade your results.  It is therefore important to enter correct information below.

	<form method="POST" action="index.py">"""
	
	print '<input type="hidden" name="className" value="'+className+'">'	
	print '<input type="hidden" name="caseNum" value="'+caseNum+'">'	
	print '<input type="hidden" name="userKey" value="'+str(userKey)+'">'
	print '<INPUT type="hidden" value="True" name="answerQs">'

	print """
	<font color="blue"><H2>Enter your information:</H2></font>
	<TABLE border="0">
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your Name:</font>
		</TH><TD>
			<input size="40" MAXLENGTH="40" type="text" name="name">
		</TD></TR>
	<TR>
		<TH bgcolor="#EEEEEE">
			<font size="3">Enter your Email Address:</font>
		</TH><TD>
			<input size="40" MAXLENGTH="40" type="text" name="email">
		</TD></TR>
	</TABLE>

	<input type="submit" value="Start Exercise">
	<input type="reset"> 
	</form>
	<BR>
	"""


def mk_new_entry():
	userKey = str(int(float(time.time())))		# we generate the key that the user will be using for the day
	input = advdb.query("INSERT into users VALUES ("+userKey+") ")	# Create the entry in the db
	tmpdb.query("CREATE TABLE s"+userKey+" (ticks varchar(30), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
	return userKey


def Main():
	form = cgi.FormContent()
	if not form.has_key("caseNum"):
		style.SendError("No case number was supplied to this script")
	if not form.has_key("className"):
		style.SendError("No class name specified")

	caseNum = form["caseNum"][0]  
	className = form["className"][0]

	userKey = mk_new_entry()

	SEVERE2.setupPage("Welcome to the Severe Weather Forecasting Activity")

	if form.has_key("test"):
		print """
		You may proceed through this exercise as a guest of this system.  Your answers will not be emailed to anybody.<BR>
		<BR>You may want to choose to not answer any of the specific questions that pop up during the exercise.  This helps to
		speed up the exercise quite a bit.  You will still be asked the questions about where you believe severe weather to occur.
		<BR><BR>
		<form method="POST" action="index.py">
		<input name="answerQs" value="True" CHECKED  type="radio">Answer Questions<BR>
		<input name="answerQs" value="False" type="radio">No questions please<BR>
		"""
		print '<INPUT type="hidden" value="'+className+'" name="className">'
		print '<INPUT type="hidden" value="'+caseNum+'" name="caseNum">'
		print '<INPUT type="hidden" value="'+str(userKey)+'" name="userKey">'
		print '<INPUT type="hidden" value="nob@nowhere.com" name="email">'
		print '<INPUT type="hidden" value="NOB" name="name">'

		print """
		<BR><input type="SUBMIT" value="Let's Start!!">
		</form>"""

		SEVERE2.finishPage("advanced", className)
		sys.exit(0)
	
	ask_for_info(caseNum, userKey, className)

	SEVERE2.finishPage("advanced", className)

Main()
