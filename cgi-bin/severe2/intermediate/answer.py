#!/usr/bin/python
# This takes questions asked and them grades them, puts them in a database and send user on their way
# Daryl Herzmann 11-16-99

import functs, cgi, pg, string, style, SEVERE2

mydb = pg.connect('severe2', 'localhost', 5432)
qs = ['q0','q1','q2','q3','q4','q5','q6']	# I hope that we never have more than 7 questions

def update_time(userKey, bonus_pts, lastTime):
	queryTest = mydb.query("SELECT * from users WHERE userKey = '"+str(userKey)+"' and gradeTime = '"+lastTime+"' ").getresult()
	functs.updateUser(userKey, "gradeTime", lastTime)
	if len(queryTest) == 0:
		bonus_pre = mydb.query("SELECT bonuspoints from users WHERE userKey = '"+str(userKey)+"' ").getresult()[0][0]
		bonus_pts = int(float(bonus_pre)) + bonus_pts
		functs.updateUser(userKey, "bonuspoints", bonus_pts)


def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = functs.retreiveUser()

	functs.setupPage()
	functs.printTime(lastTime)
	functs.makeHelp()

	bonus_pts = 0
	pause_page = 1
	i = 0
	
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			if form.has_key(quest+"text"):
				donothing = 1
			else:
				try:
					this_option = form[quest+"option"][0]
				except:
					style.SendError("You need to answer Question number "+str(i)+", go back")			

	print """<font color="#a0522d">
	<BLOCKQUOTE><P>Listed below is the answer for the question that you just answered.  Feel free to review the weather
	data up till this point, if you missed this question. Otherwise, continue on with the exercise.</P></BLOCKQUOTE></font>
	"""

	print '<H2 align="CENTER">Question Response</H2>'
	i = 0
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			q_id = form[quest][0]
			
			this_option = form[quest+"option"][0]
			intval = form["intval"][0]

			try:
				this_answer = mydb.query("SELECT answer from intanswers WHERE intval = '"+intval+"' and casenum = '"+caseNum+"' ").getresult()
				option_wanted = "option"+this_answer[0][0]
				if option_wanted == "optionN":
					option_wanted = "nooption"
				ans_txt = mydb.query("SELECT "+option_wanted+" from intquestions WHERE intval = '"+intval+"' ").getresult()
				comments = mydb.query("SELECT correct, wrong from intanswers WHERE intval =  '"+intval+"' and caseNum = '"+caseNum+"' ").getresult()
				this_answer = this_answer[0][0]
				if string.lower(this_answer) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
					print "<H3>You answered <font color='red'>correctly</font> for question "+str(i)+":</H3>"
					print "<P><B><i>The Correct answer was =></i> "+this_answer+". "+ans_txt[0][0]+"</B>"
					
					print "<BR><BR clear='all'>"
					print comments[0][0]
					print "<BR clear='all'>"
					bonus_pts = bonus_pts + 10
					pointsReceived = 10
				elif (option_wanted == "nooption"):
					bonus_pts = bonus_pts + 10
					pointsReceived = 10
				else:
					print "<H3>You answered <font color='red'>incorrectly</font> for question "+str(i)+":</H3>"
					print "<P><B><i>The Correct answer was =></i> "+this_answer+". "+ans_txt[0][0]+"</B>"

					print "<BR><BR clear='all'>"
					print comments[0][1]
					print "<BR clear='all'>"
					pointsReceived =0

				print "<P>Bonus Points Received:" + str(pointsReceived)
			except:

				print "An error occurred trying to find the answer for this question..."				

			print "<HR>"
			
	print '<CENTER><a href="/cgi-bin/severe2/intermediate/hour.py?userKey='+userKey+'">'
	print '<img src="/gen/button.php?label=Click%20To%20Continue&font_size=30" BORDER="0"></a></CENTER>'

	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3)
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1)

	update_time(userKey, bonus_pts, lastTime)
	functs.updateUser(userKey, "gradeTime", lastTime)

	functs.finishPage()

Main()
