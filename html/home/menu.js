<script language="JavaScript">
<!--
bName = navigator.appName;  
bVer = parseInt(navigator.appVersion); 
if ((bName == "Netscape" && !(bVer < 3)) || (bName ==
"Microsoft Internet Explorer" && !(bVer < 4))) ver = "good";  
if (ver == "good") { 
trnav1on = new Image(161,26); 
trnav1on.src = "/images/doc_men_on.gif"; 
trnav1off = new Image(161,26); 
trnav1off.src = "/images/doc_men_off.gif"; 
trnav2on = new Image(161,26);
trnav2on.src = "/images/proj_men_on.gif"; 
trnav2off = new Image(161,26);  
trnav2off.src = "/images/proj_men_off.gif"; 
trnav3on = new Image(161,26);  
trnav3on.src = "/images/prop_men_on.gif"; 
trnav3off = new Image(161,6); 
trnav3off.src = "/images/prop_men_off.gif"; 
trnav4on = new Image(161,27); 
trnav4on.src = "/images/home_men_on.gif"; 
trnav4off = new Image(161,27);  
trnav4off.src = "/images/home_men_off.gif"; 
} 
function rollon(imgName)  { 
if (ver == "good") { 
imgOn = eval(imgName + "on.src"); 
document[imgName] .src = imgOn; 
} 
} 
function rolloff(imgName) { 
if (ver == "good") {
document[imgName] .src = eval(imgName + "off.src"); 
} 
} 
// --> 
</script>
