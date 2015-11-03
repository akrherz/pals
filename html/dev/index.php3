<HTML>
<HEAD>
	<TITLE>Partnerships to Advance Learning in Science</TITLE>
</HEAD>

<body bgcolor="WHITE">

<TABLE width="640">
<TR>
	<TD bgcolor="#EEEEEE">
	<img src="/images/pals_logo.gif">
	</TD>
</TR>

<TR>
	<TD bgcolor="WHITE">
	<?php
#	print (date("l h:i A"));
	print ( time() );

	$connection = pg_connect("","","","akrherz");
#	$connection = pg_connect("localhost", "5432", "akrherz");
	$query = "SELECT * from board";
	$result = pg_exec($connection, $query);
	print $result ;
	pg_close($connection);

	?>
	</TD>
</TR>
</TABLE>
