// Navbar toggle
$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
});

// Select forms
$(document).ready(function () {
    $('select').formSelect();
});

// Collapsibles
$(document).ready(function () {
    $('.collapsible').collapsible();

});

// floating button
$(document).ready(function () {
    $('.fixed-action-btn').floatingActionButton();
    $('.fixed-action-btn').floatingActionButton('methodName');
    $('.fixed-action-btn').floatingActionButton('methodName', paramName);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
        direction: 'left'
    });
});

// toolbar
$('.fixed-action-btn').floatingActionButton({
    toolbarEnabled: true
});

//modals
$(document).ready(function () {
    $('.modal').modal();
});

// navbar responsiveness - removes valign-wrapper so css can change flex direction
function removeValignWrapperClass(screensize) {
    const searchBar = document.getElementById('search')
    if (screensize.matches) { // If media query matches
        console.log(searchBar)
        searchBar.classList.remove('valign-wrapper')
    } else {
        searchBar.classList.add('valign-wrapper')
    }
}

let screensize = window.matchMedia("(max-width: 600px)")
removeValignWrapperClass(screensize) // Call listener function at run time
screensize.addListener(removeValignWrapperClass) // Attach listener function on state changes