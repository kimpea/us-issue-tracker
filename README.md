# Unicorn Simulator Issue Tracker

## UX

This web application is an issue tracker for an imaginary application called 'Unicorn Simulator'. It is designed to allow users to report any bugs they encounter within Unicorn Simulator, and also to request new features to be made by the development team. This application is specifically aimed towards the users of 'Unicorn Simulator' and would be of no use to any other type of target market. This type of user will want to be able to have their own account where they can report bugs, request features, upvote and comment on tickets. This user will also want to know the status of a reported bug or a requested feature. My project is a suitable way of achieving this because it provides a form for the user to use when signing in or registering onto the application, forms for users to report bugs and request new features, and functions which will allow the user to upvote bugs/features and write their own comments to contribute to the community.

General User Stories:

 - As a user type, I want to be able to create an account with my own username and password, and login with these credentials each time I want to access the application.
 - As a user type, I would like to be able to login and report a bug.
 - As a user type, I would like to be able to login and request a new feature.
 - As a user type, I would like to be able to upvote a bug.
 - As a user type, I would like to be able to upvote a feature and donate money towards the development process of this feature.
 - As a user type, I would like to be able to see a bug or feature's current status.
 - As a user type, I would like to be able to write comments on bugs and features.
 - As a user type, I would like to be able to visually see what progress has been made for reported bugs and requested features.

Real Life User Stories:

 - User 1: I'd like my username to be 'USER1' and would also like to have my own password when logging in.
 - User 2: I would like to be able to report a gameplay bug for Unicorn Simulator.
 - User 3: I would like to request a new gameplay feature to the developers.
 - User 4: I would like to upvote a bug which someone else has reported.
 - User 5: I would love to upvote a feature and donate some money to the developers to help them develop this feature.
 - User 6: I would like to see what bugs and features are being developed or have been completed.
 - User 7: I would like to comment on other users' reports and see if I also have the same issues as them.
 - User 8: Being able to visually see the progress made over certain periods of time would be a great advantage for this application.

Wireframes:

 - Wireframes have been created using Wireframe.cc. These can be viewed in [/documentation/wireframes](/documentation/wireframes/).

## Features

 - Login/Register form - this will allow the user to either log into an existing account or create a new account, inserting them into the database.
 - Report bug form - this will allow the user to report a bug, inserting this report into the database.
 - Request feature form - this will allow the user to request a new feature, inserting the form data into the database.
 - Upvote bug - this will allow the user to upvote a reported bug which is in need of attention.
 - Upvote feature (for price of £20 per upvote) - this will allow the user to upvote a requested feature whilst donating £20 towards the development process at the same time.
 - Comment form - this will allow users to comment on reported bugs and requested features and involve them in the community.
 - Log out - this will allow the user to log out of the current session.

### Existing Features

- Login/Register form - allows User 1 to have their username as 'USER1' and also their own password.
- Report bug form - allows User 2 to report a gameplay bug for Unicorn Simulator.
- Request feature form - allows User 3 to request a new gameplay feature to the developers.
- Upvote bug - allows User 4 to upvote someone else's bug.
- Upvote feature - allows User 5 to upvote a feature by paying £20 per upvote.
- Comment form - allows User 7 to comment on another user's report.
- Log out - allows all signed up users to log out after using the application (if they wish).

### Features Left to Implement
- Newsletter Subscription - there is currently a form present within the application for newsletter subscriptions, however, there is no functionality to it yet, but may be implemented in future builds.

## Technologies Used

- HTML
    - This project uses **HTML** to build the foundation of the web application and includes links to Bootstrap 4, Bootstrap JS, CSS, and Font Awesome.
- CSS
    - This project uses **CSS** to style the features of the web application, including the header, footer and each page of the issue tracker. It is also used to modify Bootstrap 4 styles.
