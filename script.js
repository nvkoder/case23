document.addEventListener("DOMContentLoaded", function() {
    const titleElement = document.getElementById("title");
    titleElement.innerHTML = titleElement.innerHTML.replace("-", "<span class='lightning'></span>");
});

// script.js
window.onload = function() {
    // Tilføj JavaScript-funktionalitet efter behov
    console.log('Dokumentet er indlæst.');
};

