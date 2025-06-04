"use strict"

let IP_DEST = "";

const ips = {
    "MartinDimitrov": "192.168.1.3",
    "DanieleGotta": "192.168.1.99",
    "EdoardoCasanova": "192.168.1.104" 
}

let usernameMittente;
let usernameDestinario;

window.onload = function(){
    $(".chat-window").hide();

    let rq = inviaRichiesta("GET", "server/getProprioUtente.php")
    rq.catch(errore)

    rq.then(function (response) {
        usernameMittente = response.data[0].userName;
    })

    rq = inviaRichiesta("GET", "server/getUtenti.php")
    rq.catch(errore)

    rq.then(function (response) {
        const users = response.data;

        for (const user of users) 
        {
            const div = document.createElement("div");
            div.classList.add("user");
            div.textContent = user.userName;
            document.querySelector(".users-list").appendChild(div);

            div.addEventListener("click", function(){
                usernameDestinario = user.userName
                IP_DEST = ips[user.userName]
                console.log(IP_DEST)
                document.querySelector(".chat-header").textContent = "Chat con " + user.userName
                $(".chat-window").show();
            })
        }
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

    document.getElementById("btnInvia").addEventListener("click", () => {
        fetch(`http://${IP_SERVER}:5000/api/invia`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messaggio: document.querySelector("input[type='text']").value,
                IPDest: IP_DEST
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);

            fetch(`http://${IP_SERVER}:5000/api/messaggi`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                let messaggi = data.messaggi;
                mostraMessaggi(messaggi);
                
            })
            .catch(error => {
                console.error("Errore durante la richiesta:", error);
            });

        })
        .catch(error => {
            console.error("Errore durante la richiesta:", error);
        });
    })

    function mostraMessaggi(messaggi)
    {
        const divMessages = document.querySelector(".messages");

        divMessages.innerHTML = "";

        // divMessages.innerHTML = "";
            // <div class="messageReceived">
            //     <div class="card rec">
            //         <div class="textBox">
            //         <div class="textContent">
            //             <p class="h1">persona1</p>
            //         </div>
            //         <p class="p">ricevuto</p>
            //         <div>
            //         </div>
            //         </div>
            //     </div>
            // </div>

        for(const messaggio of messaggi)
        {
            if(messaggio.tipo == "ricevuto")
            {
                divMessages.innerHTML += `
                    <div class="messageReceived">
                        <div class="card rec">
                            <div class="textBox">
                                <div class="textContent">
                                    <p class="h1">${Object.keys(messaggi).filter(key => messaggi[key] === IP_DEST)}</p>
                                </div>
                                <p class="p">${messaggio.messaggio}</p>
                                <div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
            else
            {
                divMessages.innerHTML += `
                    <div class="messageSent">
                        <div class="card sent">
                            <div class="textBox">
                            <div class="textContent">
                                <p class="h1">${Object.keys(ips).filter(key => ips[key] === messaggio.mittente)}</p>
                            </div>
                            <p class="p">${messaggio.messaggio}</p>
                            <div>
                            </div>
                        </div>
                    </div>
                `
            }
        }
    }

    setInterval(() => { 
        fetch(`http://${IP_SERVER}:5000/api/messaggi`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            let messaggi = data.messaggi;
            mostraMessaggi(messaggi);
        })
        .catch(error => {
            console.error("Errore durante la richiesta:", error);
        });
    }, 2000)

}

