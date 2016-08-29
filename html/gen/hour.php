<?php
 $label = $_GET["label"];
 $font_size = $_GET["font_size"];
	$Font = '/home/www/pals/html/gen/fonts/handgotn.TTF';
	if (!$font_size) {
		$font_size = 15; }


	$size = imagettfbbox($font_size, 0, $Font, $label);
	$dx = abs($size[2] - $size[0]);
	$dy = abs($size[5] - $size[3]);
	$x_pad = 30 ;
	$y_pad = 10 ;
	$width = $dx + $x_pad;
	$height = $dy + $y_pad;

	$gif = ImageCreate($width + 10,$height );

	$white = ImageColorAllocate($gif,250,250,250);
	$black = ImageColorAllocate($gif,0,0,0);
	$red = ImageColorAllocate($gif, 250, 0, 0);
	$grey = ImageColorAllocate($gif, 110, 110, 110);

	ImageColorTransparent($gif, $white);	

	$xborder = (int) ($x_pad/2) -5;	

# Top Line
	ImageLine($gif, 0, (int) $height*0, $width - $xborder, (int) $height*0, $red);

# Left hand side lines
	ImageLine($gif, $xborder - (int)$xborder*2/3, (int) $height*1/3, $xborder, (int) $height*1/3, $red);
	ImageLine($gif, $xborder - (int)$xborder*1/3, (int) $height*2/3, $xborder, (int) $height*2/3, $red);

# Right hand side lines
	ImageLine($gif, $dx + $xborder + 10, (int) $height*1/3, $width - (int)$xborder*2/3, (int) $height*1/3, $red);
	ImageLine($gif, $dx + $xborder + 10, (int) $height*2/3, $width - (int)$xborder*1/3, (int) $height*2/3, $red);

# Bottom Line
	ImageLine($gif, $xborder, (int) $height-1, $width, (int) $height-1, $red);


	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2)+1, $dy + (int) ($y_pad/2), $grey, $Font, $label);
	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2) , $dy + (int) ($y_pad/2)-1, $black, $Font, $label);

	header("content-type: image/png");
	ImagePng($gif);
	ImageDestroy($gif);
?>
