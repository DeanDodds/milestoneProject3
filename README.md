# The Recipe App
Recipe app is a website dedicated to sharing delicious food. Everyone is welcome from beginner cooks to profeesional chef. Our aim is to build a community of foodies where we can share our recipe ideas with each
other. 

<a href="https://dean-milestone-project-3.herokuapp.com/">Go to live website.....</a>

<a href="https://dean-milestone-project-3.herokuapp.com/">![live website preview](/assets/screenshots/mockup.png)</a>
# Table of contents

1. [User Experience (UX)](#user-experience)
   - [User Stories](#user-stories)
   - [Design](#design)
   - [Wireframes](#wireframes)
2. [Features](#features)
   - [Future Features](#future-features)
3. [Technologies Used](#technologies)
   - [Langagues Used](#langagues)
   - [Frameworks, Libraries and Programs used](#frameworks)
   - [Data Modling](#data)
4. [Deployment](#deployment)
   - [Making a Local Clone](#clone)
   - [Forking the GitHub Repository](#fork)
5. [Credis](#credits)
   - [Images](#images)
   - [Code](#code)
6. [Acknowledgements](#acknowledgements)

# 1. User Experience (UX) <a id="user-experience"></a>

## User Stories <a id="user-stories"></a>

### First Time Visitor Goals
- As a first time visitor, I want to easily understand the purpose of the website.
- As a first time visitor, I want to eaily navigate through the website to find the information I want.
- As a first time visitor, I want to be able to view the website on all my devices.
-  As a first time visitor, I want to view recipes without logging in.
- As a first time visitor, I want to be able to create and acount easily if i want to. 

### Returning Visitor Goals
- As a returning visitor, I want to be able to easily log in to my account.
- As a returning visitor, I want to be able to add my own recipes to the website.
- As a returning visitor, I want to be able to save websites to my account.
- As a returning visitor, I want to be able to rate recipes.
- As a returning visitor, I want to be able to sign up to the newsletter and find out the latest information 
- As a returning visitor, I want to be able to find social media links to different platforms.


### Website Creator Goals
- As the website creator, I want to be able to advertise cooking products.
- As the website creator, I want to be able to edit and delete all recipes.
- As a website creator, I want to create a website that works on all platforms.
- As a website creator, I want to create a good user experience by having a clear navigation system.
- As a website creator, I want my website load times to be low. I do not want users leaving the site before it has time to load.
- As a website creator, I want my website to be as accesible as possible in order to be inclusive to all potenial users.


## Design <a id="design"></a>

### Typography

- Pacifico is the main font used for my logo with a Sans Serif fallback.
- Bitter is the main font used for all headers with a Sans Serif fallback.
- Open Sans is the font used for the main text area of the web appliction with a Sans Serif fallback. This compliments the Bitter font nicely.

### Colour theme

![Color palette 1](/assets/screenshots/colorpallete.jpeg)

## Imagery

- 1 X favicon

### Home page 

- 1 x hero image 

### Recipe page, profile and favourites
- 1 x hero image 
- 1 x default image incase user does not link an image to their recipe

### About page
- 1 x hero image 
- 4 x profile images for team members 

## Wireframes <a id="wireframes"></a>

The wireframes for the website were created on Drawio, there is a desktop, tablet and mobile wireframe for this website

- Home page laptop wireframe [View](/assets/wireframes/wireframes-home-page-laptop-and-tablet.drawio.png)
- Home page mobile wireframe [View](/assets/wireframes/wireframes-home-page-mobile.drawio.png)
- About page laptop wireframe [View](/assets/wireframes/wireframes-aboutus-page-laptop-tablet.drawio.png)
- About page mobie wireframe [View](/assets/wireframes/wireframes-aboutus-pape-mobile.drawio.png)
- Recipe laptop wireframe [View](/assets/wireframes/wireframes-recipe-page-laptop.drawio.png)
- Recipe tablet wireframe [View](/assets/wireframes/wireframes-recipe-page-tablet.drawio.png)
- Recipe mobile wireframe [View](/assets/wireframes/wireframes-recipe-page-mobile.drawio.png)
- Sign up page laptop wireframe [View](/assets/wireframes/wireframes-register-page-laptop.drawio.png)
- Sign up page mobile wireframe [View](/assets/wireframes/wireframes-register-page-mobile.drawio.png)
- Login page laptop wireframe [View](/assets/wireframes/wireframes-login-page-laptop.drawio.png)
- Login page mobile wireframe [View](/assets/wireframes/wireframes-login-page-mobile.drawio.png)
- Contact us laptop wireframe [View](/assets/wireframes/wireframes-contactus-page-laptop.drawio.png)
- Contact us mobile wireframe [View](/assets/wireframes/wireframes-aboutus-pape-mobile.drawio.png)

## Database modeling. <a id="data"></a>

I have modeled my database on a non-relational database system. I have used the Mongodb. I have used the following mapping 

![screenshot of data structure ](/assets/screenshots/diagram.png)

---

# 2. Features <a id="features"></a>

### Responsiveness

- Responsiveness on all device sizes.


### Navigation Bar 
All pages have a collapsible navigation bar, this makes it fully responsive on all devices.
- on larger screens 

![screenshot of laptop navbar ](/assets/screenshots/navbar.png)
- on smaller screens 

![screenshot of mobile navbar ](/assets/screenshots/navbarmobile.png)

### Footer
All pages have a responsive footer that contains links to social media and a sign up for the newletter form.
- on larger screens 

![screenshot of laptop footer ](/assets/screenshots/footer.png)
- on smaller screens 

![screenshot of mobile footer ](/assets/screenshots/footermobile.png)

### Sign up page 

a form to allow users to sign up for an accout 
![screenshot of the sign up page ](/assets/screenshots/signup.png)

### Login Page 
a form to allow users to log in to thier accout 
![screenshot of the log in page ](/assets/screenshots/login.png)

### Logout option
log out button in the navbar 
![screenshot of the log out button ](/assets/screenshots/navbar.png)

### Home page 
Home page will outline the purpose of the website to the user 

![screenshot of Home Page ](/assets/screenshots/Homepage.png)
---

### About page 
Will inform the user about the company and the team behind the website. Each team member will have there own card with a photo and a short bio.

![screenshot of About Page ](/assets/screenshots/about.png)

### Recipe page 
  The recipe page will show all recipes in the database. if the user is logged in they will be able to like the recipes and save them to thier favourites.

![screenshot of Recipe Page ](/assets/screenshots/profile.png)

### Profile page 
If a user is logged in they will be able to see the profile page. This page will allow users to view the recipes they have created, delete recipes they have created, and create new recipes.

![screenshot of profile Page ](/assets/screenshots/profile.png)

### Administration page
An admin page that allows admin to edit and delete user profiles and recipes
![screenshot of admin Page ](/assets/screenshots/adminpage.png)

### Contact us page 
Contact form allowing users to easily get in touch with any questions

 ![screenshot of Contact Page ](/assets/screenshots/contact.png)

 ### Add recipe page
 Form allowing users to add their own recipes 

 ![screenshot of add recipe form ](/assets/screenshots/addrecipe.png)

 ### Edit recipe page
 Form allowing users to edit their own recipes.
 
 ![screenshot of edit recipe Page ](/assets/screenshots/edit.png)

## Defensive Programing 

In order to protect my users data I have used some defensive programing. My application protects the data through:
1. Python functions that check:
 * to see if the user is signed in by checking user session cookies 
 * if a user is editing data. The function will check that the user who is signed in is the creater of the data or an admin user. <br> 

These steps help prevent the use of brute force.   

| ![brute force attempt](/assets/screenshots/bruteforce.png) |
|:--:|
| <b>screen shot showing an attempt to copy the delete recipe link when the user is not signed in</b>|

2. Using Jinga checks to hide links because:
* certain links are hidden if you are not logged in 
* admin pages can only be seen by users with admin privileges 

![log out user nav](/assets/screenshots/logoutnav.png) |
|:--:|
| <b>Users who are not logged in cannot see the profile page</b>|
 
![nav tabs](/assets/screenshots/admin.png) |
|:--:|
| <b>Screen shot showing that only admin users can see the control panel</b>|


# 3. Technologies Used <a id="technologies"></a>

## Langagues Used <a id="langagues"></a>

- <a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics">HTML5</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
- <a href="https://www.python.org/">Python</a>
- <a href="https://www.javascript.com/">JavaScript</a>


## Frameworks, Libraries and Programs used <a id="frameworks"></a>

- <a href="https://materializecss.com/">Meteralize:</a>
  Used for responsiveness and styling of the website.
- <a href="https://flask.palletsprojects.com/en/2.0.x/">Flask: </a>
  Used to build the application
- <a href="https://www.mongodb.com/">Mongodb: </a>
Used to store my database 
- <a href="https://werkzeug.palletsprojects.com/en/2.1.x/">Werkzeug: </a>
  Flask dependency, which is a utility library
- <a href="https://fontawesome.com/">Font Awesome:</a>
  Used to import icons that used across every page of the website.
- <a href="https://fonts.google.com/">Google Fonts:</a>
  Used to import Montserrat and Lora fonts.
- <a href="https://gitpod.io/">Gitpod: </a>
  Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- <a href="https://github.com/">GitHub:</a>
  Used to store the projects code once pushed from Gitpot.
- <a href="https://app.diagrams.net/">Drawio.net:</a>
  Used to create all wireframes.
- <a href="http://https://randomkeygen.com/">Randomkeygen:</a>
  Used to generate secure passwords.
- <a href="https://dashboard.heroku.com/apps">HEROKU:</a> Used to deploy the python app.
- <a href="https://www.photopea.com/">Photopea</a> Used to edit photos. 
- <a href="https://tinypng.com/">TinyPNG</a> Used to compress images. 

## Feature Features 
Feature features i would like to add are
* Cooking product advertising 
* Admin newsletter form 

---

# 4. Deployment <a id="deployment"></a>

# Github <a id=pages></a>

## Making a local clone <A id="clone"></a>

You can clone a Github repository to your local computer by following these steps:

1. On GitHub.com, navigate the repository page
2. Above the list of files, click on the Code dropdown menu
3. Select the download zip file 
4. Once the files have downloaded you can extract them form the zip file and run them on your local environment 

You can see more information on making local clones [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)

## Forking the GitHub Repository <a id="fork"></a>

Forking a Github repositary allows you to make a copy that you can work on without effecting the original repository. You can fork a repository by:

1. On GitHub.com, navigate the repository page of the repository you would like to fork
2. On the top right hand side of the page locate click fork button 
3. A copy of this resository should now be in your own repositories

## Setting up a mongodb database 

To create a mongodb database 
1. First you need to go to the <a href="http://mongodb.com">mongodb.com</a> and create an account.
2. Then you must create a cluster and give it a name - this is the cluster of service the data will run on. 
3. Next you need to select a cloud provider
4. Then select a region 
5. Select the network access 
6. Now you can create you database on the new cluster. To begin you select create your own data from the menu and give the database a name.
7. Create your collections
8. Lastly press the insert document button and add the fields and values into that     

## Environment variables and app set up

In order to connect you to the database and set up your python app you must set up a env.py file. This is a  file containing key value pairs of all the environment variables required to configure you application. This is then linked into you app.py file. 

| ![example env.py file](/assets/screenshots/examplleenv.png) |
|:--:|
| <b>example env.py file</b>|

## Deployment to a local server 

In order to text your website locally you can deploy it on a local server for testing purposes. To run your application on the local server you must run you app.py file in your terminal by using:
```
python3 app.py
```
This will deploy the app on a local port 8080. You can stop the app running by pressing control and c on mac or ctrl and c on windows. Close all ports by typing:
```
pkill -9 python3 
```
## Deploying a your Live Python app through HEROKU

Before you can set up a HEROKU app you must set up the following files:
- requirements.txt file - this tells HEROKU what dependencies are needed 
- a Procfile file - this specifies the commands that are executed by the app on startup
in you github repository.

1. To begin with HEROKU you must first create an account on the <a href="https://id.heroku.com/login">HEROKU website</a>
2. Once logged in, create a new app. When seleting the app name, keep in mind that it must be unique. Then select your region and create app.
3. Then select the deploy tab and scoll to the deployment method section. You can connect your app by either the HEROKU CLI or through Github. I selected GitHuB so I can use the automatic deployment feature 
4. Then go to the settings tab and set up you Congfi Vars. These variables will be the same as the ones in you env.py file 
5. You can then go back to the deploy tab and select automatic deployment 
6. Your site is now live    
------

# 6. Credits <a id="credits"></a>

## Images <a id="images"></a>
- Hero Image by Maarten van den Heuvel <a href="https://images.pexels.com/photos/2284166/pexels-photo-2284166.jpeg?cs=srgb&dl=pexels-maarten-van-den-heuvel-2284166.jpg&fm=jpg">Pexels</a>
- fivicon Icon made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- default Photo by Adonyi Gábor: https://www.pexels.com/photo/assorted-vegetables-on-brown-wooden-table-1414651/
- Team profile photo by Pixabay: https://www.pexels.com/photo/man-smiling-behind-wall-220453/
- Team profile photo Photo by Pixabay: https://www.pexels.com/photo/woman-wearing-black-spaghetti-strap-top-415829/

## Content 
- recipes - <a href="https://www.bbcgoodfood.com/">from BBC good food</a>

## Code <a id="code"></a>
- star rating html -<a href="https://www.codingnepalweb.com/star-rating-html-css-javascript/">CodeNepal</a>
- login, sign up and search bar from code institue mini project.
- box shadow taken from <a href="https://getcssscan.com/css-box-shadow-examples">Get Scan</a>

---

# 7. Acknowledgements <a id="acknowledgements"></a>
- Chris Quinn - My Mentor for continuous helpful feedback and advice.
- The Code Institute Slack Community.