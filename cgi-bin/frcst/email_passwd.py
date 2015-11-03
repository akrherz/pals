#!/usr/local/bin/python
# This program will email the kiddies their password if they forget
# Daryl Herzmann 9-30-99

import cgi, pg, style, string, os, sys

mydb = pg.connect('frcst')

def validate_passwd(userid):
        entry = mydb.query("SELECT passwd from users WHERE userid = '"+userid+"' ").getresult()
        try:
                passwd_db = entry[0][0]
                return passwd_db
        except:
                style.SendError("Unable to fullfill request, email me..")

def mk_new():
	style.header("I forgot my password!!", "white")
	print '<form method="POST" action="email_passwd.py">'
	style.top_box("Enter your userid:", "black", "white", "#EEEEEE")
	print '<input type="text" name="userid">'
	style.bot_box()

	style.top_box("Submit:", "white", "white", "white")
	print '<input type="submit" value="Email me my password">'
	style.bot_box()


	print '</form>'
	sys.exit(0)

def Main():
	form = cgi.FormContent()
	if not form.has_key("userid"):
		mk_new()
	userid = form["userid"][0]
	passwd = validate_passwd(userid)
	email_add = userid[6:]+"@iastate.edu"


	sysstring = 'echo "' + passwd+ '"  | mail -s "Your Password for Exercise" "'+email_add+'"'
        os.system(sysstring)

	style.header("I forgot my password!!", "white")
	print 'Your password has been emailed to you!<BR>'
	print '<a href="/frcst/">Forecasting Main Page</a>'



Main()
