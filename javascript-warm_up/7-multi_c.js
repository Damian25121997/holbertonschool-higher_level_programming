#!/usr/bin/node

// The script display in console

const x = process.argv[2];

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < x; index++) {
    console.log('C is fun');
  }
}
