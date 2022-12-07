#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  const array = [];
  for (len; list[len]; len--) {
    array.push(list[len]);
  }
  return array;
};
