#!/usr/bin/node

const num = process.argv[2];
!Number(num) ? console.log('Not a number') : console.log('My number: ' + num);
