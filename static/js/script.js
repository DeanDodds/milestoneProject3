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