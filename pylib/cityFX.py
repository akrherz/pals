#!/usr/local/bin/python
# Functions file for the city forecasting activity
# Daryl Herzmann 15 September 2000



def setupPage(title = "Archived City Forecasting Activity"):
	print 'Content-type: text/html \n\n'
	print '<HTML>\n<HEAD>'
	print '\t<TITLE>'+title+'</TITLE>'
	print '</HEAD>\n<body bgcolor="white">'
	print """
	<TABLE width="100%">
                <TR><TD background="/icons/sidebg.gif" align="CENTER" NOWRAP>
                        <font size="+3" color="white"><B>Archived Forecasting Activity</b></font>
                </TD></TR>
        <TR><TD>"""
	

def finishPage():
	print """</TD></TR>
                <TR><TD background="/icons/sidebg.gif" align="right" NOWRAP>
                        <font size="+1" color="white"><B>&copy; 2000 PALS</b></font>
                </TD></TR>
                <TR><TD align="right" NOWRAP>
                        <a href="http://www.pals.iastate.edu">PALS Home</a> &nbsp; | &nbsp; 
                        <a href="http://www.pals.iastate.edu/cityFX">City Forecasting</a> &nbsp; | &nbsp;


                </TD></TR>
        </TABLE>"""