- [JavaScript](https://www.javascript.com/)
    - This project uses **JavaScript** to provide the functionality for the Stripe API and for the back-to-top button.
- [Python](https://www.python.org/)
    - This project uses **Python** to provide the backend functionality of the issue tracker, including functions to report bugs and request features.
- [Django](https://www.djangoproject.com/)
    - This project uses **Django**, a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
- [Stripe](https://stripe.com/en-GB/)
    - This project uses the **Stripe** payment API, providing a secure payment form for the application.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Pygal](http://www.pygal.org/en/stable/)
    - This project uses **Pygal** charts to dynamically present data collected from the database.
- [Font Awesome](https://fontawesome.com/)
    - This project uses **Font Awesome** to provide icons for the application.
- [Wireframes.cc](https://wireframe.cc/)
    - This project uses **Wireframes CC** for the Skeleton and Surface Plan, providing desktop and mobile views of the web application.

## Testing

### Automated Testing

Within this application, 44 automated tests have been carried out using Django TestCase testing tools. All 44 tests have passed. From your command line, enter ```python3 manage.py test``` to run the tests. Tests can be found in the links below:

Accounts:
 - [test_forms.py](/accounts/test_forms.py)
 - [test_views.py](/accounts/test_views.py)

Bugs:
 - [test_forms.py](/bugs/test_forms.py)
 - [test_models.py](/bugs/test_models.py)
 - [test_views.py](/bugs/test_views.py)

Features:
 - [test_forms.py](/features/test_forms.py)
 - [test_models.py](/features/test_models.py)
 - [test_views.py](/features/test_views.py)

Home:
 - [test_forms.py](/home/test_forms.py)
 - [test_models.py](/home/test_models.py)
 - [test_views.py](/home/test_views.py)

Cart:
 - [test_views.py](/cart/test_views.py)

Checkout:
 - [test_forms.py](/checkout/test_forms.py)
 - [test_models.py](/checkout/test_models.py)
 - [test_views.py](/checkout/test_views.py)

### Manual Testing

Below are scenarios which a user may experience throughout navigating the website. These have been used to manually test the application's features.

1. Home
    1. Click on 'Home' in navigation bar
    2. Be directed to the home page

2. Register
    1. Click on 'Register' button in the navigation bar
    2. Fill in email address, username, password and password confirmation fields in the form
    3. If any fields are left empty, be presented with 'Please fill in this field.' tooltip.
    4. Once fields are filled in, click 'Register' button
    5. Be presented with 'You have successfully registered' message and also logged in

3. Login
    1. Click on 'Login' button in the navigation bar
    2. Fill in the login form with username and password
    3. Click on the 'Login' button
    4. Be presented with 'You have successfully logged in!' message

4. Logout
    1. Click 'Logout' button in the navigation bar
    2. Be redirected to the home page, and presented with a 'You have successfully logged out!' message

5. Profile
    1. When logged in, click 'Profile' in the navigation bar.
    2. Be directed to your profile page, displaying your username and email address, and any reported bugs and requested features you have made. 

6. Report bug
    1. When logged in, click on 'Report A Bug' in the navigation bar
    2. Be directed to report_bug.html
    3. Fill in the name and description of the bug
    4. If either fields are left empty, be presented with 'Please fill in this field.' tooltips.
    5. Click on 'Submit Report'
    6. Be directed to bug_detail.html for the bug you have just reported

7. Reported bugs
    1. Click on 'Reported Bugs' in the navigation bar
    2. Be directed to bugs.html and presented with a table of all submitted bugs, showing their names, upvotes, date posted and statuses. 
    3. Also be presented with a pie chart for the bug statuses with total, daily, weekly and monthly filters.
    4. If there is no data collected for a certain period, be presented with 'No data has been collected for this period yet'.
    5. To view a specific bug, click on any bug name in the table and be directed to bug_detail.html for that chosen bug.

8. Upvote bug
    1. When logged in, click on any bug name that has an 'OPEN' or 'IN PROGRESS' status and be directed to bug_detail.html for that specific bug.
    2. Click on 'Upvote' and see the upvote counter increase by one. 

9. Comment on bug/feature
    1. When logged in and viewing bug or feature_detail for any bug/feature, write a comment in the comment field.
    2. Click 'Post' and the page will refresh to show your comment, displaying your username and the time it was posted.

10. Request features
    1. When logged in, click on 'Request New Feature' in the navigation bar
    2. Be directed to request_feature.html
    3. Fill in the name and description of the feature
    4. If either fields are left empty, be presented with 'Please fill in this field.' tooltips.
    5. Click on 'Submit'
    6. Be directed to feature_detail.html for the feature you have just requested

11. Requested features
    1. Click on 'Requested Features' in the navigation bar
    2. Be directed to features.html and presented with a table of all requested features, showing their names, upvotes, date posted and statuses. 
    3. Also be presented with a pie chart for the feature statuses with total, daily, weekly and monthly filters.
    4. If there is no data collected for a certain period, be presented with 'No data has been collected for this period yet'.
    5. To view a specific feature, click on any feature name in the table and be directed to feature_detail.html for that chosen feature.

12. Upvote feature
    1. When logged in, click on any feature name and be directed to feature_detail.html for that specific feature.
    2. Select how many upvotes you would like to apply to this feature and click 'Add'.
    3. Be directed to cart.html
    4. Click 'Checkout' and be presented with a checkout form.
    5. Use '4242424242424242' for the Credit Card Number and '111' for the CVV. Pick any expiry month and year past the current date. These are Stripe's official testing numbers – no realistic payment will be made. 
    6. Be presented with error messages if any of the fields are not filled in.
    7. Click 'Submit Payment' and be presented with 'You have successfully paid.' message.

13. FAQs
    1. When logged out, click on 'FAQs' in the footer and be presented with frequently asked questions.
    2. When logged in, click on 'FAQs' in the footer and be presented with frequently asked questions and a question form.
    3. Fill in the name and description fields and click 'Submit Question'. If the description field is left empty, you should still be able to post your question. 
    4. Be presented with a 'Your question has been submitted successfully.' message. 

14. About
    1. Click on 'About' in the footer. 
    2. Be directed to about.html.

16. Back to top button
    1. Scroll down on any page with large amounts of content.
    2. A button on the bottom right of the page should appear.
    3. Click this button to return to the top of the page

### Responsive Testing

This website has been tested on different device screen sizes using Google Chrome Developer Tools and Mozilla Firefox Developer Tools. Minor bugs have been fixed as a result of this testing and I can confirm that this website functions responsively on all device screen sizes. 

### Code Validation

HTML code has been passed through the official W3 Validator - errors showing up were due to Jinja syntax. Any other errors within the code have been corrected.
CSS code has been passed through the official W3 Validator - no errors were found.

### Bugs

 - User is currently able to upvote a bug as many times as they like. This is unfair towards other users of the website - a user may wish to gain the highest priority for their bug as possible by upvoting many times, even if the bug does not need to be fixed urgently. This could be fixed in future versions of the application.  
 - Graphs change size when user interacts with them while using a mobile or tablet device. For example, if a user clicks on the 'Daily' tab and then back to 'Total', the graph will be significantly smaller than before. This is not a bug which needs to be fixed urgently, however, it can be fixed in future versions of the application.