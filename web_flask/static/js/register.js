document.getElementById('signupForm').addEventListener('submit', function(event) {
            event.preventDefault();
            var email = document.getElementById('email').value;
            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;

            // Send the registration data to the Flask route using Fetch API
            fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: email,
                    username: username,
                    password: password
                })
            })
            .then(response => {
                if (response.ok) {
                    // Redirect to another page or perform other actions upon successful registration
                    window.location.href = '/login'; // Redirect to the login page
                } else {
                    // Handle error responses
                    return response.json().then(data => {
                        alert(data.error); // Display error message
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
