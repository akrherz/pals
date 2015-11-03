#!/usr/local/bin/python
# This is the keywords search for PALS
# Daryl Herzmann 1/13/99

from cgi import *
from pgext import *
import style, string

mydb = connect('c2w')


def setup_html():
	style.header("COMET Keyword Searches","white")
	print '<TABLE WIDTH="600" border="0" ROWSPACING="0" CELLSPACING="0"><TR>'
	print '<TD WIDTH="150"></td><TD WIDTH="450"></td></tr>'
	print '<tr><td colspan="2" bgcolor="#00fcf8"><img src="/images/pals_logo.gif" align="left"><spacer type="vertical" size="30">'
	print '<center><H1>COMET Keyword Searches</H1></center><BR clear="all">'

def letters_dir():
	alpha = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
	print '<table width="150" border="0" CELLSPACING="0">'
	print '<tr bgcolor="#FFCCCC"><td><B><font color="black">Select a letter:</B></font></td></tr>'
	print '<tr valign="top"><td>'
	for let in alpha:
		print '<a href="keywords.py?letter='+let+'">'+let+'</a> | ' 
	print '<spacer type="vertical" size="50">'
	print '</td></tr>'
	print '<tr bgcolor="#FFCCCC"><td><B><font color="black">Other Search Options:</B></font></td></tr>'
	print '<TR><TD><IMG SRC="/images/point_02.gif">'
	print '<font size="3"><A HREF="/c2w/adm/search.html">New Search</A></font><spacer type="vertical" size="50"></TD></TR>'
	print '</table>'


def words_dir(letter):
	flag = 'nope'
	letter = string.lower(letter)
	print '<center>'
	if letter == 'null':
		print '<H3>Select a letter from the side to start the search.</H3></center>'
	else:
		print '<H3>Please Select a word from below:</H3></center>'
		print '<B>Keywords that begin with '+letter+':</B><BR>'
		keywords = mydb.query("SELECT * from keywords").getresult()
		keywords.sort()
		print '<multicol cols="3">'
		for i in range(len(keywords)):
			keyword = keywords[i][0]
			if keyword[0] == letter:
				flag = 'yup'
				temp = string.upper(keyword[0])
				print '<input type="radio" name="string" value="'+keyword+'">'+temp+keyword[1:]
				print '<BR>'
		print '</multicol>'
		if flag == 'nope':
			print '<center><font color="red">'
			print '<BR><B>No words where found in the database starting with '+letter+'</B><BR>'
			print '</font></center>'
		else:
			dirs_dir()
			search_html()
			submit()
		
def dirs_dir():
	print '<center><H3>Refine your search:</H3></center>'
	print '<B>By searching in directories:</B><BR>'
        print '<select name=filename>'
        print '<option value="all" selected>All directories'
        print '<option value="acsse">ACSSE'
        print '<option value="csm">CSM'
        print '<option value="fire">Fire'
        print '<option value="forecast">Forecast'
        print '<option value="hydro">Hydro'
        print '<option value="marine1">Marine I'
        print '<option value="marine2">Marine 2'
        print '<option value="satellite1">Satellite I'
        print '<option value="satellite2">Satellite 2'
        print '</select><BR>'

def search_html():
	print '<B>By searching in fields:</B><BR>'
        print '<SELECT NAME="field">'
        print '<OPTION VALUE="description" SELECTED>Description only'
        print '<option value="filename">Filename only'
        print '<option value="both">Description and Filename'
        print '</select>'

def submit():
	print '<center><h3>Submit your keyword search:</H3>'
	print '<input type="submit" value="Search for keyword">'

def Main():
	form = FormContent()
	letter = "null"
	if form.has_key("letter"):
		letter = form["letter"][0]
	setup_html()
	print '<tr align="top"><td valign="top" bgcolor="#EEEEEE">'
	letters_dir()
	print '</td><td>'
	print '<form method="post" action="http://www.pals.iastate.edu/cgi-bin/C2W/search.py">'
	words_dir(letter)
	print '</td></tr>'
	print '<tr><td colspan="2">'
	style.std_bot()
	print '</td></tr></form></TABLE>'
Main()
