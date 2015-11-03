<?
	$width = 87;
	$height = 60;
	$Font = './fonts/handgotn.TTF';

	$gif = ImageCreate($width,$height);

	$black = ImageColorAllocate($gif,0,0,0);
	$white = ImageColorAllocate($gif,250,250,250);
	$green = ImageColorAllocate($gif, 0, 255, 0);
	$red = ImageColorAllocate($gif, 255, 0, 0);
	$grey = ImageColorAllocate($gif, 110, 110, 110);
	
	ImageFilledRectangle($gif,2,2, $width, $height, $grey);
	ImageFilledRectangle($gif,1,1, $width -2 , $height -2, $white);
	
	$size = imagettfbbox(15, 0, $Font, $month);
	$dx = abs($size[2] - $size[0]);
	$dy = abs($size[5] - $size[3]);
	$x_pad = ($width - $dx) / 2 ;
	ImageTTFText($gif, 15, 0, $x_pad , 15, $black, "./fonts/handgotn.TTF", $month);

	$size = imagettfbbox(20, 0, $Font, $day);
	$dx = abs($size[2] - $size[0]);
	$dy = abs($size[5] - $size[3]);
	$x_pad = ($width - $dx) / 2 ;
	ImageTTFText($gif, 20, 0, $x_pad , 35, $red, "./fonts/handgotn.TTF", $day);

	$size = imagettfbbox(15, 0, $Font, $yeer);
	$dx = abs($size[2] - $size[0]);
	$dy = abs($size[5] - $size[3]);
	$x_pad = ($width - $dx) / 2 ;
	ImageTTFText($gif, 15, 0, $x_pad , 55, $black, "./fonts/handgotn.TTF", $yeer);


	
	
#	ImageString($gif, 3, 5, 5, $month ,$black);
#	ImageString($gif, 3, 5, 20, $day ,$black);
#	ImageString($gif, 3, 5, 35, $yeer ,$black);

	header("content-type: image/gif");
	ImageGif($gif);
	ImageDestroy($gif);
?>
