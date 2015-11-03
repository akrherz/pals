#!/usr/local/bin/python
# This all the database calls that are needed in order to add a case...


import pg, os

admindb = pg.connect('svr_frcst')


def Main():
	className = "test"
	dbName = "svr_"+className
	Instructor = "Daryl Herzmann"
	EmailAdd = "akrherz@iastate.edu"

	os.system("createdb "+dbName)

	mydb = pg.connect(dbName)

	insert = admindb.query("INSERT into classes (class_abv, instructor, instructor_email) VALUES ('"+className+"', '"+Instructor+"', '"+EmailAdd+"')")

	create = mydb.query("CREATE TABLE annote (ztime varchar(20), comments varchar(4000), analysis varchar(4000))")

	create = mydb.query("CREATE TABLE spec_questions (ticks varchar(20), question varchar(500), type char(1), optiona varchar(200) DEFAULT 'N', optionb varchar(200) DEFAULT 'N', optionc varchar(200) DEFAULT 'N', optiond varchar(200) DEFAULT 'N', optione varchar(200) DEFAULT 'N', optionf varchar(200) DEFAULT 'N', optiong varchar(200) DEFAULT 'N', optionh varchar(200) DEFAULT 'N', answer char(1), topic varchar(20), cor_comments varchar(2000), wro_comments varchar(2000),link varchar(90) )")

	create = mydb.query("CREATE TABLE users (userid varchar(20), name varchar(100), email varchar(40), last_time varchar(40), etime char(1), state varchar(30), optiona char(1) DEFAULT 'N', optionb char(1) DEFAULT 'N',optionc char(1) DEFAULT 'N',optiond char(1) DEFAULT 'N', bonus_points varchar(3) default '0')")

	create = mydb.query("create table released_cases (case_num varchar(5)) ")

	print 'Hello, I am done!!'

Main()
