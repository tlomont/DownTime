var startTime, nowTime, timer = 60;
var timeLeft = 60;
var reduceTimer;
var min, sec = 0;
var tagLine;

$(document).ready(function() { 
	setTimer();
	getNextUrl();
});

function next(){
	getNextUrl();
};

function setTimer(){
	timeLeft = window.location.hash.substr(1);;
	reduceTime();
}

function chooseTagline() {
	var rand = Math.floor(Math.random()*6);
	if(rand==0){
		tagLine = "Do you believe in diminishing returns? So do we. Get back to work.";
	} else if(rand==1){
		tagLine="Have you seen Gattaca? I recommend it. Get back to work.";
	} else if(rand==2){
		tagLine = "Let’s play a game. Pretend to be the very best you could be. Exemplary. Now, what would you be doing? Get back to work.";
	} else if(rand==3){
		tagLine = "Dain bramaged. Get back to work.";
	} else if(rand==4){
		tagLine = "Gooooo! Get out of here. Don’t you understand? Get! I don’t want you anymore. Get back to work.";
	} else if(rand==5){
		tagLine="OMG……liiike….Get back to work.";
	}
}

function reduceTime(){
	if(timeLeft<0){
		chooseTagline();
		document.getElementById("tagLine").innerHTML=tagLine;
		dimOn();
		//alert("hell naaaa");
		reduceTimer=null;
	}else{
		updateTime();
		reduceTimer = setTimeout(function(){reduceTime()}, 1000);
		timeLeft--;
	}
}

/* function getTimer(){
	nowTime = (Date.now()/1000);
	timer = (nowTime - startTime);
	return timer;
}

	function getTimeLeft(){
	timeElapsed = getTimer();
	timeLeft = timeStart - Math.floor(getTimer());
	return timeLeft;
}

function runTimer(){
	while(true){
		document.getElementById("timer").innerHTML=getTimeLeft();
	}
} 
*/

function getNextUrl(){
	$.get( "../backend/fetch_new_content.php", { user: localStorage.user, timeLeft: timeLeft } )
		.done(function( data ) {
				if (data.indexOf("youtube")>=0){
					//alert('hi');
					data=data.replace("watch?","embed/");
					//alert(data);
					

				}
				document.getElementById("mainframe").src=data;
  		});
}

function updateTime(){
 	min = Math.floor(timeLeft/60);
 	sec = timeLeft%60;
 	if(min < 10 && sec>=10){
		document.getElementById("timer").innerHTML= "0"+min+":"+sec;
	} else if(min<10 && sec<10){
		document.getElementById("timer").innerHTML= "0"+min+":0"+sec;
	} else if(min>=10 && sec<10){
		document.getElementById("timer").innerHTML= min+":0"+sec;
	} else if(min>=10 && sec>10){
		document.getElementById("timer").innerHTML= min+":"+sec;
	}
}


function oneMore(){
	timeLeft=60;
	dimOff();
	reduceTime();
}


function dimOff()
{
    document.getElementById("darkLayer").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
function dimOn()
{
    document.getElementById("darkLayer").style.display = "";
    document.getElementById("overlay").style.display = "";
}