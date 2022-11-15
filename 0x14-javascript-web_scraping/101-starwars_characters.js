#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
request(url, async function (error, response, body) {
  if (error === null) printer(JSON.parse(body).characters, 0);
});

function printer (characters, i) {
  request(characters[i], function (error, response, body) {
    if (error === null) {
      console.log(JSON.parse(response.body).name);
      if (i + 1 < characters.length) printer(characters, i + 1);
    }
  });
}
