#!/usr/bin/node
// Script that counts movies with character “Wedge Antilles” is present.

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

let movieCount = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);
    movies.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          movieCount += 1;
        }
      });
    });
    console.log(movieCount);
  }
});
