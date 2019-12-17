#!/usr/local/bin/python
#Finds all of the links and just prints them out

from pgext import * 
from cgi import * 
import os, sys, string

mydbase = connect("c2w")

print 'Content-type: text/html\n\n'
print '<HEAD>\n<TITLE>Links printed out</TITLE>\n</HEAD>\n'
print '<body bgcolor="white">'
print '<table width="700" border="0">'
print '<tr>'
print '<td colspan="2" rowspan="6"><img src="/images/pals_logo.gif" align="left"><H1>Links<BR>Submitted</H1>'
print '<a href="https://pals.agron.iastate.edu/links/linksub.html">Add link</a>'
print '<td colspan="4"><b>Link Categories</b></td></tr>'
print '<td colspan="4"><font color="red">A is the name of the collumn</td></tr>'
print '<td><font color="red">|</td><td colspan="3"><font color="orange">B is this collumn</td></tr>'
print '<td><font color="red">|</td><td><font color="orange">|</td><td colspan="2"><font color="purple">C is this collumn</td></tr>'
print '<td><font color="red">|</td><td><font color="orange">|</td><td><font color="purple">|</td><td><font color="green">D is this collumn</td></tr>'
print '<td><font color="red">|</td><td><font color="orange">|</td><td><font color="purple">|</td><td><font color="green">|</td></tr>'
print '<th align="left">Link'
print '<th align="left">Description'
print '<th><font color="red">|'
print '<th><font color="orange">|'
print '<th><font color="purple">|'
print '<th><font color="green">|'
print '<th align="left">submitted</tr>\n'

aselect = ""
aselect = mydbase.query("select * from linkex where kindA != 'null'")
aselect = aselect.getresult()
aselect.sort()
print '<tr height="10">\n<td colspan="7" align="left" valign="center" bgcolor="lavander"><B><spacer type="horizontal" size="50">'
print '<img src="/images/point_02.gif">Those with AA</B>'
for i in range(len(aselect)):
       	kindA = aselect[i][2]
       	kindB = aselect[i][3]
       	url = aselect[i][1]
       	kindC = aselect[i][4]
       	kindD = aselect[i][5]
       	link = aselect[i][0]
       	description = aselect[i][6]
       	entime = aselect[i][7]		
                
	print '<tr border="1">'
        print '<td><a href="'+url+'">'+link+'</a>\n'
	if len(description) > 0:
		print '<td><a href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/info.py?url='+url+'">info</a>\n'
	else:
		print '<td></td>'

	if kindA == "null": kindA = ""
	print '<td><font color="red">'+kindA+'</td>'
		
	if kindB == "null": kindB = "" 
        print '<td><font color="orange">'+kindB+'</td>'
			
	if kindC == "null": kindC = "" 
        print '<td><font color="purple">'+kindC+'</td>'
			
	if kindD == "null": kindD = "" 
        print '<td><font color="green">'+kindD+'</td>'
			
	print '<TD ALIGN="LEFT" VALIGN="CENTER">'+entime[4:10]+entime[22:27]+'</TD>'
        print '</TR>'
	

bselect = ""  
bselect = mydbase.query("select * from linkex where kindB != 'null'")  
bselect = bselect.getresult()  
bselect.sort()
print '<tr><td colspan="7">&nbsp;</td>'
print '<tr height="10">\n<td colspan="7" align="left" valign="center" bgcolor="lavander"><B><spacer type="horizontal" size="50">'
print '<img src="/images/point_02.gif">Those with BB</B>'
for i in range(len(bselect)): 
        kindA = bselect[i][2]
        kindB = bselect[i][3]
        url = bselect[i][1]
        kindC = bselect[i][4]
        kindD = bselect[i][5]
        link = bselect[i][0]
        description = bselect[i][6]
        entime = bselect[i][7]

        print '<tr>'
        print '<td><a href="'+url+'">'+link+'</a>\n'
	if len(description) > 0: 
                print '<td><a href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/info.py?url='+url+'">info</a>\n'
        else: 
                print '<td></td>'

	if kindA == "null": kindA = "" 
        print '<td><font color="red">'+kindA+'</td>'

        if kindB == "null": kindB = "" 
        print '<td><font color="orange">'+kindB+'</td>'

        if kindC == "null": kindC = "" 
        print '<td><font color="purple">'+kindC+'</td>'

        if kindD == "null": kindD = "" 
        print '<td><font color="green">'+kindD+'</td>'

        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+entime[4:10]+entime[22:27]+'</TD>'

	print '</TR>'


cselect = ""  
cselect = mydbase.query("select * from linkex where kindC != 'null'")  
cselect = cselect.getresult()  
cselect.sort()
print '<tr><td colspan="7">&nbsp;</td>'
print '<tr height="10">\n<td colspan="7" align="left" valign="center" bgcolor="lavander"><B><spacer type="horizontal" size="50">'
print '<img src="/images/point_02.gif">Those with CC</B>'
for i in range(len(cselect)): 
        kindA = cselect[i][2]
        kindB = cselect[i][3]
        url = cselect[i][1]
        kindC = cselect[i][4]
        kindD = cselect[i][5]
        link = cselect[i][0]
        description = cselect[i][6]
        entime = cselect[i][7]
        
        print '<tr>'
        print '<td><a href="'+url+'">'+link+'</a>\n'
	if len(description) > 0: 
                print '<td><a href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/info.py?url='+url+'">info</a>\n'
        else: 
                print '<td></td>'

        if kindA == "null": kindA = "" 
        print '<td><font color="red">'+kindA+'</td>'

        if kindB == "null": kindB = "" 
        print '<td><font color="orange">'+kindB+'</td>'
        
        if kindC == "null": kindC = "" 
        print '<td><font color="purple">'+kindC+'</td>'

        if kindD == "null": kindD = "" 
        print '<td><font color="green">'+kindD+'</td>'

        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+entime[4:10]+entime[22:27]+'</TD>'
        
        print '</TR>'



dselect = ""  
dselect = mydbase.query("select * from linkex where kindD != 'null'")  
dselect = dselect.getresult()  
dselect.sort()
print '<tr><td colspan="7">&nbsp;</td>'
print '<tr height="10">\n<td colspan="7" align="left" valign="center" bgcolor="lavander"><B><spacer type="horizontal" size="50">'
print '<img src="/images/point_02.gif">Those with DD</B>'
for i in range(len(dselect)): 
        kindA = dselect[i][2]
        kindB = dselect[i][3]
        url = dselect[i][1]
        kindC = dselect[i][4]
        kindD = dselect[i][5]
        link = dselect[i][0]
        description = dselect[i][6]
        entime = dselect[i][7]
        
        print '<tr>'
        print '<td><a href="'+url+'">'+link+'</a>\n'
	if len(description) > 0: 
                print '<td><a href="https://pals.agron.iastate.edu/cgi-bin/daryl_dev/info.py?url='+url+'">info</a>\n'
        else: 
                print '<td></td>'

        if kindA == "null": kindA = "" 
        print '<td><font color="red">'+kindA+'</td>'

        if kindB == "null": kindB = "" 
        print '<td><font color="orange">'+kindB+'</td>'
        
        if kindC == "null": kindC = "" 
        print '<td><font color="purple">'+kindC+'</td>'

        if kindD == "null": kindD = "" 
        print '<td><font color="green">'+kindD+'</td>'

        print '<TD ALIGN="LEFT" VALIGN="CENTER">'+entime[4:10]+entime[22:27]+'</TD>'
        
        print '</TR>'

print '</table>'
print '</html>'
