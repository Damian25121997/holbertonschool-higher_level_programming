#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, data) {
  if (error) console.log(error);
  console.log('code: ' + data.statusCode);
});
