#!/usr/bin/env python2
# This function will mail me the results of the excercise and then I can see what is going on
# Daryl Herzmann 7-16-99


import posix, functs, mx.DateTime, pg, time, regsub, os, string
tmpdb = pg.connect('severe2_tmp', 'localhost', 5432)
advdb = pg.connect('severe2_adv', 'localhost', 5432)

SENDTO = "akrherz+pals@iastate.edu"

def Main(userKey, caseNum, forecast_pts, bonus_pts, className):

	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum, className = functs.retreiveUser()
	
	name = advdb.query("SELECT name, email from users WHERE userKey = '"+str(userKey)+"' ").dictresult()
	subject = "Adv SxFrcst output for "+name[0]["name"]

	try:
		remoteHost = os.environ["REMOTE_HOST"]
	except:
		remoteHost = "NATF"

	nowDate = mx.DateTime.now()
	startDate = mx.DateTime.localtime( int(float(userKey)) )
	endDate = mx.DateTime.ISO.ParseDateTimeGMT(endTime)
	now_date = nowDate.strftime("%x %I:%M %p")
	start_date = startDate.strftime("%x %I:%M %p")
	str_date = endDate.strftime("%x %I Z")

	mailstring =              "**** On-Line Forecasting Exercise Results **** \n"
	mailstring = mailstring + "Case Number        => "+caseNum+" \n"
	mailstring = mailstring + "Case End Date      => "+str_date+" \n"
	mailstring = mailstring + "Student Name       => "+name[0]["name"]+" \n"
	mailstring = mailstring + "Student Email      => "+name[0]["email"]+" \n"
	mailstring = mailstring + "Student Started At => "+start_date+" \n"
	mailstring = mailstring + "Student Finished At=> "+now_date+" \n"
	mailstring = mailstring + "Class of Student   => "+className+" \n"
	mailstring = mailstring + "IP of Remote Host => "+remoteHost+" \n"
	mailstring = mailstring + "********************************************** \n\n"
	
	mailstring = mailstring + "**** Points earned from automatic Grading **** \n"
	mailstring = mailstring + "Forecasting Points => "+forecast_pts+"\n"
	mailstring = mailstring + "Bonus Points       => "+bonus_pts+"\n"
	mailstring = mailstring + "********************************************** \n\n"

	forecasts = advdb.query("SELECT etime, state, optiona, optionb, optionc, optiond from users WHERE userKey = '"+str(userKey)+"' ").getresult()
	mailstring = mailstring + "****         The Students Forecast        **** \n"
	mailstring = mailstring + "Forecasted State  => "+forecasts[0][1]+"\n"
	if caseNum[0] == 's':
		mailstring = mailstring + "Forecasted Time   => "+forecasts[0][0]+"\n"
		mailstring = mailstring + "Heavy Rainfall    => "+forecasts[0][2]+"\n"
		mailstring = mailstring + "Tornado           => "+forecasts[0][3]+"\n"
		mailstring = mailstring + "Hail              => "+forecasts[0][4]+"\n"
	elif caseNum[0] == 'w':
		mailstring = mailstring + "Six Inch Snowfall => "+forecasts[0][2]+"\n"
		mailstring = mailstring + "Twelve Inch Snow  => "+forecasts[0][3]+"\n"
		mailstring = mailstring + "Freezing Rainfall => "+forecasts[0][4]+"\n"
		mailstring = mailstring + "Wind Chill        => "+forecasts[0][5]+"\n"
	mailstring = mailstring + "********************************************** \n\n"

	sections = tmpdb.query("SELECT * from s"+str(userKey)+" ").dictresult()
	mailstring = mailstring + "*****   Answers to individual questions  ***** \n"
	for i in range(len(sections)):
		q_id = sections[i]["ticks"]
		question = sections[i]["question"]
		theirAnswer = sections[i]["answer"]
		correctAnswer = sections[i]["cor_answer"]
		theirAnswer = regsub.gsub("&#180;", "'", theirAnswer)

		if len(theirAnswer) > 1 or correctAnswer == 'T': # We have a text question
			mailstring = mailstring +" \n Question "+q_id+": \n \t "+question+" \n \n "+name[0]["name"]+" Replied: \n \t "+theirAnswer+" \n"

		else:	# We have a multiple choice
			guessOption= "option"+string.lower(theirAnswer[0][0])
			answerOption = "option"+string.lower(correctAnswer[0][0])
			
			guessTxt = advdb.query("SELECT "+guessOption+" from questions WHERE q_id = '"+q_id+"' ").getresult()
			if len(guessTxt) == 0:
					guessTxt = advdb.query("SELECT "+guessOption+" from questions_custom WHERE className = '"+className+"' and validTime = '"+q_id+"' ").getresult()
			answerTxt = advdb.query("SELECT "+answerOption+" from questions WHERE q_id = '"+q_id+"' ").getresult()
			if len(answerTxt) == 0:
					answerTxt = advdb.query("SELECT "+answerOption+" from questions_custom WHERE className = '"+className+"' and validTime = '"+q_id+"' ").getresult()

			mailstring = mailstring +" \n Question "+q_id+": \n \t "+question+" \n \n "+name[0]["name"]+" Replied: \n \t "+string.upper(theirAnswer)+". "+guessTxt[0][0]+"\n"
			mailstring = mailstring +"\n The Correct Answer was: \n \t "+correctAnswer[0][0]+". "+answerTxt[0][0]+" \n"

		mailstring = mailstring +"-------------------------------------------------------------------------------"
	
	instructorEmail =advdb.query("SELECT instructor_email from classes WHERE class_abv = '"+className+"' ").getresult()[0][0]

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+SENDTO+'"'
	posix.system(sysstring)

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+instructorEmail+'"'
	posix.system(sysstring)

#	delete = ldb.query("DELETE from "+usersTable+" WHERE userid = '"+str(key)+"' ")
	#drop = ldb.query("DROP TABLE s"+key+" ")
