'use strict'

window.addEventListener('load', function () {
    $("form").eq(0).on("submit", Login)

    async function Login(event) {
        event.preventDefault()

        const username = $('#username').val()
        const password = $('#password').val()


        if (username == "" || password == "") {
            alert("TODO: Visualizzazione utente e password errata")
        }
        if (username == 'server' && password == 'server') {
            fetch("https://api.ipify.org?format=json")
                .then(response => response.json())
                .then(data => {
                    window.location.href = "./server.html";
                })
        }
        else {
            let rq = await inviaRichiesta("POST", "server/login.php", { username, password }).catch(errore)

            if (rq.data == "ok") {
                window.location.href = "./index.html"
            }
        }
    }
})