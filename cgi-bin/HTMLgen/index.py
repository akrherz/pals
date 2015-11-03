#!/usr/local/bin/python
# This is testing of HTMLgen
# Daryl Herzmann 4-9-99


import HTMLgen

def Table_ex():
	table = HTMLgen.Table('Data for Creston', border="0")

	headers = ['City','Date','High','Low']
	table.heading = headers

	data_row = ['0200','January 1, 1999','98','34']
	data_row2 = ['0200','January 1, 1999','98','34']
	table.body = [data_row, data_row2]

	print table

def Main():
	print 'Content-type: text/html \n\n'
	print '<HTML>'

	table = HTMLgen.TableLite(border="0", width="600")
	caption = HTMLgen.Caption('Data for Corning, Iowa')
	body = []

	THlist = map(HTMLgen.TH, ['head 1', 'head 2', 'head 3'])
	heading = HTMLgen.TR()
	heading = heading + THlist

	TDlist = map(HTMLgen.TD, ['one', 'two', 'three'])
	r1 = HTMLgen.TR(align="center")
	r1 = r1 + TDlist

	TDlist2 = map(HTMLgen.TD, ['four', 'five', 'six'])
	r2 = HTMLgen.TR(align="center")
	r2 = r2 + TDlist2

	table.append(caption, heading, r1, r2)

	print table
Main()
