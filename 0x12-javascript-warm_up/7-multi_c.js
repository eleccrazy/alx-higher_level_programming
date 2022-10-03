#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2 || !parseInt(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 1;
  while (i <= parseInt(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
