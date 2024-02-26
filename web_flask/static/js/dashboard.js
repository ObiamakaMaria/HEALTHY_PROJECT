const spanEmail = document.querySelector('.s-name');
const spanName = document.querySelector('.s-email');

fetch('/info')
  .then(response => {
    // Check if the response is successful (status code 200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    } else {
      // Handle errors
      throw new Error('Failed to fetch user info');
    }
  })
  .then(data => {
    // Print the result
    console.log('User Info:', data);
    spanEmail.innerText = data.email;
    spanName.innerText= data.name;
  })
  .catch(error => {
    // Handle errors
    console.error('Error:', error);
  });

