#!/usr/local/bin/python
# Add the answer into the database system
# Daryl Herzmann 8-30-99
# UPDATED 10-19-99: Added a safe-guard in entering validation for days that where not forecasted for...

import cgi, pg, style, grader, time, totals, sys

mydb = pg.connect('frcst')

def test_day(yeer, month, day, class_name):
	select = mydb.query("SELECT * from cases WHERE day = '"+day+"' and month = '"+month+"' and yeer = '"+yeer+"' and class_name = '"+class_name+"' ").getresult()
	if len(select) == 0:
		print 'Bzzzzzzzzz, You entered an incorrect forecasting day. Go back and check date'
		sys.exit()	



def Main():
	print 'Content-type: text/html \n\n'

	form = cgi.FormContent()
	try:
                class_name = str(form["class_name"][0])
                yeer = str(form["yeer"][0])
                month = str(form["month"][0])
                day = str(form["day"][0])
                DMX_high = str(form["DMX_high"][0])
                DMX_low = str(form["DMX_low"][0])
                DMX_prec = str(form["DMX_prec"][0])
                DMX_snow = str(form["DMX_snow"][0])
                FLOATER_high = str(form["FLOATER_high"][0])
                FLOATER_low = str(form["FLOATER_low"][0])
                FLOATER_prec = str(form["FLOATER_prec"][0])
                FLOATER_snow = str(form["FLOATER_snow"][0])
                climo_DMX_high = str(form["climo_DMX_high"][0])
                climo_DMX_low = str(form["climo_DMX_low"][0])
                climo_DMX_prec = str(form["climo_DMX_prec"][0])
                climo_DMX_snow = str(form["climo_DMX_snow"][0])
                climo_FLOATER_high = str(form["climo_FLOATER_high"][0])
                climo_FLOATER_low = str(form["climo_FLOATER_low"][0])
                climo_FLOATER_prec = str(form["climo_FLOATER_prec"][0])
                climo_FLOATER_snow = str(form["climo_FLOATER_snow"][0])
                FLOATER_prec_num = str(form["FLOATER_prec_num"][0])
                FLOATER_snow_num = str(form["FLOATER_snow_num"][0])
                DMX_prec_num = str(form["DMX_prec_num"][0])
                DMX_snow_num = str(form["DMX_snow_num"][0])
                climo_FLOATER_prec_num = str(form["climo_FLOATER_prec_num"][0])
                climo_FLOATER_snow_num = str(form["climo_FLOATER_snow_num"][0])
                climo_DMX_prec_num = str(form["climo_DMX_prec_num"][0])
                climo_DMX_snow_num = str(form["climo_DMX_snow_num"][0])
                MOS_DMX_high = str(form["MOS_DMX_high"][0])
                MOS_DMX_low = str(form["MOS_DMX_low"][0])
                MOS_DMX_prec = str(form["MOS_DMX_prec"][0])
                MOS_DMX_snow = str(form["MOS_DMX_snow"][0])
                MOS_FLOATER_high = str(form["MOS_FLOATER_high"][0])
                MOS_FLOATER_low = str(form["MOS_FLOATER_low"][0])
                MOS_FLOATER_prec = str(form["MOS_FLOATER_prec"][0])
                MOS_FLOATER_snow = str(form["MOS_FLOATER_snow"][0])
		
        except:
                style.SendError("CGI Parse Error, please go back.")
	
	test_day(yeer, month, day, class_name)

	delete = mydb.query("DELETE from answers WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ")
	delete = mydb.query("DELETE from climo WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ")
	delete = mydb.query("DELETE from forecasts WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid = '"+class_name+"_mos' ")

        insert = mydb.query("INSERT into answers VALUES ('"+yeer+"','"+month+"','"+day+"','"+DMX_high+"','"+DMX_low+"','"+DMX_prec+"','"+DMX_snow+"','"+FLOATER_high+"','"+FLOATER_low+"','"+FLOATER_prec+"','"+FLOATER_snow+"', '"+DMX_prec_num+"', '"+DMX_snow_num+"', '"+FLOATER_prec_num+"','"+FLOATER_snow_num+"','"+class_name+"')")
        insert = mydb.query("INSERT into climo VALUES ('"+yeer+"','"+month+"','"+day+"','"+climo_DMX_high+"','"+climo_DMX_low+"','"+climo_DMX_prec+"','"+climo_DMX_snow+"','"+climo_FLOATER_high+"','"+climo_FLOATER_low+"','"+climo_FLOATER_prec+"','"+climo_FLOATER_snow+"','"+climo_DMX_prec_num+"', '"+climo_DMX_snow_num+"', '"+climo_FLOATER_prec_num+"','"+climo_FLOATER_snow_num+"','"+class_name+"' )")
        insert = mydb.query("INSERT into forecasts VALUES ('"+class_name+"_mos', '"+yeer+"','"+month+"','"+day+"','"+MOS_DMX_high+"','"+MOS_DMX_low+"','"+MOS_DMX_prec+"','"+MOS_DMX_snow+"','"+MOS_FLOATER_high+"','"+MOS_FLOATER_low+"','"+MOS_FLOATER_prec+"','"+MOS_FLOATER_snow+"')")

	print '<HTML><HEAD>'
#        print '<meta http-equiv="Refresh" content="1; URL=answers.py?class_name='+class_name+'">'
        print '</HEAD>'
        print '<body>'
        print '<H2> Update successful </H2>'

	grader.Main(str(yeer), str(month), str(day), class_name )
	print '<BR><BR>Totalling points for '+class_name+'<BR>'
	totals.Main(class_name)
	print 'Done for '+class_name+'<BR>'

Main()
