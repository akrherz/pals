<?
	$gif = ImageCreate(1,1);
	$black = ImageColorAllocate($gif,0,0,0);
	
	ImageFilledRectangle($gif,0,0,1,1, $black);
	
	header("content-type: image/gif");
	ImageGif($gif);
?>
