var car={
    make: "Toyota",
    year: 1990,
    model: "Camry",
    carAlert: function(){
        alert("We've got a car here!!");
    }

};

console.log(car["make"])
console.log(car["year"])
console.log(car["model"])
// this is basically an object i.e. this.method
// this.method is equivalent to  car.carAlert()
console.log(car.carAlert())


var object={
    name: "Uday Vikram Singh",
    greet: function(){
        console.log("Hello "+this.name)
        alert("Welcome "+this.name)
    }
}

// this is equivalent to object(dictionary)
object["name"];
object.greet();