#!/usr/local/bin/python
#Displays image file


def lister():
	print '<HR>'




def Main():
	print 'Content-type: text/html\n\n'
	print '<HTML>'
	print '<HEAD>\n<TITLE>\nImage displayer</TITLE>\n</HEAD>\n'
	
	print '<body bgcolor="white">'
	
	lister()

	print '<img src="/images/pals_logo.gif">'

	print '</body></html>'

Main()
