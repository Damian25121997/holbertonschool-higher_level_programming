#!/usr/bin/node

// The script display in console
if (process.argv[3] === undefined) {
  console.log(process.argv[2] + ' is ' + undefined);
} else if (process.argv[2] === undefined && process.argv[3] === undefined) {
  console.log(undefined + ' is ' + undefined);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
