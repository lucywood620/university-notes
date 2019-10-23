var adjective=["big","beautiful","obnoxious"];
var noun=["cat","dog","goat","hedgehog"];
var verb=["speaks","shuts","sits","sends"];
var adverb=["abnormally","famously","frightfully"];

function givepoetry() {
	return adjective[Math.floor(Math.random() * adjective.length)]+ " " +
		noun[Math.floor(Math.random() * noun.length)]+ " " +
		verb[Math.floor(Math.random() * verb.length)]+ " " +
		adverb[Math.floor(Math.random() * adverb.length)];

}

function putpoetry(){
	document.getElementById("poetry").innerHTML = givepoetry();
}


function givepoetry2() {
	var adjective2=document.getElementById("adjective").value.split(" ");
	var noun2=document.getElementById("noun").value.split(" ");
	var verb2=document.getElementById("verb").value.split(" ");
	var adverb2=document.getElementById("adverb").value.split(" ");
	return adjective2[Math.floor(Math.random() * adjective2.length)]+ " " +
		noun2[Math.floor(Math.random() * noun2.length)]+ " " +
		verb2[Math.floor(Math.random() * verb2.length)]+ " " +
		adverb2[Math.floor(Math.random() * adverb2.length)];
}

function putpoetry2(){
	document.getElementById("poetry").innerHTML = givepoetry2();
}
