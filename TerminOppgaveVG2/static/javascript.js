let Cookies = 0;
 
printCookies()
 
function printCookies(){
    document.getElementById("showCookies").innerHTML = Cookies + " Cookies In Stock"
}
 
function clickCookie(){
    Cookies = Cookies + 1
    printCookies()
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
