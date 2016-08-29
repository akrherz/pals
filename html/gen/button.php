<?
	$Font = './fonts/handgotn.TTF';
	if (!$font_size) {
		$font_size = 15; }


	$size = imagettfbbox($font_size, 0, $Font, $label);
	$dx = abs($size[2] - $size[0]);
	$dy = abs($size[5] - $size[3]);
	$x_pad = 30 ;
	$y_pad = 10 ;
	$width = $dx + $x_pad;
	$height = $dy + $y_pad;

	$gif = ImageCreate($width,$height );

	$white = ImageColorAllocate($gif,250,250,250);
#	$green = ImageColorAllocate($gif, 0, 250, 0);
	$black = ImageColorAllocate($gif,0,0,0);
	$blue = ImageColorAllocate($gif, 0, 0, 250);
	$red = ImageColorAllocate($gif, 250, 0, 0);
	$grey = ImageColorAllocate($gif, 110, 110, 110);

	ImageColorTransparent($gif, $white);	

#	ImageFilledRectangle($gif,2,2, $width, $height, $red);

	$xborder = (int) ($x_pad/2) - 5;	

# Top Line
	ImageLine($gif, 0, (int) $height*0, $width - $xborder, (int) $height*0, $red);

#	ImageLine($gif, $xborder - (int)$xborder*2/3, (int) $height*1/3, $width - (int)$xborder*2/3, (int) $height*1/3, $grey);
#	ImageLine($gif, $xborder - (int)$xborder*1/3, (int) $height*2/3, $width - (int)$xborder*1/3, (int) $height*2/3, $grey);

# Left hand side lines
	ImageLine($gif, $xborder - (int)$xborder*2/3, (int) $height*1/3, $xborder, (int) $height*1/3, $red);
	ImageLine($gif, $xborder - (int)$xborder*1/3, (int) $height*2/3, $xborder, (int) $height*2/3, $red);

# Right hand side lines
	ImageLine($gif, $dx + $xborder +10, (int) $height*1/3, $width - (int)$xborder*2/3, (int) $height*1/3, $red);
	ImageLine($gif, $dx + $xborder +10, (int) $height*2/3, $width - (int)$xborder*1/3, (int) $height*2/3, $red);

# Bottom Line
	ImageLine($gif, $xborder, (int) $height-1, $width, (int) $height-1, $red);

#	ImageFilledRectangle($gif, $size[0], $size[3], $size[2] , $size[5], $blue);


	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2)+1, $dy + (int) ($y_pad/2), $grey, "./fonts/handgotn.TTF", $label);
	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2) , $dy + (int) ($y_pad/2)-1, $black, "./fonts/handgotn.TTF", $label);

#	ImageArc($gif, $height /2, $x_pad, $x_pad *2, $height , 90, 270, $red);

	header("content-type: image/gif");
	ImageGif($gif);
	ImageDestroy($gif);
?>
