/*
Build a basic arithmetic calculator without a frontend
The calculator should be able to perform basic operations like Addition, Subtraction, Multiplication, & Division
*/

// user input, two number and operation

let number = Number(prompt("Enter First Number:"));

var operations = prompt("Choose Operation:(+, -, *, /)");

let number_2 = Number(prompt("Enter Second Number:"));

// program logic and expression

if (operations == "+"){
    var result = number + number_2
    window.alert("Answer: " + result)
}
else if(operations == "-"){
    var result = number - number_2
    window.alert("Answer: " + result)
}
else if(operations == "*"){
    var result = number * number_2
    window.alert("Answer: " + result)
}
else if(operations == "/"){
    var result = number - number_2
    window.alert("Answer: " + result)
}