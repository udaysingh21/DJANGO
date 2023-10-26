// Grab the header and change its color

var myheader=document.querySelector("h1");
myheader.style.color = "red";

// Random Color Function
// heading must change its color to another random color every second

function getRandomColor(){
    var letters="0123456789ABCDEF";
    var color="#";

    for (var i=0;i<6;i++){
        console.log(Math.random(),Math.random()*16,Math.floor(Math.random()*16))
        color+=letters[Math.floor(Math.random()*16)]
    }

    return color
}

// Simple function for clarity
function changeHeaderColor(){
    colorInput=getRandomColor();
    myheader.style.color=colorInput;
}

// Now perform the action over intervals (milliseconds):
setInterval("changeHeaderColor()",100);