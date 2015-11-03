#!/usr/local/bin/python
# Ok, this will enter the database materials and then start the afternoon journey
# Daryl Herzmann 7-16-99

import cgi, pg, functs, style

admindb = pg.connect("sessions_417")
userdb = pg.connect("archadmin")

qs = ['q0','q1','q2','q3','q4','q5','q6']

def enter_text(key, secs, question, ans, cor_ans):
	insert = admindb.query("INSERT into s"+str(key[:-7])+" VALUES ('"+str(secs)+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")

def update_time(key, secs):
	update = userdb.query("UPDATE sessions_417 set last_time = '"+str(secs)+"' WHERE key = '"+str(key)+"' ")

def Main():
	form = cgi.FormContent()
	refer = form["refer"][0]
	secs = form["secs"][0]
        key = form["key"][0]

	for quest in qs:
		if form.has_key(quest):
			this_question = form[quest+"question"][0]
			if form.has_key(quest+"text"):			# We have a text question
				text_ans = form[quest+"text"][0]
				text_ans = functs.clean_str(text_ans)
				enter_text(key, secs, this_question, text_ans, "T") 
			else:
				try:
					this_option = form[quest+"option"][0]
				except:
					style.SendError("You need to answer the question, go back")

				this_option_text = form[quest+"option_txt"+this_option][0]
				this_answer = "K"
				enter_text(key, secs, this_question, this_option_text, this_answer)

	update_time(key, secs)
	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
        print '<meta http-equiv="Refresh" content="0; URL='+refer+'?secs='+str(secs)+'&key='+key+'">'
        print '</HEAD>'


Main()


