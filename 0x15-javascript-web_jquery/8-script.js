$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;

    if (movies && movies.length > 0) {
      const ulElement = $('#list_movies');

      $.each(movies, function(index, movie) {
        ulElement.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
