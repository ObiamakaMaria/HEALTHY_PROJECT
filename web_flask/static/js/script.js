// My JavaScript functionality
$(document).ready(function () {
  var API_KEY = "AIzaSyB5lc-HbdcwEiDpaeQoPQy7U8hnj1gXFdw";

  $("#form").submit(function (event) {
    event.preventDefault();
    alert("form is submitted");

    var search = $("#search").val();

    videoSearch(API_KEY, search, 6);
  });

  function videoSearch(key, search, maxResults) {
    $.get(
      "https://www.googleapis.com/youtube/v3/search?key=" +
        key +
        "&type=video&part=snippet&maxResults=" +
        maxResults +
        "&q=" +
        search,
      function (data) {
        console.log(data);

        // Clear previous results
        $("#videos").empty();

        // Loop through each video item and embed video
        data.items.forEach(function (item) {
          var videoId = item.id.videoId;
          var videoTitle = item.snippet.title;

          // Construct iframe for video embedding
          var iframeCode =
            '<iframe width="250" height="300" src="https://www.youtube.com/embed/' +
            videoId +
            '" frameborder="0" allowfullscreen></iframe>';

          // Append video iframe to the #videos div
          $("#videos").append(iframeCode);
        });
      }
    );
  }
});
