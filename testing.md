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


# known bugs

- cusine in catergories not displaying properly
