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

// star rating imput code from - https://www.codingnepalweb.com/star-rating-html-css-javascript/
const btn = document.querySelector("button");
const post = document.querySelector(".post");
const widget = document.querySelector(".star-widget");
const editBtn = document.querySelector(".edit");
btn.onclick = () => {
    widget.style.display = "none";
    post.style.display = "block";
    editBtn.onclick = () => {
        widget.style.display = "block";
        post.style.display = "none";
    }
    return false;
}