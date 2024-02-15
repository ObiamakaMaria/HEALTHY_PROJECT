document.getElementById('articleForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var title = document.getElementById('title').value;
    var content = document.getElementById('content').value;

    // Send the article data to the Flask route using Fetch API
    fetch('/article', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: title,
            content: content
        })
    })
    .then(response => {
        if (response.ok) {
            // Redirect to another page or perform other actions upon successful article submission
            window.location.href = '/articles'; // Redirect to the articles page
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

