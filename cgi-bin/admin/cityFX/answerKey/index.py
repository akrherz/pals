#!/usr/local/bin/python
# This script just allows the kids to enter in a validation to a certain.
# Daryl Herzmann 24 September 2000


import os, cgi, pg, regsub
mydb = pg.connect("cityfx", 'localhost', 5432)


def createIntResponse(qid, answer, right_text, wrong_text):
	if answer == "N":
		answer = "0"
	print '<input name="'+qid+'_answer" type="text" value="'+str(answer)+'">'

	print '<P><B>Correct Text:</B><BR>'
	print '<TEXTAREA name="'+qid+'_right" COLS="60" ROWS="6" WRAP>'+right_text+'</TEXTAREA>'

	print '<P><B>Wrong Text:</B><BR>'
	print '<TEXTAREA name="'+qid+'_wrong" COLS="60" ROWS="6" WRAP>'+wrong_text+'</TEXTAREA>'


def mkOption(let, val, selected):
	print '	<option value="'+let+'" ',
	if (let == selected):
		print "SELECTED "
	print '>'+val


def createSelectResponse(qid, rs1, answer, right_text, wrong_text):
	print '<SELECT name="'+qid+'_answer">'
	if len(rs1["optiona"]) > 0:	mkOption("A", rs1["optiona"], answer)
	if len(rs1["optionb"]) > 0:	mkOption("B", rs1["optionb"], answer)
	if len(rs1["optionc"]) > 0:	mkOption("C", rs1["optionc"], answer)
	if len(rs1["optiond"]) > 0:	mkOption("D", rs1["optiond"], answer)
	if len(rs1["optione"]) > 0:	mkOption("E", rs1["optione"], answer)
	if len(rs1["optionf"]) > 0:	mkOption("F", rs1["optionf"], answer)
	if len(rs1["optiong"]) > 0:	mkOption("G", rs1["optiong"], answer)
	if len(rs1["optionh"]) > 0:	mkOption("H", rs1["optionh"], answer)
	
	print '</SELECT>'

	print '<P><B>Correct Text:</B><BR>'
	print '<TEXTAREA name="'+qid+'_right" COLS="60" ROWS="6" WRAP>'+right_text+'</TEXTAREA>'

	print '<P><B>Wrong Text:</B><BR>'
	print '<TEXTAREA name="'+qid+'_wrong" COLS="60" ROWS="6" WRAP>'+wrong_text+'</TEXTAREA>'

def generateForm(cityID, caseID):
	rs1 = mydb.query("SELECT * from questions").dictresult()

	print '<input type="HIDDEN" name="mode" value="e">'


	for i in range(len(rs1)):
		qid = rs1[i]["qid"]
		question = rs1[i]["question"]
		questiontype = rs1[i]["questiontype"]
		try:
			answer = mydb.query("SELECT answer, right_text, wrong_text from answers WHERE cityID = '"+cityID+"' \
				and caseID = '"+caseID+"' and qid = "+str(qid)+" ").dictresult()
			ans = answer[0]["answer"]
			right_text = answer[0]["right_text"]
			wrong_text = answer[0]["wrong_text"]
		except:
			ans = "N"
			right_text = ""
			wrong_text = ""

		print '<HR>'+question+'<BR>'
		if questiontype == "I":
			createIntResponse(str(qid), ans, right_text, wrong_text)
		else:
			createSelectResponse(str(qid), rs1[i], ans, right_text, wrong_text)

		

def whichCity(caseID, selected = "AAA"):
	rs1 = mydb.query("SELECT * from cities").dictresult()

	

	print '<input type="HIDDEN" name="caseID" value="'+caseID+'">'

	print '<SELECT name="cityID">'
	for i in range(len(rs1)):
		citycode = rs1[i]["citycode"]
		cityname = rs1[i]["cityname"]
		mkOption(citycode, cityname, selected)
		
	print '</SELECT>'
	

		
def whichCase(selected = "0"):
	rs1 = mydb.query("SELECT caseid, to_char(starttime, 'DD Month YYYY') as starttime from cases").dictresult()

	print '<SELECT name="caseID">'
	for i in range(len(rs1)):
		caseID = str(rs1[i]["caseid"])
		starttime = rs1[i]["starttime"]
		mkOption(caseID, starttime, selected)
		
	print '</SELECT>'		
			
def clean_str(re_string):
        re_string = regsub.gsub("'", "&#180;", re_string)
        return re_string


def enterForm():
	myForm = cgi.FormContentDict()

        postedDict = myForm.dict
        postedKeys = postedDict.keys()

	cityID = myForm["cityID"][0]
	caseID = myForm["caseID"][0]
	
#	print postedDict
#	print "<BR>"
#	print postedKeys

	for i in range(len( postedKeys )):
		thisKey = postedKeys[i]
		thisValue = postedDict[thisKey][0]
		qid = str(thisKey[:-7])
		if thisKey[-2:] == "er":  # Something to enter
	
			try:
				sq1 = "DELETE from answers WHERE qid = "+qid+" and cityID = '"+cityID+"' \
					and caseID = '"+caseID+"' "
				sq2 = "INSERT into answers(caseID, qid, answer, cityID, right_text, wrong_text) VALUES("+caseID+", "+qid+", \
					'"+thisValue+"', '"+cityID+"', '"+clean_str(myForm[qid+"_right"][0])+"', '"+clean_str(myForm[qid+"_wrong"][0])+"')"
				mydb.query(sq1)
				mydb.query(sq2)
				
			except:
				print "Did not enter a value for question "+qid+"<BR>"
def Main():
	form = cgi.FormContent()
	
	print 'Content-type: text/html \n\n'
	print """<HTML>
	<HEAD>
		<TITLE>Edit Answers for cityFX</TITLE>
	</HEAD>
	<BODY BGCOLOR="WHITE">"""
	
	print "<H3>Edit Answer Key for Archived City Forecasting</H3>"
	print """<blockquote>
	You are editing the answers for the Archived City Forecasting Exercise.	
	</blockquote>
	"""
	print '<FORM METHOD="POST" ACTION="index.py">'
	
	
	if form.has_key("mode"):
		enterForm()
		print '<P>Input Successfull!<BR>'
		print '<a href="index.py?caseID='+form["caseID"][0]+'">Choose Different City</a>'
	
	elif form.has_key("cityID"):
		cityID = form["cityID"][0]
		caseID = form["caseID"][0]
	
		whichCase( caseID )
		whichCity( caseID, cityID) 
		
		print '<H3>Current Answers in DB for this day/location:</H3>'
		
		generateForm(cityID, caseID)
	
	elif form.has_key("caseID"):
		whichCase( form["caseID"][0] )
		print '<P>2.You must now specify which city to make answer key for.<BR>'
		caseID = form["caseID"][0]
		whichCity(caseID)
	else:
		print '<P>1.You need to specify a case before the exercise can start.<BR>'
		whichCase()
		
		
	print '<BR><BR><INPUT TYPE="SUBMIT">'
	print '</form>'
	
	print '<HR><a href="/admin">PALS Admin Page</a>'

Main()
