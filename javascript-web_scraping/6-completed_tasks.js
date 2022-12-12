#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, data, body) {
  if (error) console.log(error);
  const dictionary = {};
  const all = JSON.parse(body);
  for (const x in all) {
    const task = all[x];
    const userid = all[x].userId;
    if (task.completed) {
      if (dictionary[userid] === undefined) {
        dictionary[userid] = 1;
      } else {
        dictionary[userid] += 1;
      }
    }
  }
  console.log(dictionary);
});
