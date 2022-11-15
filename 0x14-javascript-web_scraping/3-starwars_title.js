#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
request(url, function (error, response, body) {
  if (error === null) {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
