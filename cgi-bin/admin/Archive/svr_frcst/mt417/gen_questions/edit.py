#!/usr/local/bin/python
# This program changes db stuff
# Daryl Herzmann 8-16-99

import cgi, pg, style, time, string

mydb = pg.connect('svr_frcst')

def get_date(case_num):
	entry = mydb.query("SELECT start_secs from cases WHERE case_num = '"+case_num+"' ").getresult()

	start_secs = float(entry[0][0])

	start_tuple = time.localtime(start_secs)
	return time.strftime("%B %d, %Y", start_tuple)

def get_question(question_num):
	entry = mydb.query("SELECT * from gen_417 WHERE q_id = '"+question_num+"' ").getresult()
	return entry
	
def get_old_answer(case_num, q_id):
	select = mydb.query("SELECT ans, cor_comments, wro_comments from gen_answers_417 WHERE case_num = '"+case_num+"' and q_id = '"+q_id+"' ").getresult()
	if len(select) > 0:
		ans = select[0][0]
		cor_comments = select[0][1]
		wro_comments = select[0][2]
		return ans, cor_comments, wro_comments
	else:
		return "","",""

def mk_option(letter, optionval):
	print '<BR><BR>Option '+letter+' '
#	print '<input type="text" size="100" name="option'+letter+'" value="'+optionval+'">'		
	print '<textarea cols="80" rows="2" name="option'+string.lower(letter)+'" WRAP>'+optionval+'</textarea>'		


def Main():
	form = cgi.FormContent()
	question_num = form["question_num"][0]
	case_type = form["case_type"][0]

	style.header("Edit answer for Generic Question", "white")

	quest = get_question(question_num)

	print '<H3>This is Question number '+question_num+'</H3>'

	question = quest[0][1]
	optiona = quest[0][3]
	optionb = quest[0][4]
	optionc = quest[0][5]
	optiond = quest[0][6]
	optione = quest[0][7]
	optionf = quest[0][8]
	optiong = quest[0][9]
	optionh = quest[0][10]

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" value="'+question_num+'" name="question_num">'
	print '<input type="hidden" value="'+case_type+'" name="case_type">'

	print '<B>Edit this question:</B><BR>'
	print '<textarea name="question" WRAP cols="80" rows="3">'+question+'</textarea><BR>'

	print '<B>Enter the options:</B><BR>'
	mk_option("A", optiona)
	mk_option("B", optionb)
	mk_option("C", optionc)
	mk_option("D", optiond)
	mk_option("E", optione)
	mk_option("F", optionf)
	mk_option("G", optiong)
	mk_option("H", optionh)

	print '<BR><BR>'
	print '<input type="submit" value="SUBMIT ANSWER">'

	print '</form>'
	style.std_bot()

Main()
