"use strict"

window.addEventListener("load", () => {
    fetch(`http://${IP_SERVER}:5000/api/ascoltaServer`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
    })
    .catch(error => {
        console.error("Errore durante la richiesta:", error);
    });

    
})