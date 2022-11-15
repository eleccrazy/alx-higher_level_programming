#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const request = require('request');
request(args[2], function (error, response, body) {
  if (error === null) {
    const data = body;
    fs.writeFile(args[3], data, (err) => {
      if (err) console.log(err);
    });
  }
});
