$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  const results = data.results;
  for (const idx in results) {
    $('UL#list_movies').append('<li>' + results[idx].title + '</li>');
  }
});
