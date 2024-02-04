#!/usr/bin/node
// This node script displays the status code of a GET request.

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-status-code.js <url>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Code:', response.statusCode);
  }
});
