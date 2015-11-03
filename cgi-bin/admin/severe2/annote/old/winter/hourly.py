#!/usr/local/bin/python
# Daryl Herzmann 8-20-99

import sys, style, os, posix, time, pg, std_form

admindb = pg.connect("archadmin")

def load_days():
	print '<H3>Which case do you want to edit annotations for?</H3>'

        cases = admindb.query("SELECT * from winter_cases ").getresult()
        cases.sort()

        print '<select name="case_num">'
        for i in range(len(cases)):
                case_num = cases[i][0]
                start_secs = float(cases[i][1])
                end_secs = float(cases[i][2])

                start_tuple = time.localtime(start_secs)
                end_tuple = time.localtime(end_secs)

                nice_start = time.strftime("%b %d, %Y ", start_tuple)
                nice_end = time.strftime("%b %d, %Y ", end_tuple)

                print '<option value="'+str(case_num)+'">'+nice_start+' - '+nice_end

        print '</select>'

		


def Main():
	style.header("Edit Hourly Reports","white")
	style.std_top("Edit Hourly Reports")

	print '<B>Information:</B> <dd>This is the date and time selection page for the Severe Forecasting Excercise.</dd><BR>'
	print '<B>Instruction:</B> <dd>Select the desired day and time and then click on "submit."</dd><BR>'
	print '<B>Scope of this program:</B> <dd>This edits the annotations for case days.</dd><BR>'
	print '<HR>'

	print '<form method="post" action="list.py">'

	print '<form method="POST" action="list_case.py">'
	load_days()
	print '<input type="submit" value="submit">'
	print '</form>'
	
	style.std_bot()
Main()
