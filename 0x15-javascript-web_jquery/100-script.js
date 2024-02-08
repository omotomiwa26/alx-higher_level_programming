//This Script updates the text color of the <header> element to red (#FF0000):

        document.addEventListener('DOMContentLoaded', function() {
            var header = document.querySelector('header');
            if (header) {
                header.style.color = '#FF0000';
            } else {
                console.error('Header element not found!');
            }
        });
