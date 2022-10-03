#!/usr/bin/node

function findBig (myArray) {
  let big = parseInt(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (parseInt(argv[i]) > big) {
      big = parseInt(argv[i]);
    }
  }
  return (big);
}

const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
} else {
  const firstBig = findBig(argv);
  const firstBigIndex = argv.indexOf(firstBig.toString());
  argv.splice(firstBigIndex, 1);
  const secondBig = findBig(argv);
  console.log(secondBig);
}
