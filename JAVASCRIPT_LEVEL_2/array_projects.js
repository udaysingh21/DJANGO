var students=[]



option=prompt("Please select one of the four commands: Add Student, Remove Student, Display Student, Quit")
while (option!="quit"){

    if (option=="Add Student"){
        name=prompt("Enter Student name: ");
        students.push(name);
        alert(name+" is added");
        option=prompt("Please select one of the four commands: Add Student, Remove Student, Display Student, Quit")

    }else if(option=="Remove Student"){

        name=prompt("Enter the name of student you want to remove: ");
        idx=students.indexOf(name);
        students.splice(idx,1);
        alert(name+" is removed");
        option=prompt("Please select one of the four commands: Add Student, Remove Student, Display Student, Quit")

    }else if(option=="Display Student"){

        alert(students);
        for (name of students){
            console.log(name)
        }
        option=prompt("Please select one of the four commands: Add Student, Remove Student, Display Student, Quit")
    }

}



