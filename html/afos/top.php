<html>
  <head>
    <title>NWS Text Data Query Tool</title>
  </head>
<body bgcolor="white">

<form method="GET" action="/cgi-bin/afos/retreive.py" target="display">

Enter AFOS PIL: <input type="text" name="pil" size=6 maxlength=6>

<SELECT name="limit">
	<option value="1">Latest
	<option value="2">Last 2
	<option value="5">Last 5
	<option value="10">Last 10
	<option value="99">All
</SELECT>

<input type="submit" value="GET">
</form>
