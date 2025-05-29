'use strict'

window.addEventListener('load', function () {
    $('#btnAccedi').on('click', async function () {
        const username = $('#username').val()
        const password = $('#password').val()


        if (username == "" || password == "") {
            alert("TODO: Visualizzazione utente e password errata")
        }
        if (username == 'server' && password == 'server') {
            fetch("https://api.ipify.org?format=json")
                .then(response => response.json())
                .then(data => {
                    console.log("IP pubblico del client:", data.ip)
                })
        }
        else {
			let rq = await inviaRichiesta("POST", "server/login.php", { username, password }).catch(errore)

            console.log(risposta.data[0])
        }
    })
})