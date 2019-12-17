#!/usr/local/bin/python 

from pgext import * 
from cgi import *
import os, sys, regsub

mydbase = connect("akrherz")

def SendError(str): 
	errmsg = escape(str) 
	print "Content-type: text/html\n\n" 
	print "<HEADER>\n<TITLE> CGI Error </TITLE>\n</HEADER>\n" 
	print "<BODY bgcolor=#FFFFFF>\n" 
	print "<H1>CGI Error</H1>\n" 
	print '<H3>' + errmsg + '</H3>\n' 
	print "</BODY>" 
	sys.exit(0) 

def Main():
	print 'Content-type: text/html\n\n' 
        print '<HEADER>\n<TITLE>Entering message</TITLE>\n</HEADER>\n' 
        print '<BODY bgcolor="white">\n'

	form = FormContent()

	subject = form["subject"][0]
	name = form["name"][0]
	address = form["address"][0]
	description = form["description"][0]

	subject = regsub.gsub("'","&#180;",subject)
	name = regsub.gsub("'","&#180;",name)
	description = regsub.gsub("'","&#180;",description)

	if not form.has_key("subject"): SendError("You need to enter a subject") 
        if not form.has_key("name"): SendError("You should enter your name") 
        if not form.has_key("address"): SendError("What is your email address")
	if not form.has_key("description"): SendError("What is it's description")

	time = os.popen('date', 'r').read()

	enter = mydbase.query("INSERT INTO board VALUES('"+time+"','"+subject+"','"+name+"','"+address+"','"+description+"')")
	 
	print '<img src="../../images/pals_logo.gif" align=left>\n'
        print '<spacer type=vertical size="30">\n'
        print '<H1>PALS bulletin board</H1>\n'
        print '<a href="https://pals.agron.iastate.edu/home/bboard.html">Add comment</a>'
	print '<BR CLEAR="all"><HR>'


        search = mydbase.query("select * from board")
        search = search.getresult()

        for i in range(len(search)):
                subject = search[i][1]
                name = search[i][2]
                address = search[i][3]
                description = search[i][4]
                date = search[i][0]
                date = date[4:10]+date[22:27]
                print "<P>\n<b>Subject:"
                print subject+'</b>'
                print "<BR>\n<dd>"
                print description
                print "<BR>\n"
                print '<P align="right">'
                print "( Posted by:"
                print '<A HREF="mailto:'+address+'" STYLE="color:blue">'+name+'</A>'
                print 'Posted on:'
                print date+')'
                print '</p><HR>'
Main()






