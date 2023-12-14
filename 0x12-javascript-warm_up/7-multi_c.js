#!/usr/bin/node

const argv = process.argv[2];

const numberOccur = parseInt(argv);

let i;

if (!isNaN(numberOccur)) {
  for (i = 0; i < numberOccur; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
