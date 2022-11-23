$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (result) {
  $('DIV#character').text(result.name);
});
