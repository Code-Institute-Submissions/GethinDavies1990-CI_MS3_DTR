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

