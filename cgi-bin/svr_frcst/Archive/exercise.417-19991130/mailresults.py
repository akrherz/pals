#!/usr/local/bin/python
# This function will mail me the results of the excercise and then I can see what is going on
# Daryl Herzmann 7-16-99

import posix, pg, time, regsub, string

admindb = pg.connect('svr_frcst')
my417db = pg.connect('svr_417')
sessionsdb = pg.connect('sessions_417')

SENDTO = "wgallus@iastate.edu"
CCTO = "akrherz@iastate.edu"

def Main(secs, key, case_num, str_date, forecast_pts, bonus_pts):
	name = admindb.query("SELECT name, email from users_417 WHERE userid = '"+str(key)+"' ").getresult()
	subject = "OnLine 417 output for "+name[0][0]

	now = time.time()
	now_tuple = time.localtime(now)
	now_date = time.strftime("%x %I:%M %p", now_tuple)

	mailstring =              "**** On-Line Forecasting Exercise Results **** \n"
	mailstring = mailstring + "Case Number        => "+case_num+" \n"
	mailstring = mailstring + "Case End Date      => "+str_date+" \n"
	mailstring = mailstring + "Student Name       => "+name[0][0]+" \n"
	mailstring = mailstring + "Student Email      => "+name[0][1]+" \n"
	mailstring = mailstring + "Time of Submission => "+now_date+" \n"
	mailstring = mailstring + "********************************************** \n\n"
	
	mailstring = mailstring + "**** Points earned from automatic Grading **** \n"
	mailstring = mailstring + "Forecasting Points => "+forecast_pts+"\n"
	mailstring = mailstring + "Bonus Points       => "+bonus_pts+"\n"
	mailstring = mailstring + "********************************************** \n\n"

	forecasts = admindb.query("SELECT etime, state, optiona, optionb, optionc, optiond from users_417 WHERE userid = '"+str(key)+"' ").getresult()
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

	sections = sessionsdb.query("SELECT * from s"+key+" ").getresult()
	mailstring = mailstring + "*****   Answers to individual questions  ***** \n"
	for i in range(len(sections)):
		ticks = sections[i][0]
		question = sections[i][1]
		answer = sections[i][2]
		cor_answer = sections[i][3]
	
		answer = regsub.gsub("&#180;", "'", answer)

		this_answer = my417db.query("SELECT ans from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+ticks+"' ").getresult()

		mailstring = mailstring +" \n Question "+ticks+": \n \t "+question+" \n \n "+name[0][0]+" Replied: \n \t "+answer+" \n"
		try:
			option = "option"+string.lower(this_answer[0][0])
			this_answer_txt = admindb.query("SELECT "+option+" from gen_417 WHERE q_id = '"+ticks+"' ").getresult()
			mailstring = mailstring +"\n The Correct Answer was: \n \t "+this_answer[0][0]+". "+this_answer_txt[0][0]+" \n"
		except:
			print 
		mailstring = mailstring +"--------------------------------------------------------"

	sysstring = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+SENDTO+'"'
	posix.system(sysstring)

	sysstring2 = 'echo "' + mailstring+ '"  | mail -s "'+subject+'" "'+CCTO+'"'
	posix.system(sysstring2)

	delete = admindb.query("DELETE from users_417 WHERE userid = '"+str(key)+"' ")
	drop = sessionsdb.query("DROP TABLE s"+key+" ")
