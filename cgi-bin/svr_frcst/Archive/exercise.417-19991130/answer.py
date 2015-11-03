#!/usr/local/bin/python
# This takes questions asked and them grades them, puts them in a database and send user on their way
# Daryl Herzmann 11-16-99

import cgi, pg, functs, style, string, sys

admindb = pg.connect("svr_frcst")
my417db = pg.connect("svr_417")
sessionsdb = pg.connect('sessions_417')

scriptBase = "http://www.pals.iastate.edu/cgi-bin/svr_frcst/exercise.417" 
qs = ['q0','q1','q2','q3','q4','q5','q6']	# I hope that we never have more than 7 questions

def enter_text(key, question, ans, cor_ans, q_id):
	test = sessionsdb.query("SELECT ticks from s"+str(key)+" WHERE ticks = '"+q_id+"' ").getresult()
	if len(test) == 0:
		insert = sessionsdb.query("INSERT into s"+str(key)+" VALUES ('"+q_id+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")
	else:
		print '[Values Not entered, you allready answered this question, Thats cheating]<BR>'

def update_time(key, secs, bonus_pts):
	bonus_pre = admindb.query("SELECT bonus_points from users_417 WHERE userid = '"+str(key)+"' ").getresult()[0][0]
	bonus_pts = int(float(bonus_pre)) + bonus_pts

	update = admindb.query("UPDATE users_417 set last_time = '"+str(secs)+"', bonus_points = '"+str(bonus_pts)+"' WHERE userid = '"+str(key)+"' ")

def check_time(key, secs):
	update = admindb.query("SELECT last_time from users_417 WHERE userid = '"+str(key)+"' ").getresult()
        if int(float( update[0][0] )) >= int(secs):
                return 1                                # WE have been here
        else:
                return 0



def Main():
	form = cgi.FormContent()
	refer = form["refer"][0]
	secs = form["secs"][0]
        key = form["key"][0]
	case_num = form["case_num"][0]
	interval = form["interval"][0]
	print 'Content-type: text/html \n\n'

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


	print '<H2><font color="blue">Question Response</font></H2>'
#	print '--------> I am still working on the format for this page, be patient <----------'
	i = 0
	for quest in qs:
		i = i + 1
		if form.has_key(quest):
			this_question = form[quest+"question"][0]
			q_id = form[quest+"q_id"][0]
			if form.has_key(quest+"text"):			# We have a text question
				text_ans = form[quest+"text"][0]
				text_ans = functs.clean_str(text_ans)
				print '<HR><font color="red">Question '+str(i)+':</font><BR>'  
				enter_text(key, this_question, text_ans, "T", q_id)
				print 'Your Text response was entered and will be sent to Dr Gallus..<HR>'
			else:
				print '<HR><font color="red">Question '+str(i)+':</font><BR>'
				pause_page = 0
				this_option = form[quest+"option"][0]

				this_option_txt = form[quest+"option_txt"+this_option][0]

				this_answer = my417db.query("SELECT ans from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()
				try:
					enter_text(key, this_question, this_option_txt, this_answer[0][0], q_id)
				except:	
					enter_text(key, this_question, this_option_txt, "N", q_id)
			
				if len(this_answer) == 0:
					print 'This question '+q_id+' for case num '+case_num+' needs to be answered yet<HR>'
					this_answer = "NA"
				else:
					this_answer = this_answer[0][0]
					if string.lower(this_answer) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
						reply = my417db.query("SELECT cor_comments from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()
						print "<H3>You answered Correctly:</H3>"
						bonus_pts = bonus_pts + 10
					else:
						reply = my417db.query("SELECT wro_comments from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()
						print "<H3>You answered Incorrectly:</H3>"
					option_wanted = "option"+this_answer
					ans_txt = admindb.query("SELECT "+option_wanted+" from gen_417 WHERE q_id = '"+q_id+"' ").getresult()
					print "<P><B><i>You were asked =></i></b> "+this_question
					print "<P><B><i>You responded =></i></b> "+this_option_txt
					print "<P><B><i>The Correct answer was =></i></b> "+this_answer+". "+ans_txt[0][0]
					print "<P><B><i>Dr Gallus's response =></i></b>" +reply[0][0]
					print "<HR>"
					

	update_time(key, secs, bonus_pts)

	print '<HTML><HEAD>'
	if (pause_page):
	        print '<meta http-equiv="Refresh" content="0; URL='+refer+'?interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'&q=yes">'
        print '</HEAD>'

	print '<P align="right"><a href="'+refer+'?interval='+interval+'&secs='+str(secs)+'&key='+key+'&case_num='+case_num+'&q=yes">'
	print '<img src="/gen/button.php3?label=Click%20To%20Continue" BORDER="0"></a>'

Main()


