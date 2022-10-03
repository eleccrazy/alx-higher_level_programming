#!/usr/bin/node

const num = process.argv[2];
!parseInt(num) ? console.log('Not a number') : console.log('My number: ' + parseInt(num));
