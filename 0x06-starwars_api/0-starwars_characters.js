#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) return console.error(err);
  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(url => {
    request(url, (err, res, body) => {
      if (!err) {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
});
