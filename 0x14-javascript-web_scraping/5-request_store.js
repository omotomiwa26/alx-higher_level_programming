#!/usr/bin/node
// This node script gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node get-webpage-content.js <url> <output-file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (writeError) => {
      if (writeError) {
        console.error('Error writing to the file:', writeError);
      }
    });
  }
});
