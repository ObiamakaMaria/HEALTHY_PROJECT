const categoryLink = document.getElementById('category-link');
const container2 = document.querySelector('.container-2');
const overlay = document.querySelector('.overlay');
const container = document.querySelector('.grid-result');
const seeMore = document.querySelector('#seeMoreBtn');
const rMsg = document.querySelector('.r-msg');
const inputs =  document.querySelector('.search-box');
function toggleBodyScrolling() {
  document.body.style.overflow = (container2.style.display === 'grid') ? 'hidden' : 'auto';
}
categoryLink.addEventListener('click', function() {
  container2.style.display = 'grid';
  overlay.style.display = 'block';
  toggleBodyScrolling()
});
overlay.addEventListener('click', function(){
  container2.style.display ='none';
  overlay.style.display = 'none';
  toggleBodyScrolling()
})

var pageToken;
var tmp;
const btn = document.querySelector('.search-button')

btn.addEventListener('click', function(){
container.innerHTML = '';
rMsg.style.display = 'none';
seeMore.style.display = 'none';
pageToken ='';
var query = inputs.value;
console.log(query);
    if (inputs.value != "")
{
    tmp = query;
    console.log(query);
    fetchData(query, pageToken)
    .then(function(response) {
        console.log(response);
        pageToken = response.nextPageToken;
  function embedVideos() {
    response.results.forEach(video => {
      const iframe = document.createElement('iframe');
      iframe.classList.add('videoFrame');
      iframe.src = video.url;
      iframe.title = video.title;
      container.appendChild(iframe);
      seeMore.style.display = 'block';
      rMsg.style.display = 'block';
      rMsg.innerText = "Results and realted videos for your search";
    });
    }
    if (response.results.length < 1)
     {
      rMsg.style.display = 'block';
      rMsg.innerText = "An error ocurred try different input or wait for some time";
     }
    else
     embedVideos()      
       // Process the response data here
    })
    .catch(function(error) {
        console.error(error);
        // Handle errors here
    });
   
}

else {
	alert("input must not be empty");
}
 


});
seeMore.addEventListener('click', function(){

    fetchData(tmp, pageToken)
    .then(function(response) {
        console.log(response);
        pageToken = response.nextPageToken;
    function embedVideos() {
     response.results.forEach(video => {
      const iframe = document.createElement('iframe');
      iframe.classList.add('videoFrame');
      iframe.src = video.url;
      iframe.title = video.title;
      container.appendChild(iframe);
    });
    }
    embedVideos()
       // Process the response data here
    })
    .catch(function(error) {
        console.error(error);
        // Handle errors here
    });





});
function fetchData(query, pageToken) {
    return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        var url = '/search';
        xhr.open('POST', url);
        xhr.setRequestHeader('Content-Type', 'application/json');
        var data = {
            query: query,
            pageToken: pageToken
        };
        var jsonData = JSON.stringify(data);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                resolve(response);
            } else {
                reject('Request failed with status: ' + xhr.status);
            }
        };
        xhr.onerror = function() {
            reject('Request failed');
        };
        xhr.send(jsonData);
    });
}

