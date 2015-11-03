#!/usr/local/bin/python
# New annotation add
# Daryl Herzmann 8/9/98

import style, sys

def Main():
	style.header("New Annotation","white")
	style.std_top("New One")
	print '<form method="post" action="add_annote.py">'
        print '<H3>Enter a day in the form mo.da.year (ex 06.09.1998)</H3>'
        print '<input type="text" name="day">'
        print '<H3>Enter description</H3>'
        print '<textarea name="descrip" cols="90" rows="20"></textarea>'
        print '<input type="submit" value="New Entry">'
	print '</form></body></html>'
	sys.exit(0)

Main()
