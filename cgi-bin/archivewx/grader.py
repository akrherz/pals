#!/usr/local/bin/python
# The new and improved version that passes the data on...
# Daryl Herzmann 9/14/98

from cgi import *
import style, pgext

mydbase = pgext.connect("archdays")

def Main():
	real = "18"
	form = FormContent()
	today = form["day"][0]
	state = form["state"][0]	
	time = form["time"][0]	
	month_name = form["month_name"][0]
	month_num = form["month_num"][0]
	if state == "( Select a State )": style.SendError("Please enter a state")
	if time == "( Select a time )": style.SendError("Please choose a time")	
        if form.has_key("T"): 
		tornado = form["T"][0]
        else: tornado = "no"
	if form.has_key("H"): 
		hail = form["H"][0]
	else: hail = "no"
	if form.has_key("R"): 
		rain = form["R"][0]
	else: rain = "no"
	if tornado == "no":
		if hail == "no":
			if rain == "no":
				style.SendError("Please enter a severe weather event")

	if form.has_key("real"): real = form["real"][0]

	realnext = int(real)+(1)
        realnext = str(realnext)	
	string = 'state='+state+'&time='+time+'&T='+tornado+'&R='+rain+'&H='+hail+'&real='+realnext+'&day='+today+'&month_name='+month_name+'&month_num='+month_num
	construct = mydbase.query("Select * from "+today+" where ztime = '"+real+"'").getresult() 
        try:
		events = construct[0][1]
        except IndexError:
		events = "Needs to be written yet"
	try:
		analysis = construct[0][2]
	except IndexError:
		analysis = "Needs to be written yet"
	if int(real) >= 24:
		day = str(int(today[3:5])+(1))
		if len(day) == 1: day = "0"+day
		real = str(int(real)-24)
		ustime = str(int(real)+7) 
		real = "0"+real	
		thisday = today[:3]+day+today[5:9]
	elif int(real) == 18:
		day = today[4:6]
                ustime = str(int(real)-17)
		thisday = today[:4]+day+today[6:]
	else:
		day = today[3:5]
		ustime = str(int(real)-17)
		thisday = today[:3]+day+today[5:]
	if len(thisday) > 9:
		nice_date = month_name+' '+thisday[4:6]+', '+thisday[6:]
	else:
		nice_date = month_name+' '+thisday[3:5]+', '+thisday[5:]

	print 'Content-type: text/html\n\n'
	print '<HTML><HEAD><TITLE>'+real+'Z on the '+nice_date+'</TITLE></HEAD>'
	print '<base href="https://pals.agron.iastate.edu/archivewx/data_days/'+today+'/">'
	print '<Body bgcolor="white">'

	print '<center><H1>'+real+'Z ('+ustime+'PM CDT) '+nice_date+'</H1></center>'
	print '<H3>What has happened this past hour:</H3>'
	print events

	print '<BR><BR>'

	print '<H3>Weather Advisories for this hour:</H3>'
	print '<a href="data/98'+month_num+day+real+'.txt">Watches and Warnings</a>'

	print '<H3>Weather Data for '+real+'Z:</H3>'
	print '<P><a href="data/sfc98'+month_num+day+real+'.gif">Surface Chart</a> ---' 
	print '<a href="data/temp98'+month_num+day+real+'.gif">Surface Temps</a> ---' 
	print '<a href="data/dew98'+month_num+day+real+'.gif">Surface Dew Points</a> --' 
	print '<a href="data/NAT98'+month_num+day+real+'.gif">National Radar</a>' 
	
	print '<H3>Analysis:</H3>'
	print analysis

	if real == "05":
		print "<center><HR><H2>Let's view your forecast results</H2>"
		print '<a href="https://pals.agron.iastate.edu/cgi-bin/archivewx/results.py?'+string+'">'
		print 'CLICK HERE</a></center>'

	else:
		print '<H3>Help Topics</H3>'
		print '<a href="/archivewx/help/z.html">What is Z time</a> ---'
       		print '<a href="/archivewx/help/text.html">Watches and Warnings Data</a> ---'
       		print '<a href="/archivewx/help/temp.html">Surface Temperature Map</a><BR>'
       		print '<a href="/archivewx/help/sfcmap.html">Surface Map</a> ---'
        	print '<a href="/archivewx/help/dewp.html">Surface Dewpoints Map</a> --'
	        print '<a href="/archivewx/help/radar.html">Radar</a>'
		print '<HR><center><a href="https://pals.agron.iastate.edu/cgi-bin/archivewx/grader.py?'+string+'">'
		ustime = str(int(ustime)+1)
		print "Let's see what happens at "+ustime+" PM</a>"
	style.std_bot()
       	sys.exit(0) 
Main()
