#!/usr/bin/node

// The script display in console
const arg = process.argv
let array = []
for (let x = 2;arg[x]; x++) {
    array.push(parseInt(arg[x]));
}
array.sort( function(a, b) {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
})
array.reverse()
let x = 0
if (array.length === 0 || array.length === 1)
{
    console.log(x)
} else {
    x = array[1]
    console.log(x)
}