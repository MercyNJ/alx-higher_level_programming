#!/usr/bin/node
// Script that  prints all characters of a Star Wars movie.

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  fetchCharacters(0);
});

const fetchCharacters = (i) => {
  if (i === characters.length) {
    return;
  }

  request(characters[i], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    fetchCharacters(i + 1);
  });
};
