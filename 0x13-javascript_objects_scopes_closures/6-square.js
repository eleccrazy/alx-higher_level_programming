#!/usr/bin/node

const Squ = require('./5-square.js');

module.exports = class Square extends Squ {
  charPrint (c) {
    let ch;
    if (c) {
      ch = c;
    } else {
      ch = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(ch.repeat(this.width));
    }
  }
};
