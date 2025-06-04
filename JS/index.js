"use strict"

window.onload = function(){

    document.getElementById("invia").addEventListener("click", () => {
        fetch(`http://${IP_SERVER}:5000/api/invia`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "messaggio": document.querySelector("input[type='text']").value,
                "IPDest": "192.168.1.3",
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            console.log(data.messaggio);
        })
        .catch(error => {
            console.error("Errore durante la richiesta:", error);
        });

        // -------

        // fetch(`http://${IP_SERVER}:5000/api/messaggi?IPMittente=192.168.1.3`, {
        //     method: "GET",
        //     headers: {
        //         "Content-Type": "application/json"
        //     }
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log(data.messaggi);
        //     document.querySelector(".messageSent").textContent = data.messaggi[0].messaggio;
        // })
        // .catch(error => {
        //     console.error("Errore durante la richiesta:", error);
        // });
    })

    fetch(`http://${IP_SERVER}:5000/api/ascolta`, {
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
}

