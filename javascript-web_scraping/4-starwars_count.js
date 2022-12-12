#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, data, body) {
  if (error) console.log(error);
  let count = 0;
  const all = JSON.parse(body).results;
  for (let x = 0; x < all.length; x++) {
    for (let y = 0; y < all[x].characters.length; y++) {
      if (all[x].characters[y].includes('/18/')) {
        count += 1;
        break;
      }
    }
  }
  console.log(count);
}
);
