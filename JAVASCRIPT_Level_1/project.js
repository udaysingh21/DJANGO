firstname=prompt("Enter your firsrt name: ");
lastname=prompt("Enter your last name: ");
age=prompt("Enter your age: ");
height=prompt("Enter your height: ");
petname=prompt("Enter your pet name: ");

console.log(firstname)
console.log(lastname)
console.log(age)
console.log(height)
console.log(petname)

if (firstname[0]==lastname[0] && 20<age<30 && height>=170 && petname[petname.length-1]==='y'){
console.log("WELCOME SPY 😎")
}else{
console.log("GET BACK or You will be SHOT down 🔫")
}