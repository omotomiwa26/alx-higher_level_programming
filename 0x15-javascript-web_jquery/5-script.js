// // This Script adds a list element to a list when the user clicks on the tag DIV#add_item:
$(document).ready(function() {
    $('#add_item').click(function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });
});