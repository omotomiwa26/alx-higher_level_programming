// This Script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag

$(document).ready(function() {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: function(data) {
            $('#hello').text(data.hello);
        },
        error: function() {
            $('#hello').text('Failed to fetch translation');
        }
    });
});