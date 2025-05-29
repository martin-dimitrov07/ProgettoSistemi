const IP_SERVER = "192.168.1.3"

let users = []

let messageStart = "Connessione stabilita"

window.onload = function(){

    document.getElementById("invia").addEventListener("click", () => {
        fetch(`http://${IP_SERVER}:5000/api/invia`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "messaggio": messageStart,
                "IPDest": "192.168.1.3",
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
        })
        .catch(error => {
            console.error("Errore durante la richiesta:", error);
        });
    })

    document.getElementById("ascoltaServer").addEventListener("click", () => {
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

    fetch(`http://${IP_SERVER}:5000/api/ascolta`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.messaggio);
    })
    .catch(error => {
        console.error("Errore durante la richiesta:", error);
    });

}

