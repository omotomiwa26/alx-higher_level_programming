#!/usr/bin/node
// This node script prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-star-wars-movie.js <movie-id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);

      console.log(movieData.title);
    } else {
      console.error('Error:', response.statusCode);
    }
  }
});
