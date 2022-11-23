$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (result) {
  $('UL#list_movies').append(...result.results.map(movie => `<li>${movie.title}</li>`));
});
