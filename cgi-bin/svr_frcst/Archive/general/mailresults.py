#!/usr/local/bin/python
# This function will mail me the results of the excercise and then I can see what is going on
# Daryl Herzmann 7-16-99

from pgext import *
import posix

admindb = connect('archadmin')

sections = ('ans7am', 'ans8am', 'ans9am', 'ans10am', 'ans11am', 'ans12pm', 'ans1pm', 'ans2pm', 'ans3pm', 'ans4pm', 'ans5pm', 'ans6pm', 'ans7pm', 'ans8pm', 'ans9pm', 'ans10pm', 'ans11pm')

SENDTO = "akrherz@iastate.edu"

def Main(secs, key):
	name = admindb.query("SELECT name from sessions WHERE key = '"+str(key)+"' ").getresult()
	subject = "OnLine General output for "+name[0][0]

	mailstring = "Answers to individual sections "
	for section in sections:
		results = admindb.query("SELECT "+section+" from sessions WHERE key = '"+str(key)+"' ").getresult()
	
		if len(results[0][0]) > 0:
			mailstring = mailstring + "\n\t\t" + section + "\n" + results[0][0]

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+SENDTO+'"'
        posix.system(sysstring)

	delete = admindb.query("DELETE from sessions WHERE key = '"+str(key)+"' ")
