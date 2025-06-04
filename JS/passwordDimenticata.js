'use strict'

window.addEventListener('load', function () {
    const form = document.getElementById('resetPasswordForm')
    const campoNuovaPassword = document.getElementById('newPassword')
    const campoConfermaPassword = document.getElementById('confirmPassword')
    const messaggioErrore = document.getElementById('errorMessage')
    const messaggioSuccesso = document.getElementById('successMessage')

    form.addEventListener('submit', async function (evento) {
        evento.preventDefault()

        const nuovaPassword = campoNuovaPassword.value
        const confermaPassword = campoConfermaPassword.value

        // Nasconde i messaggi precedenti
        messaggioErrore.style.display = 'none'
        messaggioSuccesso.style.display = 'none'

        // Controlla se la password è troppo corta
        if (nuovaPassword.length < 8) {
            messaggioErrore.textContent = 'La password deve contenere almeno 8 caratteri'
            messaggioErrore.style.display = 'block'
            return
        }

        // Controlla se le password coincidono
        if (nuovaPassword != confermaPassword) {
            messaggioErrore.textContent = 'Le password non corrispondono'
            messaggioErrore.style.display = 'block'
            return
        }

        // Simulazione invio al server
        let rq = await inviaRichiesta("POST", "server/aggiornaPassword.php", { "password": nuovaPassword, "username": $("#username").val() })

        // Mostra il messaggio di successo
        messaggioSuccesso.style.display = 'block'

        // Reindirizza l’utente dopo 2 secondi
        setTimeout(() => {
            window.location.href = 'index.html'
        }, 2000)
    })

    // Controllo in tempo reale mentre si scrive
    campoConfermaPassword.addEventListener('input', function () {
        const nuovaPassword = campoNuovaPassword.value
        const confermaPassword = campoConfermaPassword.value

        if (confermaPassword && nuovaPassword !== confermaPassword) {
            campoConfermaPassword.style.borderColor = '#e74c3c'
        } else {
            campoConfermaPassword.style.borderColor = 'transparent'
        }
    })
})
