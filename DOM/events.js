var over=document.querySelector("#one");
over.addEventListener('mouseover',function(){
    over.textContent="Mouse currently over !!";
    over.style.color= "red";
})

over.addEventListener('mouseout',function(){
    over.textContent="Hover over me !!";
    over.style.color= "black";
})


var click=document.querySelector("#two");
click.addEventListener('click',function(){
    click.textContent="Clicked on !!";
    click.style.color= "blue";
})

var doubleclick=document.querySelector("#three");
doubleclick.addEventListener('dblclick',function(){
    doubleclick.textContent=" Double Clicked on !!";
    doubleclick.style.color= "green";
})

console.log("Connected !!")