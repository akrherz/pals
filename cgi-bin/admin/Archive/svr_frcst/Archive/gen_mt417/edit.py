#!/usr/local/bin/python
# This program edits the question and then submits it to enter.py
# Daryl Herzmann 7-15-99
# UPDATED 7-21-99: Added support for up to 3 questions per hour

import cgi, style, sys, posix
from pgext import *

mydb = connect('archadmin')
table_str = "gen_questions_417"

def mk_question(question):
	print '<H4>Edit the Text of the Question:</H4>'
	print '<TEXTAREA cols="80" rows="3" name="quest" WRAP>'+question+'</TEXTAREA><BR>' 

def mk_type(type):
	print '<H4>Select the type of question:</H4>'
	print '<SELECT name="type">'
	print '		<option value="M">Multiple Choice'
	print '         <option value="T" '
	if type == "T":
		print "SELECTED"
	print '>Text Response'
	print '</SELECT><BR>'

def mk_optiona(optiona):
	print '<H4>Enter Text for A Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiona" value="'+optiona+'"><BR>'

def mk_optionb(optionb):
	print '<H4>Enter Text for B Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionb" value="'+optionb+'"><BR>'

def mk_optionc(optionc):
	print '<H4>Enter Text for C Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionc" value="'+optionc+'"><BR>'

def mk_optiond(optiond):
	print '<H4>Enter Text for D Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiond" value="'+optiond+'"><BR>'

def mk_optione(optione):
	print '<H4>Enter Text for E Option (If applies):</H4>'
	print '<input type="text" size="80" name="optione" value="'+optione+'"><BR>'

def mk_optionf(optionf):
	print '<H4>Enter Text for F Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionf" value="'+optionf+'"><BR>'

def mk_optiong(optiong):
	print '<H4>Enter Text for G Option (If applies):</H4>'
	print '<input type="text" size="80" name="optiong" value="'+optiong+'"><BR>'

def mk_optionh(optionh):
	print '<H4>Enter Text for H Option (If applies):</H4>'
	print '<input type="text" size="80" name="optionh" value="'+optionh+'"><BR>'

def mk_answer(answer):
	print '<H4>Enter the answer if it applies, ex) A, B, C, D, E, F, G, or H: </H4>'
	print '<input type="text" size="2" MAXLENGTH="1" name="answer" value="'+answer+'"><BR>'

def mk_wro_comments(wro_comments):
	print '<H4>Enter comments to appear if the user gets the question wrong</H4>'
	print '<TEXTAREA cols=80 rows=10 name="wro_comments" WRAP>'+wro_comments+'</TEXTAREA><BR>'

def mk_cor_comments(cor_comments):
	print '<H4>Enter comments to appear if the user gets the question correct</H4>'
	print '<TEXTAREA cols=80 rows=10 name="cor_comments" WRAP>'+cor_comments+'</TEXTAREA><BR>'

def Main():
	style.header("Edit Questions for 417", "white")
	form = cgi.FormContent()

	ticks = form["tod"][0]

	print '<H2 align="CENTER">Edit:</H2>'

	question = "N"
	type = "T"
	optiona = "N"
	optionb = "N"
	optionc = "N"
	optiond = "N"
	optione = "N"
	optionf = "N"
	optiong = "N"
	optionh = "N"
	answer = "N"
	cor_comments = "N"
	wro_comments = "N"
	link = "N"

	print '<form method="POST" action="change.py">'
	print '<input type="hidden" name="ticks" value="'+str(ticks)+'">'
	mk_question(question)
	mk_type(type)
	mk_optiona(optiona)	
	mk_optionb(optionb)	
	mk_optionc(optionc)	
	mk_optiond(optiond)	
	mk_optione(optione)	
	mk_optionf(optionf)	
	mk_optiong(optiong)	
	mk_optionh(optionh)	
	mk_answer(answer)
	mk_cor_comments(cor_comments)
	mk_wro_comments(wro_comments)

	print '<input type="SUBMIT" value="Make Changes">'

	print '</form></body></html>'

	
Main()
