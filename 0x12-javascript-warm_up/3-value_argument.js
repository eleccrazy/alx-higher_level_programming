#!/usr/bin/node

const argv = process.argv;
if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
