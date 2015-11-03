#!/usr/local/bin/python
# This program grades the kiddies and changes the db
# Daryl Herzmann 8-30-99

import cgi, pg, math

mydb = pg.connect('frcst')

def grade_temp(ans, guess):
	return int(float( math.fabs(ans - guess) )) 

def grade_prec( ans, guess):
#	print ans, guess
	if ans == 9 and (guess == 0 or guess == 1):
		return int(0)

	if ans == guess:
		return int(0)
	if ans == 9:
		ans = 1

	return int(float( 4 * math.fabs( ans - guess) )) 


def Main(yeer, month, day, class_name):
	print '<PRE>'
				# First we determine the class_name for this excercise
#	entry = mydb.query("SELECT class_name from cases WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' ").getresult()  
#	class_name = str(entry[0][0])
				# Then I make a list of all users in this class
	students = mydb.query("SELECT userid from users WHERE userid ~* '"+class_name+"' ").getresult()

				# Get the answers out of the database
	answers = mydb.query("SELECT * from answers WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ").getresult()
	dmx_high = answers[0][3]
	dmx_low = answers[0][4]
	dmx_prec = answers[0][5]
	dmx_snow = answers[0][6]
	floater_high = answers[0][7]
	floater_low = answers[0][8]
	floater_prec = answers[0][9]
	floater_snow = answers[0][10]
				# Get the climodat out for those that did not forecast
	answers = mydb.query("SELECT * from climo WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and class_name = '"+class_name+"' ").getresult()
	climo_dmx_high = answers[0][3]
	climo_dmx_low = answers[0][4]
	climo_dmx_prec = answers[0][5]
	climo_dmx_snow = answers[0][6]
	climo_floater_high = answers[0][7]
	climo_floater_low = answers[0][8]
	climo_floater_prec = answers[0][9]
	climo_floater_snow = answers[0][10]

	mos = (class_name+'_mos',)
	students.append(mos)

	for j in range(len(students)):		# Itterate for each student
		this_student = students[j][0]
		graders = mydb.query("SELECT * from forecasts  WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid = '"+this_student+"' ").getresult()
		try:
			udmx_high = graders[0][4]
		        udmx_low = graders[0][5]
	        	udmx_prec = graders[0][6]
	        	udmx_snow = graders[0][7]
	        	ufloater_high = graders[0][8]
	        	ufloater_low = graders[0][9]
	        	ufloater_prec = graders[0][10]
	        	ufloater_snow = graders[0][11]
		except:
			print this_student +' did not have there forecast done, using climodat for their forecast.<BR>'
			insert = mydb.query("INSERT into forecasts VALUES ('"+this_student+"', '"+yeer+"', '"+month+"', '"+day+"', '"+climo_dmx_high+"', '"+climo_dmx_low+"', '"+climo_dmx_prec+"', '"+climo_dmx_snow+"', '"+climo_floater_high+"', '"+climo_floater_low+"', '"+climo_floater_prec+"', '"+climo_floater_snow+"') ")
			udmx_high = climo_dmx_high
			udmx_low = climo_dmx_low
		        udmx_prec = climo_dmx_prec
			udmx_snow = climo_dmx_snow
			ufloater_high = climo_floater_high
			ufloater_low = climo_floater_low
			ufloater_prec = climo_floater_prec
			ufloater_snow = climo_floater_snow
		

		dmx_high_err = grade_temp( int(dmx_high), int(udmx_high) )
		dmx_low_err = grade_temp( int(dmx_low), int(udmx_low) )
		floater_high_err = grade_temp( int(floater_high), int(ufloater_high) )
		floater_low_err = grade_temp( int(floater_low), int(ufloater_low) )

		dmx_prec_err = grade_prec( int(dmx_prec), int(udmx_prec) )
		dmx_snow_err = grade_prec( int(dmx_snow), int(udmx_snow) )
		floater_prec_err = grade_prec( int(floater_prec), int(ufloater_prec) )
		floater_snow_err = grade_prec( int(floater_snow), int(ufloater_snow) )

		dmx_err = dmx_high_err + dmx_low_err + dmx_prec_err + dmx_snow_err
		floater_err = floater_high_err + floater_low_err + floater_prec_err + floater_snow_err
		tot_err = dmx_high_err + dmx_low_err + floater_high_err + floater_low_err + dmx_prec_err + dmx_snow_err + floater_prec_err + floater_snow_err 

		delete = mydb.query("DELETE from grades WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' and userid = '"+this_student+"' ")
#		insert = mydb.query("INSERT into grades values ('"+this_student+"', '"+yeer+"', '"+month+"', '"+day+"', '"+dmx_high_err+"', '"+dmx_low_err+"', '"+dmx_prec_err+"', '"+dmx_snow_err+"', '"+floater_high_err+"', '"+floater_low_err+"' ,'"+floater_prec_err+"','"+floater_snow_err+"', '"+str(tot_err)+"' ) ")
		insert = mydb.query("INSERT into grades values ('"+this_student+"', '"+yeer+"', '"+month+"', '"+day+"' ,  "+str(dmx_high_err)+" , "+str(dmx_low_err)+" , "+str(dmx_prec_err)+" , "+str(dmx_snow_err)+" , "+str(dmx_err)+" , "+str(floater_high_err)+" , "+str(floater_low_err)+" , "+str(floater_prec_err)+" , "+str(floater_snow_err)+", "+str(floater_err)+"  , "+str(tot_err)+" ) ")
		print "Graded "+this_student+"'s forecast successfully...<BR>"

#		print dmx_high_err+ dmx_low_err+ floater_high_err+ floater_low_err +dmx_prec_err+dmx_snow_err+floater_prec_err+ floater_snow_err

	print '<BR><BR><a href="/cgi-bin/frcst/last.py?class_name='+class_name+'">Click me for grades</a> [Working]' 
	print '<BR><BR><a href="/cgi-bin/frcst/totals.py?class_name='+class_name+'">Click me for Cumulative Results</a> [Working]' 

	print '<BR><BR><H3>Done grading</H3>'

# Main('1999','12','1', 'mt311')
