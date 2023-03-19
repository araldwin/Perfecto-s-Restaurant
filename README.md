# Perfecto's Restaurant

Perfecto's Restaurant is the restaurant that serves the most delicious and famous all over the world. where you can eat Brunch because it is open from 10:00am-10:00pm. you can book thru online to reserve a seat or table.

The purpose of this Portfolio Project #4(Full Stack Project), this is part of me achieving the Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).A Restaurant web page where Users can book or reserve a table.
![Image](static/images/readme/amiresponsive.png)

[View live website here](https://myrestaurant2023.herokuapp.com/)

## Table of content
1. [Project](#project)
   - 1.1 [Objective](#objective)
   - 1.2 [Site Users Goal](#site-user-goal)
   - 1.3 [Site Owners Goal](#site-owners-goal)
   - 1.4 [Project Management](#project-management)
2. [User Experience](#user-experience)
   - 2.1 [Wireframes](#wireframes)
   - 2.2 [User Stories](#user-stories)
   - 2.3 [Site Stracture](#site-structure)
   - 2.4 [Design](#design)
      - 2.4.1 [Typography](#typography)
      - 2.4.2 [Color scheme](#color-scheme)
3. [Features](#features)
   - 3.1 [Navigation bar](#navigation-bar)
   - 3.2 [Login](#login)
   - 3.3 [Register](#register)
   - 3.4 [Make a reservation](#make-a-reservation)
   - 3.5 [Reservation list](#reservation-list)
   - 3.6 [Update reservation](#update-reservation)
   - 3.7 [Cancel reservation](#cancel-reservation)
   - 3.8 [Hero section](#hero-section)
   - 3.9 [About section](#about-section)
   - 3.10 [Our menu section](#our-menu-section)
   - 3.11 [Footer](#footer)
 4. [Technologies Used](#technologies-used)
    - 4.1 [Languages](#langauges)
    - 4.2 [Frameworks, Toolkit & Software](#frameworks-toolkit-software)
    - 4.3 [Libraries](#libraries)
5. [Testing](#testing)
   - 5.1 [Code Validation](#51-code-validation)
   - 5.2 [Fixed bugs](#52-fixed-bugs)
   - 5.3 [Supported screens and browsers](#53-supported-screens-and-browsers)
   - 5.4 [Test cases](#54-test-cases)
   - 5.5 [Automation test](#55-automation-test)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Project
<hr>


### Objective
<hr>
Since I was a child, I love to cook and I learned this from my mother, I love to experiment with my dishes to have different flavors that are delicious. the idea of ​​the name Perfecto it is my grandfather's name which I love very much. and I want to build a restaurant one day with a variety of delicious dishes that are famous in different countries. this is my dedication to my grandfather and my dear mother.


### Site Users Goal
<hr>
This restaurant will provide a unique experience and taste to those who love to eat and try different cuisines.



### Site Owners Goal
<hr>
The purpose of the site owner is to deliver to users the website where they can eat Global Cuisine such as Japanese, Indian, German, American, and many others in this restaurant.



### Project Management
<hr>
I used a project board as instructed in the module tutorial, but I haven't practiced using it much and I don't know what I should put in it. and due to my lack of time to do this project I won't be able to use it much because I'm always in a hurry, but in the next projects and if it's my time to do it full time I'm sure I'll be able to use it more and I'll be able to use it right
### Github Project Board
<hr>

![Image](static/images/readme/githubprojectboard.png)


[Back to top](#table-of-content)

## User Experience
<hr>


### Wireframes
<hr>

 - I used balsamiq to create wireframes for my project.

   - [View wireframes here](https://balsamiq.cloud/s4lj2vf/pr3c5y)


### User Stories
<hr>

- as a Site User:
   - I can register an account so that I can book a reservation.
   - I can login to my account using username and password so that the system can authenticate me.
   - I can view the list of food menu so that i can decide what i want to eat and make a reservation.
   - I can book a reservation to the website so that it is easy and fast.
   - I can choose the time and date so that i can be sure that i have a table on that day and time.
   - I can enter how many people I am with so that there are many. they can prepare a big table for us.
   - I can leave a note on my reservation so that i can say what my request are.
   - I can see that my reservation is successful or valid so that i can make sure that i have a reservation.
   - I can see the list of my booking so that I can see its details in case I forget it.
   - I can update my booking in case I entered a wrong detail I can change it.
   - I can see the validation when I cancel my booking so I'm sure it's canceled.
   - I can logout to my account so that no one else can use my site using my details.

- as a Site Admin:
   - I can create, read, update and delete bookings/reservations so that I can manage my restaurant booking system
   - I can prohibit double booking so that our operation is not disturbed and other guests can book.


[Back to top](#table-of-content)

### Site Structure
<hr>
   
   - This website is divided into two parts, when the User is logged out and when the User is logged in. there is a slight difference here. that when the User is logged out it cannot book a reservation. but when the User is logged in User can book a reservation, view reservation, update, and cancel.

[Back to top](#table-of-content)

### Design
<hr>

- In the design of my website I chose an appropriate font-color and font-style that is clear and easy to read by the User.

  - ### Typography
   <hr>
   <details><summary>typography screen shot</summary>
      <p> <img src="static/images/readme/typography.png"></p>
      </details>
      In this project I used only two font-styles. it is the Phudu and the Open sans. I used Phudu mostly for headers and Open sans for paragraphs and so on. I want to use only simple fonts and easy to read by the User.
   
 
   - ### Color scheme
   <hr>
   <details><summary>color scheme screen shot</summary>
      <p> <img src="static/images/readme/perfectos-colorscheme.png"></p>
      </details>
      In this Perfecto's restaurant project I used #fffff, #0c0b09, #fea116 for the general font-color of the page and #d9ba85 for the hover links. i used #000000 for the background color of the spinner. I also used an rgb color like rgb(0, 0, 0) which is linear-gradient and transparent for the background of the navbar so that it looks nice and doesn't get in the way of the page when it is scrolled down. For the buttons I used the color #fea116, #ffb639 and #ffffff to match the color of my logo and the backgournd picture and #cda45e for the hover. I used the color #a40000 for validation in the log-in modal and registration-modal.

[Back to top](#table-of-content)

## Features
- ### A Simple, Easy to Remember URL:[Perfecto's Restaurant](https://myrestaurant2023.herokuapp.com/)
<hr>

### Navigation bar
- Here in the navigation bar there is a slight difference when the User is logged in or logged out. we can also see here the customize logo of Perfecto's Restaurant ang hom, about, menu, and book a reservation. 

*when logged out*
-  Here in screen shot of the navbar logout this is what we can see when a User is logged out, the images also show the appearance when desktop and mobile view.
   <details><summary>navbar logout screen shot</summary>
         <p align="center"> <img src="static/images/readme/navbar-logout.png">
         Desktop view
         </p>
         <hr>
         <p align="center"> <img src="static/images/readme/navbar-mobile-logout.png">
         <br>
         Mobile view
         </p>
         <hr>
         <p align="center"> <img src="static/images/readme/navbar-mobile-logout1.png">
         <br>
         Burger Menu
         </p>
   </details>

*when logged in*
-  Here in screen shot of the navbar login this is what we can see when a Users is logged in, the images also show the appearance when desktop and mobile view.
   <details><summary>navbar login screen shot</summary>
         <p align="center"> <img src="static/images/readme/navbar-login.png">
         Desktop view
         </p>
         <hr>
         <p align="center"> <img src="static/images/readme/navbar-mobile-login.png">
         <br>
         Mobile view
         </p>
         <hr>
         <p align="center"> <img src="static/images/readme/navbar-mobile-login1.png">
         <br>
         Burger Menu
         </p>
   </details>

*feature differences*
-  The feature difference is the image of **logged out** and **logged in** views, there is not much difference in its appearance except for LOGIN | REGISTER and BOOK A RERVATION on click. When the Users is logged in, this is what the Users will see that is different.
   <details><summary>login difference screen shot</summary>
         <p align="center"> <img src="static/images/readme/login-diff.png"></p>
         <p align="center"> <img src="static/images/readme/login-diff1.png"></p>
   </details>

- Its other difference is that when the Users is logged in, Users can make a reservation and view his reservation, update and cancel the reservation. and when the Users is logged out, the Users does not have access to view and make a reservation and see reservation... except for this Users can see the food menu to choose what the Users wants to eat before booking.

### Login

- I used a modal on my login page so it looks good and has an engaging and stylish design. The Restaurant Logo can be seen here and Users must login using their registered username and password.
   <details><summary>Login modal screen shot</summary>
         <p> <img src="static/images/readme/login-modal.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/login-mobile-modal.png"><br>Mobile view (320 x 480)</p>
   </details>

### Register

- I also used it on my registration page a modal to make it look nice and engaging.
   <details><summary>Register modal screen shot</summary>
         <p> <img src="static/images/readme/register-modal.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/register-mobile-modal.png"><br>Mobile view (390 x 844)</p>
   </details>

### Make a reservation

- In this page, I just made a simple and old style page because I have very little time to do my project due to my full time job. I just used a background to make it look nice.
   <details><summary>Make a reservation screen shot</summary>
         <p> <img src="static/images/readme/make-a-reservation-page.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/make-a-reservation-mobile-page.png"><br>Mobile view (390 x 844)</p>
   </details>

### Reservation list

- Similar to the make a reservation page it is simple and old style. Users can see what they have booked here. And on this page Users can update or cancel their bookings. But there is also a difference here in the feature when there is no book and when it is my book. See the difference in the screen shot below.
   <details><summary>No reservation listed screen shot</summary>
         <p> <img src="static/images/readme/reservation-list-empty-page.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/reservation-list-empty-mobile-page.png"><br>Mobile view (390 x 844)</p>
   </details>

   <details><summary>With reservation listed screen shot</summary>
         <p> <img src="static/images/readme/reservation-list-page.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/reservation-list-mobile-page.png"><br>Mobile view (390 x 844)</p>
   </details>

### Update reservation

- This page is just like make a reservation the look is simple old style. I could make it more beautiful and unique design but I really don't have enough time because of my work and responsibilities at home.
   <details><summary>Update reservation screen shot</summary>
         <p> <img src="static/images/readme/update-reservation-page.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/update-reservation-mobile-page.png"><br>Mobile view (390 x 844)</p>
   </details>

### Cancel reservation

- Here on the cancel reservation, I used a modal to view it interactively. I didn't change the style from bootsrap.
   <details><summary>Cancel reservation listed screen shot</summary>
         <p> <img src="static/images/readme/cancel-reservation.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/cancel-reservation-mobile.png"><br>Mobile view (390 x 844)</p>
   </details>

### Hero section

- Here in the Hero section I used a carousel to display different images as a background so that it is beautiful and engaging to look at. In the middle of this section Users can see the big title Welcome to Perfecto's to let the Users know that I am glad that the Users visit my webpage and see what is available in our restaurant.
below it, the Users will also see the ```view our menu``` buttons so that Users can easily see our food offerings.
   <details><summary>Hero section screen shot</summary>
         <p> <img src="static/images/readme/hero-section.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/hero-mobile-section.png"><br>Mobile view (320 x 480)</p>
   </details>

### About us section

- This is our about us section telling restaurant services we can offer.
   <details><summary>About us section screen shot</summary>
         <p> <img src="static/images/readme/about-us-section.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/about-us-mobile-section.png"><br>Mobile view (320 x 480)</p>
   </details>

### Our menu section

- This is our menu section, Users can see here the different food cuisine, the name, the rate, the description and the price. in rating the food at the moment users cannot rate it but it will be added later on in the future features of the project.
   <details><summary>Our menu section screen shot</summary>
         <p> <img src="static/images/readme/our-menu-section.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/our-menu-mobile-section.png"><br>Mobile view (320 x 480)</p>
   </details>

### Footer section

- In the footer, this is where Users can see the restaurant's social links. this is just a very simple footer
   <details><summary>Footer screen shot</summary>
         <p align="center"> <img src="static/images/readme/footer-section.png"></p>
         <hr>
         <p align="center"> <img src="static/images/readme/footer-mobile-section.png"><br>Mobile view (320 x 480)</p>
   </details>

## Future features

   1. In the login modal page, add a remember me box and forgot password?. Where the Users does not need to type again and again on his/her login page and it will login automatically. And in case the Users forgets his/her password the Users can restore it or create a new passwork to make his account more secure.
   2. In the Registration modal it is also necessary to add that when the Users register there is a confirmation email that will be sent to the Users email address to verify the Users who registered.
   3. In our menu section add a drinks menu the Users are able to rate the food by their own.
   4. Add Contact Us with map location of the restaurant section.
   5. Add more style to Make a reservation and update a reservation page.
   6. A photo gallery section.
   7. A comment ang rate us section.

[Back to top](#table-of-content)

## Technologies Used

### Langauges
   - [Python](https://www.python.org/)
   - [JavaScript](https://www.javascript.com/)
   - [HTML5]()
   - [CSS3]()
   - [ElephantSQL](https://www.elephantsql.com/)

### Frameworks Toolkit Software
   - [Am I Responsive](https://ui.dev/amiresponsive) - online tool used to create mockup to present responsive design of this project.
   - [Balsamiq](https://balsamiq.com) - design tool used for creating wireframes.
   - [Bootsrap 5](https://getbootstrap.com/) - a CSS framework and toolkit used for developing responsive and mobile-first websites.
   - [Canva](https://canva.com) - used to create the Perfecto's Restaurant logo.
   - [Chrome DevTools]() - used to inspect the rendered HTML (DOM) and network activity of my pages. Used to troubleshoot ad serving issues.
   - [Cloudinary](https://cloudinary.com) - a service that hosts image files in the project.
   - [Coolors.co](https://coolors.co) - used to create color palette.
   - [CSS Valitadtion](https://jigsaw.w3.org/css-validator/) - used to validate CSS code.
   - [Django](https://www.djangoproject.com/) - Python web framework used for this project.
   - [Fontawesome](https://fontawesome.com/icons/) - where i import font icons for this project.
   - [Favicon.io](https://favicon.io/favicon-generator/) - generator i use to create favicon for this project.
   - [Google Fonts](https://fonts.google.com) - where i import and use font-style for this project.
   - [Git](http://gitscm.com) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
   - [Gitpod](https://gitpod.io) - IDE used to code the project.
   - [GitHub](https://github.com) - GitHub is used to store the project's code after being pushed from Git.
   - [Heroku](https://heroku.com) - a container-based cloud Platform used to deploy, manage, and scale apps.
   - [HTML Validation](https://validator.w3.org/) -used to validate HTML code.
   - [JSHint Validation](https://jshint.com/)  - used to validate JavaScript code.
   - [Lighthouse]() - used to test site perfomance
   - [Visual Studio Code for Windows](https://code.visualstudio.com/) - IDE used to code the project.
   - [Unsplash](https://www.unsplash.com/) - for the webpage main background image.
   - [Windows Snipping Tool]() - used to save the screen shot.
  
### Libraries

   - [asgiref==3.6.0](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI. You can read more at https://asgi.readthedocs.io/en/latest/.
   - [cloudinary==1.32.0](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload and manage your cloud's assets.
   - [coverage==7.2.1](https://pypi.org/project/coverage/) - Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.
   - [dj-database-url==0.5.0](https://pypi.org/project/dj-database-url/0.5.0/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
   - [dj3-cloudinary-storage==0.0.6](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
   - [Django==3.2.18](https://www.djangoproject.com/download/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. 
   - [gunicorn==20.1.0](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
   - [Pillow==9.4.0](https://pypi.org/project/Pillow/) - Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors
   - [psycopg2==2.9.5](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
   - [pytz==2022.7.1](https://pypi.org/project/pytz/) - pytz brings the Olson tz database into Python. This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.
   - [sqlparse==0.4.3](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

[Back to top](#table-of-content)

## Testing

### 5.1 Code Validation
   - [JS Hint](https://jshint.com/) - used to check JavaScript codes.
      <details><summary>validation screen shot</summary>
            <p> <img src="static/images/readme/js_hint.png"></p>    
      </details>
      <hr>
   - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) - used to validate the project CSS codes.
      <details><summary>validation screen shot</summary>
            <p> <img src="static/images/readme/css_validation.png"></p>    
      </details>
      <hr>
   - [Nu Html Checker](https://validator.w3.org/nu/#textarea) - used to check the project html codes.
      <details><summary>validation screen shot</summary>
            <p> <img src="static/images/readme/html_checker.png"></p>    
      </details>
      <hr>

   - [Pylint]() - used to check the project python codes.
      <details><summary>LightHouse DevTools report screen shot</summary>
            <p> <img src="static/images/readme/pylint_checker.png"></p>    
      </details>
      <hr>
   
   - [DevTools lighthouse report]()
      <details><summary>LightHouse DevTools report screen shot</summary>
            <p> <img src="static/images/readme/lighthouse.png"></p>    
      </details>
[Back to top](#table-of-content)
      <hr>
### 5.2 Fixed bugs
-----
   ```
   var pagination = document.getElementById('pagination');
   var paginationElement = document.querySelector('.pagination');

   if (document.querySelectorAll('.card').length === 0 && paginationElement) {
   paginationElement.style.display = 'none';
   }

   ```
   <img src="static/images/readme/pagination-error-in-update-page.png">
   
   - to fix the bug:

   ```
   var paginationElement = document.querySelector('.pagination');
   var cardElements = document.querySelectorAll('.card');

   if (cardElements.length === 0 && paginationElement !== null) {
   paginationElement.style.display = 'none';
   }
   ```
-----
   - Food list not rendering to home page our menu section view.
   
   <img src="static/images/readme/food-not-rendering.png">
   
   - to fix this bug:

   <img src="static/images/readme/fix-food-not-rendering.png">
-----


[Back to top](#table-of-content)

### 5.3 Supported screens and browsers
- Supported browsers
   - Google Chrome
   - Microsoft Edge
   - Safari

- Supported screens
   - Such a viewport was obtained from the am i responsive website where it was used to have an appropriate size for responsive design.
   - Apple products:
      - iPad Pro = 1024x1366px
      - iPad and iPad Mini = 768x1024px
      - iPad Air = 820x1180px
      - iPhone 13 Pro Max = 428x926px
      - iPhone 13, iPhone 13 Pro, iPhone 12 Pro = 390x844px
      - iPhone X = 375x812px
      - iPhone 5 = 320x568
   - I used google developer tools to test the responsiveness of given iPad and iPhone devices.  

[Back to top](#table-of-content)

### 5.4 Test Cases
   #### Homepage - User Logged Out

| Test description | Status |
| :---: | --- |
| &check; | Clicking the Home button on the nav bar re-loads the home page |
| &check; | clicking the About button on the nav bar scrolls down to the About me section of the homepage |
| &check; | clicking the Menu button on the nav bar scrolls down to the Our menu section of the homepage |
| &check; | clicking the View our menu button on the hero section scrolls down to Our menu section of the homepage |
| &check; | clicking the Book a reservation button on the nav bar redirect to the add_reservation.html page but user can't see the booking form |
| &check; | clicking the Login here button on the add_reservation.html page drops the login modal |
| &check; | Clicking the Login button on the nav bar drops the login modal |
| &check; | Clicking the Register button on the nav bar drops the registration modal |
| &check; | The user could not see make a reservation button when clicking book a reservation button in the nav bar |
| &check; | The user could not see view my reservation button when clicking book a reservation button in the nav bar ||
| &check; | The user can see the list of food with food name, rate, description, and price in our menu section |
| &check; | Clicking the Twitter link in the footer area opens Twitter |
| &check; | Clicking the Facebook link in the footer area opens Facebook |
| &check; | Clicking the Instagram link in the footer area opens Instagram |
| &check; | Clicking the Tiktok link in the footer area opens Tiktok |

   #### Homepage - User Logged In

| Test description | Status |
| :---: | --- |
| &check; | Clicking the Home button on the nav bar re-loads the home page |
| &check; | clicking the About button on the nav bar scrolls down to the About me section of the homepage |
| &check; | clicking the Menu button on the nav bar scrolls down to the Our menu section of the homepage |
| &check; | clicking the View our menu button on the hero section scrolls down to Our menu section of the homepage |
| &check; | clicking the Book a reservation button on the nav bar drops down a list make a reservation and view resevation button |
| &check; | Log in button could not be seen by user and change it into Welcome, name of user and logout button |
| &check; | Clicking the Log out button on the nav bar redirect to home page |
| &check; | The user can see make a reservation button when clicking book a reservation button in the nav bar |
| &check; | The user can see view my reservation button when clicking book a reservation button in the nav bar |
| &check; | The user could not see view my reservation button when clicking book a reservation button in the nav bar |
| &check; | The user can see the list of food with food name, rate, description, and price in our menu section |
| &check; | Clicking the Twitter link in the footer area opens Twitter |
| &check; | Clicking the Facebook link in the footer area opens Facebook |
| &check; | Clicking the Instagram link in the footer area opens Instagram |
| &check; | Clicking the Tiktok link in the footer area opens Tiktok |

   #### Make a reservation page - User Logged In

| Test description | Status |
| :---: | --- |
| &check; | The user can view the add_reservation.html page book form |
| &check; | The user cannot reserve a table when the view book form is not filled up except for the note |
| &check; | When the user is trying to 'reserve table' without filling the form that is needed to be filled a message validation message shows up "Please fill out this field" |
| &check; | When the user 'reserve table' with the date from the past an error message will pop up "Book date cannot be in the past" |
| &check; | The user can only 'reserve table' a time between 10:00 to 19:00 or else error message will pop up "You can only reserve table between 10:00 to 19:00" |
| &check; | When the user 'reserve table' with the date from the past and the time is not restaurant opening hours both error message pops up |
| &check; | When the user 'reserve table' with more than maximum of no. of guest an error message shows up "Value must be less than or equal to 10" |
| &check; | When the user already have reservation on that date an error message will pop up "You have already reserved a table for this date." |
| &check; | When the user filled up a valid form and click 'reserve table' a success message validation shows up "Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!" |

   
   #### View my reservation page - User Logged In


| Test description | Status |
| :---: | --- |
| &check; | The user can view the reservation_list.html page |
| &check; | The user cannot view the pagination when the user doesnt book a reservation |
| &check; | When the user does have a reservation, user can view the pagination |
| &check; | When the user doesnt book a reservation yet the view is Reservation list empty |
| &check; | clicking update button opens the update_reservation.html page |

   #### Update reservation page - User Logged In

| Test description | Status |
| :---: | --- |
| &check; | The user can view the update_reservation.html page |
| &check; | The user cannot update the reservation when the view book form is not filled up except for the note |
| &check; | When the user is trying to 'update' without filling the form that is needed to be filled a message validation message shows up "Please fill out this field" |
| &check; | When the user 'update reservation' with the date from the past an error message will pop up "Book date cannot be in the past" |
| &check; | The user can only 'update reservation' a time between 10:00 to 19:00 or else error message will pop up "You can only reserve table between 10:00 to 19:00" |
| &check; | When the user 'update reservation' with the date from the past and the time is not restaurant opening hours both error message pops up |
| &check; | When the user 'update reservation' with more than maximum of no. of guest an error message shows up "Value must be less than or equal to 10" |
| &check; | When the user already have reservation on that date an error message will pop up "You have already reserved a table for this date." |
| &check; | When the user filled up a valid form and click 'update' a success message validation shows up "Reservation updated successfully. We will call back or send an Email to confirm your reservation. Thank you!" |

   #### Cancel reservation page - User Logged In

| Test description | Status |
| :---: | --- |
| &check; | The user can view the delete_reservation_modal.html |
| &check; | Clicking close button will redirect the user to reservation list page |
| &check; | Clicking cancel reservation button will throw a validation "Your reservation is successfully canceled." it will delete the reservation and redirect to reservation list page |

[Back to top](#table-of-content)

### 5.5 Automation test
#### The Total of this projects automation is 99%
   - To run the Automation test
      - change the database setting in settings.py into default database setting and uncomment the sql database
      - run `coverage run --source=book manage.py test` into the terminal

      <img src="static/images/readme/Screenshot 2023-03-19 224545.png">
-----
   - Coverage report
      - There are two ways to view the coverage report 
         1. Views into the terminal
            - type `coverage report` into the terminal
               <details><summary>coverage report screen shot</summary>
               <p> <img src="static/images/readme/Screenshot 2023-03-19 224545.png"></p>
               </details>
         2. Views into the html page
            - type `coverage html` into the terminal
            - type `python3 -m http.server` then select open browser
            - select htmlcov/
               <details><summary>coverage report in browser screen shot</summary>
               <p> <img src="static/images/readme/Screenshot 2023-03-19 225833.png"></p>
               </details>
-----
#### Automation cannot fixed/missing
   <details><summary>screen shot</summary>
   <p> <img src="static/images/readme/Screenshot 2023-03-19 230553.png"></p>
   <p> <img src="static/images/readme/Screenshot 2023-03-19 230625.png"></p>
   </details>

[Back to top](#table-of-content)

## Deployment

### Deplyoment to Heroku

This project is deployed on [Heroku](https://heroku.com), these are the steps:
   1. First create a new Github repository using the [Code institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
   2. Find in the middle of the page `Use this template` and click it, after clicking you will see the `Create a new repository` link. Ande select it.
   3. Enter your repository name and click `create a repository from template` at the bottom of the page.
   4. After creating a new repository. press the green `gitpod` button. to open the Gitpod editor.
   5. In IDE(integrated development environment)  you need to install the following libraries for this project.
      - ```pip3 install 'django<4' gunicorn```
      - ```pip3 install dj_database_url==0.5.0 psycopg2```
      - ```pip install dj3-cloudinary-storage```
      - ```pip install Pillow```
   6. After installing the libraries. you need to create a requirements.txt file.
      - ```pip3 freeze --local > requirements.txt```
      
   7. After installing your necessary libraries, now you can start and create a project . to create a project type this:
      - ```django-admin startproject name_of_project```
   8. Next to this is the creation of apps.
      - ```python3 manage.py startapp name_of_app```
   9. Remember that for each app you need to put it in the settings of your project inside the INSTALLED_APPS list.
      - in my project i made two apps it is **book** and **food**.
         <details><summary>installed apps screen shot</summary>
         <p><img src="static/images/readme/installed-apps.png"></p>
         </details>
   10. The next thing you need to do is to migrate the changes to the database. You also need to migrate every time you have new apps or there is a changes in your app models.
      - ```python3 manage.py migrate```
   11. Now you can run your project using ```python3 manage.py runserver```.
   12. Next step is to **_create your [Heroku](https://heroku.com) app_**. Log into [Heroku](https://heroku.com) and go to the dashboard.
         <details><summary>Creating Heroku app process</summary>
         <br>
         <p>1. Click "New"</p>
         <img src="static/images/readme/Screenshot 2023-03-13 153504.png">
         <br>
         <p>2. Click "Create new app"</p>
         <img src="static/images/readme/Screenshot 2023-03-13 153724.png">
         <br>
         <p>3. Give your app a name and select the region closest to you. When you're done, click "Create app" to confirm. Heroku app names must be unique. If yours isn't, Heroku will give you a warning</p>
         <img src="static/images/readme/Screenshot 2023-03-13 153840.png">
         </details>
         <hr>
   13. Next step is to **_[create your database](https://www.elephantsql.com/)_**. These steps will create a new PostgreSQL database instance for use with your project.
       The database provided by Django is only accessible within Gitpod and is not suitable for a production environment. Your deployed project on Heroku will not be able to access it. So, you need to create a new database that can be accessed by Heroku.
        > If you don't have an ElephantSQL.com account yet, the [steps to create one are here](https://www.elephantsql.com/).
        <details><summary>Create a database process</summary>
         <br> 
         <p>1. Log in to your ElephantSQL.com to access your dashboard</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160953.png">
         <br>
         <p>2. Click “Create New Instance”</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160244.png">
         <br>
         <p>3. Set up your plan. Give your plan a Name (this is commonly the name of the project). Select the Tiny Turtle (Free) plan. You can leave the Tags field blank<p>
         <img src="static/images/readme/Screenshot 2023-03-13 160411.png">
         <br>
         <p>4. Select "Select Region"</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160450.png">
         <br>
         <p>5. Select a data center near you</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160643.png">
         <br>
         <p>6. Then click “Review”</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160726.png">
         <br>
         <p>7. Check your details are correct and then click “Create instance” </p>
         <img src="static/images/readme/Screenshot 2023-03-13 160914.png">
         <br>
         <p>8. Return to the ElephantSQL dashboard and click on the database instance name for this project</p>
         <img src="static/images/readme/Screenshot 2023-03-13 160209.png">
         <br>
         <p>9. In the URL section, click the copy icon to copy the database URL</p>
         <img src="static/images/readme/Screenshot 2023-03-13 161050.png">
         </details>
         <hr>
   14. Next step is you need to **_create an env.py file_** to keep things secret.There are a variety of variables that we don’t want to publish in your repository. In fact if you do, you may get an email from GitHub warning our about an exposed secret. To ensure your application works properly when deployed, you need a way to provide these variables without exposing them to the public.
         <details><summary>Create an env.py file process</summary>
         <br> 
         <p>1. In your project workspace, create a file called env.py. </p>
         <img src="static/images/readme/Screenshot 2023-03-13 164003.png">
         <br>
         <p>2. Add the following line of code.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 164525.png">
         </details>
   - In the code above set **environment variables** then set a **DATABASE_URL** variable, with the value you just copied from ElephantSQL as follows 
      > Replace **copiedURL** with the relevant string from ElephantSQL.
   - As this is a Django application it has a **SECRET_KEY**, which it uses to encrypt session cookies. The secret key can be whatever you like.
      > Replace **secretKey** with your key.
   - Make sure you **save** the file.
   15. Next step is you need to make some **_changes to your settings.py file_**.
         <details><summary>Modifying settings.py process</summary>
         <br> 
         <p>1. Now you have created an env.py file, you need to make your Django project aware of it. Open up your settings.py file and add the following code below your Path import</p>
         <img src="static/images/readme/Screenshot 2023-03-13 172638.png">
         <br>
         <p>The if statement here acts as a little protection for the application in case you try to run it without an env.py file present. You will use the other import in a moment.</p>
         <br>
         <p>2. A little further down, remove the insecure secret key provided by Django. Instead, we will reference the variable in the env.py file, so change your SECRET_KEY variable to the following:</p>
         <img src="static/images/readme/Screenshot 2023-03-13 172744.png">
         <br>
         <p>3. Now that is taken care of, we need to hook up your database. We are going to use the dj_database_url import for this, so scroll down in your settings file to the database section. Comment out the original DATABASES variable and add the code below, as shown</p>
         <img src="static/images/readme/Screenshot 2023-03-13 172835.png">
         <br>
         <p>4. With those changes in place, make sure to save your file. Your application will now connect to your remote database hosted on ElephantSQL. Run the migration command in your terminal to migrate your database structure to the newly-connected ElephantSQL database.</p>
         </details>
         <hr>
   16. Next step is to connect your app to [Cloudinary](https://cloudinary.com/).
         > if you don't have account [Cloudinary](https://cloudinary.com/), you may click the link to create an account.
         <details><summary>Connecting Cloudinary app process</summary>
         <br> 
         <p>1. Go to your Cloudinary dashboard, go to more info and click copy API Environment variable, you will use this to connect our app to Cloudinary.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 181707.png">
         <br>
         <p>2. Now go back to env.py file and add another line at the bottom. Set the CLOUDINARY_URL, and then paste in the value that you copied. see image below:</p>
         <img src="static/images/readme/Screenshot 2023-03-13 182805.png">
         <br>
         <p>3. Then proceed to your project settings and add "cloudinary_storage" and "cloudinary" apps in INSTALLED_APPS like the image below: </p>
         <img src="static/images/readme/installed-apps.png">
         <br>
         <p>4. You need to store your media and static files down near the end of your settings.py file and add few lines, see image below:</p>
         <img src="static/images/readme/Screenshot 2023-03-13 184531.png">
         <br>
         <p>5. Back up to the top of settings.py and under the base directory add in the template directory.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 185011.png">
         <br>
         <p>6. Then scroll down to midway in settings.py file and change the DIRS key, like the image below.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 185335.png">
         </details>
         <hr>
   17. Now you need to connect your [Heroku](https://heroku.com) app to your database.
         <details><summary>Connecting Heroku app to database process</summary>
         <br> 
         <p>1. Go back to the Heroku dashboard open the Settings tab.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 174134.png">
         <br>
         <p>2. Go to Reveal Config Vars.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 174506.png">
         <br>
         <p>3. Add 5 config vars: DATABASE_URL, SECRET_KEY, CLOUDINARY_URL, PORT, DISABLE_COLLECSTATIC.</p>
         <p>DATABASE_URL, and for the value, copy in your database URL from ElephantSQL, no need to add quotation marks.</p>
         <p>CLOUDINARY_URL, and for the value, copy in your API Environment variable URL, remove the "CLOUDINARY_URL=" written in from of the url.</p>
         <p>SECRET_KEY containing your secret key.</p>
         <p>DISABLE_COLLECSTATIC, and for the value is set to 1, don't forget to remove this when it comes to deplyoment of full project.</p>
         <p>PORT, with the value of 8000.</p>
         <img src="static/images/readme/Screenshot 2023-03-13 174858.png">
         <br>
         <p>4. After that add Heroku host name into "ALLOWED_HOSTS" in your settings.py file, and this is your Heroku app name followed by herokuapp.com and add `localhost` too, to run locally. see the image below</p>
         <img src="static/images/readme/Screenshot 2023-03-13 190225.png">
         </details>
         <hr>
   18. Now you can just create three directories, the directories you need are going to be media, static and template folders. and you can create these on the top level next to your manage.py file. 

   19. You also need to create procfile, Heroku needs this so that it knows hot to run the project. remember the capital P on Procfile. procfile is short for process file. you need to add your project name in here in my case it is "restaurant".
         <details><summary>Creating Procfile</summary>
         <img src="static/images/readme/Screenshot 2023-03-13 191210.png">
         </details>
         <hr>
   20. Now that's all done let's try deployment so save your files, add commit and push to our repository. And we're going to use Github as our deployment method here.
   21. So go back to your Heroku dashboard and click on the deploy tab. And click on Github for deployment method, you might need to connect your Github account.
   22. Then search the name of your repository, then scroll down to the bottom of the page and click on deploy branch.
   23. So when it says that the app has been deployed successfully. Click on [open app](https://myrestaurant2023.herokuapp.com/) to view it.

   [Back to top](#table-of-content)

## Credits

   - [Hello Django](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/) - code institute tutorial videos on how to do testing.
   - [I think therefore i blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) - code institute tutorial videos on how to do my project.
   - [Django Documentaion](https://www.djangoproject.com/) - to help me understand and solve some problems for my project.
   - [Codemy](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) - Youtube tutorials i used on how to build my project.
   - [W3C School](https://www.w3schools.com/django/django_collect_static_files.php) - helps me to solve some bugs and additional knowledge and understanding on my project journey. 
   - [Stack Overflow](https://stackoverflow.com/) - used to solve bugs, and learn to understand more about what the code does and how it works properly.
   - [Bootsrap made](https://bootstrapmade.com/) - template ideas to make my front end.
   - [Real python](https://realpython.com/) - used to understand and solve some problems for my project.
   - [Google images]() - were i got background photos for my project.
   - [Technology IT](https://www.youtube.com/watch?v=EI02wQ51GjA&list=PLBTOBXTz1YFZK0moSgoZq93V_AdvrUGSj&index=1) - Youtube tutorials i used on how to build my project.
   
   ## Acknowledgements

   - Mr. Rohit to my mentor
   - Student Support team
   - Slack community
   - Code institute

## Disclaimer
   - Perfecto's Restaurant was created for educational purpose only.
   
   [Back to top](#table-of-content)
   





   









