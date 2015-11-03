#!/usr/local/bin/python
# This will make the total results for Catherine to print out
# Daryl Herzmann 9-1-99
# 9-6-99: Clean up code, document, clean up appearance

import pg, cgi, style, time
mydb = pg.connect('frcst')

def mysort(list, field):
	res = []
	for x in list:
		i = 0
		for y in res:
			if int(x[field]) <= int(y[field]):
				break
			i = i+1
		res[i:i] = [x]	

	return res

def Main(table_name, sort, class_name, refer, yeer, month, day, floater):
	if table_name == "grades":
	        entries = mydb.query("SELECT userid, dmx_high, dmx_low, dmx_prec, dmx_snow, dmx_err, floater_high, floater_low, floater_prec, floater_snow, floater_err, total_err from grades WHERE yeer = '"+yeer+"' and month = '"+month+"' and day = '"+day+"' ").getresult()
	if table_name == "totals":
		entries = mydb.query("SELECT * from totals WHERE userid ~* '"+class_name+"'").getresult()
	
	now = time.time()
	now_tuple = time.localtime(now)
	nice_date = time.strftime("%B %d, %Y -- %I:%M %p", now_tuple)

	new_entries = []
	if class_name == 'mt411' and table_name == 'totals':
		for i in range(len(entries)):
			stuid = entries[i][0]
			tmp_entries = entries[i]
			p1_tot = mydb.query("SELECT total_err from totals_p1 WHERE userid = '"+stuid+"' ").getresult()
			tmp_entries = tmp_entries + (str(p1_tot[0][0]),) + (str(int(p1_tot[0][0]) + int(tmp_entries[11])),)
			new_entries.append(tmp_entries)
	else:
		new_entries = entries		


	new_entries = mysort(new_entries, sort)
	print '<TABLE>'
	print '<TR>'
	print '<TH rowspan="2">USERID:</TH><TH colspan="5">Des Moines</TH><TD></TD><TH colspan="5">'+floater+'</TH><TD></TD>'
	print '<TH rowspan="2"><a href="'+refer+'?class_name='+class_name+'&sort=11">Totals:</a></TH>'
	if class_name == 'mt411' and table_name == 'totals':
		print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=12">1rst</a></TH>'
		print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=13">Cum Tot</a></TH>'
	print '</TR>'

	print '<TR>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=1">High:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=2">Low:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=3">Prec:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=4">Snow:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=5">Tot:</a></TH>'
	print '<TH></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=6">High:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=7">Low:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=8">Prec:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=9">Snow:</a></TH>'
	print '<TH><a href="'+refer+'?class_name='+class_name+'&sort=10">Tot:</a></TH>'
	if class_name == 'mt411' and table_name == 'totals':
		print '<TH colspan="2"></TH>'
	print '</TR>'

	spacer = " "
	
	
        for i in range(len(new_entries)):
		if (i % 2) == 0:
			print '\n\n<TR bgcolor="#EEEEEE"><TD>'
		else:
			print '\n\n<TR><TD>'
                this_entry = new_entries[i]
                stuid =  this_entry[0]
		lookup = mydb.query("SELECT name from users WHERE userid = '"+stuid+"' ").getresult()
		try:
			realname = lookup[0][0]
		except:
			realname = this_entry[0]

		print realname+"</TD>"

                for j in range(len(this_entry)):
			thi = this_entry[j]
			entry = str(thi)
                        if entry[0] == "m":
                                doy = "nothing"
                        else:
				if j == 6 or j == 11:
					print '<TD bgcolor="black"><BR></TD>'
                                print '<TD align="center">'
				if j == 5 or j == 10:
					print '<font color="blue">'
				if j == 11:
					print '<font color="red">'
				print entry+'</TD>', 
				
#		if class_name == 'mt411' and table_name == 'totals':
	#		p1_tot = mydb.query("SELECT total_err from totals_p1 WHERE userid = '"+stuid+"' ").getresult()
		#	tot_tot = int(p1_tot[0][0]) + int(thi)
			#print '<TH>'+str(tot_tot)+'</TH>'

                print '</TR>'
	print '</TABLE>'

	print '<P>This table was generated at: '+nice_date
	print '<BR><BR><P>Click on a column heading to sort on that value'

	print '<BR><BR><a href="/frcst/index.html">Forecasting Frontpage</a>'
