#!/usr/local/bin/python
# THis is a rather silly python program that will gen javascript, barf...
# Daryl Herzmann 2-9-2000

import cgi, re, time, printHTML, style, math, os, sys


def Main():
	form = cgi.FormContent()
	if form.has_key('buildDate'):
		hour = ("0"+form["ztime"][0])[-2:]
		day = ("0"+form["day"][0])[-2:]
		year = form["year"][0]
		month = ("0"+form["month"][0])[-2:]
		dateStr = str(year)+str(month)+str(day)+str(hour)
	else:
		try:
			dateStr = form["dateStr"][0]
		except:
			style.SendError("The variable 'dateStr' is undefined!")

	try:
		year = dateStr[0:4]
		month = dateStr[4:6]
		day = dateStr[6:8]
		hour = dateStr[8:10]
		timeTuple = (int(year), int(month), int(day), int(hour), 0, 0, 0, 0, -1)
	except:
		style.SendError("dateStr variable is not formated correctly, YYYYMMDDHH ")

	try:
		timeSpan = int( form["increment"][0] )
	except:
		style.SendError("The variable 'increment' is undefined!")

	try:
		mapType = form["mapType"][0]
	except:
		style.SendError("The variable 'mapType' is undefined!")


	print 'Content-type: text/html \n\n'
	print '<HTML><HEAD></HEAD>'
	now = time.mktime(timeTuple)
	if timeSpan < 0:
		now = now + timeSpan*3600
	nowTuple = time.localtime(now)
	fdirName = time.strftime("%Y_%m_%d/", nowTuple)
        ffileName = time.strftime(mapType+"%y%m%d%H.gif", nowTuple)


	printHTML.printTop()

	print 'first_image = 1;'
	print 'last_image = '+str(math.fabs(timeSpan)+1)+';'
	print 'animation_height = 540;'
	print 'animation_width = 720;'

	printHTML.printBot()

	htmlRoot = '/home/httpd/html/archivewx/data/'
	goodAnimation = 0

	print 'theImages[0] = new Image();'
	print 'theImages[0].src = "'+fdirName+ffileName+'";'
	print 'imageNum[0] = true;'
	fileRef = htmlRoot+fdirName+ffileName
	if os.path.isfile(fileRef):
		goodAnimation = 1
		outputText = '<font color="green">'+fileRef+'</font><BR>'
	else:
		outputText = '<font color="red">'+fileRef+'</font><BR>'


	printHTML.printBot15()


	for i in range(1, math.fabs(timeSpan)+1):
		thisSecs = now + i*3600
		thisTuple = time.localtime(thisSecs)		
		dirName = time.strftime("%Y_%m_%d/", thisTuple)
		fileName = time.strftime(mapType+"%y%m%d%H.gif", thisTuple)
		
		print 'theImages['+str(i)+'] = new Image();'
		print 'theImages['+str(i)+'].src = "'+dirName+fileName+'";'
		fileRef = htmlRoot+dirName+fileName
		if os.path.isfile(fileRef):
			goodAnimation = 1
			outputText = outputText +'<font color="green">'+fileRef+'</font><BR>'
		else:
			outputText = outputText +'<font color="red">'+fileRef+'</font><BR>'
		
		print 'imageNum['+str(i)+'] = true;'
		print 'document.animation.src = theImages['+str(i)+'].src;'
		print 'document.control_form.frame_nr.value = '+str(i)+';'

	if not goodAnimation:
		print """
		</script>
		Sorry none of the files in your request were found, please go back and try again.</BR>
		<BR><BR>Files in this Animation: <font color="green">Files found</font> / <font color="red">Files not found</font><BR><BR>
		"""

		print outputText
		sys.exit(0)


	printHTML.printBot2()

	print 'SRC="'+fdirName+ffileName+'"'

	printHTML.printBot3()

	print '<BR><BR>Files in this Animation: <font color="green">Files found</font> / <font color="red">Files not found</font><BR><BR>'	

	print outputText
Main()
