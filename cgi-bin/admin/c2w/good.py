#!/usr/local/bin/python
# This program changes the good / bad standing in movies db
# Daryl Herzmann 7/8/99

from pgext import *
import cgi, style

mydb = connect('c2w')

comet_dirs = ('acsse','csm','fire','forecast','hydro','marine1','marine2','satellite1','satellite2')

def make_dirs():
        print '<H3>Select a directory to edit:</H3>'
        for comet_dir in comet_dirs:
                print '<a href="restrict.py?dir='+comet_dir+'">'
                print comet_dir+'</a><BR>'

def dir_loader(dir):
	files = mydb.query("SELECT runtime, filename from movies WHERE filename ~* '.*"+dir+".*'").getresult()
	files.sort()
	print '<table border="0" align="left" WRAP>'
	print '<TR><TH colspan="3"><H3>Good Files in '+dir+':</H3></TH></TR>'
	print '<TR><TH>Filename:</TH><TH colspan="2">Change Status To:</TH></TR>'
	for i in range(len(files)):
		runtime = files[i][0]
		filename = files[i][1]
		i = str(i)
		print '<TR><TD>'
                print '<B><a href="/c2w/'+filename+'">'+filename+'</a></B></TD>'
                print '<TD><input type="radio" name="rfile'+i+'" value="y" CHECKED>Yes</TD>'
                print '<input type="hidden" name="rfile'+i+'name" value="'+filename+'">'
                print '<TD><input type="radio" name="rfile'+i+'" value="n">No<BR></TD></TR>'
        print '<input type="hidden" value="'+i+'" name="rtotal"></TABLE>'


def Main():
	style.header("Best of COMET","white")
	form = cgi.FormContent()
	if form.has_key("cwd"):
		cwd = form["cwd"][0]
		ntotal = int(form["ntotal"][0])
		ytotal = int(form["ytotal"][0])
		for i in range(ntotal+1):
			i = str(i)
			if form["nfile"+i][0] == "N":
			change_to_n(form["nfile"+i+"name"][0])

		for j in range(ytotal + 1):
                        j = str(j)
                        if ytotal == "0": 
				break
                        if form["yfile"+j][0] == "Y":
                                change_to_y(form["yfile"+j+"name"][0])

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


