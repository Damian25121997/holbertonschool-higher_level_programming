#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + url + '/', function (error, data, body) {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
