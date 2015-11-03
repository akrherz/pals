#!/usr/local/bin/python
# This takes questions asked and them grades them, puts them in a database and send user on their way
# Daryl Herzmann 11-16-99

from functs import *
qs = ['q0','q1','q2','q3','q4','q5','q6']	# I hope that we never have more than 7 questions

def enter_text(ldb, key, question, ans, cor_ans, q_id, bonus_pts):
	test = ldb.query("SELECT ticks from s"+str(key)+" WHERE ticks = '"+q_id+"' ").getresult()
	if len(test) == 0:
		insert = ldb.query("INSERT into s"+str(key)+" VALUES ('"+q_id+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")
		return bonus_pts
	else:
		print '[Values Not entered, you allready answered this question, Thats cheating]<BR>'
		return 0

def update_time(ldb, key, secs, bonus_pts, className):
	tableName = "users"
	bonus_pre = ldb.query("SELECT bonus_points from "+tableName+" WHERE userid = '"+str(key)+"' ").getresult()[0][0]
	bonus_pts = int(float(bonus_pre)) + bonus_pts

	update = ldb.query("UPDATE "+tableName+" set last_time = '"+str(secs)+"', bonus_points = '"+str(bonus_pts)+"' WHERE userid = '"+str(key)+"' ")


def Main():
	refer = form["refer"][0]
	secs = form["secs"][0]
	interval = form["interval"][0]
	tsecs = int(float(form["secs"][0]))      # The current time
	secs_tuple = time.localtime(tsecs)       # The tuple of the current time

	svrFrcst.svrTop(secs_tuple, tsecs)

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


	print '<H2 align="CENTER">Question Response</H2>'
	i = 0
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			this_question = form[quest+"question"][0]
			q_id = form[quest+"q_id"][0]
			if form.has_key(quest+"text"):			# We have a text question
				text_ans = form[quest+"text"][0]
				text_ans = clean_str(text_ans)
				print '<HR><font color="blue">Question '+str(i)+':</font><BR>'  
				bogus = enter_text(ldb, key, this_question, text_ans, "T", q_id, 0)
				print 'Your Text response was entered and will be sent to Dr Gallus..<HR>'
			else:
				print '<HR><font color="blue">Question '+str(i)+':</font><BR>'
				pause_page = 0
				this_option = form[quest+"option"][0]

				this_option_txt = form[quest+"option_txt"+this_option][0]

				specTable = "spec_questions"
				if len(str(q_id)) > 5:
					this_answer = ldb.query("SELECT answer from "+specTable+" WHERE ticks = '"+q_id+"' ").getresult()
					option_wanted = "option"+this_answer[0][0]
					ans_txt = ldb.query("SELECT "+option_wanted+" from "+specTable+" WHERE ticks = '"+q_id+"' ").getresult()
					comments = ldb.query("SELECT cor_comments, wro_comments from "+specTable+" WHERE ticks = '"+q_id+"' ").getresult()
				else: 
					this_answer = mydb.query("SELECT ans from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()
					if len(this_answer) == 0:
						print 'This question '+q_id+' for case num '+case_num+' needs to be answered yet<BR>'
						this_answer = "NA"
					else:
						option_wanted = "option"+this_answer[0][0]
						ans_txt = mydb.query("SELECT "+option_wanted+" from gen_417 WHERE q_id = '"+q_id+"' ").getresult()
					comments = mydb.query("SELECT cor_comments, wro_comments from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()

				if this_answer == "NA":
					print " "
				else:
					this_answer = this_answer[0][0]
					if string.lower(this_answer) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
						print "<H3>You answered Correctly:</H3>"
						print "<P><B><i>You were asked =></i></b> "+this_question
						print "<P><B><i>You responded =></i></b> "+this_option_txt
						print "<P><B><i>The Correct answer was =></i></b> "+this_answer+". "+ans_txt[0][0]
						print "<P><B><i>Dr Gallus's response =></i></b>" +comments[0][0]
						bonus_pts = bonus_pts + 10
					else:
						print "<H3>You answered Incorrectly:</H3>"
						print "<P><B><i>You were asked =></i></b> "+this_question
						print "<P><B><i>You responded =></i></b> "+this_option_txt
						print "<P><B><i>The Correct answer was =></i></b> "+this_answer+". "+ans_txt[0][0]
						print "<P><B><i>Dr Gallus's response =></i></b>" +comments[0][1]
				try:
					bonus_pts = enter_text(ldb, key, this_question, this_option_txt, this_answer[0][0], q_id, bonus_pts)
				except:	
					bonus_pts = enter_text(ldb, key, this_question, this_option_txt, "N", q_id, bonus_pts)
			
				print "<HR>"
					

	update_time(ldb, key, secs, bonus_pts, className)

	print '<HTML><HEAD>'
	if (pause_page):
	        print '<meta http-equiv="Refresh" content="0; URL='+refer+'?className='+className+'&interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'&q=yes">'
	        print '</HEAD>'
		sys.exit(0)
        print '</HEAD>'

        if case_num[0] == 'w':
                mk_data(secs_tuple, 3)
        else:
                mk_data(secs_tuple, 1)

	print '<P align="right"><a href="'+refer+'?className='+className+'&interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'&q=yes">'
	print '<img src="/gen/button.php3?label=Click%20To%20Continue&font_size=30" BORDER="0"></a>'

	svrFrcst.svrBot()

Main()
