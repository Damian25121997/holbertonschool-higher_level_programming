#!/usr/bin/node
const $ = window.$;
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
