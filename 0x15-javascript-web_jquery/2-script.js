// This Script updates the text color of the <header> element to red when the user clicks on the tag

$(document).ready(function() {
    $('#red_header').click(function() {
        $('header').css('color', '#FF0000');
    });
});