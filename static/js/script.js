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

// toolbar
$('.fixed-action-btn').floatingActionButton({
    toolbarEnabled: true
});

//modals
$(document).ready(function () {
    $('.modal').modal();
});

// admin buttons 

function viewRecipes() {
    document.getElementById('recipes').classList.remove('off')
    document.getElementById('users').classList.add('off')
    document.getElementById('admin-users').classList.add('off')

}


function viewUsers() {
    document.getElementById('recipes').classList.add('off')
    document.getElementById('users').classList.remove('off')
    document.getElementById('admin-users').classList.add('off')
}

function viewAdminUsers() {
    document.getElementById('admin-users').classList.remove('off')
    document.getElementById('recipes').classList.add('off')
    document.getElementById('users').classList.add('off')

}


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