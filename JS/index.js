const IP_SERVER = ""

let users = []

let messageStart = "Connessione stabilita"

window.onload = function(){

    document.getElementById("invia").addEventListener("click", () => {
        fetch("http://localhost:5000/api/invia", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "messaggio": messageStart,
                "IPmittente": "192.168.1.3",
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

    document.getElementById("ascolta").addEventListener("click", () => {
                fetch("http://localhost:5000/api/ascolta", {
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


}

