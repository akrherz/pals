#!/usr/local/bin/python
# This again, is a functions reference for the forecasting exercise...
# 2-12-2000: Daryl Herzmann

import cgi, style, time

def svrTop(secs_tuple, secs = 0):
        if secs != 0:
                if secs_tuple[-1] == 1:
                        secs = int(secs) - 5*3600
                else:
                        secs = int(secs) - 6*3600
                now_tuple = time.localtime( secs )
                date_str = time.strftime("%B %d, %Y", now_tuple)
                time_str = time.strftime("%I:%M %p [%Z]", now_tuple)+'&nbsp;&nbsp; ( '+str(secs_tuple[3])+' Z )'
        else:
                date_str = "Welcome!!"
                time_str = ""

        style.header("Severe Weather Forecasting Exercise", "white")

        print """
        <TABLE width="100%">
        <TR>
        <TD>
                <img src="/icons/svrTop.gif">
        </TD>
        <TD>
                <TABLE width="100%">
                <TR><TD background="/icons/sidebg.gif" align="CENTER" NOWRAP>
                        <font size="+3" color="white">Current Date & Time:</font>
                </TD></TR>
                <TR><TD bgcolor="white" align="CENTER" NOWRAP>
        """
        print '<font color="blue" size="+2">'+date_str+'</font><BR>'
        print '<font color="red" size="+2">'+time_str+'</font>'
        print """
                </TD></TR></TABLE>
        </TD></TR></TABLE>
        """
	
def svrBot():
	print """
	<BR clear="all"><BR>
	<TABLE WIDTH="100%" colspacing="0" rowspacing="0" cellpadding="0" cellspacing="0" border="0">
        	<TR>
		<TD bgcolor="#EEEEEE" align="right">
			 2000, PALS, all rights reserved
		</TD></TR>
	
		<TR>
		<TD bgcolor="#0854a8">
			<font color="#0854a8">Space Holder</font>
		</TD></TR>
	
		<TR>
		<TD bgcolor="yellow">
			<a href="/">PALS Homepage</a> | <a href="/svr_frcst/index.html">Sx Frcst Exercise Homepage</a>
		</TD></TR>
	</TABLE>"""	

def printIntro(caseNum, className = "nill"):
	import pg
	mydb = pg.connect('svr_frcst')
	try:
		entry1 = mydb.query("SELECT comments from intro WHERE case_num = '"+caseNum+"' ").getresult()[0][0]
	except:
		entry1 = "Not yet written"
	print '<font color="blue"><H2>Preview of this Case:</H2></font>'
	try:
		ldb = pg.connect('svr_'+className)
		entry2 = ldb.query("SELECT comments from intro WHERE case_num = '"+caseNum+"' ").getresult()[0][0]
		print entry2
	except:
		print entry1
	print '<BR><BR>'
