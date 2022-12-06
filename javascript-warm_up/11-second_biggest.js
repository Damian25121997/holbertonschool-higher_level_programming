#!/usr/bin/node

// The script display in console
const arg = process.argv;
const array = [];
for (let x = 2; arg[x]; x++) {
  array.push(arg[x]);
}
array.sort();
array.reverse();
let x = 0;
if (array.length === 0 || array.length === 1) {
  console.log(x);
} else {
  x = array[1];
  console.log(x);
}
