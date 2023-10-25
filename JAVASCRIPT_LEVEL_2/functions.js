function helloyou(name){
console.log("Hello "+name);
}

function add(a,b){
    console.log(a+b);
}

function hellosomeone(name="Uday Vikram Singh"){
    console.log("Hello "+name);
}

function  fun(name="Sam" ,title="Sir"){
    console.log(title+" "+name)
}


function  returname(name="Sam" ,title="Sir"){
    return title+" "+name;
}

function times5(num){
    var result=num*5;
    return result
}

var n="Global Variable";
var stuff="Global Stuff";
function assign(stuff){
    console.log(n)
    stuff="Re-assign stuff inside function";
    console.log(stuff); // global variable
}

assign();
console.log(stuff);