#!/usr/bin/node
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const all_movies = data.results;
  for (let x = 0; x < all_movies.length; x++) {
    $('UL#list_movies').append('<li>' + all_movies[x].title + '</li>');
  }
});
