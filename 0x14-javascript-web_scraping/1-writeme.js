#!/usr/bin/node
// This node script writes a string to a file.

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node write-file.js <file-path> <string-to-write>');
  process.exit(1);
}
const filePath = process.argv[2];
const stringToWrite = process.argv[3];
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error writting to the file:', err);
  }
});
