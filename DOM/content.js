var p=document.querySelector("p");
p.textContent="New Content";
p.innerHTML= "<strong>I am bold</strong>";

var link=document.querySelector("#special");
var linkA=link.querySelector("a");
linkA.getAttribute("href");
linkA.setAttribute("href","https://digipodium.com/")
linkA.textContent="DIGIPODIUM LINK";