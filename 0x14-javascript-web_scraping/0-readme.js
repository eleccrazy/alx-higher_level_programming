#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], (err, data) => {
  if (err) console.log(err);
  else console.log(data.toString());
});
