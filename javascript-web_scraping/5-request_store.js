#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, data, body) {
  if (error) console.log(error);
  fs.writeFile(file, body, 'utf8', function (error_) {
    if (error_) console.log(error_);
  });
});
