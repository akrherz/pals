#!/usr/local/bin/python
# This program will monitor the integraty of the data on file
# Daryl Herzmann, 25-Apr-2000

import time, os
nowTuple = time.gmtime( time.time() )
localTuple = time.localtime( time.time() )
niceDate = time.strftime("%d %B %Y -- %H:%M:%S", nowTuple)
localDate = time.strftime("%d %B %Y -- %I:%M:%S %p", localTuple)
nowHour = nowTuple[3]
nowSecs = time.mktime(nowTuple)

htmlRoot = '/hhh/archivewx/data/'

dataCheck = [	('Ruc Model', '/data/gempak/hrs/', '_ruc.gem', '2'),
		('ETA Model', '/data/gempak/hrs/', '_eta.gem', '12'),
		('AVN Model', '/data/gempak/hrs/', '_a.gem', '12'),
		('MRF Model', '/data/gempak/hrs/', '_m.gem', '24')
	]

hourlyCheck = [	('Surface Temps', 'temp', ':24 after'),
		('Surface Plot', 'sfc', ':19 after'),
		('IR Sat', 'sat', ':49 after'),
		('Water Vapor', 'wvap', ':45 after'),
		('Surface Moisture Div', 'moist', ':24 after'),
		('Surface Dew Points', 'dew', ':24 after')
	]


def hourlyVerify(prefix):
	testFile = time.strftime(htmlRoot+'%Y_%m_%d/'+prefix+'%Y%m%d%H.gif', nowTuple)
	testSecs =nowSecs

	cont = 0
	while not (os.path.isfile(testFile)):
                testSecs = testSecs - 3600
                testTuple = time.localtime(testSecs)
                testFile = time.strftime(htmlRoot+"%Y_%m_%d/"+prefix+"%y%m%d%H.gif",testTuple)
                cont = cont +1
                if cont > 10:
                        break

	return testSecs, cont


def lastFile(dirName, suffix):
	os.chdir(dirName)
	return os.popen("ls *"+suffix+" | sort | tail -1")


def Main():
	print 'Content-type: text/html \n\n'
	print """
	<HTML>
	<HEAD>
		<TITLE>PALS Data Watcher</TITLE>
		<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
		<META HTTP-EQUIV="REFRESH" CONTENT="600">

	</HEAD>
	<body bgcolor="white">
	[This page reloads every 10 minutes]<BR><BR>
	"""
	
	print "GMT Time -> "+ niceDate
	print "<BR>"
	print "Local Time -> "+localDate

	print """
	<H3>Raw Model Data:</H3>
	<TABLE>
		<TR><TH NOWRAP>Valid:</TH><TH NOWRAP>Data Product:</TH><TH NOWRAP>Last Valid:</TH></TR>

	"""
	for i in range(len(dataCheck)):
		thisLast = lastFile( dataCheck[i][1] , dataCheck[i][2]).read()
		thisTime = "20"+thisLast[:8]
		timeMake = time.strptime(thisTime, "%Y%m%d%H")
		thisDate = time.strftime("[%d %B %Y]  %H Z", timeMake)
		timeSecs = time.mktime(timeMake)

		print '<TR>'
		print '<TD>'
		if ( (nowSecs - timeSecs) > int(dataCheck[i][3])*3600 ):
			print '<img src="/icons/b.png">'
		else:
			print '<img src="/icons/g.png">'
		print '</TD>'

		print '<TD>'+dataCheck[i][0]+'</TD><TD>'+thisDate+'</TD>'

		print '</TR>'
	print '</TABLE>'


	print """
	<H3> ***  PALS Web Pics: *** </H3>
	<TABLE>
	<TR>
		<TH>Valid:</TH>
		<TH NOWRAP>Data Product:</TH>
		<TH NOWRAP>Last Valid:</TH>
		<TH NOWRAP>Gen Time:</TH>
	</TR>

	"""
	for j in range(len(hourlyCheck)):
		tSecs, cont = hourlyVerify(hourlyCheck[j][1])
		timeStamp = time.localtime(tSecs)
		thisDate = time.strftime("[%d %B %Y]  %H Z", timeStamp)
		print '<TR>'
                print '<TD>'
		if cont > 2:
			print '<img src="/icons/b.png">'
		else:
			print '<img src="/icons/g.png">'
		print '</TD>'
        
                print '<TD NOWRAP>'+hourlyCheck[j][0]+'</TD><TD NOWRAP>'+thisDate+'</TD>'
                print '<TD NOWRAP align="right">'+hourlyCheck[j][2]+'</TD>'

                print '</TR>'   
        print '</TABLE>'


Main()
