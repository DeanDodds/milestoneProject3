# Table of contents

1. [Validation](#validation) 
   - [html validator](#html)
   - [css validator](#css)
   - [python Pep8 complience](#pep8) 
   - [javaScript jshint complience](#javscript) 
2. [Lighthouse reports](#lighthouse)
3. [Testing user stories](#stories)
   - [First Time Visitor Goals](#1st)
   - [Returning Visitor Goals](#2nd)
   - [Site Owner Goals](#owner)
4. [Test Plan](#test-plan)
5. [Further testin](#further)

# 1. Validation <a id="validation"></a>

I used the W3C Markup and CSS Validator Service to ensure there was no syntax errors throughout my website.

# Html <a id="html"></a> 

| ![index page validation](/assets/screenshots/homeval.png) |
|:--:|
| <b>index page validation - Passed  - No errors or warnings</b>|

 ![Recipes page validation](/assets/screenshots/recipeval.png) |
|:--:|
| <b>Recipe page validation - Passed  - No errors or warnings</b>|

 ![About us  page validation](/assets/screenshots/aboutval.png) |
|:--:|
| <b>About us validation - Passed  - No errors or warnings</b>|

 ![Contact us  page validation](/assets/screenshots/contactval.png) |
|:--:|
| <b>Contact us validation - Passed  - No errors or warnings</b>|

 ![Profile page validation](/assets/screenshots/profileval.png) |
|:--:|
| <b>Profile page validation - Passed  - No errors or warnings</b>|

 ![Add recipe validation](/assets/screenshots/addrecipeval.png) |
|:--:|
| <b>Add recipe validation - Passed  - No errors or warnings</b>|

 ![Favourites validation](/assets/screenshots/favouritesval.png) |
|:--:|
| <b>Favourites validation - Passed  - No errors or warnings</b>|

 ![Admin Page validation](/assets/screenshots/controlpanelval.png) |
|:--:|
| <b>Admin page validation - Passed  - No errors or warnings</b>|

 ![login validation](/assets/screenshots/loginval.png) |
|:--:|
| <b>Login page validation - Passed  - No errors or warnings</b>|

![Sign up validation](/assets/screenshots/signupval.png) |
|:--:|
| <b>Sign up page validation - Passed  - No errors or warnings</b>|

![a individual recipe validation](/assets/screenshots/eachrecipeval.png) |
|:--:|
| <b>individual recipe page validation - Passed  - No errors or warnings</b>|

## CSS <a id="css"></a>

![CSS validation](/assets/screenshots/cssval.png) |
|:--:|
| <b>CSS validation  - Passed  - All errors and warnings from the meterialised css files</b>|

## Python Pep8 complience <a id="pep8"></a>

I used the Pep8 validator to to ensure there was no syntax errors in my python code

![env.py file validated](/assets/screenshots/envval.png) |
|:--:|
| <b>env.py file validated  - Passed  - 1 error however the line cannot be split to fix this error</b>|

![app.py file validated](/assets/screenshots/appval.png) |
|:--:|
| <b>app.py file validated  - Passed  - No errors or warnings</b>|

## JavaScript jshint complience <a id="javascript"></a>

I used the jShint validator to to ensure there was no syntax errors in my JavaScript code

![script.js validated](/assets/screenshots/jshint.png) |
|:--:|
| <b>script.js validated  - Passed  - unsed variables are onclick functions function</b>|

# 2. Lighthouse Testing <a id="lighthouse"></a>

All my pages have went through google devtools lighthouse analysis which are scored on: 
* Performance 
* Accesibility 
* Best Practices 
* Search Engine Optimization (SEO)

![home page lighthouse scores](/assets/screenshots/homeseo.png) |
|:--:|
| <b>home page lighthouse scores - All fine  - no issues</b>|

![About us page lighthouse scores](/assets/screenshots/aboutlight.png) |
|:--:|
| <b>About us page lighthouse scores - All fine  - no issues</b>|

![Recipes page lighthouse scores](/assets/screenshots/recipelight.png) |
|:--:|
| <b>Recipes page lighthouse scores - All fine  - no issues</b>|

![Contact us page lighthouse scores](/assets/screenshots/contactlight.png) |
|:--:|
| <b>Contact us page lighthouse scores - All fine  - no issues</b>|

![Profile page lighthouse scores](/assets/screenshots/profilelight.png) |
|:--:|
| <b>Profile page lighthouse scores - All fine  - no issues</b>|

![Favourites page lighthouse scores](/assets/screenshots/favouriteslight.png) |
|:--:|
| <b>Favourites pag lighthouse scores - All fine  - no issues</b>|

![Sign up page lighthouse scores](/assets/screenshots/signuplight.png) |
|:--:|
| <b>Sign up page lighthouse scores - All fine  - no issues</b>|

![Login page lighthouse scores](/assets/screenshots/loginlight.png) |
|:--:|
| <b>Login page lighthouse scores - All fine  - no issues</b>|

![individual recipe pages lighthouse scores](/assets/screenshots/eachrecipelight.png) |
|:--:|
| <b>individual recipe pages - Accesibility and best practices to be improved - Accesibility could be improved   - Aria labels to be added and labels to be added to links </b>|

![Add recipe page lighthouse scores](/assets/screenshots/addrecipelight.png) |
|:--:|
| <b>Add recipe page lighthouse scores - Accesibility could be improved   - Aria labels to be added and labels to be added to links </b>|

![Admin page lighthouse scores](/assets/screenshots/adminpagelight.png) |
|:--:|
| <b>Admin page lighthouse scores - Accesibility could be improved   - Aria labels to be added and labels to be added to links through tooltips </b>|

# 3. Testing User Stories <a id="stories"></a>

### First Time Visitor Goals <a id="1st"></a>
1. As a first time visitor, I want to easily understand the purpose of the website.
 * When entering the site users can clearly see the navigation bar and the purpose of the site is very clear

 ![home page screenshot](/assets/screenshots/Homepage.png) |
|:--:|
| <b>Outline of the home page and a clear navigation bar at the top of the page</b>|

2.  As a first time visitor, i want to eaily navigate through the website to find the information i want.
   * The website has a navigation bar at the top of every page allowing
    the user to easily navigate through the pages 

![navbar screenshot](/assets/screenshots/navbar.png) |
|:--:|
| <b>clear navigation bar at the top of each page </b>|

3. As a first time visitor, I want to be able to view the website on all my devices.
 * Website is fully responsive. 

![home page mobile](/assets/screenshots/iphone.png) |
|:--:|
| <b>mobile version for small screens</b>|

![home page tablet](/assets/screenshots/tablet.png) |
|:--:|
| <b>Tablet version for medium screens</b>|

4. As a first time visitor, I want to view recipes without logging in.
 * Log in page can easily be navigated to using the navigation bar.
 * Users can view the recipes easily wihout making an account. 
 
![recipe page](/assets/screenshots/logoutedrecipecard.png) |
|:--:|
| <b>Users can search and view all recipes without logging in</b>|

5. As a first time visitor, I want to beable to create and account easily if i want to. 
 * Sign in page can easily be navigated to using the navigation bar.
 * Sign up to an accounts is very easy and sign posted in the navigation bar and login page.

![Sign in page](/assets/screenshots/signup.png) |
|:--:|
| <b>Users can sign up using the sign up page </b>|
 
### Returning Visitor Goals <a id="2nd"> </a>


1. As a returning visitor, I want to beable to easily log in to my account.
 * Login page is clearly sign posted in the navigation bar 

![login page](/assets/screenshots/login.png) |
|:--:|
| <b>Users login using the login page</b>|

2. As a returning visitor, I want to beable to add my own recipes to the website.
 * Once logged in users can add recipes to the website on the add recipe page.

![add recipe page](/assets/screenshots/addrecipe.png) |
|:--:|
| <b>Users lcan add a recipe to the website if they have an accout </b>|

3. As a returning visitor, I want to beable to save recipes to my account.
 * users are easily able to save there favourite recipes to their account as all recipes have a like button.
 * The recipes are then saved to the users favourites page.

 ![favourites button](/assets/screenshots/editbuttons.png) |
|:--:|
|<b>Buttons on each recipe card for deleting, editing and adding recipes to favourites</b>|

4. As a returning visitor, I want to beable to rate recipes.
 * All recipes can be rated from 1-5 on their indivadual recipe pages. users can also see how many time the recipe has been rated.

![rating form](/assets/screenshots/ratingform.png) |
|:--:|
|<b>Star rating form</b>|

5. As a returning visitor, I want to beable to sign up to the newsletter and find out the latest information 
 * There is a newsletter sign up form in the footer of every page.

![newsletter sign up form](/assets/screenshots/footermobile.png) |
|:--:|
|<b>Sign up to newsletter clearly sign posted in the footer</b>| 

6. As a returning visitor, i want to beable to find social media links to different platforms.
 *  There is social media links in the footer of every page. 

![social media links](/assets/screenshots/footer.png)|
|:--:|
|<b>social media links clearly sign posted in the footer</b>| 



### Website Creator Goals <a id="owner"></a>
1. As the website creator, I want to beable to advertise cooking products.
 * This goal was not hit however is a feature to revist in the future. 
2. As the website creator, I want to beable to edit and delete all recipes.
 * Admin page allows all recipes to be edited by an admin users.

 ![admin page](/assets/screenshots/adminpage.png) |
|:--:|
|<b>admin users can delete users and recipes from the control panel admin page</b>|  

3. As a website creator, I want to create a website that works on all platforms.
 * website is fully responsive.

![home page mobile](/assets/screenshots/iphone.png) |
|:--:|
| <b>mobile version for small screens</b>|

![home page tablet](/assets/screenshots/tablet.png) |
|:--:|
| <b>Tablet version for medium screens</b>|

4. As a website creator, I want to create a good user experience by having a clear navigation system.
 * website navigation is clear 

![navbar screenshot](/assets/screenshots/navbar.png) |
|:--:|
|<b>clear navigation bar at the top of each page </b>|

5. As a website creator, I want my website load times to be low. I do not want users leaving the site before it has time to load.
 * all pages have an above 90 light house score see [Lighthouse reports](#lighthouse)
  
6. As a website creator, I want my website to be as accesible as possible in order to be inclusive to all potenial users.
 * Most pages have a above 90 accesibility score. See [Lighthouse reports](#lighthouse)

# 4. Test Plan 
                                                       
| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|1|Navigation links|Home button pressed|Opens home page|![home page](/assets/screenshots/Homepage.png)|Pass|Works as expected|
|2|Navigation links|Recipe button pressed|Opens Recipe page|![recipe page](/assets/screenshots/logoutedrecipecard.png)|Pass|Works as expected|
|3|Navigation links|About button pressed|Opens About page|![About page](/assets/screenshots/about.png)|Pass|Works as expected|
|4|Navigation links|Contact button pressed|Opens Contact page|![contact page](/assets/screenshots/contact.png)|Pass|Works as expected|
|5|Navigation links|Profile button pressed|Opens Profile page|![profile page](/assets/screenshots/profile.png)|Pass|Works as expected|
|6|Navigation links|Signup Page button pressed|Opens Sign up  page|![sign up page](/assets/screenshots/signup.png)|Pass|Works as expected|
|7|Navigation links|Log in button pressed|Opens Log in page|![sign in page](/assets/screenshots/login.png)|Pass|Works as expected|
|8|Navigation tab link| My recipe button pressed|Opens My recipes page|![profile page](/assets/screenshots/profile.png)|Pass|Works as expected|
|9|Navigation tab link|Favourites button pressed|Opens Favourites page|![favourites page](/assets/screenshots/favouritepage.png)|Pass|Works as expected|
|10|Navigation tab link|Add recipe button pressed|Opens Add recipe page|![add recipe](/assets/screenshots/addrecipe.png)|Pass|Works as expected|
|11|Navigation links|Log Out button pressed|Logs user out of account<br><br>Opens login page<br><br>Flashes "You have been logged out"|![logging out](/assets/screenshots/loggedout.png)|Pass|Works as expected|
|12|Sign up Page|Login in using new username and password |New username and passoword added to database. <br><br>Flash "Sign up successfull!". <br><br>  User signed in and able to see profile and log out navigation buttons| ![sign in](/assets/screenshots/login.png) |Pass | Worked as expected |
|13|Sign up Page|Try to sign up using a existing username| Clear Form<br><br>Flash "Username already exists. Please choose another username"|![user exsits](/assets/screenshots/exsitinguser.png)|Pass|Worked as expected|
|14|Sign up Page|Sign up with an in valid username and password|Form will not submit and display required message |![new user](/assets/screenshots/newuser.png)|Pass|  Works as expected
|15|Login Page| Login with correct details |User logged in. <br><br>Flash "Welcome" display the username message<br><br>Loads profile page.|![login](/assets/screenshots/login.png)|Pass| Works as expected 
|16|login Page| Login with an incorrect username but correct password|"Incorrect Username and/or Password"|![incorrect password](/assets/screenshots/password.png)|Pass|Worked as expected 
|17|login Page| Login with a valid username but incorrect password|Flash "Incorrect Username and/or Password"|![invalid login](/assets/screenshots/username.png)|Pass|Worked as expected |
|18|Recipe Page| Press view recipe Button| Opens Recipe page for the recipe clicked on|![recipe page](/assets/screenshots/eachrecipe.png)|Pass|Worked as expected|
|19|Recipe Page|Press the favourites button on a recipe that is not currently a favourite|favourites button should be check with a background color<br><br>recipe should be added to the users favourites page|![favourited](/assets/screenshots/favourited.png)<br><br>![favourite page](/assets/screenshots/favouritepage.png)|Passes|worked as expected |
|20|Recipe Page|Press the favourites button on a recipe that is currently a favourite|favourites button should be uncheck and  background color removed<br><br>recipe should be removed from the users favourites page|![unfavourited](/assets/screenshots/unfavourtited.png)<br><br>![favourite page ](/assets/screenshots/unfavourtedpage.png)|Passes|worked as expected |
|21|Recipe Page|search for a keyword that should return one result|The search returns one recipe card|![search](/assets/screenshots/search1.png)|Pass|Works as expected|
|22|Recipe Page|search for a keyword that will return no results|Display "no reslts found"|!![search](/assets//screenshots/search2.png)|Pass|Works as expected|
|23|Recipe page|search for a keyword that should return multible results|Display multiple recipe cards|!![search](/assets/screenshots/search3.png)|Pass| Works as expectd|
|24|My recipes Page|Click the delete recipe button and click ok button |modal should pop uo and ask for confirmation. Once ok is pressed recipe is deleted from the database and my recipe page reloads without the recipe|![deleted](/assets/screenshots/deleted.png)|Pass|Works as expected|
|24|My Recipes Page|Click the edit recipe button|Edit recipe page loads and populated with the recipe data|![edit recipe](/assets/screenshots/edit.png)|passed|works as expected|
|25|Add recipe|Fill out add recipe form correctly and submit to website|form submits <br><br>flashes a Confirmation message|![recipe added](/assets/screenshots/recipeadded.png)|passed|Worked as expected|

# Further Testing <a id="further"></a> 
## Further Testing <a id="ftesting"></a>

I have tested my project on a variety of browsers such as:
  ### Google Chrome 

  ![Screen shot of Google Chrome](/assets/screenshots/Homepage.png)


  ### Firefox 
  ![Screen shot of Firefox Browser ](/assets/screenshots/firefox.png)


  ### Safari

  ![Screen shot of Safari](/assets/screenshots/safari.png)
  
  
I have also tested it on a range of devices such as:
  * Iphone 6
  * Iphone S
  * Laptop 
  * Desktop
  * Huawei T10 tablet

I have used the Chrome developer tools to test responsiveness on different device simulations and asked my friends and family to visit the website, sign up, create recipes and report any problems they encounter. 

# Bugs 
- cusine in catergories not displaying properly - fixed

# known bugs
- User admin check boxes not click able 
- edit form ingrendents and instructions does not display correctly