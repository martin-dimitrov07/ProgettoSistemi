document.getElementsByClassName('login-btn')[0].addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if(username || password) 
    {

    }
    else {
        document.getElementById('error-message').style.display = 'block';
    }

});