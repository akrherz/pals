#!/usr/local/bin/python

# We can not use the functs file, it is too different
import cgi, pg, time, svrFrcst, sys, style
usersTable = "users"	

def ask_for_info(case_num, key, className):
	print """
	<font color="blue"><H2>Instructions:</H2></font>

	<P>Before you can begin this exercise, you need to enter your name and email address so that your
	instructor can grade your results.  It is therefore important to enter correct information below.

	<form method="POST" action="index.py">"""
	
	print '<input type="hidden" name="className" value="'+className+'">'	
	print '<input type="hidden" name="case_num" value="'+case_num+'">'	
	print '<input type="hidden" name="key" value="'+str(key)+'">'
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

	<input type="submit" value="Start Excercise">
	<input type="reset"> 
	</form>
	<BR>
	"""

def mk_new_entry(ldb, className):
	key = str(int(float(time.time())))		# we generate the key that the user will be using for the day
	input = ldb.query("INSERT into "+usersTable+" VALUES ("+key+") ")	# Create the entry in the db
	create = ldb.query("CREATE TABLE s"+key+" (ticks varchar(20), question varchar(1000), answer varchar(2000), cor_answer varchar(200) ) ")
	return key


def Main():
	form = cgi.FormContent()
	if not form.has_key("case_num"):
		style.SendError("No case number was supplied to this script")
	if not form.has_key("className"):
		style.SendError("No class name specified")

	case_num = form["case_num"][0]  
	className = form["className"][0]

	sessiondb = pg.connect('svr_'+className)
	key = mk_new_entry(sessiondb, className)

	svrFrcst.svrTop("Blah")

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
		print '<INPUT type="hidden" value="'+case_num+'" name="case_num">'
		print '<INPUT type="hidden" value="'+key+'" name="key">'
		print '<INPUT type="hidden" value="nob@nowhere.com" name="email">'
		print '<INPUT type="hidden" value="NOB" name="name">'

		print """
		<BR><input type="SUBMIT" value="Let's Start!!">
		</form>"""

		svrFrcst.svrBot()
		sys.exit(0)
	
	ask_for_info(case_num, key, className)

	svrFrcst.svrBot()
Main()
