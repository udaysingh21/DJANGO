// Clicks

$("h1").click(function(){
//this refers to an object on which we are currently performing the event ,here this refers to 'h1'
    $(this).text("I WAS CHANGED")

})

$("li").click(function(){
    console.log("li was clicked !!");
})

// Key Press
$('input').eq(0).keypress(function(){
//    $('h3').toggleClass('turnBlue');
//console.log(event);
if (event.which===13){
    $('h3').toggleClass("turnBlue")
}
});

// on()

$("h1").on("mouseenter",function(){
// this points to the object on which we are currently performing the event.
// Here, this points to "h1"
$(this).toggleClass("turnBlue");

})

// Events and Animations
$('input').eq(1).on('click',function(){
//    $('.container').fadeOut(3000);
    $('.container').slideUp(3000);
})