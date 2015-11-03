#!/usr/local/bin/python
# This function will mail me the results of the excercise and then I can see what is going on
# Daryl Herzmann 7-16-99

from functs import *
import posix

SENDTO = "akrherz@iastate.edu"

def Main(ldb, secs, key, case_num, str_date, forecast_pts, bonus_pts, className):
	usersTable = "users"
	name = ldb.query("SELECT name, email from "+usersTable+" WHERE userid = '"+str(key)+"' ").getresult()
	subject = "Adv SxFrcst output for "+name[0][0]

	try:
		remoteHost = os.environ["REMOTE_HOST"]
	except:
		remoteHost = "NATF"

	now = time.time()
	now_tuple = time.localtime(now)
	start_tuple = time.localtime( int(float(key)) )
	now_date = time.strftime("%x %I:%M %p", now_tuple)
	start_date = time.strftime("%x %I:%M %p", start_tuple)

	mailstring =              "**** On-Line Forecasting Exercise Results **** \n"
	mailstring = mailstring + "Case Number        => "+case_num+" \n"
	mailstring = mailstring + "Case End Date      => "+str_date+" \n"
	mailstring = mailstring + "Student Name       => "+name[0][0]+" \n"
	mailstring = mailstring + "Student Email      => "+name[0][1]+" \n"
	mailstring = mailstring + "Student Started At => "+start_date+" \n"
	mailstring = mailstring + "Student Finished At=> "+now_date+" \n"
	mailstring = mailstring + "Class of Student   => "+className+" \n"
	mailstring = mailstring + "IP of Remote Hosts => "+remoteHost+" \n"
	mailstring = mailstring + "********************************************** \n\n"
	
	mailstring = mailstring + "**** Points earned from automatic Grading **** \n"
	mailstring = mailstring + "Forecasting Points => "+forecast_pts+"\n"
	mailstring = mailstring + "Bonus Points       => "+bonus_pts+"\n"
	mailstring = mailstring + "********************************************** \n\n"

	forecasts = ldb.query("SELECT etime, state, optiona, optionb, optionc, optiond from "+usersTable+" WHERE userid = '"+str(key)+"' ").getresult()
	mailstring = mailstring + "****         The Students Forecast        **** \n"
	mailstring = mailstring + "Forecasted State  => "+forecasts[0][1]+"\n"
	if case_num[0] == 's':
		mailstring = mailstring + "Forecasted Time   => "+forecasts[0][0]+"\n"
		mailstring = mailstring + "Heavy Rainfall    => "+forecasts[0][2]+"\n"
		mailstring = mailstring + "Tornado           => "+forecasts[0][3]+"\n"
		mailstring = mailstring + "Hail              => "+forecasts[0][4]+"\n"
	elif case_num[0] == 'w':
		mailstring = mailstring + "Six Inch Snowfall => "+forecasts[0][2]+"\n"
		mailstring = mailstring + "Twelve Inch Snow  => "+forecasts[0][3]+"\n"
		mailstring = mailstring + "Freezing Rainfall => "+forecasts[0][4]+"\n"
		mailstring = mailstring + "Wind Chill        => "+forecasts[0][5]+"\n"
	mailstring = mailstring + "********************************************** \n\n"

	sections = ldb.query("SELECT * from s"+key+" ").getresult()
	mailstring = mailstring + "*****   Answers to individual questions  ***** \n"
	for i in range(len(sections)):
		ticks = sections[i][0]
		question = sections[i][1]
		answer = sections[i][2]
		cor_answer = sections[i][3]
	
		answer = regsub.gsub("&#180;", "'", answer)

		specTable = "spec_questions"
		this_answer = mydb.query("SELECT ans from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+ticks+"' ").getresult()
		if len(this_answer) == 0:
			this_answer = ldb.query("SELECT answer from "+specTable+" WHERE ticks = '"+ticks+"' ").getresult()

		str_ticks = ticks
		if len(str(ticks)) > 5:
			now_tuple = time.localtime( float(int(ticks)) )
			str_ticks = time.strftime("%x %HZ", now_tuple)

		mailstring = mailstring +" \n Question "+str_ticks+": \n \t "+question+" \n \n "+name[0][0]+" Replied: \n \t "+answer+" \n"
		try:
			option = "option"+string.lower(this_answer[0][0])
			this_answer_txt = mydb.query("SELECT "+option+" from gen_417 WHERE q_id = '"+ticks+"' ").getresult()
			if len(this_answer_txt) == 0:
				this_answer_txt = ldb.query("SELECT "+option+" from "+specTable+" WHERE ticks = '"+ticks+"' ").getresult()
			mailstring = mailstring +"\n The Correct Answer was: \n \t "+this_answer[0][0]+". "+this_answer_txt[0][0]+" \n"
		except:
			print ""
 
		mailstring = mailstring +"-------------------------------------------------------------------------------"
	
	instructorEmail = mydb.query("SELECT instructor_email from classes WHERE class_abv = '"+className+"' ").getresult()[0][0]

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+SENDTO+'"'
	posix.system(sysstring)

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+instructorEmail+'"'
	posix.system(sysstring)

	delete = ldb.query("DELETE from "+usersTable+" WHERE userid = '"+str(key)+"' ")
	drop = ldb.query("DROP TABLE s"+key+" ")