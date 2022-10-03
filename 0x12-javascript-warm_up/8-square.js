#!/usr/bin/node

const argv = process.argv;
if (argv.length < 3 || !parseInt(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  for (let row = 0; row < size; row++) {
    console.log('X'.repeat(size));
  }
}
