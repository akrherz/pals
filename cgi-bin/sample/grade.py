#!/usr/local/bin/python
# Basic Script that will eventually evolve into a grader of archived forecasts
# Daryl Herzmann 7/13/98

from cgi import *
import style

def checker():
	form = FormContent() 
	if not form.has_key("1.1.1"): style.SendError("Need to have a city Entered")
	if not form.has_key("2.1.1"): style.SendError("Enter a Temperature in #2")
	if not form.has_key("3.1"): style.SendError("Clouds or No clouds in #3")
	if not form.has_key("4.1"): style.SendError("Advection during the day?? in #4") 
	if not form.has_key("5.1"): style.SendError("Any fronts?? in #5")
	if not form.has_key("6.1"): style.SendError("Nighttime Temp?? in #6")
	if not form.has_key("7.1"): style.SendError("Advection during the day?? in #7")
	if not form.has_key("8.1"): style.SendError("Any fronts?? in #8")
	if not form.has_key("9.1"): style.SendError("Advection during the day?? in #9")	
	if not form.has_key("10.1"): style.SendError("Any precip?? in #10")	
	if not form.has_key("12.1"): style.SendError("Wind speed?? in #12")

def get_score():
	score = int(0)
	form = FormContent()
	hi_temp = int(form["2.1.1"][0])
	day_cloud = form["3.1"][0]
	day_advect = form["4.1"][0]
	day_fronts = form["5.1"][0]
	night_temp = int(form["6.1"][0])
	night_advect = form["7.1"][0]
	night_fronts = form["8.1"][0]
	night_clouds = form["9.1"][0]
	precip = form["10.1"][0]
	wind_sped = int(form["12.1"][0])
	wind_dir = form["13.1"][0]	
	if hi_temp >= 77:
		if hi_temp <= 87: score = (score)+1
	if day_cloud == "1": score = (score)+1
	if day_advect == "3": score = (score)+1
	if day_fronts == "5": score = (score)+1
	if night_temp >= 65:
		if night_temp <= 75: score = (score)+1
	if night_advect == "3": score = (score)+1
	if night_fronts == "3": score = (score)+1
	if night_clouds == "1": score = (score)+1
	if precip == "1": score = (score)+1
	if wind_sped >= 0: 
                if wind_sped <= 11: score = (score)+1 
	if form.has_key("11.1"): score = (score)+1
	if form.has_key("11.1.2"): score = (score)+1
	if form.has_key("11.1.3"): score = (score)+1
	if wind_dir == "NE": score = (score)+1
	if wind_dir == "N": score = (score)+1
	if wind_dir == "E": score = (score)+1

	return score

def body(score):
	print '<center><H3>You got<strong> ',score,'</strong> out of 14</H3></center>'
	print '<a href="javascript:history.go(-1)">go back and try again</A><BR>'
	print '<a href="/mteor/sample/answers.html">View the Answers</a>'


def Main():
	checker()
	style.header("Your Score","/images/ISU_bkgrnd.gif")
	style.std_top("Your Sample Forecast Score")
	score = get_score()
	body(score)	
	style.std_bot()

Main()
