<?
	if (!isset($label)) {
		$label = "Hello";
	}

#	$gif = ImageCreate(125,30);
	$gif = ImageCreateFromGif("/home/www/pals/html/campbell/src/iowa.gif");

#	$bg = ImageColorTransparent($gif,1); 

	$white = ImageColorAllocate($gif,250,250,250);
	$black = ImageColorAllocate($gif,0,0,0);
	$green = ImageColorAllocate($gif, 0, 255, 0);
	
	ImageFilledRectangle($gif,0,0,125,30,$green);
	ImageFilledRectangle($gif,2,2,123,28,$white);
	
#	ImageArc($gif, 100, 100, 100, 50, 145, 90, $black);
	ImageTTFText($gif, 20, 0, 10, 20, $black, "/usr/X11R6/lib/X11/fonts/winttf/handgotn.TTF", "Weather");
	
	
#	ImageString($gif, 5, 70, 5,$label,$black);
#	ImageString($gif, 5, 71, 6,$label,$white);

#	header("content-type: image/gif");
	ImageGif($gif);
?>
