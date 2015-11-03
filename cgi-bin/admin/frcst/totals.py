#!/usr/local/bin/python
# This program will update the totals database
# Daryl Herzmann 9-4-99

import pg, time

mydb = pg.connect('frcst')


def Main(class_name):
		# First get rid of all values in the totals table
	delete = mydb.query("delete from totals WHERE userid ~* '"+class_name+"' ")

		# Figure out each case that we need to total up for
	cases = mydb.query("select * from cases WHERE class_name = '"+class_name+"' ").getresult()

		# Find all the students for this class
	students = mydb.query("SELECT userid from users WHERE userid ~* '"+class_name+"' ").getresult()

		# Also include mos in the forecast results
	ne = (class_name+"_mos", )
	students.append(ne)

	for student in students:
		student = str(student[0])
		dmx_high_tot = 0
		dmx_low_tot = 0
		dmx_prec_tot = 0
		dmx_snow_tot = 0
		dmx_err_tot = 0
		float_high_tot = 0
		float_low_tot = 0
		float_prec_tot = 0
		float_snow_tot = 0
		float_err_tot = 0
		tot_tot = 0
		for case in cases:
			try:
				yeer = str(case[0])
				month = str(case[1])
				day = str(case[2])
				results = mydb.query("SELECT * from grades WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid = '"+student+"' ").getresult()
				dmx_high_tot =  int(dmx_high_tot + float(results[0][4]))
				dmx_low_tot = 	int(dmx_low_tot + float(results[0][5]))
				dmx_prec_tot = 	int(dmx_prec_tot + float(results[0][6]))
				dmx_snow_tot = 	int(dmx_snow_tot + float(results[0][7]))
				dmx_err_tot = int(dmx_err_tot + float(results[0][8]))
				float_high_tot =int(float_high_tot + float(results[0][9]))
				float_low_tot = int(float_low_tot + float(results[0][10]))
				float_prec_tot =int(float_prec_tot + float(results[0][11]))
				float_snow_tot =int(float_snow_tot + float(results[0][12]))
				float_err_tot =  int(float_err_tot + float(results[0][13]))
				tot_tot = 	int(tot_tot + float(results[0][14]))
			except:
				print yeer, month, day

		if student == "mos":
			student = class_name+"_mos"
#		print dmx_high_tot, dmx_low_tot, dmx_prec_tot , dmx_snow_tot, float_high_tot, float_low_tot, float_prec_tot, float_snow_tot, tot_tot	
		insert = mydb.query("INSERT into totals VALUES ('"+student+"', "+str(dmx_high_tot)+" , "+str(dmx_low_tot)+" ,"+str(dmx_prec_tot)+" ,"+str(dmx_snow_tot)+" ,"+str(dmx_err_tot)+","+str(float_high_tot)+" ,"+str(float_low_tot)+" ,"+str(float_prec_tot)+" ,"+str(float_snow_tot)+","+str(float_err_tot)+" ,"+str(tot_tot)+" ) ")


#Main("mt311")


