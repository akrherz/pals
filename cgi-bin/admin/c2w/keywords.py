#!/usr/local/bin/python
# This program allows admins to easily edit the keywords list....
# Daryl Herzmann 1/29/99

from pgext import *
from cgi import *
import style

mydb = connect('c2w')

def actions(done):
	print '<H3>Previous Action => '+done+'</H3>'
	print '<HR>'
	print '<a href="keywords.py?option=add">Add a keyword</a><HR>'


def words():
	keywords = mydb.query("Select * from keywords").getresult()
	keywords.sort()
	print '<TABLE>'
	for i in range(len(keywords)):
		keyword = keywords[i][0]
		print '<TR><TH>'+keyword+'</TH>'
		print '<TD><a href="keywords.py?option=delete&keyword='+keyword+'">Delete</a></TD>'
		print '<TD><a href="keywords.py?option=change&keyword='+keyword+'">Edit</a></TD></TR>'
	print '</TABLE>'

def delete_word(word):
	mydb.query("DELETE from keywords where keywords = '"+word+"'")

def insert(word):
	mydb.query("INSERT into keywords values ('"+word+"')")

def changer(word):
	print '<FORM METHOD="POST" ACTION="keywords.py">'
	print '<input type="hidden" name="option" value="change2">'
	print '<input type="text" name="keyword" value="'+word+'">'
	print '<input type="submit" value="Change to">'
	print '<input type="reset">'
	print '</form>'

def Main():
	style.header('Edit COMET keywords',"white")
	print '<H2 align="center">COMET Keywords editor</H2>'
	form = FormContent()
	if form.has_key("option"):
		option = form["option"][0]
		if option == "delete":
			delete_word(form["keyword"][0])
			actions("Deleted keyword '"+form["keyword"][0]+"'")
			words()
		if option == "change":
			delete_word(form["keyword"][0])
			changer(form["keyword"][0])
		if option == "change2":
			insert(form["keyword"][0])
			actions("Inserted keyword '"+form["keyword"][0]+"'")
			words()
		if option == "add":
			changer("Enter Word Here")
	else:
		actions("Nothing done")
		words()



	style.std_bot()
Main()
