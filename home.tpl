<html>
<head>

<!--This imports the jquery file hosted by bottle-->
<script type="text/javascript" src="static/jquery.js" charset="utf-8"></script>

<!--This sets up the control boxes, with size and color information -->
<style>
body{
    background-color:darkgray;
}
    
    /*Title style for your controls*/
    h1 {
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }

    /*styles for your three main button types*/
    .controls {
        width: 180px;
        padding: 10px;
        font-size: 18pt;
        text-align: center;
        background-color: darkgreen;
        color: white;
        margin: 0px;
        border: 5px groove green;
        float: left;
    }
    .controls2 {
	width: 180px;
	font-size: 18pt;
	text-align: center;
	padding: 10px;
	background-color: darkblue;
	color: white;
	float:left;
	margin:0px;
	border: 5px groove blue;
    }
    .controls3 {
	width: 180px;
	font-size: 18pt;
	text-align: center;
	padding: 10px;
	background-color: darkred;
	color: white;
	float: left;
	margin: 0px;
	border: 5px groove red;
    }

    /*style for your controls heading*/
    .controls4 {
        width: 650px;
        font-size: 18pt;
        text-align: center;
        padding: 10px;
        background-color: none;
        color: Black;
        float: left;
        margin: 0px;
        border: 5px hidden;
    }
    /*style for your small buttons*/
    .controls5 {
	width: 40px;
	font-size: 18pt;
	text-align: center;
	padding: 10px;
	background-color: darkgreen;
	color: white;
	float: left;
	margin: 0px;
	border: 5px groove green;
    }

    /*Sets the size of the control box*/    
    .leftcontrol{
	max-width:650px;
        margin-left: auto;
        margin-right: auto;
    }

     /*Sets the size of your main div*/  
    .main {
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

</style>

<script>
function sendCommand(command)
{
	$.get('/', {command: command});
}

function keyPress(event){
	code = event.keyCode;
	if (code == 119) {
		sendCommand('f');
	}
	else if (code == 97) {
		sendCommand('l');
	}
	else if (code == 115) {
		sendCommand('s');
	}
	else if (code == 100) {
		sendCommand('r');
	}
	else if (code == 122) {
		sendCommand('b');
	}
}

$(document).keypress(keyPress);

</script>
</head>
<body>



<div class="main">
<h1>Tank Controls {{name.title()}}!</h1>
    <div class="leftcontrol">
    <h4 class="controls4">Turret Controls</h4>
    <h4 class="controls5" onClick="sendCommand('TU3');">TU3</h4>
    <h4 class="controls5" onClick="sendCommand('TU2');">TU2</h4>
    <h4 class="controls5" onClick="sendCommand('TU1');">TU1</h4>
    <h4 class="controls" onClick="sendCommand('ST');">Stop up/down</h4>
    <h4 class="controls5" onClick="sendCommand('TD1');">TU1</h4>
    <h4 class="controls5" onClick="sendCommand('TD2');">TU2</h4>
    <h4 class="controls5" onClick="sendCommand('TD3');">TU3</h4>
    <h4 class="controls5" onClick="sendCommand('TL3');">TL3</h4>
    <h4 class="controls5" onClick="sendCommand('TL2');">TL2</h4>
    <h4 class="controls5" onClick="sendCommand('TL1');">TL1</h4>
    <h4 class="controls" onClick="sendCommand('CT');">Stop Turret</h4>
    <h4 class="controls5" onClick="sendCommand('TR1');">TR1</h4>
    <h4 class="controls5" onClick="sendCommand('TR2');">TR2</h4>
    <h4 class="controls5" onClick="sendCommand('TR3');">TR3</h4>
    <h4 class="controls2" onClick="sendCommand('sf');">Safe FWD</h4>
    <h4 class="controls2" onClick="sendCommand('f');">Tank Forward</h4>
    <h4 class="controls2" onClick="sendCommand('td');">Turret Dance</h4>
    <h4 class="controls2" onClick="sendCommand('l');">Tank Left</h4>
    <h4 class="controls2" onClick="sendCommand('s');">Tank Stop</h4>
    <h4 class="controls2" onClick="sendCommand('r');">Tank Right</h4>
    <h4 class="controls3" onClick="sendCommand('lo');">Lights On</h4>
    <h4 class="controls2" onClick="sendCommand('b');">Tank Reverse</h4>
    <h4 class="controls3" onClick="sendCommand('Lof');">Lights Off</h4>
</div>

    </div>
<!--<table align="center">
<tr><td></td><td class="controls" onClick="sendCommand('f');">W</td><td></td></tr>
<tr><td  class="controls" onClick="sendCommand('l');">A</td>
    <td  class="controls" onClick="sendCommand('s');">S</td>
    <td  class="controls" onClick="sendCommand('r');">D</td>
</tr>
<tr><td></td><td  class="controls" onClick="sendCommand('b');">Z</td><td></td></tr>
</table>-->


</body>
</html>
