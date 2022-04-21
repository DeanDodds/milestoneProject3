# Table of contents

1. [Validation](#validation) 
   - [html validator](#html)
   - [css validator](#css)
   - [python Pep8 complience](#pep8) 
   - [javaScript jshint complience](#javscript) 

# 1. Validation <a id="validation"></a>

I used the W3C Markup and CSS Validator Service to ensure there was no syntax errors throughout my website.

# Html <a id="html"></a> 




# Test Plan 
                                                       
| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|1|Navigation links|Home button pressed|Opens home page|!!!|Pass|Works as expected|
|2|Navigation links|Recipe button pressed|Opens Recipe page|!!!|Pass|Works as expected|
|3|Navigation links|About button pressed|Opens About page|!!!|Pass|Works as expected|
|4|Navigation links|Contact button pressed|Opens Contact page|!!!|Pass|Works as expected|
|5|Navigation links|Profile button pressed|Opens Profile page|!!!|Pass|Works as expected|
|6|Navigation links|Signup Page button pressed|Opens Sign up  page|!!!|Pass|Works as expected|
|7|Navigation links|Sign in button pressed|Opens Sign in page|!!!|Pass|Works as expected|
|8|Navigation links| My recipe button pressed|Opens My recipes page|!!!|Pass|Works as expected|
|9|Navigation links|Favourites button pressed|Opens Favourites page|!!!|Pass|Works as expected|
|10|Navigation links|Add recipe button pressed|Opens Add recipe page|!!!|Pass|Works as expected|
|11|Navigation links|Log Out button pressed|Logs user out of account<br><br>Opens login page<br><br>Flashes "You have been logged out"|!!!|Pass|Works as expected|
|12|Sign up Page|Login in using new username and password |New username and passoword added to database. <br><br>Flash "Sign up successfull!". <br><br>  User signed in and able to see profile and log out navigation buttons| !!!! |Pass | Worked as expected |
|13|Sign up Page|Try to sign up using a existing username| Clear Form<br><br>Flash "Username already exists. Please choose another username"|!!!!|Pass|Worked as expected|
|14|Sign up Page|Sign up with an in valid username and password|Form will not submit and display required message |!!!|Pass|  Works as expected
|15|Login Page| Login with correct details |User logged in. <br><br>Flash "Welcome" display the username message<br><br>Loads profile page.|!!!|Pass| Works as expected 
|16|login Page| Login with an incorrect username but correct password|"Incorrect Username and/or Password"|!!!|Pass|Worked as expected 
|17|login Page| Login with a valid username but incorrect password|"Incorrect Username and/or Password"|!!!|Pass|Worked as expected |
|18|Recipe Page| Press view recipe Button| Opens Recipe page for the recipe clicked on|!!!|Pass|Worked as expected|
|19|Recipe Page|Press the favourites button on a recipe that is not currently a favourite|favourites button should be check with a background color<br><br>recipe should be added to the users favourites page|!!!<br><br>!!!|Passes|worked as expected |
|19|Recipe Page|Press the favourites button on a recipe that is currently a favourite|favourites button should be uncheck and  background color removed<br><br>recipe should be removed from the users favourites page|!!!<br><br>!!!|Passes|worked as expected |
|20|Recipe Page|search for a keyword that should return one result|The search returns one recipe card|!!!|Pass|Works as expected|
|21|Recipe Page|search for a keyword that will return no results|Display "no reslts found"|!!!|Pass|Works as expected|
|22|Recipe page|search for a keyword that should return multible results|Display multiple recipe cards|!!!|Pass| Works as expectd|
|23|My recipes Page|search for a keyword that should return one result|The search returns one recipe card|!!!|Pass|Works as expected|
|24|My recipes Page|search for a keyword that will return no results|Display "no reslts found"|!!!|Pass|Works as expected|
|25|My recipes page|search for a keyword that should return multible results|Display multiple recipe cards|!!!|Pass| Works as expectd|
|26|My recipes Page|Press the favourites button on a recipe that is not currently a favourite|favourites button should be check with a background color<br><br>recipe should be added to the users favourites page|!!!<br><br>!!!|Passes|worked as expected |
|27|My recipes Page|Click the favourites button on a recipe that is currently a favourite|favourites button should be uncheck and  background color|!!!!!!|Passes| works as expected|
|28|My recipes Page|Click the delete recipe button and click ok button |modal should pop uo and ask for confirmation. Once ok is pressed recipe is deleted from the database and my recipe page reloads without the recipe|!!!|Pass|Works as expected|
|29|My Recipes Page|Click the edit recipe button|Edit recipe page loads and populated with the recipe data|!!!|!|!|
|30|



# known bugs

- cusine in catergories not displaying properly
- edit form ingrendents and instructions does not display correctly