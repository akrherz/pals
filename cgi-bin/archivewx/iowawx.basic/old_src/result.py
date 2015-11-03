#!/usr/local/bin/python
# This will output the results from the search
# Daryl Herzmann 1/14/99
# UPDATED 3/4/99, Gonna make this beast work...
# UPDATED 3/11/99, Integrated the wx pics

from cgi import *
from pgext import *
import style

mydb = connect('iowawx')

def query_db(city, year, month, day):
	search = mydb.query("SELECT * from "+city+" WHERE yeer = '"+year+"' AND month = '"+month+"' AND day = '"+day+"'")
	search = search.getresult()

	print search
	print '<HR>'
	if len(search) == 0:			# If we do not get a result, send back std_err
		print '<B>This date does not exist in the database, please try again.</B>'	
		sys.exit()

	elif len(search[0]) == 7:						# This is the case in the eighties when
		return search[0][-3] , search[0][-2], search[0][-1], -99.0	# the climatological week was though in

	else:										# Normal cases
		return search[0][-4] , search[0][-3], search[0][-2], search[0][-1]

def sun(high, low):
	if (high - low) > 25:
		return "sunny"
	elif (high - low) > 15:
		return "p_sunny"
	elif (high - low) > 5:
		return "m_cloudy"
	else:
		return "cloudy"

def chk_data(high, low, rain, snow):
	if high == -99.0:
		high = "Missing Data"
	if low == -99.0:
		low = "Missing Data"
	if rain == -99.0:
		rain = "Missing Data"
	if snow == -99.0:
		snow = "Missing Data"

	return high, low, rain, snow 

def result_table(date, pict, high, low, rain, snow):
#	print '<TR><TH colspan="2"><img src="/images/'+pict+'.gif"></TH></TR>'
	print '<TR><TH>'+date+'<TD>'+high+'</TD><TD>'+low+'</TD><TD>'+rain+'</TD><TD>'+snow+'</TD></TR>'


def convert_month(month):
	month = month[-2:]
        file = '/home/httpd/html/src/months.con'
        f = open(file,'r').read()

	lines = re.split('\n',f)
        for i in range(len(lines)):
                line = lines[i]
		if month == line[-2:]:
                        name = line[:-3]
        return name

def convert_station(code):
	code = code[-4:]
        file = '/home/httpd/html/src/stations.con'
        f = open(file,'r').read()

	lines = re.split('\n',f)
        for i in range(len(lines)):
		line = lines[i]
		info = re.split(',',line)
		if code == info[0]:
			name = info[3]
        return name

def table_header():
	print '<TABLE WIDTH="600" BORDER="0" CELLSPACING="1" ROWSPACING="1">'
	print '<TR><TH>Date:</TH><TH>High Temp:</TH><TH>Low Temp:</TH><TH>Precip:</TH><TH>Snow:</TH></TR>'
	

def Main():
	form = FormContent()
	year = form["year"][0]
	month = form["month"][0]
	str_month = convert_month("0"+month)
	day = form["day"][0]
	city = form["city"][0]
	station = convert_station(city)
	style.header("IOWAWX Query results","white")
	style.std_top("Data for "+station+" on "+str_month+" "+day+" "+year+".")

	date = str_month+" "+day+", "+year

	high, low, rain, snow = query_db(city, year, month, day)
	sun_type = sun(int(high), int(low))
	high, low, rain, snow  = chk_data(high, low, rain, snow)


	table_header()

	result_table(date, sun_type, str(high), str(low), str(rain), str(snow))

	print '</TABLE>'

	print high, low, rain, snow, sun_type

Main()
