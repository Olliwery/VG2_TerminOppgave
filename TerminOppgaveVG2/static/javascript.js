let Pizza = 0;
 
printPizza()
 
function printPizza(){
    document.getElementById("showPizza").innerHTML = Pizza + " Pizzas In Stock"
}
 
function clickPizza(){
    Pizza = Pizza + 1
    printPizza()
}


function openPopup(nr) {
    let popup = document.getElementById(nr);
    let overlay = document.getElementById('overlay');
    popup.classList.add("open-popup"); // Show popup
    overlay.classList.add("show");    // Show and blur overlay
}

function closePopup(nr) {
    let popup = document.getElementById(nr);
    let overlay = document.getElementById('overlay');
    popup.classList.remove("open-popup"); // Hide popup
    overlay.classList.remove("show");    // Remove blur overlay
}


let grid = document.querySelector(".grid");
let popup = document.querySelector(".popup");
let playAgain = document.querySelector(".playAgain");
let scoreDisplay = document.querySelector(".scoreDisplay");
let left = document.querySelector(".left");
let bottom = document.querySelector(".bottom");
let right = document.querySelector(".right");
let up = document.querySelector(".top");
let width = 10;
let currentIndex = 0;
let appleIndex = 0;
let currentSnake = [2, 1, 0];
let direction = 1;
let score = 0;
let speed = 0.8;
let intervalTime = 0;
let interval = 0;