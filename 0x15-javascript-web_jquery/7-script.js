// This script fetches star wars character name from URL

$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/1/?format=json',
        method: 'GET',
        success: function(data) {
            $('#character').text(data.name);
        },
        error: function() {
            $('#character').text('Failed to fetch character name');
        }
    });
});
