// one click - X
// double click - O
// triple click - Blank (delete everything inside cell)

// getting all the cells through their class
var cells=document.querySelectorAll(".tbl")

// single click
cells.forEach(cell => {
    cell.addEventListener('click',function(){
    cell.textContent="X";
    })
})

// double click
cells.forEach(cell => {
    cell.addEventListener('dblclick',function(){
    cell.textContent="O";
    })
})


