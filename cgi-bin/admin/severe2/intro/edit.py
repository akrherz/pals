#!/usr/local/bin/python
# Edits entries into the diary database
# Daryl Herzmann 8/8/98
# UPDATED 7-27-99: With my new knowledge, I can do this correctly :)

import style, cgi, pg, time

mydb = pg.connect("severe2", 'localhost', 5432)

def adds(comment):
        print '<H3>Edit Comments ( These appear at the top of the pages )</H3>'
	print '<textarea name="comments" cols="80" rows="10" WRAP>'+comment+'</textarea>'

def get_entry(caseNum):
	entries = mydb.query("SELECT comments from intro where casenum = '"+caseNum+"' ").getresult()
	return entries


def Main():
	style.header("Edit Annotation","white")

	form = cgi.FormContent()
	try:
		caseNum = form["caseNum"][0]
	except:
		style.SendError("CGI Parse Error")

	entry = get_entry(caseNum)

	try:
		comment = entry[0][0]
	except IndexError:
		comment = "Write Something here"

	style.std_top('Edit entry for '+caseNum)
	print """
	<HR>
		<a href="index.py">Select a different Case</a><BR>"""

        print '<form method="post" action="change.py">'
	print '<input type="hidden" name="caseNum" value="'+str(caseNum)+'">'
	adds(comment)
	print '<input type="submit" value="Click to Save this Entry">'
	print '</form>'

	
	style.std_bot()

Main()

