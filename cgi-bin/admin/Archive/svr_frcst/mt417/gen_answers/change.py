#!/usr/local/bin/python
# This program enters db stuff
# Daryl Herzmann 8-16-99
# 11-5-99: Lets make this work.....


import pg, cgi, time, style
mydb = pg.connect('svr_frcst')


def Main():
	form = cgi.FormContent()
	caseNum = form["caseNum"][0]
	question_num = form["question_num"][0]
	answer = form["answer"][0]
	cor_comments = style.clean_str(form["cor_comments"][0])
	wro_comments = style.clean_str(form["wro_comments"][0])



	insert = mydb.query("DELETE from gen_answers_417 WHERE case_num = '"+caseNum+"' and q_id = '"+question_num+"'  ")
	insert = mydb.query("INSERT into gen_answers_417 VALUES ('"+caseNum+"','"+question_num+"','"+answer+"', '"+cor_comments+"','"+wro_comments+"') ")

	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD>'
	print '<meta http-equiv="Refresh" content="0; URL=list.py?caseNum='+caseNum+'">'
        print '</HEAD>' 

Main()
