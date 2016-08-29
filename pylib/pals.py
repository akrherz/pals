#!/usr/local/bin/python
# THis is the pals function file!
# Daryl Herzmann 9 May 2000

import style

def formValue( form, val):
	try:
		return form[val][0]
	except:
		style.SendError("Can not find value for "+val)

def blackBorderTop(width = "100%", bgcolor = "black"):
	print '<TABLE width="'+width+'" bgcolor="'+bgcolor+'" cellspacing="0" cellpadding="0" border="0">'
	print '<TR><TD>'
	print '	<TABLE bgcolor="WHITE" width="100%" cellpadding="3"><TR><TD>'
	
def blackBorderBot():
	print '</TD></TR></TABLE>'
	print '</TD></TR></TABLE>'	
