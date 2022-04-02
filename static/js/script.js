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

// Get ingrendents lists 
let addIngredientsBtn = document.getElementById("add-item-button")
addIngredientsBtn.addEventListener("click", addIngredients)

function addIngredients() {

    let ingredientsList = document.getElementById('ingredients-list');
    let ingredients = document.getElementById('ingredients').value;
    let amount = document.getElementById('amount').value;
    let units = document.getElementById('units').value;
    let ingredientsListItem = `${amount + units} ${ingredients}`;
    let li = document.createElement('li');
    let node = document.createTextNode(ingredientsListItem);

    li.appendChild(node);
    ingredientsList.appendChild(li);
}