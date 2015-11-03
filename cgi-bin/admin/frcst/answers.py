#!/usr/local/bin/python
# This program simply asks someone for values  (answer key)
# Daryl Herzmann 8-30-99

import os, style, std_form, cgi

def mk_prec(sec_head):
        print '<TD><SELECT name="'+sec_head+'">'
        print '<option value="0">0'
        print '<option value="9">Trace'
        print '<option value="1">Trace - 0.05'
        print '<option value="2">0.06 - 0.25'
        print '<option value="3">0.26 - 0.50'
        print '<option value="4">0.51 - 1.00'
        print '<option value="5">1.01 +'
        print '</SELECT></TD>'

def mk_snow(sec_head):
        print '<TD><SELECT name="'+sec_head+'">'
        print '<option value="0">0'
        print '<option value="9">Trace'
        print '<option value="1">Trace - 2"'
        print '<option value="2">2.01" - 4"'
        print '<option value="3">4.01" - 8"'
        print '<option value="4">8.01" +'
        print '</SELECT></TD>'


def Main():
	form = cgi.FormContent()
	class_name = form["class_name"][0]

	style.header("Make answer key", "white")
	style.std_top("Answer key for "+class_name)

	print '<H3 align="center">Select and enter values</H3>'

	print '<form method="POST" action="enter_answer.py">'
	print '<input type="hidden" name="class_name" value="'+class_name+'">'

	print '<TABLE>'
        print '<TR><TH>Select Year:</TH><TH>Select Month:</TH><TH>Select Day:</TH></TR>'

        print '<TR><TD><SELECT name="yeer">'
        print '<option value="1999">1999'
        print '</SELECT></TD>'

        print '<TD>'
        std_form.months()
        print '</TD>'

        print '<TD>'
        std_form.days()
        print '</TD></TR></TABLE>'

	print '<CENTER>'
        print '<TABLE WIDTH="100%">'
	print '<TR><TH></TH><TH>High Temp:</TH><TH>Low Temp:</TH><TH>Precipation:</TH><TH>Actual Rainfall:</TH><TH>Snowfall:</TH><TH>Actual Snowfall:</TH></TR>'

        print '<TR><TD>Des Moines:</TD>'
        print '<TD><input type="text" size="3" name="DMX_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="DMX_low" MAXLENGTH="3"></TD>'
	mk_prec("DMX_prec")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="DMX_prec_num"></TD>'
	mk_snow("DMX_snow")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="DMX_snow_num"></TD></TR>'


        print '<TR><TD>Des Moines Climo:</TD>'
        print '<TD><input type="text" size="3" name="climo_DMX_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="climo_DMX_low" MAXLENGTH="3"></TD>'
        mk_prec("climo_DMX_prec")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="climo_DMX_prec_num"></TD>'
	mk_snow("climo_DMX_snow")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="climo_DMX_snow_num"></TD></TR>'


        print '<TR><TD>Floater:</TD>'
        print '<TD><input type="text" size="3" name="FLOATER_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="FLOATER_low" MAXLENGTH="3"></TD>'
	mk_prec("FLOATER_prec")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="FLOATER_prec_num"></TD>'
	mk_snow("FLOATER_snow")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="FLOATER_snow_num"></TD></TR>'

        print '<TR><TD>Floater Climo:</TD>'
        print '<TD><input type="text" size="3" name="climo_FLOATER_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="climo_FLOATER_low" MAXLENGTH="3"></TD>'
        mk_prec("climo_FLOATER_prec")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="climo_FLOATER_prec_num"></TD>'
	mk_snow("climo_FLOATER_snow")
	print '<TD><input type="text" SIZE="5" MAXLENGTH="5" name="climo_FLOATER_snow_num"></TD></TR>'

        print '<TR><TD>MOS DMX forecast:</TD>'
        print '<TD><input type="text" size="3" name="MOS_DMX_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="MOS_DMX_low" MAXLENGTH="3"></TD>'
        mk_prec("MOS_DMX_prec")
	print '<TD></TD>'
	mk_snow("MOS_DMX_snow")
	print '<TD></TD></TR>'

        print '<TR><TD>MOS FLOATER forecast:</TD>'
        print '<TD><input type="text" size="3" name="MOS_FLOATER_high" MAXLENGTH="3"></TD>'
        print '<TD><input type="text" size="3" name="MOS_FLOATER_low" MAXLENGTH="3"></TD>'
        mk_prec("MOS_FLOATER_prec")
	print '<TD></TD>'
	mk_snow("MOS_FLOATER_snow")
	print '<TD></TD></TR></TABLE>'

        print '<input type="submit" value="submit answers">'

        print '</form>'


Main()
