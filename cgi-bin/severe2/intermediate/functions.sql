/* CREATE FUNCTION abstime_datetime(int4)
	RETURNS datetime
	AS '-' LANGUAGE 'internal';

CREATE FUNCTION datetime(int4)
	RETURNS datetime
	AS 'select abstime_datetime($1)' LANGUAGE 'SQL';
*/

CREATE table users (
	userkey int,
	lasttime datetime,
	gradetime datetime,
	state varchar(40),
	etime int,
	optiona char(1),
	optionb char(1),
	optionc char(1),
	optiond char(1),
	bonuspoints int default 0,
	casenum varchar(5) default 'null'
	);

GRANT all on users to nobody;
	
CREATE table cases (
	starttime datetime,
	endtime datetime,
	casenum varchar(5)
	);

GRANT all on users to nobody;
	
CREATE table annotations (
	validtime datetime,
	comments text,
	analysis text,
	casenum varchar(5) default 'all'
	);

GRANT all on users to nobody;
