#!/usr/local/bin/python
# This is a program that will ask the general questions at 6 hours in
# Daryl Herzmann 8-19-99

import pg, sys

admindb = pg.connect('archadmin')

def states():
        print '<SELECT NAME="state"><OPTION> Alabama <OPTION> Arkansas <OPTION> Arizona<OPTION> California <OPTION> Colorado <OPTION> Connecticut <OPTION> Delaware <OPTION> Florida<OPTION> Georgia <OPTION> Idaho <OPTION> Illinois <OPTION> Indiana<OPTION> Iowa <OPTION> Kansas<OPTION> Kentucky <OPTION> Louisiana <OPTION> Maine <OPTION> Maryland'
        print '<OPTION> Massachusetts<OPTION> Michigan <OPTION> Minnesota <OPTION> Mississippi <OPTION> Missouri <OPTION> Montana<OPTION> Nebraska <OPTION> Nevada <OPTION> New_Hampshire <OPTION> New_Jersey <OPTION> New_Mexico'
        print '<OPTION> New_York <OPTION> North_Carolina <OPTION>North_Dakota <OPTION> Ohio <OPTION> Oklahoma<OPTION> Oregon <OPTION> Pennsylvania <OPTION> Rhode_Island <OPTION> South_Carolina <OPTION> South_Dakota'
        print '<OPTION> Tennessee <OPTION> Texas <OPTION> Utah <OPTION>Vermont <OPTION> Virginia <OPTION> Washington<OPTION> Wisconsin <OPTION> West_Virginia <OPTION> Wyoming </SELECT>'

def types():
        print '<CENTER>'
        print '<table width="100%" align="center"><tr>'
        print '<th><INPUT TYPE=checkbox NAME="six" VALUE="six"> 6 to 12 inches of Snow</th>'
        print '<th><INPUT TYPE=checkbox NAME="twelve" VALUE="twelve"> Greater than 12 inches of Snow</th>'
        print '<th><INPUT TYPE=checkbox NAME="freeze" VALUE="f"> Freezing Rain / Ice </th>'
        print '</tr></table>'


def Main(case_num, secs, key, refer):
	print '<form method="POST" action="wrapper.py">'
	print '<input type="hidden" name="case_num" value="'+str(case_num)+'">'
	print '<input type="hidden" name="secs" value="'+str(secs)+'">'
	print '<input type="hidden" name="key" value="'+str(key)+'">'
	print '<input type="hidden" name="refer" value="'+str(refer)+'">'

	states()
	types()

	print '<input type="submit" value="Submit Forecast">'
	print '</form>'

	sys.exit()
