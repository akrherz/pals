#! /usr/local/bin/python 

import sys, string 
from socket import *

CHECK_FOR =(('akrherz','shadow.iitap.iastate.edu'),('akrherz','pals.agron.iastate.edu'),('akrherz','isum.iastate.edu'),('akrherz','las1.iastate.edu'),('akrherz','isua.iastate.edu'))
 
def check_machine(username, machine): 
    sock = socket(AF_INET, SOCK_STREAM) 
    try: 
        sock.connect(machine, 79) 
    except: 
        return ''
    sock.send(username + '\n') 
    while 1: 
        info = sock.recv(1024) 
        if info: 
            return info

print "Content-type: text/html\n\n"
print "<header>\n<title>Where is Herz?</title>\n</header>\n"  
print "<body bgcolor='white'>\n" 
print "<center><h2>Places Herz is currently logged in...</h2></center>"
ret = []
for account in CHECK_FOR: 
    temp = string.splitfields(check_machine(account[0], account[1]), '\n') 
    for line in temp: 
        line = string.lower(line) 
        if line[:8] == 'on since': 
            ret.append('Found on '+account[1]+' ('+account[0]+')') 
            break 
print '<h3>Herz is logged in '+`len(ret)`+' times.<ul>' 
if len(ret): 
    	for login in ret: 
        	print '<li>'+ login + '</li>'
    	print '</ul>' 
else: 
    	print 'Herz is not logged in anywhere'
print "</body>\n</html>\n"
