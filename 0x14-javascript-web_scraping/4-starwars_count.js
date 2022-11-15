#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error === null) {
    const jsonData = JSON.parse(body);
    let count = 0;
    for (const resultIndex in jsonData.results) {
      const film = jsonData.results[resultIndex];
      for (const characterIndex in film.characters) {
        const character = film.characters[characterIndex];
        if (character.endsWith('/18/')) count += 1;
      }
    }
    console.log(count);
  }
});
