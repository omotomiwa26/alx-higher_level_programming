// This script fetches and lists the title for all movies by using the API URL

$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            var movies = data.results;
            var $list = $('#list_movies');
            $.each(movies, function(index, movie) {
                $list.append('<li>' + movie.title + '</li>');
            });
        },
        error: function() {
            $('#list_movies').append('<li>Failed to fetch movies</li>');
        }
    });
});