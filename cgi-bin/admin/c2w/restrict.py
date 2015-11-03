#!/usr/local/bin/python
# This is the program that restricts and allows access to COMET files
# Daryl Herzmann 1/16/99

from cgi import *
from pgext import *
import style

# Global Stuff
mydb = connect('c2w')
comet_dirs = ('acsse','csm','fire','forecast','hydro','marine1','marine2','satellite1','satellite2')

def make_dirs():
	print '<H3>Select a directory to edit:</H3>'
	for comet_dir in comet_dirs:
		print '<a href="restrict.py?dir='+comet_dir+'">'
		print comet_dir+'</a><BR>'

def dir_loader(dir):
	released = mydb.query("SELECT * from movies WHERE filename ~* '.*"+dir+".*'").getresult()
	released.sort()
	print '<table border="0" align="left" WRAP>'
	print '<TR><TH colspan="3"><H3>Files Released to Public in '+dir+':</H3></TH></TR>'
	print '<TR><TH>Filename:</TH><TH colspan="2">Change Status To:</TH></TR>'
	for i in range(len(released)):
		filename = released[i][1]
		i = str(i)
		print '<TR><TD>'
		print '<B><a href="/c2w/'+filename+'">'+filename+'</a></B></TD>'
		print '<TD><input type="radio" name="rfile'+i+'" value="y" CHECKED>Yes</TD>'
		print '<input type="hidden" name="rfile'+i+'name" value="'+filename+'">'
		print '<TD><input type="radio" name="rfile'+i+'" value="n">No<BR></TD></TR>'
	print '<input type="hidden" value="'+i+'" name="rtotal"></TABLE>'

	print '<spacer type="horizontal" size="10">'

	unreleased = mydb.query("SELECT * from unreleased WHERE filename ~* '.*"+dir+".*'").getresult()
	unreleased.sort()
	print '<table border="0">'
	print '<TR><TH colspan="3"><H3>Files NOT Released to Public in '+dir+':</H3></TH></TR>'
	print '<TR><TH>Filename:</TH><TH colspan="2">Change Status To:</TH></TR>'
	j = "0"
	for j in range(len(unreleased)):
		filename = unreleased[j][1]
		j = str(j)
		print '<TR><TD>'
		print '<B><a href="/c2w/'+filename+'">'+filename+'</a></B></TD>'
		print '<TD><input type="radio" name="ufile'+j+'" value="y">Yes</TD>'
		print '<input type="hidden" name="ufile'+j+'name" value="'+filename+'">'
		print '<TD><input type="radio" name="ufile'+j+'" value="n" CHECKED>No<BR></TD></TR>'
	print '<input type="hidden" value="'+j+'" name="utotal"></TABLE>'

	print '<input type="hidden" value="'+dir+'" name="cwd">'
	
def change_to_r(file):
	movies = mydb.query("SELECT * from unreleased WHERE filename ~* '.*"+file+".*'").getresult()

	url = movies[0][0]
	filename = movies[0][1]
	title = movies[0][2]
	description = movies[0][3]
	size = str(movies[0][4])
	runtime = movies[0][5]
	keywords = movies[0][6]
	release = movies[0][7]
	insert = mydb.query("INSERT into movies values ('"+url+"' , '"+filename+"' , '"+title+"' , '"+description+"' , "+size+" , '"+runtime+"' , '"+keywords+"' , '"+release+"')")
	delete = mydb.query("DELETE from unreleased WHERE filename = '"+file+"'")
	print '<H3>Changing status of '+filename+' to released</H3>'

def change_to_u(file):
	movies = mydb.query("SELECT * from movies WHERE filename ~* '.*"+file+".*'").getresult()

	url = movies[0][0]
	filename = movies[0][1]
	title = movies[0][2]
	description = movies[0][3]
	size = str(movies[0][4])
	runtime = movies[0][5]
	keywords = movies[0][6]
	release = movies[0][7]
	insert = mydb.query("INSERT into unreleased values ('"+url+"' , '"+filename+"' , '"+title+"' , '"+description+"' , "+size+" , '"+runtime+"' , '"+keywords+"' , '"+release+"')")
	delete = mydb.query("DELETE from movies WHERE filename = '"+file+"'")
	print '<H3>Changing status of '+filename+' to unreleased:</H3>'


def Main():
	style.header("Restrict / Allow Access to C2W","white")
	form = FormContent()
	if form.has_key('cwd'):
		cwd = form["cwd"][0]
		rtotal = int(form["rtotal"][0])
		utotal = int(form["utotal"][0])
		for i in range(rtotal + 1):
			i = str(i)
			if form["rfile"+i][0] == "n":
				change_to_u(form["rfile"+i+"name"][0])

		for j in range(utotal + 1):
			j = str(j)
			if utotal == "0": break
			if form["ufile"+j][0] == "y":
				change_to_r(form["ufile"+j+"name"][0])


	if form.has_key('dir'): 
		print '<form method="POST" action="restrict.py">'
		dir_loader(form["dir"][0])
		print '<BR clear="all"><HR><HR>'
		print '<input type="submit" value="Make Changes">'
		print '<input type="reset">'
		print '</form>'
	else:
		make_dirs()

Main()
