// This Script adds, removes and clears LI elements from a list when the user clicks

$(document).ready(function() {
    $('#add_item').click(function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });

    $('#remove_item').click(function() {
        $('ul.my_list li:last-child').remove();
    });

    $('#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});