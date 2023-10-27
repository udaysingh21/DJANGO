var cells=document.querySelectorAll("td");

function playgame(){
    if (this.textContent===" "){
        this.textContent="X";
    }else if(this.textContent==="X"){
        this.textContent="O";
    }else{
        this.textContent=" ";
    }
};

for (var i=0;i<cells.length;i++){
    // for each cell we are adding an Event Listener
    cells[i].addEventListener('click',playgame)

}

