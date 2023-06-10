# Motivate Fitness
This is an appoinment booking application for an online personal training service.

You can visit the live site [here](https://pt-booking.herokuapp.com/)

![Am I Responsive](static/readme/amiresponsive.JPG)

## Contents
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [Wireframes](#wireframes)
    - [Database](#database)
    - [Design](#design)
- [Features](#features)
    - [Existing Features](#existing-features) 
    - [Future Features](#future-features)
- [Technologies](#technologies)
    - [Languages and Frameworks](#languages-and-frameworks)
    - [Technologies Used](#technologies-used)
    - [Libraries](#libraries)
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Lighthouse Testing](#lighthouse-testing)
    - [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

### **Agile Methodology**
#### **GitHub Project Board**

* This project was made using agile methodologies. Epics, user stories, bugs and issues are recorded on the [Project Board](https://github.com/users/HPCarey/projects/4/views/1)

![Screenshot of project board](static/readme/project_board2.png)

![Sprint 2](static/readme/project-board-sprint-2.png)

[Back to top](#contents)

## **User Experience**
### **User Stories**
* Epics, site user stories and admin user stories can be seen on the [project board](https://github.com/users/HPCarey/projects/4/views/1)

[Back to top](#contents)


### **Wireframes**
Wireframes were created using Balsamiq.

See [Wireframes.](static/readme/pt-booking-app.pdf)

![Landing page](static/wireframes/landing_page.png)
![Registration Page](static/wireframes/registration_page.png)
![Booking Page](static/wireframes/booking_page.png)
![Sign-in Page](static/wireframes/sign_in_page.png)
![User Profile](static/wireframes/user_profile.png)


[Back to top](#contents)

### **Database**
[Lucid chart](https://www.lucidchart.com/pages/) was used to make the entity relationship diagram showing my custom models and the user model which is built with Django AllAuth. Lucid chart was also used to make the flow chart mapping out the user journey throuh the site. 

![Flow Chart](static/readme/flow_chart_final.png)

![Database](static/readme/entity_relationship_diagram_final.png)

[Back to top](#contents)
### **Design**
#### **Typography**
* [Font awesome](https://fontawesome.com/)
* I used [figma](https://www.figma.com/file/RgYErSjELw326fP4MH6jt4kT/Nunito-Pairings/duplicate?node-id=1%3A198) to check what fonts pair well with Nunita and ended up going with Roboto.

#### **Images**
 
* Hero Images were taken from 
    * [Pexels](https://www.pexels.com/photo/man-working-out-2294361/)

#### **Colour Scheme and Accessibility**
 * First I uplaoded the hero image to [colormind](http://colormind.io/image/)to generate a few different palettes.

 * Input these hex values into the contrast grid on [Eightshapes](https://contrast-grid.eightshapes.com/) to check the WCAG 2.0 minimum contrast scores which helped me to pick a background and foreground colour that meet the accessibility requirements for good UX.


 ![Hero image](static/images/hero-image-guy-2.jpg)

 ![Colour Palette](static/readme/colormind.png)

 ![Colour Grid](static/readme/contrast_grid.png)


[Back to top](#contents)
## **Features**
### **Existing Features**
### **logo**
* Logo provided by site owner for his business
![logo](static/images/logo_original.jpeg)
#### **Navigation Bar**
* The navigation bar is featured on all pages of the site. 
* The Login link changes to Logout depending on user authorisation.
* The account link takes you to the login page.
* When user is logged in, the account link becomes a my profile dropdown menu giving logged in users access to their booking information via the user profile page and a logout link. 
* The logo acts as a home link as well as the home-nav link.
* The nav bar is fully responsive using bootstrap and becomes collapsable for mobile and tablet.

![Navbar desktop]()

![Navbar mobile expanded]() 

![Navbar mobile collapsed]()



[Back to top](#contents)

#### **Landing page**
* The landing page features the hero image.
* There is also a text overlay on the hero image with a call to action "Book Now!" button, as well as a short description of what's on offer.
* The book now button takes authorised user's to the booking form, but unauthorised user's are directed to the login form.

![landing](static/images/readme_images/)

#### **Footer**
* The footer contains links social media as well as copyright information.


![Footer](static/images/readme_images/footer.jpg)

[Back to top](#contents)
#### **Login Page**
* The login page was built using Django AllAuth. 
* I imported the template and gave it some basic styling using bootstrap. I also extended my base template so the user stays on the page when logging in and changed the text.
* The login page contains a link to the sign-up page so new users can register their accounts.

![Login](static/images/readme_images/login.jpg)

[Back to top](#contents)
#### **Sign Up Page**
* The sign up page is also from the authentication module allauth. 
* I imported the template and gave it some basic styling using bootstrap.
* Once signed up the user is redirected to the home page.

![Sign up](static/images/readme_images/sign_up.jpg)

[Back to top](#contents)
#### **Booking Page**
* The place booking page is only accessible when logged in. If you are not logged in you will get redirected to the login page instead.
* The form contains all the necessary fields for the trainer to prepare for the consultation.
* The datepicker is the standard HTML element for picking dates. 
* In the model, there is a function to validate that the booking can't be done on a date in the past. 
* In the form itself there is also a validation that disables dates that are closer than two days in the future. 
* There is also a limit that you can't book more than 60 days in advance

![Place booking](static/images/readme_images/)


[Back to top](#contents)

#### **User Profile**
* A page where the user can view their upcoming appointments with the trainer.
* There is a cancel and change button for each appointment that takes the user to a new page to complete either of those actions. 


![Edit Bookings](static/images/readme_images/)

* When the user clicks "change" they are brought to a change appoinmtent form, which shows the date

![Cancel Bookings](static/images/readme_images/)

* When a user tries to cancel a booking, they are taken to a confirmation page first and aske dto press the cancle button to confirm delete.



[Back to top](#contents)

#### **Admin**
* The trainer/admin can view, edit and delete all bookings via the admin panel.
* They can view relevant information regarding the clients gender, health conditions and goals so that they can prepare for the pt session.
* They can  also add appointments in the case that an appointment is made over the phone or via social media messaging apps. 
* The trainer also has the ability to confirm a booking.

![Admin panel](static/images/readme_images/)

[Back to top](#contents)


### **Future Features**
* For now the client only wants a simple promotional site with a call to action in order to attract potential clients, but in the future as their online clientele grows, the site could feature a services/programmes section which could detail various packages, services and price points.
* A personal information section in the profile UI that clients can update and edit in order to communicate there need and changing circumstances with trainers. 
* An onsite payment system using stripe so that the trainer can take payments upfront for consultations, programmes and online one-to-one training sessions.
* A UI for the trainer which would allow them to manage bookings without having to go through the django admin panel.
* Email confirmation of confirmed appointments and for the registration process.
* A link to goodle calendar API to help users and admin keep track of appointments outside the app. 

[Back to top](#contents)
## **Technologies**
### **Languages and Frameworks** 
* [Django](https://www.djangoproject.com/) 
* [Bootstrap](https://getbootstrap.com/)
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS) 
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

[Back to top](#contents)

### **Technologies Used** 
* [Gitpod](https://gitpod.io/)
* [Balsamiq](https://balsamiq.com/) 
* [Cloudinary](https://cloudinary.com/) 
* [Heroku](https://dashboard.heroku.com) 
* [ElephantSQL](https://www.elephantsql.com/)
* [PEP8 Validation](http://pep8online.com/)
* [HTML Validation](https://validator.w3.org/)
* [CSS Validation](https://jigsaw.w3.org/css-validator/) 
* [JSHint Validation](https://jshint.com/) 
* [Lucid chart](https://www.lucidchart.com/pages/)
* [Font awesome](https://fontawesome.com/)
* [Pairfonts](https://pairfonts.com/)
* [Google fonts](https://fonts.google.com/)
* [Balsamiq](https://balsamiq.com/wireframes/)
* [Github](https://github.com/)
* [Gitpod](https://gitpod.io/)
* [Tiny PNG](https://tinypng.com/)
* [Pixabay](https://pixabay.com)
* [Unsplash](https://unsplash.com)
* [Pexels](https://www.pexels.com)
* [Eightshapes](https://contrast-grid.eightshapes.com/)
* [rgbacolorpicker](https://rgbacolorpicker.com/hex-to-rgba)
* [Am I responsive](https://ui.dev/amiresponsive)


[Back to top](#contents)
### **Libraries**
The following libraries are used in the project and are located in the requirements.txt file.

## **Testing**
The testing documentation can be viewed [here](/TESTING.md)

[Back to top](#contents)

## **Bugs**

* I have recorded details of bugs and solutions in the project boars user stories:
[Project Board](https://github.com/users/HPCarey/projects/4/views/1)


[Back to top](#contents)
## **Deployment**

### Steps to deploy:

#### **Gitpod**
This project was created using the Code Institute
1. Create a repository in github using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template). 
2. Click Use this Template and add a repository name.
3. Click Create Repository from template
4. Install Django and the rest of the libraries listed in the libraries section. 
5. Freeze requirements using: pip3 freeze --local > requirements.txt
6. Create the project:(django-admin startproject motivatefitness .  )
    - Note the '.' at the end to ensure we don't need to cd into the app every time.
7. Create the booking app: (python3 manage.py startapp booking)
8. Add project to INSALLED_APPS
9. Migrate changes and run server locally to check it's working

#### **ElephantSQL**
Before deploying to heroku, an external database was created to host the app data.
1. Create an [ElephantSQL](https://www.elephantsql.com/) account. Code Institute provides the steps to do that [here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up).
2. Click the green "Create New Instance" button.
3. Set your plan to Tiny Turtle (Free) and give it a name.
4. Select a data centre near you and click review.
5. Check the details are correct and click create instance.
6. Return to the ElephantSQL dashboard and select the newly created database instance.
7. Copy the database URL using the copy icon. 
8. Add this database url to your env file.
9. Later you will also add this url to your Heroku Config Vars.

#### **Environemental variables and settings.py**
1. Create the env.py file in the top level directory.
2. Import os library and set the database url and a secret key variables.
        - The database is your ElephantSQL URL
        - The secret key you can make up or use a [generator](https://djecrety.ir/)
3. In settings.py, point to the env.py for the local server:

    ![settings](static/readme/deployment/import_env.JPG)
4. Remove the automtic django secret key and get it from the env.py.
![secret](static/readme/deployment/hide_secret.JPG)
5. Comment out the old DataBase section and replace it with the one below.
![database](static/readme/deployment/db_url.JPG)
6. Save all files and makemigrations.
7. Set up Cloudinary to store the static and media files.
8. Add cloudinary url to env.py file.
9. Add 'cloudinary_storage', to INSTALLED_APPS, in settings.py, above 'django.contrib.staticfiles',.
10. Then add'cloudinary', underneath  'django.contrib.staticfiles',.
11. In settings.py, under the Static files, add the code to tell Django to use cloudinary to store media and static files. 
    ![](static/readme/deployment/static_instructions.JPG)
12. Link files to the templates directory in settings.py underneath the BASE_DIR. 
![templates](static/readme/deployment/templates_dir.JPG)

13. Change the templates directory to TEMPLATES_DIR. 
![templates2](static/readme/deployment/templates_dir_2.JPG)

14. Add the heroku hostname (herokuappname.herokuapp.com)to ALLOWED_HOSTS along with localhosts. 
    - I have added the specific local host url instead of 'localhost' because at some point, it stopped allowing this access to the local browser.
    - If you want to use the app and localhost is not working, then replace it with you local browser url. 
15. Create 3 new folders on the top level directory, named media, static and templates.
16. Create a Procfile and add web: gunicorn PROJ_NAME.wsgi
17. Check all migrations have been made, save and git add, commit and push.
18. App is ready for initial deployment to heroku.  

[Back to top](#contents)
#### **Heroku**
Initial deployment to heroku was done early with the intention of making the final deployment process more smooth.
1. Log in to [Heroku](https://www.heroku.com/).
2. From the dashboard, click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. Enter a name for the app and select your region.
4. Click Create App.                  
5. Find the Settings Tab and scroll down to Config Vars.
6. Click Reveal Config Vars.
7. Enter the key-value pairs for DATABASE_URL, SECRET_KEY and CLOUDINARY_URL.
7. As a temporary measure, set a key value of DISABLE_COLLECTSTATIC to 1, to be removed before final deployment.
8. Navigate to the Deployment tab and choose Github as the deployment method.
9. Search for the repo name and connect to the correct repository.
10. Scroll down and deploy branch.
11. Finally click the open app button once the build is finished.

#### **Final Deployment**
1. Set DEBUG to false.
2. Underneath DEBUG, set a variable called X_FRAME_OPTIONS to 'SAMEORIGIN' to allow browser to user summernote editor.
3. Save everything, git add, commit and push.
4. Got to Heroku config vars and remove the DISABLE_COLLECSTATIC key value pair.
5. Navigate to the deploy tab and follow the same steps as before to deploy.

[Back to top](#contents)


## **Credits**
I used the following resources to help me plan, build and fix bugs in my project.

### Design and UI sources
Hero Image
* [Taken from Pexels from Li Sun](https://www.pexels.com/@823sl/)
* [Set responsive background image using bootstrap](https://www.youtube.com/watch?v=aw2Zj7jXNcU&ab_channel=TechHub) : 


* [Responsive Background Images w/ Bootstrap 5 (in HTML/CSS)](https://www.youtube.com/watch?v=W87XNjvXiWw&ab_channel=ADesignerWhoCodes) 

* [Responsive Bootstrap Website Tutorial with Full Screen Landing Page](https://www.youtube.com/watch?v=Zn64_IVLO88&ab_channel=DrewRyan):
This video helped me to research project ideas

### Code Credits and Sources:
1. This project was created using the guidelines from the Hello Django and I think therefore I blog walkthrough projects and the django blog start files from Code Institute.

* [Starter Files](https://github.com/Code-Institute-Solutions/django-blog-starter-files)

2. The following tutorial was used as inspiration to plan my project.

* [Django Tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)

3. The following article helped me create the dropdown menu for the gender option in the appoinments model.
* [Stack Overflow](https://stackoverflow.com/questions/31130706/dropdown-in-django-model)

4. This tutorial helped with creating a template view for delete confirmation.
* [openclassrooms](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349788-delete-objects-safely-with-user-confirmation)

5. Sources used for the datetime picker UI
* [Stack Overflow](https://stackoverflow.com/questions/55404397/how-to-use-timeinput-widget-in-django-forms)
* [Stack Overflow](https://stackoverflow.com/questions/51022722/how-to-restrict-date-and-time-in-django-bootstrap-datetimepicker-plus)

### Code Institute project sources:
I'd also like to mention some of the projects of my fellow CI studens which helped me plan and execute parts of my project
* [NailsbyFaar](https://github.com/DOdrums/PortfolioProjectFour/tree/main/salon) by [Dirk Ornee](https://github.com/DOdrums)

* [Locksmith Booking](https://github.com/spangen87/locksmith-booking) by [spangen87](https://github.com/spangen87)
* [Sandra's Kitchen](https://github.com/devisis/sandras-kitchen) by [DevIsis](https://github.com/devisis)






[Back to top](#contents)
## **Acknowledgements**

To my mentor and everyone who offered advice and support on slack.