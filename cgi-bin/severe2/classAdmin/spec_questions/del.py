#!/usr/local/bin/python
# This delete an entry outta the db system
# Daryl Herzmann 10-20-99

import pg, cgi, style, DateTime, os
className = os.environ["REMOTE_USER"]
mydb = pg.connect('severe2_adv', 'localhost', 5432)


def Main():
	form = cgi.FormContent()
	zticks = str(form["zticks"][0])
	caseNum = str(form["caseNum"][0])

	nowDate = DateTime.gmtime(zticks)

        strTicks = DateTime.ISO.strGMT(nowDate)

	delete = mydb.query("DELETE from questions_custom WHERE className = '"+className+"' and validTime = '"+strTicks+"' ")

	style.jump_page('index.py?caseNum='+caseNum)

Main()
