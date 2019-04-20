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