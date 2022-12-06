#!/usr/bin/node

// The script display in console

const c = process.argv[2];
const g = process.argv[3];

function add (a, b) {
  if (parseInt(a) && parseInt(b)) {
    const h = parseInt(a) + parseInt(b);
    return (h);
  } else {
    return NaN;
  }
}
const x = add(c, g);
console.log(x);
