#!/usr/bin/node
// This node script prints the number of movies where the character “Wedge Antilles” with character ID-18 is present.

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: node get-wedge-antilles-movies.js <api-url>');
    process.exit(1);
}

const apiUrl = process.argv[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/'

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        if (response.statusCode === 200) {
            const filmsData = JSON.parse(body);

            const moviesWithWedge = filmsData.results.filter(film => film.characters.includes(charUrl));

            console.log(moviesWithWedge.length);
        } else {
            console.error('Error:', response.statusCode);
        }
    }
});
