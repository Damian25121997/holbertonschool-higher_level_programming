#!/usr/bin/node

// The script display in console

const a = parseInt(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const r = factorial(a);
console.log(r);
