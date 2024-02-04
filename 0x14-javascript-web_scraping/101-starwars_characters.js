#!/usr/bin/node
// This node script prints all characters of a Star Wars movie:

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-movie-characters.js <movie-id>');
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

      const charactersList = movieData.characters;

      charactersList.forEach((characterUrl) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error('Error:', characterError);
          } else {
            if (characterResponse.statusCode === 200) {
              const characterData = JSON.parse(characterBody);
              console.log(characterData.name);
            } else {
              console.error('Error:', characterResponse.statusCode);
            }
          }
        });
      });
    } else {
      console.error('Error:', response.statusCode);
    }
  }
});
