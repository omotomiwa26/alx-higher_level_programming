#!/usr/bin/node

const argv = process.argv[2];

const intArgv = parseInt(argv);

if (!isNaN(intArgv)) {
  console.log(`My number: ${intArgv}`);
} else {
  console.log('Not a number');
}
