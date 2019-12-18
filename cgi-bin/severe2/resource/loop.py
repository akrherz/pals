#!/usr/bin/env python2
# This program generates loops for the data information as presented 
# Daryl Herzmann 26 June 2000

# ****
# This script was a major hack, now it only supports a true dateStr
#	
#	I also need a "mapType" variable to tell me what to display
#	And I need a "timeSpan" argument to let me know how long to go!
# ****

import cgi, re, time, printHTML, style, math, os, sys, pals

archiveDir = '/hhh/archivewx/data/'
urlRoot = 'https://pals.agron.iastate.edu/archivewx/data/'

def fetchArray(startSecs, mapType, timeSpan):
	goodArray = []
	thisSecs = startSecs +3600
	limiter = 0
	for i in range(0, math.fabs(timeSpan)+1):
		thisSecs = thisSecs -3600
		thisTuple = time.localtime(thisSecs)		
		dirName = time.strftime("%Y_%m_%d/", thisTuple)
		fileName = time.strftime(mapType+"%y%m%d%H.gif", thisTuple)
		fileRef = archiveDir+dirName+fileName
#	    print fileRef
		if os.path.isfile(fileRef):
			goodArray.append(dirName+fileName)
		else:
			i = i -1
		limiter = limiter + 1
		if (limiter > 20): break

	return goodArray

def Main():
	print 'Content-type: text/html \n\n'
	form = cgi.FormContent()
	dateStr = pals.formValue(form, "dateStr")

	timeSpan = int(float( pals.formValue(form, "timeSpan") ))
	mapType = pals.formValue(form, "mapType")
	
	# Now we try to parse this dateStr back into its componets to build a time tuple
	try:
		startTuple = time.strptime(dateStr, "%Y%m%d%H")
		startSecs = time.mktime(startTuple)	
		startTuple = time.localtime(startSecs)	
	except ValueError:
		style.SendError("dateStr variable is not formated correctly, YYYYMMDDHH ")

	goodArray = fetchArray(startSecs, mapType, timeSpan)

	
	# Now we need to find at least one good file to start us off

	if len(goodArray) < 2:
		style.SendError("Could not find any plots for your loop, sorry")
	
#	print goodArray
	printHTML.printTop()

	print 'first_image = 1;'
	print 'last_image = '+str(int(float( len(goodArray) )) )+';'

	printHTML.printBot()
	
	print 'theImages[0] = new Image();'
	print 'theImages[0].src = "'+goodArray[-1]+'";'
	print 'imageNum[0] = true;'
	outputText = '<font color="green">'+goodArray[-1]+'</font><BR>\n'

	printHTML.printBot15()

	for i in range(1, len(goodArray)):
		fileRef = archiveDir+goodArray[-1-i]
		print 'theImages['+str(i)+'] = new Image();'
		print 'theImages['+str(i)+'].src = "'+goodArray[-1-i]+'";'
		outputText = outputText +'<font color="green">'+goodArray[-1-i]+'</font><BR>\n'
		print 'imageNum['+str(i)+'] = true;'
		print 'document.animation.src = theImages['+str(i)+'].src;'
		print 'document.control_form.frame_nr.value = '+str(i)+';'
	

	printHTML.printBot2()

	print 'SRC="'+goodArray[-1]+'"'

	printHTML.printBot3()

	print '<BR><BR>Files in this Animation: <font color="green">Files found</font> / <font color="red">Files not found</font><BR><BR>'	

	print outputText

Main()
