// Setter initial verdi for Pizza til 0
let Pizza = 0;

// Kaller funksjonen for å oppdatere visningen av pizza i lager
printPizza();

// Funksjon for å oppdatere visningen av antall pizzaer
function printPizza() {
    document.getElementById("showPizza").innerHTML = Pizza + " Pizzas In Stock";
}

// Funksjon som øker antall pizzaer med 1 når klikkes
function clickPizza() {
    Pizza = Pizza + 1; // Øker Pizza med 1
    printPizza(); // Oppdaterer visningen
}

// Funksjon for å åpne popup-vinduet
function openPopup(nr) {
    let popup = document.getElementById(nr); // Henter popup-elementet med id
    let overlay = document.getElementById('overlay'); // Henter overlay (bakgrunn)
    popup.classList.add("open-popup"); // Vist popup-vinduet
    overlay.classList.add("show");    // Vist og blur bakgrunn
}

// Funksjon for å lukke popup-vinduet
function closePopup(nr) {
    let popup = document.getElementById(nr); // Henter popup-elementet
    let overlay = document.getElementById('overlay'); // Henter overlay (bakgrunn)
    popup.classList.remove("open-popup"); // Skjuler popup-vinduet
    overlay.classList.remove("show");    // Fjerner blur bakgrunn
}

// Variabler for slange-spillet
let grid = document.querySelector(".grid"); // Henter grid-elementet for slange
let popup = document.querySelector(".popup"); // Henter popup-elementet
let playAgain = document.querySelector(".playAgain"); // Henter element for å spille igjen
let scoreDisplay = document.querySelector(".scoreDisplay"); // Henter element for å vise poeng
let left = document.querySelector(".left"); // Henter venstre pil knapp
let bottom = document.querySelector(".bottom"); // Henter ned pil knapp
let right = document.querySelector(".right"); // Henter høyre pil knapp
let up = document.querySelector(".top"); // Henter opp pil knapp

// Definerer spillvariabler for slange-spillet
let width = 10; // Antall celler i bredden
let currentIndex = 0; // Startindeks for slangen
let appleIndex = 0; // Indeks for eplet
let currentSnake = [2, 1, 0]; // Indekser for slangen
let direction = 1; // Startretning for slangen (1 = høyre)
let score = 0; // Start poengsum
let speed = 0.8; // Hastigheten på slange-bevegelsen
let intervalTime = 0; // Tid mellom hver bevegelse
let interval = 0; // Intervallet for å oppdatere spillet
