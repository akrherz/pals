#!/usr/local/bin/python
# This script will hand off to loop, which will generate a handy radar loop
# Daryl Herzmann 28 Feb 2001
# 21 Mar 2001:  Added ability to specify a time and then a loop length

import pg, cgi, DateTime, time, printHTML, os

mydb = pg.connect('wx', 'localhost', 5432)
mydb.query("SET TIME ZONE 'GMT'")


def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	mySite = form["site"][0]
	myTimes = []

	if form.has_key("all"): # Lets loop it all baby
		myCase = form["all"][0]
		rs = mydb.query("SELECT starttime, stoptime from radardata WHERE caseid = "+myCase+" ").dictresult()

	        startDate = DateTime.ISO.ParseDateTimeGMT(rs[0]["starttime"])
	        endDate = DateTime.ISO.ParseDateTimeGMT(rs[0]["stoptime"])
	        startSecs = startDate.gmticks()
	        endSecs = endDate.gmticks()

	        now = startSecs
	
	        while ( now <= endSecs ):
	                thisTuple = time.gmtime(now)
	                timeString = time.strftime("%y%m%d%H%M", thisTuple)
			myTimes.append( timeString )
	                now = now + 5*60

	elif form.has_key("start"):
		loopLength = form["steps"][0]
		startTime  = form["start"][0]  
		thisTime = startTime
		for i in range( int(loopLength) ):
			thisGoodTime = time.mktime( time.strptime(thisTime, "%y%m%d%H%M") ) + i*300
			myTupleTime  = time.localtime( thisGoodTime )
			timeString = time.strftime("%y%m%d%H%M", myTupleTime)
                        myTimes.append( timeString )

	else:
		myTimes = form["timeStamp"]
		myTimes.sort()

	siteDir = mySite
	if form.has_key("blind"):
		siteDir = mySite+"b"

#	print myTimes

	myYear = myTimes[0][:2]
	myMonth = myTimes[0][2:4]
	myDay = myTimes[0][4:6]

	if myYear[0] == "9":
		myYear = "19"+myYear
	else:
		myYear = "20"+myYear

        webRoot = 'https://pals.agron.iastate.edu/archivewx/data/'+myYear+'_'+myMonth+'_'+myDay+'/'+siteDir+'/'
        htmlRoot = '/home/httpd/html/archivewx/data/'+myYear+'_'+myMonth+'_'+myDay+'/'+siteDir+'/'

	goodFiles = []
	outputText = ""
	for myTime in myTimes:
		fileRef = htmlRoot+mySite+str(myTime)+".gif"
		#print fileRef
                if os.path.isfile(fileRef):
			goodFiles.append( myTime )
                        outputText = outputText +'<font color="green">'+fileRef+'</font><BR>'
                else:
                        outputText = outputText +'<font color="red">'+fileRef+'</font><BR>'


	myTimes = goodFiles


	printHTML.setupHTML()

	print '<BASE HREF="'+webRoot+'">'	


	printHTML.printTop()


        print 'first_image = 1;'
        print 'last_image = '+str( len(myTimes) )+';'
        print 'animation_height = 540;'
        print 'animation_width = 720;'

        printHTML.printBot()

        goodAnimation = 0

        print 'theImages[0] = new Image();'
        print 'theImages[0].src = "'+mySite+str( myTimes[0] )+'.gif";'
        print 'imageNum[0] = true;'


        printHTML.printBot15()

	i = -1
        for myTime in myTimes:
		i = i+1                
                print 'theImages['+str(i)+'] = new Image();'
                print 'theImages['+str(i)+'].src = "'+mySite+str( myTime )+'.gif";'
                
                print 'imageNum['+str(i)+'] = true;'
                print 'document.animation.src = theImages['+str(i)+'].src;'
                print 'document.control_form.frame_nr.value = '+str(i)+';'


        printHTML.printBot2()

	print 'SRC="'+mySite+str( myTimes[0] )+'.gif"'

        printHTML.printBot3()


	print '<BR><BR>Files in this Animation: <font color="green">Files found</font> / <font color="red">Files not found</font><BR><BR>'

	if not form.has_key("blind"):
	        print outputText


Main()
