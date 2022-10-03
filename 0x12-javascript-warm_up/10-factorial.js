#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const argv = process.argv;
const num = parseInt(argv[2]);
if (!num) {
  console.log('1');
} else {
  console.log(factorial(num));
}
