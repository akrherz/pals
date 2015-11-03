#!/usr/local/bin/python
# This is my frontpage for the forecasting exercise
# Daryl Herzmann 9-23-99

import pg, style

mydb = pg.connect('svr_frcst')

def Main():
	style.header("Severe Weather Forecasting Exercise", "white")
	style.std_top("Severe Weather Forecasting Exercise")

	print '<H3>Information:</H3>'

Main()
