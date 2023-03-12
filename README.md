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
5. [Flowchart](#flowchart)
6. [Technology](#technology)
7. [Testing](#testing)
   - 7.1 Code Validation
   - 7.2 Fixed bugs
   - 7.3 Test cases
8. [Deployment](#deployment)
9. [Credits](#credits)

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

*what feature differences*
-  The feature difference is the image of **logged out** and **logged in** views, there is not much difference in its appearance except for LOGIN | REGISTER and BOOK A RERVATION on click. When the Users is logged in, this is what the Users will see that is different.
   <details><summary>login difference screen shot</summary>
         <p align="center"> <img src="static/images/readme/login-diff.png"></p>
         <p align="center"> <img src="static/images/readme/login-diff1.png"></p>
   </details>

- Its other difference is that when the Users is logged in, Users can make a reservation and view his reservation, update and cancel the reservation. and when the Users is logged out, the Users does not have access to view and make a reservation and see reservation... except for this Users can see the food menu to choose what the Users wants to eat before booking.

[Back to top](#table-of-content)

### Hero section

- Here in the Hero section I used a carousel to display different images as a background so that it is beautiful and engaging to look at. In the middle of this section Users can see the big title Welcome to Perfecto's to let the Users know that I am glad that the Users visit my webpage and see what is available in our restaurant.
below it, the Users will also see the ```view our menu``` buttons so that Users can easily see our food offerings.
   <details><summary>hero section screen shot</summary>
         <p> <img src="static/images/readme/hero-section.png"></p>
   </details>

[Back to top](#table-of-content)


### About us section

- This is our about us section telling restaurant services we can offer.
   <details><summary>About us section screen shot</summary>
         <p> <img src="static/images/readme/about-us-section.png"></p>
   </details>

[Back to top](#table-of-content)

### Our menu section

- This is our menu section, Users can see here the different food cuisine, the name, the rate, the description and the price. in rating the food at the moment users cannot rate it but it will be added later on in the future features of the project.
   <details><summary>Our menu section screen shot</summary>
         <p> <img src="static/images/readme/our-menu-section.png"></p>
   </details>

[Back to top](#table-of-content)

### Footer section

- In the footer, this is where Users can see the restaurant's social links. this is just a very simple footer
   <details><summary>Footer screen shot</summary>
         <p align=center> <img src="static/images/readme/footer-section.png"></p>
   </details>

[Back to top](#table-of-content)





   









