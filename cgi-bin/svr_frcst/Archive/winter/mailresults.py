#!/usr/local/bin/python
# This function will mail me the results of the excercise and then I can see what is going on
# Daryl Herzmann 7-16-99

import posix, pg, time, regsub

admindb = pg.connect('archadmin')
sessionsdb = pg.connect('sessions_417')

# sections = ('ans7am', 'ans8am', 'ans9am', 'ans10am', 'ans11am', 'ans12pm', 'ans1pm', 'ans2pm', 'ans3pm', 'ans4pm', 'ans5pm', 'ans6pm', 'ans7pm', 'ans8pm', 'ans9pm', 'ans10pm', 'ans11pm')

SENDTO = "akrherz@iastate.edu"

def Main(secs, key):
	name = admindb.query("SELECT name from sessions_417 WHERE key = '"+str(key)+"' ").getresult()
	subject = "OnLine 417 output for "+name[0][0]

	sections = sessionsdb.query("SELECT * from s"+str(key[:-7])+" ").getresult()

	mailstring = "Answers to individual questions "
	for i in range(len(sections)):
		ticks = sections[i][0]
		question = sections[i][1]
		answer = sections[i][2]
		cor_answer = sections[i][3]
	
		answer = regsub.gsub("&#180;", "'", answer)

		this_tuple = time.localtime( float(ticks) )
		nice_date = time.strftime("%x %I %p" ,this_tuple)

		mailstring = mailstring +"\n Question asked at "+nice_date+": \n\t "+question+" \n\n "+name[0][0]+" Replied: \n\t "+answer+" \n"
		mailstring = mailstring +"------------------------------------------------------------------"

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+SENDTO+'"'
	posix.system(sysstring)

	delete = admindb.query("DELETE from sessions_417 WHERE key = '"+str(key)+"' ")
	drop = sessionsdb.query("DROP TABLE s"+str(key[:-7])+" ")
