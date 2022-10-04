#!/usr/bin/node

const dict = require('./101-data.js').dict;

const sortedDict = {};

for (const k in dict) {
  if (!sortedDict[dict[k]]) {
    sortedDict[dict[k]] = [k];
  } else {
    sortedDict[dict[k]].push(k);
  }
}
console.log(sortedDict);
