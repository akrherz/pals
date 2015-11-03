#!/usr/local/bin/python
# This creates a new advanced class and sets everything up
# Daryl Herzmann 8 June 2000

import SEVERE2, cgi, pals, pg, os
mydb = pg.connect('severe2_adv', 'localhost', 5432)
form = cgi.FormContent()

def newClassForm():
	print """
	<P>Please Fill out the form completely.<BR>

	<form method="POST" action="newClass.py">	
	<TABLE>
	<TR><TH colspan="2"><font color="red">Required Fields</font></TH></TR>

	<TR><TH>Enter Formal Class Name:</TH>
		<TD><input type="text" name="classname" size="40"></TD></TR>

	<TR><TH>Enter An Abbreviation for your class: (No spaces!) ex)isuMT417 </TH>
		<TD><input type="text" name="class_abv" size="20"></TD></TR>

	<TR><TH>Enter your name:</TH>
		<TD><input type="text" name="name" size="40"></TD></TR>

	<TR><TH>Enter your email address:</TH>
		<TD><input type="text" name="email" size="40"></TD></TR>

	<TR><TH>Enter A Password for your class Information:</TH>
		<TD><input type="text" name="passwd1" size="12"></TD></TR>

	<TR><TH>Validate the Password for your class Information:</TH>
		<TD><input type="text" name="passwd2" size="12"></TD></TR>

	<TR><TH colspan="2"><font color="blue">Optional Fields</font></TH></TR>

	<TR><TH>Enter a class Password.  This protects the public from using your exercise:</TH>
		<TD><input type="text" name="classpasswd" size="12"></TD></TR>

	<TR><TH colspan="2"><input type="submit" value="CREATE CLASS"><input type="reset"></TH></TR>

	</TABLE></form>"""


def enterForm():
	name = pals.formValue(form, "name")
	email = pals.formValue(form, "email")
	passwd1 = pals.formValue(form, "passwd1")
	passwd2 = pals.formValue(form, "passwd2")
	classname = pals.formValue(form, "classname")
	class_abv = pals.formValue(form, "class_abv")

	classpasswd = "No"	
	if form.has_key("classpasswd"):
		classpasswd = pals.formValue(form, "classpasswd")

	tester = mydb.query("SELECT * from classes WHERE class_abv = '"+class_abv+"' ").getresult()
	if len(tester) > 0:
		print '<font color="red">The choosen value of '+class_abv+' is allready taken. Try again.</font>'
		newClassForm()
		return

	if passwd1 != passwd2:
		print '<font color="red">The passwords did not match. Try again.</font>'
		newClassForm()
		return

	mydb.query("INSERT into classes(class_abv, classname, instructor, instructor_email, passwd, classpasswd) VALUES ('"+class_abv+"', '"+classname+"', '"+name+"', '"+email+"', '"+passwd1+"', '"+classpasswd+"') ")
	os.system("/home/httpd/httpd/bin/htpasswd -b /home/httpd/cgi-bin/severe2/classAdmin/.passwd "+class_abv+" "+passwd1+" ")

	print '<H3>Class Registration worked!  Here are your values:</H3>'

	print '<P><B>Class Abreviation:</B> '+class_abv
	print '<P><B>Class Name:</B> '+classname
	print '<P><B>Instructor Name:</B> '+name
	print '<P><B>Instructor Email:</B> '+email
	print '<P><B>Administrative Password:</B> '+passwd1
	print '<P><B>Class Password:</B> '+classpasswd

	print '<H3>Getting started with your account:</H3>'

	print '<P>Please remember your administrative password.  It allows you to log into "ClassAdmin" and configure the exercise.'
 	print 'The URL to log into classAdmin is <a href="http://www.pals.iastate.edu/cgi-bin/severe2/classAdmin/index.py">http://www.pals.iastate.edu/cgi-bin/severe2/classAdmin/index.py</a>'

	print """<P>You will want to create a link somewhere to point your students to this page.  It will allow them to
	work through the cases that release to them."""
	print '<a href="http://www.pals.iastate.edu/cgi-bin/severe2/advanced/list.py?className='+class_abv+'">http://www.pals.iastate.edu/cgi-bin/severe2/advanced/list.py?className='+class_abv+'</a>'


def Main():

	SEVERE2.setupPage("Creating Class for Advanced Forecasting Exercise")


	if form.has_key("name"):
		enterForm()
	else:
		newClassForm()

	SEVERE2.finishPage()

Main()
