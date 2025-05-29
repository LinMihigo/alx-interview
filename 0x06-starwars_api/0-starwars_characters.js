#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./script.js <movie_id>');
  process.exit(1);
}

request(apiUrl, (err, _, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;
  const results = [];
  let count = 0;

  characters.forEach((url, index) => {
    request(url, (charErr, __, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }
      results[index] = JSON.parse(charBody).name;
      count++;

      if (count === characters.length) {
        results.forEach(name => console.log(name));
      }
    });
  });
});
