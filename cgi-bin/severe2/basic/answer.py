#!/usr/bin/python2
# This will be my grader, like it or not,,,

import cgi, pg, style, string, time
from functs import *

qs = ['q0','q1','q2','q3','q4','q5','q6']

#def enter_text(key, secs, question, ans, cor_ans):
#	insert = mydb.query("INSERT into s"+str(key[:-7])+" VALUES ('"+str(secs)+"', '"+question+"', '"+ans+"', '"+cor_ans+"' ) ")

def update_time(userKey, bonus_pts, gradeTime):
	queryTest = mydb.query("SELECT * from users WHERE userKey = '"+str(userKey)+"' and lastTime = '"+gradeTime+"' ").getresult()
	if len(queryTest) == 0:
		bonus_pre = mydb.query("SELECT bonuspoints from users WHERE userKey = '"+str(userKey)+"' ").getresult()[0][0]
		bonus_pts = int(float(bonus_pre)) + bonus_pts
		updateUser(userKey, "bonuspoints", bonus_pts)

def Main():
	bonus_pts = 0
	form = cgi.FormContent()
	print 'Content-type: text/html \n\n'
	userKey, lastTime, gradeTime, startTime, noonTime, endTime, caseNum = retreiveUser()

	nowDate = mx.DateTime.ISO.ParseDateTimeGMT(lastTime)
	nowTuple = nowDate.tuple()
	 
	base_ref = time.strftime("/archivewx/data/%Y_%m_%d/", nowTuple)
	print '<base href="'+base_ref+'">'


	print '<P><a href="'+scriptBase+'hour.py?userKey='+str(userKey)+'"><H3 align="right">Click Here to proceed</H3></a>'

	for quest in qs:
		if form.has_key(quest):
			try:
				this_option = form[quest+"option"][0]
			except:
				style.SendError("You need to answer the question, go back")

			this_answer = mydb.query("SELECT answer, correct, wrong from specquestions WHERE validTime = '"+lastTime+"' ").getresult()
			if string.lower(this_answer[0][0]) == string.lower(this_option): 	# Take care of sloppy db entry routines :)
				try:
					print this_answer[0][1]

				except:
					print "You answered correctly"
					print '<BR><BR>Content needs to be written yet...<BR>'
	
				bonus_pts = 10
			else:
				try:
					print this_answer[0][2]

				except:
					print "You answered incorrectly"
					print '<BR><BR>Content needs to be written yet...<BR>'
			
				bonus_pts = 0

	update_time(userKey, bonus_pts, gradeTime)
	updateUser(userKey, "gradeTime", lastTime)

Main()


