#!/usr/local/bin/python
# Email program, sends email and then shows who it sent to
# Daryl Herzmann 7/28/98

import cgi, regsub, posix, sys, style

def Main():
	form = cgi.FieldStorage()

	if not form.has_key("recipient"): style.SendError("Enter Sender")
	if not form.has_key("email"): style.SendError("Enter your email address")
	if not form.has_key("subject"): style.SendError("Enter Subject")

	real_recipient = form["recipient"].value
	real_name = form["name"].value
	real_email = form["email"].value
	real_subject = form["subject"].value
	real_content = form["content"].value

	#Format the Content of the Email
	mailsender = "Sent from our website by:\n"
	mailsender = mailsender + real_name
	mailbreak = "\n---------------------------------\n"
	mailfrom = "Senders address:\n"
	mailfrom = mailfrom + real_email
	mailcontent = "Content:\n"
	mailcontent = mailcontent + real_content
		
	mailstring = mailsender + mailbreak + mailfrom + mailbreak + mailcontent + mailbreak	

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+real_subject+'" "'+real_recipient+'"'
	posix.system(sysstring)

	style.header("Email Successfully Sent!","/images/ISU_bkgrnd.gif")
	style.std_top("Sent email")
	print '<a href="http://www.pals.iastate.edu/home/email.html">Send another Email</a>--'
        print '<a href="http://www.pals.iastate.edu">GO to PALS Homepage</a>'
	print '<HR>\n'
	print '<center>'
	print "<H1>Email Sent to:</H1>\n"
	print real_recipient
	print '<br><BR><BR><BR><BR><BR>'
	style.std_bot()

Main()
