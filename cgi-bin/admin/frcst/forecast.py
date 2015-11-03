#!/usr/local/bin/python
# Simple script to generate a forecast for students that need to enter one yet
# Whoo-hooo, this is going to work
# Daryl Herzmann 8-30-99

import pg, time, style, os, cgi, mk_forecast

def Main():
	form = cgi.FormContent()
	class_name = form['class'][0]

	if valid_time():
		style.header("Forecasting excercise", "white")
		mk_forecast.Main(class_name)
	else:
		style.SendError("You can not forecast at this time, sorry..")


	style.std_bot()

Main()

