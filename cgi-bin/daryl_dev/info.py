#!/usr/local/bin/python

from pgext import * 
from cgi import * 
import os, sys


mydbase = connect("c2w")


form = FormContent()

myurl = form["url"][0]

lookfor = ""
lookfor = mydbase.query("select * from linkex where url = '"+myurl+"'")
lookfor = lookfor.getresult()

print 'Content-type: text/html\n\n'
print '<HEAD>\n<TITLE>Description of Ya</TITLE>\n</HEAD>\n'
print '<body bgcolor="white">'

description = lookfor[0][6]
title = lookfor[0][0]
url = lookfor[0][1]
print '<H1>Description of '+title+'</H1>'

print '<BR><BR><BR>'
print '<table>'
print '<tr>'
print '<th>Title:'
print '<td>'+title+'</td>'
print '<tr>'
print '<th>URL:'
print '<td>'+url+'</td>'
print '<tr>'
print '<th>Description:'
print '<td>'+description+'</td>'
print '</table>'

print '</html>'
