// Assuming you have a form with id="loginForm" and input fields with id="username" and id="password"
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    // Get the input values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Create a JSON object with the username and password
    var data = {
        username: username,
        password: password
    };
    
    // Make an AJAX POST request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Success, do something with the response
            console.log(xhr.responseText);
        }
    };
    xhr.send(JSON.stringify(data));
});

