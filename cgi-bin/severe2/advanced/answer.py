#!/usr/bin/env python
# This takes questions asked and them grades them, puts them in a database and send user on their way
# Daryl Herzmann 11-16-99

import functs, SEVERE2, pg, cgi, string, sys, regsub, style

qs = ['q0','q1','q2','q3','q4','q5','q6']	# I hope that we never have more than 7 questions
advdb = pg.connect('severe2_adv', 'localhost', 5432)
tmpdb = pg.connect('severe2_tmp', 'localhost', 5432)

def enter_text(userKey, ans, cor_ans, q_id, bonus_pts, question):
	test = tmpdb.query("SELECT * from s"+str(userKey)+" WHERE ticks = '"+q_id+"' ").getresult()
	if len(test) == 0:
		insert = tmpdb.query("INSERT into s"+str(userKey)+" VALUES ('"+q_id+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")

def Main():
	form = cgi.FormContent()
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum, className = functs.retreiveUser()
	
	bonus_pts = int( advdb.query("SELECT bonuspoints from users WHERE userKey = '"+userKey+"' ").getresult()[0][0] )
	pause_page = 1
	i = 0
	
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			if form.has_key(quest+"txt"):
				donothing = 1
			else:
				try:
					this_option = form[quest+"option"][0]
				except:
					style.SendError("You need to answer Question number "+str(i)+", go back")			

	SEVERE2.setupPage()
	SEVERE2.printTime(lastTime)


	print '<H2 align="CENTER">Question Response</H2>'
	i = 0
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			q_id = form[quest+"q_id"][0]
			if form.has_key(quest+"text"):			# We have a text question
				textAns = form[quest+"text"][0]
				textAns = functs.clean_str(textAns)
				print '<HR><font color="blue">Question '+str(i)+':</font><BR>'  
				if len(q_id) < 5:
					question = advdb.query("SELECT question from questions WHERE q_id = '"+q_id+"' ").getresult()[0][0]
				else:
					question = advdb.query("SELECT question from questions_custom WHERE validTime = '"+q_id+"' ").getresult()[0][0]
				enter_text(userKey, textAns, 'T', q_id, '0', question)
				print 'Your Text response was entered and will be sent to your instructor..<HR>'
			else:
				print '<HR><font color="blue">Question '+str(i)+':</font><BR>'
				pause_page = 0
				this_option = string.lower( form[quest+"option"][0] )
				optionName = "option"+this_option
				if optionName == "optionyes":
					print "<H3> Did you forget to answer one of the questions? Go back and answer it!</H3>"
					SEVERE2.finishPage()
					sys.exit(0)
				

				if len(q_id) > 5: # We have a custom question
					thisQuery = advdb.query("SELECT question, answer, "+optionName+", correct, wrong from questions_custom WHERE validTime = '"+q_id+"' and className = '"+className+"' ").dictresult()
					thisQuestion = thisQuery[0]["question"]
					thisAnswer = thisQuery[0]["answer"]
					thisOptionText = thisQuery[0][optionName]
					thisCorrect = thisQuery[0]["correct"]
					thisWrong = thisQuery[0]["wrong"]
															
				else:	# We must have a standard Question 
					thisQuery = advdb.query("SELECT question, "+optionName+" from questions WHERE q_id = '"+q_id+"' ").dictresult()
					thisQuestion = thisQuery[0]["question"]
					thisOptionText = thisQuery[0][optionName]

					thisQuery = advdb.query("SELECT answer, correct, wrong from answers WHERE q_id = '"+q_id+"' and caseNum = '"+caseNum+"' ").dictresult()
					if len(thisQuery) == 0:
						print 'This question '+q_id+' for case num '+case_num+' needs to be answered yet<BR>'
						thisAnswer = "NA"
					
						thisAnswer = thisQuery[0]["answer"]
						thisCorrect = thisQuery[0]["correct"]
						thisWrong = thisQuery[0]["wrong"]
					else:
						thisAnswer = thisQuery[0]["answer"]
						thisCorrect = thisQuery[0]["correct"]
						thisWrong = thisQuery[0]["wrong"]				
			
				if thisAnswer == "NA":
					print " "
				else:
					if len(q_id) > 5: # We have a custom question
						thisAnswerText = advdb.query("SELECT option"+thisAnswer+" from questions_custom WHERE validTime = '"+q_id+"' and className = '"+className+"' ").getresult()[0][0]

					else:
						thisAnswerText = advdb.query("SELECT option"+thisAnswer+" from questions WHERE q_id = '"+q_id+"' ").getresult()[0][0]

					if string.lower(thisAnswer) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
						print "<H3>You answered Correctly:</H3>"
						print "<P><B><i>You were asked =></i></b> "+thisQuestion
						print "<P><B><i>You responded =></i></b> "+string.upper(this_option)+". "+thisOptionText
						print "<P><B><i>The Correct answer was =></i></b> "+thisAnswer+". "+thisAnswerText
						print "<P><B><i>The instructor's response =></i></b>" +thisCorrect
						bonus_pts = bonus_pts + 10
					else:
						print "<H3>You answered Incorrectly:</H3>"
						print "<P><B><i>You were asked =></i></b> "+thisQuestion
						print "<P><B><i>You responded =></i></b> "+string.upper(this_option)+". "+thisOptionText
						print "<P><B><i>The Correct answer was =></i></b> "+thisAnswer+". "+thisAnswerText
						print "<P><B><i>The instructor's response =></i></b>" +thisWrong
				
				enter_text(userKey, this_option, thisAnswer, q_id, bonus_pts, thisQuestion )
				print "<HR>"
					

	functs.updateUser(userKey, "gradeTime", lastTime)
	
	functs.updateUser(userKey, "bonuspoints", bonus_pts)

	
	if (pause_page):
		print '<P align="right"><a href="/cgi-bin/severe2/advanced/hour.py?userKey='+userKey+'">'
		print '<img src="/gen/button.php?label=Click%20To%20Continue&font_size=30" BORDER="0"></a>'
		SEVERE2.finishPage("advanced")
		sys.exit(0)

	print '<CENTER>'
	print '<P><a href="/cgi-bin/severe2/advanced/hour.py?userKey='+userKey+'">'
	print '<img src="/gen/button.php?label=Click%20To%20Continue&font_size=30" BORDER="0"></a>'
	print '</CENTER>'

	if caseNum[0] == 'w':
		SEVERE2.makeData(lastTime, userKey, caseNum, 3)
	else:
		SEVERE2.makeData(lastTime, userKey, caseNum, 1)

	SEVERE2.finishPage("advanced")

Main()
