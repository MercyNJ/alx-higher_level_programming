//  A script that  fetches and lists the title for all movies from given URL.

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
