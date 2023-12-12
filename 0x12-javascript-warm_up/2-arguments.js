#!/usr/bin/node

const argv = process.argv.length - 2;

if (argv === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
