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
	$black = ImageColorAllocate($gif,0,0,0);
	$blue = ImageColorAllocate($gif, 0, 0, 250);
	$red = ImageColorAllocate($gif, 250, 0, 0);
	$grey = ImageColorAllocate($gif, 110, 110, 110);

	ImageColorTransparent($gif, $white);	

	$xborder = (int) ($x_pad/2) - 5;	

	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2)+1, $dy + (int) ($y_pad/2), $grey, "./fonts/handgotn.TTF", $label);
	ImageTTFText($gif, $font_size, 0, (int) ($x_pad/2) , $dy + (int) ($y_pad/2)-1, $black, "./fonts/handgotn.TTF", $label);

	header("content-type: image/gif");
	ImageGif($gif);
	ImageDestroy($gif);
?>
