# This program holds the constants in my programs...
# Daryl Herzmann 5/6/99
# UPDATED 5/7/99: I think that it will work, should be fine, 100 degrees may be too much though..
# UPDATED 6/22/99: Changed the point for crawfordsville and set up a different locations var
# UPDATED 7/9/99: Added the Dictionary for Titles and Labels
# UPDATED 7/11/99: Gonna make this program modulized

import time, gd
from pg import *

mydb = connect('campbellDaily', 'localhost', 5555 )		# Where the Temp data is located
mydb2 = connect('campbellHourly', 'localhost', 5555 )		# Where the Temp data is located

now = time.time()				# Return now
now_tuple = time.localtime(now)			# Find out when today is
yest_tuple = time.localtime(now - 86400 )	# Find out when yesterday was

off = 17		# Offset on the chart
#suth_pt = [135,129]	# Sutherland
#char_pt = [273,333]	# Chariton
#ceda_pt = [358,264]	# Cedar Rapids
#ames_pt = [247,243]	# Ames
#gilm_pt = [201,187]	# Gilmore
#gilb_pt = [254,225]	# Gilbert
#nash_pt = [369,189]	# Nashua
#craw_pt = [360,313]	# Crawford
#lewi_pt = [165,299]	# Lewis
#cast_pt = [113,236]	# Castana
#kana_pt = [250,173]	# Kanaswa

suth_pt = [160,164]     # Sutherland
char_pt = [275,333]     # Chariton
ceda_pt = [387,249]     # Cedar Rapids
ames_pt = [246,243]     # Ames
nash_pt = [325,168]     # Nashua
craw_pt = [353,314]     # Crawford
lewi_pt = [165,299]     # Lewis
cast_pt = [113,236]     # Castana
kana_pt = [250,173]     # Kanaswa
rhod_pt = [293,253]     # Rhodes
musc_pt = [394,307]     # Muscatine



stations = ('a130209','a131299','a131329','a131559','a131909','a135879','a138019','a134759','a134309','a136949', 'a135849')
locations = [ames_pt, cast_pt, ceda_pt, char_pt, craw_pt, nash_pt, suth_pt, lewi_pt, kana_pt, rhod_pt, musc_pt]           # Points array



alt_craw_pt = [342,312]
alt_musc_pt = [382,304]
alt_locations = [ames_pt, cast_pt, ceda_pt, char_pt, alt_craw_pt, nash_pt, suth_pt, lewi_pt, kana_pt, rhod_pt, alt_musc_pt]

title = gd.gdFontGiant		# title type
label = gd.gdFontMediumBold	# label type


titles = {'c11, c12': "High and Low temperatures on " , \
	'c30': "4 inch Soil Temperatures on " , \
	'c40': "Average Wind Speed on " , \
	'c80' : "Total Solar Radiation values on ", \
	'c529, c530' : "5 Second Sustained Wind Gust on " , \
	'c70' : "Potiental Evapo-transpiration on " , \
	'c300' : "Max/Min 4 inch Soil Temperatures " , \
	'c90' : "24 Hour Precipitation Totals on " , \
	'c1' : "Max/Min Dew Points "}

labels = {'c11, c12': "[ F ]", \
	'c90' : "[ inches ]", \
	'c40' : "[ MPH ]", \
	'c529, c530' : "[ MPH @ Time ]" , \
	'c80' : "[ Langleys ]", \
	'c70' : "[ inches ]" , \
	'c300' : "[ F ]" , \
	'c30' : "[ F ]", \
	'c1' : "[F]"}

rounds = {'c11, c12' : 0 , \
	'c90' : 2 , \
	'c40' : 1 , \
	'c529, c530' : 0 , \
	'c80' : 0 , \
	'c70' : 2 , \
	'c300' : 0 , \
	'c30' : 0 ,\
	'c1': 0}
