document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    // Send the login data to the Flask route using Fetch API
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        if (response.ok) {
            // Redirect to another page or perform other actions upon successful login
            window.location.href = '/home';
        } else {
            // Handle error responses
            return response.json().then(data => {
                alert(data.message); // Display error message
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

