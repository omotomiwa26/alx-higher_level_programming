// This script fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: {
                lang: languageCode
            },
            success: function(data) {
                $('#hello').text(data.hello);
            },
            error: function() {
                $('#hello').text('Translation not available');
            }
        });
    });
});