#!/usr/local/bin/python
# This is my attempt at getting the winter forecast working
# Daryl Herzmann 8-18-99

import cgi, pg, style, question, time, functs

admindb = pg.connect('archadmin')
sessiondb = pg.connect('sessions_417')
annotedb = pg.connect('arch_hourly')

def been_here(key, secs):
	table_str = "win_sessions_417"
	query = admindb.query("SELECT last_time from "+table_str+" WHERE key = '"+str(key)+"' ").getresult()
	if float(secs) > float(query[0][0]):
		return 0		# Have not been here
	else:
		return 1		# Have been here

def updatedb(key, secs):
	table_str = "win_sessions_417"
        query = admindb.query("UPDATE "+table_str+" SET last_time = '"+str(secs)+"' WHERE key = '"+str(key)+"' ")

def content():
	print '<BR>'
	print '<dd>You should view the available data for this hour and then navigate onto the next hour...</dd><BR>'

def mk_next_link(case_num, key, secs):
	next_secs = int(float(secs)) + 10800

	end_secs = admindb.query("SELECT end_secs from winter_cases WHERE case_num = '"+case_num+"' ").getresult()
	end_secs = int(float(end_secs[0][0]))

	if next_secs < (end_secs - 10800):
		print '<a href="hourly.py?secs='+str(next_secs)+'&key='+str(key)+'&case_num='+str(case_num)+'"><img src="/icons/next_hour.gif" BORDER="0" align="CENTER"></a>'
	else:
		print '<a href="results.py?key='+str(key)+'&case_num='+str(case_num)+'"><img src="/icons/view_results.gif" BORDER="0" align="CENTER"></a>'

def annote(now, now_tuple, col):
        table_str = time.strftime("t%Y", now_tuple)

        try:
                select = annotedb.query("SELECT "+col+" from "+table_str+" where ticks = '"+str(now)+"'").getresult() 
        except ValueError:
                print "Needs to be written yet" 
                select = [(" "),(" ")]

        if len(select) == 0:
                print "Needs to be written yet"
        else:
                print '<font size="6">'+select[0][0][0]+'</font>'+select[0][0][1:]      # Get the neat capital letter to start
        print '<BR>'


def Main():
	form = cgi.FormContent()
	try:
		case_num = form["case_num"][0]
		secs = float(form["secs"][0])
		key = form["key"][0]
        except:
		style.SendError("CGI Value parse error")

	style.header("Severe Forecasting Exercise","#0854a8")

	if been_here(key, secs):	# If true, then no question, nor updatedb
		print 'You have allready visited this hour'
	else:
		updatedb(key, secs)			# Update the last_time
		question.Main(case_num, secs, key, "hourly.py")	# See if we have a question for this time

	now = int(float(secs)) 
	now_tuple = time.localtime(secs) 

	functs.setup_table()
	functs.mk_sub_sec("Help Topics:")

        print '<TR bgcolor="white"><TD>&nbsp;</TD><TD valign="top">'
        functs.mk_help()
        print '</TD>'

        print '<TD bgcolor="white" align="center" valign="center">'
        functs.mk_top(now_tuple)
        print '</TD></TR>'

        functs.mk_sub_sec("Instructions:")

        print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        content()
        print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Messenges for this hour:")

        print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        annote(now, now_tuple, "events")
        print '<BR>&nbsp;</TD></TR>'
	

	functs.mk_sub_sec("Weather Data:")

        print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        functs.mk_data(time.gmtime(now))
        print '<BR>&nbsp;</TD></TR>'

	functs.mk_sub_sec("Analysis for this hour:")

        print '<TR bgcolor="white"><TD><BR></TD><TD colspan="2">'
        annote(now, now_tuple, "analysis")
        print '<BR>&nbsp;</TD></TR>'

        functs.mk_sub_sec("Navigation:")
        
        print '<TR><TD bgcolor="WHITE" colspan="3" align="center"><BR>'
#	mk_before_links(now, key)
        mk_next_link(case_num, key, secs)
	print '</TD></TR>'

        print '<TR bgcolor="WHITE" height="19"><TD>&nbsp;</TD><TD colspan="2">'
        style.std_bot()
        print '<BR>&nbsp;</TD></TR></TABLE>'

        print '</BODY></HTML>'



Main()
