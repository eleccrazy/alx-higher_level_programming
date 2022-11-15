#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/people/18', function (error, response, body) {
  if (error === null) {
    const jsonData = JSON.parse(body);
    console.log(jsonData.films.length);
  }
});
