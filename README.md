# Binge Reviews Web Application
Binge Reviews is a website that allows users to add/edit/delete/view reviews for films, it also allows the user to rate a film with a start rating of 1-5.
<br>
<br><br>
![Responsive site example](binge_reviews/static/images/amiresponsive.jpg)


# Project Overview
- This project is a website that allows users to add/edit/delete/view reviews for films, it also allows the user to rate a film with a start rating of 1-5. This submission was created for milestone project 3 as part of the Code Institute - Diploma in Full Stack Software Development course.
- The repository on GitHub that contains the website source code and assets is available at this url: [Code Repository](https://github.com/GethinDavies1990/CI_MS3_DTR)
- The web application is built with a mobile first approach to allow for a responsive look and feel on all device types.
# UX
## Primary Goal
The primary goal of the website from the site owners perspective is:
- To create/edit/delete categories so users can add reviews to certain film genres.
- To allow users to add their own film reviews(review_image, film_name, review_title, category_name, review_description, created_by, rating, publish_date)
- To allow users to edit/update their own submitted reviews(film_name, review_title, category_name, review_description, rating)
- To allow users to delete their review
- To allow users to view reviews, and reviews submitted by other users

The primary goal of the website from a users perspective is:
- To allow users to add their own film reviews(review_image, film_name, review_title, category_name, review_description, created_by, rating, publish_date)
- To allow users to edit/update their own submitted reviews(film_name, review_title, category_name, review_description, rating)
- To allow users to delete their review
- To allow users to view reviews, and reviews submitted by other users
## Structure
I have structured the website into 18 pages, each with consistent styling throughout.

1. Home/Reviews: This is the landing page for the website.
2. Register: This page allows the user to register for the website and submit reviews. 
3. Login: This page allows users to login into the website
4. Profile: This page displays the users profile page.
5. Update profile: This page allows the user to edit their profile information.
6. Categories: This displays the categories page, this is only visible to an admin user to allow them to create/read/update/delete categories form the website. 
7. Add categories: This page allows the admin user to add more categories to the website
8. Edit Categories: This page allows the admin user to edit a category.
9. Add Review: This page allows the user to submit a review for a film.
10. Edit Review: This page allows the owner of a review to edit their review information. 
11. Delete Review: This button allows the user to remove their owned review from the website 
12. Reviews: This page displays all reviews submitted to the website. 
13. Review: This page displays the full review which has been submitted by a user. 
14. Error 400: This page is displayed to a user if they encounter an error 400
15. Error 404: This page is displayed if a user encounters a non existent url.
16. Error 401: This page is displayed if a user encounters an error 401
17. Error 405: This page is displayed if a user encounters an error 405
18. Error 500: This page is displayed if a user encounters an error 500

## Code Structure 
- My project was built using the Blueprints structure
- The blueprint structure is an object to structure a flask application into subsets. This helped keeping the site split into sections for organization and readability.
- This link here really helped me to understand how to structure my website using blueprints. https://realpython.com/flask-blueprint/
- The Project is structured as follows:
    - Authentication: Contains a flask route for authentication code, Register/Login/Profile etc.
    - Categories: Contains the routes for Adding categories, Edit Categories, and deleting categories. 
    - Errors: Contains the routes for error pages, 400, 401, 404, 405, 500
    - reviews: Contains the routes for the reviews code. add review, edit review, Delete review etc
    - Static
        - css( Styles css)
        - images ( images used in the project)
        - js ( Javascript used through the website)
    - Templates: includes all the templates structured into subset folders for each route. Authentication/Categories/Errors/Reviews.
    - Util: Code used to store the images in a AWS S3 bucket.
    - app.py: That sets and runs the application
    - a local env.py file, tha is not committed to source control - This ensures sensitive information is hidden in environment variables and never committed to repositories.

# Database 
- The website was built to be a data centric site, made with HTML, CSS, Javascript and the bootstrap framework was also used.
- The backend of the website consists of the Python language, The flask framework, Jinja templates and MongoDb was used to store the data.

## Database Model

The first step in setting up my database was to map out a conceptual data model. 

![Database Concept](binge_reviews/static/images/database-design/datebase-concept.jpg)

Once the concept data model was designed, I then created the physical database models within MongoDB

![Database Physical](binge_reviews/static/images/database-design/database-physical.jpeg)

## MongoDB Database information
- One production database was created (binge_reviews) and it contains 3 collections
    1. users
    2. reviews
    3. categories
- A model.py file is included in the binge_reviews/models file to display the structure of the database in the python code. 
- The databases were created manually in MongoDB at first
- I then installed MongoDB connection directly into my IDE editor. This allowed me to check any data being added nto the database very quickly as opposed to logging into the mongodb website database each time. 

## Users

- The users collection is used to store user information when they register.
The fields stored when they register are.
    - Username(string) username
    - Password(string)  password
    - First Name(String) first_name
    - Last Name(string) last_name
    - Favorite Film(string) fav_film
    - Author Bio(string) author_bio
    - Profile Image(String) profile_img
- Password - The users password is encrypted using a generate_password_hash from the werkzeug.security Python library.

![user Collection](binge_reviews/static/images/database-design/user-collection.jpg)

## Reviews

- The reviews is added by users of the website
- The fields stored in the collection are.
    - Review Image(string) review_image
    - Film Name(String) film_name
    - Review Title(string) review_title
    - Category Name(string) category_name
    - Review Description(string) review_description
    - Created by(string) created_by
    - Rating(Integer) rating
    - Publish Date(string) publish_date
![Review Collection](binge_reviews/static/images/database-design/review-collection.jpg)

## Categories
- The category information is added by the admin user only, i chose this decision to stop users added different variations of the same genre.
- The fields stored are
    - Category Name(string) category_name
![Categories](binge_reviews/static/images/database-design/category-collection.jpg)

# Amazon Web Services S3 Bucket
I decided to use the Amazon S3 bucket to store the images urls for the imagery uploaded by the user. I found this video very helpful to implement this https://www.youtube.com/watch?v=tSfdQJvTKmk&t=528s

The steps I made to implement this 
1. Created a AWS account and created an S3 bucket called binge-reviews
![S3 Bucket](binge_reviews/static/images/s3-bucket/s3-bucket.jpg)
2. I created a user in AWS IAM, and gave the user the AmazonS3FullAccess permission
3. I then gave the bucket policy the necessary permissions to allow my application to access the S3 bucket
![Bucket Permissions](binge_reviews/static/images/s3-bucket/s3-bucket-policy.jpg)
4. I imported the Boto3 python library (https://boto3.amazonaws.com/) in the util.py file I made a design decision to have an util.py in an util flask route python file that would be used to store code that could be used by multiple routes
5. I stored variables in the top of the util.py file <br>
<code>
s3_bucket_name = "binge-reviews"
s3_bucket_url = "https://binge-reviews.s3.eu-north-1.amazonaws.com/"
client = boto3.client('s3',
                      aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.environ.get(
                          "AWS_SECRET_ACCESS_KEY"))
</code>

6. A single function was written named upload_image that takes one parameter, the filename to store
7. This single function is used by the reviews, categories, authentication routes to store the images in the S3 bucket
8. This function stores a file in an AWS S3 bucket using boto3.
9. The boto3 put_object method is used to store the image taking two parameters, the file name and actual file <code> s3.Bucket(s3_bucket_name).put_object(Key=image_to_upload, Body=image)</code>
10. An image url is returned, and it is the image url that is stored in the mongodb for the relevant review, category or profile_img.
![Image URL](binge_reviews/static/images/s3-bucket/image-example.jpg)

# Scope

## User stories for site user

- User Story 1.1: As a regular user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices
- User Story 1.2: As a regular user the navigation item selected is highlighted
- User Story 1.3: As a regular user, when logged out, the home/landing page is the default page and there are three options with a logo, Home, Reviews, Login, Register displayed
- User Story 1.4: As a regular user, when logged in, the reviews page is the default page and there are six options with a logo: Home, Reviews, New Review, Log out, Profile
- User Story 2.1: As a regular user I can view the footers social icons(Twitter, facebook, instagram, pinterest, snapchat) and the relevant website opens in a new tab when clicked
- User Story 2.2: As a regular user I can view the websites terms and condition page by clicking on the link in the footer
- User Story 3.1: As a regular user I can view a hero image with latest reviews
- User Story 3.2: As a regular user I can view the latest reviews left by users
- User Story 3.3: As a regular user if I encounter an error with the application starting up I am navigated to a 500 error page
- User Story 3.4: As a regular user if I encounter an error when using the application(adding a review, category or registering), a message is displayed
- User Story 4.1: As a regular user I can register for an account by providing my username, password, first name, last name, favourite film and profile image, and I am redirected to the profile page.
- User Story 4.2: As a regular user my username must be a minimum of 5 characters, and a max of 25 characters.
- User Story 4.3: As a regular user my password must be a minimum of 8 characters.
- User Story 4.4: As a regular user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the users profile page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed
- User Story 4.5: As a regular user, when I am logged into the site, and I click Logout I am successfully logged out of the site, and brought to the home/reviews page, and the navigation bar is updated with three options with a logo, Home, Reviews, Login, Register
- User Story 4.6: As a regular user, when I am logged into the site, and I click the back button I am automatically redirected to the Login Page, and the navigation bar is updated with three options with a logo, Home, Reviews, Login, Register
- User Story 5.1: Add Review - As a regular user I can add a Review by adding a Film Name, Upload a Review Image, add a Review Title, Select a category for the film, add the review decription content, and rate the film out of 5.
- User Story 5.2: Add Review - As a regular user the review image I upload must be png or jpg format
- User Story 5.3: Edit Review - As a regular user I can edit a review by uploading a review image, updating the fFilm name, updating the review title, Updating the selected category, Updating the review description, and editing the rating.
- User Story 5.4: Delete Review - As a regular user I can delete a review I created by confirming I want to delete
- User Story 5.6: View Review - As a regular user I can view a review by clicking on the 'Full review' button
- User Story 5.7: Search - As a regular user I can search on text for the review name, film name. And the result will display those information
- User Story 6.1: As a regular user I can view my profile page: Username, First Name, Last Name, Favourite Film, and Author Bio.
- User Story 6.2: As a regular user I can update my profile password
- User Story 6.3: As a regular user I can update my profile details: Username, First Name, Last Name, Favourite Film 
- User Story 6.4: As a regular user I can delete my account. The user will be asked to confirm deletion of their profile. 

## User stories for site owner

The user stories overlap with regular users and admin users. The admin user does have rights to delete all reviews, add categories, delete categories. 

- User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices
- User Story 1.2: As an admin user the navigation item selected is highlighted
- User Story 1.3: As an admin user, when logged out, the home/landing page is the default page and there are three options with a logo, Home, Reviews, Login, Register displayed
- User Story 1.4: As an admin user, when logged in, when logged in, the reviews page is the default page and there are six options with a logo: Home, Reviews, New Review, Log out, Profile
- User Story 2.1: As an admin user I can view the footers social icons(Twitter, facebook, instagram, pinterest, snapchat) and the relevant website opens in a new tab when clicked
 User Story 3.1: As an Admin user I can view a hero image with latest reviews
- User Story 3.2: As an Admin  user I can view the latest reviews left by users
- User Story 3.3: As an Admin user if I encounter an error with the application starting up I am navigated to a 500 error page
- User Story 3.4: As an Admin user if I encounter an error when using the application(adding a review, category or registering), a message is displayed
- User Story 4.1: As an Admin user I can register for an account by providing my username, password, first name, last name, favourite film and profile image, and I am redirected to the profile page.
- User Story 4.2: As an Admin user my username must be a minimum of 5 characters, and a max of 25 characters.
- User Story 4.3: As an Admin user my password must be a minimum of 8 characters.
- User Story 4.4: As an Admin user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the users profile page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed
- User Story 4.5: As an Admin user, when I am logged into the site, and I click Logout I am successfully logged out of the site, and brought to the home/reviews page, and the navigation bar is updated with three options with a logo, Home, Reviews, Login, Register
- User Story 4.6: As an Admin user, when I am logged into the site, and I click the back button I am automatically redirected to the Login Page, and the navigation bar is updated with three options with a logo, Home, Reviews, Login, Register
- User Story 5.1: Add Review - As an Admin user I can add a Review by adding a Film Name, Upload a Review Image, add a Review Title, Select a category for the film, add the review decription content, and rate the film out of 5.
- User Story 5.2: Add Review - As an Admin user the review image I upload must be png or jpg format
- User Story 5.3: Edit Review - As an Admin user I can edit a review by uploading a review image, updating the fFilm name, updating the review title, Updating the selected category, Updating the review description, and editing the rating.
- User Story 5.4: Delete Review - As an Admin user I can delete a review I created by confirming I want to delete
- User Story 5.6: View Review - As an Admin user I can view a review by clicking on the 'Full review' button
- User Story 5.7: Search - As an Admin user I can search on text for the review name, film name. And the result will display those information
- User Story 6.1: As an Admin user I can view my profile page: Username, First Name, Last Name, Favourite Film, and Author Bio.
- User Story 6.2: As an Admin user I can update my profile password
- User Story 6.3: As an Admin user I can update my profile details: Username, First Name, Last Name, Favourite Film 
- User Story 6.4: As an Admin user I can delete my account. The user will be asked to confirm deletion of their profile. 
- User Story 7.1: As an Admin user I can delete reviews left by other users,
- User Story 7.2: As an Admin user I can delete categories I have created
- User Stories 7.3 As an Admin I can edit a category I have created

# Wireframes
## Desktop
<br>
<details><summary>Home</summary>
<img src="binge_reviews/static/images/wireframes/desktop/desktop - homepage.png">
</details>
<br>
<details><summary>Profile</summary>
<img src="binge_reviews/static/images/wireframes/desktop/desktop - profile.png">
</details>
<br>
<details><summary>Register</summary>
<img src="binge_reviews/static/images/wireframes/desktop/desktop - Register.png">
</details>
<br>
<details><summary>Review</summary>
<img src="binge_reviews/static/images/wireframes/desktop/desktop - review.png">
</details>
<br>

## Tablet 
<br>
<details><summary>Login</summary>
<img src="binge_reviews/static/images/wireframes/tablet/tablet - Login.png">
</details>
<br>
<details><summary>Profile</summary>
<img src="binge_reviews/static/images/wireframes/tablet/tablet - profile.png">
</details>
<br>
<details><summary>Register</summary>
<img src="binge_reviews/static/images/wireframes/tablet/tablet - register.png">
</details>
<br>
<details><summary>Review</summary>
<img src="binge_reviews/static/images/wireframes/tablet/tablet - review.png">
</details>
<br>

## Phone
<br>
<details><summary>Home</summary>
<img src="binge_reviews/static/images/wireframes/phone/phone - homepage.png">
</details>
<br>
<details><summary>Login</summary>
<img src="binge_reviews/static/images/wireframes/phone/phone - login.png">
</details>
<br>
<details><summary>Profile</summary>
<img src="binge_reviews/static/images/wireframes/phone/phone - profile.png">
</details>
<br>
<details><summary>Register</summary>
<img src="binge_reviews/static/images/wireframes/phone/phone - register.png">
</details>
<br>

# Colours
The colours chosen were to keep the design simple with a dark theme.

- #F01D7F - Hot pink for the logo, primary buttons, and outlines for elements
<details><summary>#F01D7F Image</summary>
<img src="binge_reviews/static/images/colours/pink.jpg">
</details>
<br>
- #000 - Background for the main pages and also background of review cards
<br>
<details><summary>#F000 Image</summary>
<img src="binge_reviews/static/images/colours/black.jpg">
</details>
<br>
- #28282B - This was used as the background colour of the secondary buttons.
<br>
<details><summary>#28282B Image</summary>
<img src="binge_reviews/static/images/colours/grey.jpg">
</details>
<br>
# Typography

Rubik was mainly used for the main headers of the website

![Rubik](binge_reviews/static/images/typography/rubik.jpg)

Poppins was used for the smaller headings and also the p and a tags

![Poppins](binge_reviews/static/images/typography/poppins.jpg)
<br>

# Features

## Feature 1 Navigation Bar

Description feature 1

- The navigation bar us displayed on all pages. The nav bar was made using bootstrap 5.3 and is responsive on all device sizes. On Tablet and mobile devices it transforms into a hamburger menu.

- When the user is not logged in, there are 5 navigation elements. The logo, 'Home', 'Reviews', 'Login' and 'Register'

- When the user is logged in there are 6 navigation elements. The logo, 'Home', 'Reviews', 'New Review', 'Log out' and 'Profile page' The profile page uses a google icon 'User' instead of text.

- When the admin user is logged in there are 7 navigation elements. The logo, 'Home', 'Reviews', 'New Review', 'Categories', 'Log out' and 'Profile page' The profile page uses a google icon 'User' instead of text.

- Only logged in users can make a review.

- Logged out users, can still see the reviews.

- The logout button once clicked redirects the user to the 'Home/index' page

### Nav Bar Logged out Desktop

![Nav Bar Desktop Logged Out](binge_reviews/static/images/features/nav/desktop-logged-out-nav.jpg)

### Nav Bar Logged In Desktop

![Nav Bar Logged In desktop](binge_reviews/static/images/features/nav/desktop-logged-in-nav.jpg)

### Nav Bar logged In Admin User

![Nav Bar Admin Logged in](binge_reviews/static/images/features/nav/desktop-logged-in-nav-admin.jpg)

### Nav Bar Logged out Tablet

![Nav Bar Logged Out tablet](binge_reviews/static/images/features/nav/tablet-logged-out-nav.jpg)

### Nav Bar Logged Out Tablet Expanded

![Nav Bar Logged Out expanded](binge_reviews/static/images/features/nav/tablet-logged-out-nav-expanded.jpg)

### Nav Bar logged In Expanded

![Nav Bar Logged in Expanded](binge_reviews/static/images/features/nav/phone-logged-in-nav-expanded.jpg)

### Nav Bar Logged In Phone

![Nav Bar Logged In Phone](binge_reviews/static/images/features/nav/phone-logged-in-nav.jpg)

### Nav Bar Logged Out Phone Expanded

![Nav Bar Logged Out expanded](binge_reviews/static/images/features/nav/tablet-logged-out-nav-expanded.jpg)

### Nav Bar logged In Phone

![Nav Bar Logged in Expanded](binge_reviews/static/images/features/nav/phone-logged-in-nav-expanded.jpg)

### User Stories Feature 1

- User Story 1.1: As a regular user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices
- User Story 1.2: As a regular user the navigation item selected is highlighted
- User Story 1.3: As a regular user, when logged out, the home/landing page is the default page and there are three options with a logo, Home, Reviews, Login, Register displayed
- User Story 1.4: As a regular user, when logged in, the reviews page is the default page and there are six options with a logo: Home, Reviews, New Review, Log out, Profile

## Feature 2 Footer

Description Feature 2

The footer is displayed on all pages of the website and has one section, I decided to only display one feature in the footer to keep the website clean and minimal.

1. Social Media Links

### Desktop Footer
![Desktop Footer](binge_reviews/static/images/features/footer/desktop-footer.jpg)

### Tablet Footer
![Tablet Footer](binge_reviews/static/images/features/footer/Tablet-footer.jpg)

### Phone Footer
![Phone Footer](binge_reviews/static/images/features/footer/phone-footer.jpg)

### User Stories Feature 2
- User Story 2.1: As an admin user I can view the footers social icons(Twitter, facebook, instagram, pinterest, snapchat) and the relevant website opens in a new tab when clicked

## Feature 3 Landing Page (Home)

### Description feature 3

The home page is displayed when the user accesses the website, on the homepage a 'Featured review' is present, this is the latest review published using the jinja for loop fucntion to loop through all the reviews, an 'If' statement is then nested to show the latest published review <br>
<code>{% for review in reviews|reverse %}<br>
        {% if loop.first %}<br>
        {% endif %}<br>
        {% endfor %}</code>






