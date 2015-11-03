#!/usr/local/bin/python
# This will be my grader, like it or not,,,

import cgi, pg, style, string, time
from functs import *

admindb = pg.connect("svr_frcst")

qs = ['q0','q1','q2','q3','q4','q5','q6']

def enter_text(key, secs, question, ans, cor_ans):
	insert = admindb.query("INSERT into s"+str(key[:-7])+" VALUES ('"+str(secs)+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")

def update_time(key, secs, bonus_pts):
	queryTest = admindb.query("SELECT * from users WHERE userid = '"+str(key)+"' and grade_secs = "+secs+" ").getresult()
#	last_time = admindb.query("SELECT last_time from users WHERE userid = '"+str(key)+"' ").getresult()[0][0]
#	if int(last_time) == int(secs) :
	if len(queryTest) == 0:
		bonus_pre = admindb.query("SELECT bonus_points from users WHERE userid = '"+str(key)+"' ").getresult()[0][0]
		bonus_pts = int(float(bonus_pre)) + bonus_pts

		update = admindb.query("UPDATE users set last_time = '"+str(secs)+"', grade_secs = '"+str(secs)+"', bonus_points = '"+str(bonus_pts)+"' WHERE userid = '"+str(key)+"' ")

def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	refer = form["refer"][0]
	secs = form["secs"][0]
        key = form["key"][0]
	case_num = form["case_num"][0]

	now_tuple = time.localtime( int(float(secs)) )

	cor_filename = time.strftime("/home/httpd/html/archivewx/data/%Y_%m_%d/ans%y%m%d%H.html", now_tuple) 
	wro_filename = time.strftime("/home/httpd/html/archivewx/data/%Y_%m_%d/answ%y%m%d%H.html", now_tuple) 
	base_ref = time.strftime("http://www.pals.iastate.edu/archivewx/data/%Y_%m_%d/", now_tuple)
	print '<base href="'+base_ref+'">'


	print '<P><a href="'+scriptBase+refer+'?secs='+str(secs)+'&key='+key+'&case_num='+case_num+'"><H3 align="right">Click Here to proceed</H3></a>'

	for quest in qs:
		if form.has_key(quest):
#			this_question = form[quest+"question"][0]
			if form.has_key(quest+"text"):			# We have a text question
				text_ans = form[quest+"text"][0]
#				text_ans = clean_str(text_ans)
#				enter_text(key, secs, this_question, text_ans, "T") 
			else:
				try:
					this_option = form[quest+"option"][0]
				except:
					style.SendError("You need to answer the question, go back")

				this_option_text = form[quest+"option_txt"+this_option][0]
				this_answer = admindb.query("SELECT answer from spec_questions WHERE ticks = '"+secs+"' ").getresult()[0][0]
				if string.lower(this_answer) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
					try:
						f = open(cor_filename,'r')
					        comp = f.read()
		        			f.close()
						print comp
					except:
						print "You answered correctly"
						print '<BR><BR>Content needs to be written yet...<BR>'
						print 'I was looking for this file -> '+cor_filename
					bonus_pts = 10
				else:
					try:
						f = open(wro_filename,'r')
					        comp = f.read()
	        				f.close()
						print comp
					except:
						print "You answered incorrectly"
						print '<BR><BR>Content needs to be written yet...<BR>'
						print 'I was looking for this file -> '+wro_filename
					bonus_pts = 0

	update_time(key, secs, bonus_pts)

#	print '<HTML><HEAD>'
#        print '<meta http-equiv="Refresh" content="0; URL='+refer+'?secs='+str(secs)+'&key='+key+'&case_num='+case_num+'">'
 #       print '</HEAD>'



Main()


