<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92393141-b4ee0780-f11f-11ea-9cd7-47f4d7c5c4b4.png" alt="Corona Tales">
</div>
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92393335-07c7bf00-f120-11ea-881b-543875d38d5b.png" alt="Home Page">
</div>

[Corona Tales](https://corona-tales.herokuapp.com/) is designed as a text-base story sharing platform based around the coronavirus epidemic. Its goal is to allow people to post, share and search experiences and opinions on the site. The inspiration came from the various ways people have begun to use social networking during the epidemic, in manners not sen before. I wanted to create a site which is based more on thoughtful exploration rather than instant gratification, such as Instagram or Facebook, but still allow for personalisation. Certain design choices which would be out of line with similar systems were made deliberately and will be explained.

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colors](#colors)
    - [Styling](#styling)
    </details></li>

    <li><details>
    <summary><a href="#seamless-design">Seamless Design</a></summary>

    - [Preloader](#preloader)
    - [AJAX](#ajax)
    - [Infinite Scroll](#infinite-scroll)
    </details></li>
    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Home Page](#home-page)
    - [Profile Page](#profile-page)
    - [Other Pages](#other-pages)
    </details></li>

    <li><details>
    <summary><a href="#additional-features">Additional Features</a></summary>

    - [App Structure](#app-structure)
    - [Security](#security)
    </details></li>

    <li><details>
    <summary><a href="#features-not-yet-implemented">Features Not Yet Implemented</a></summary>

    - [Basic](#basic)
    - [Content](#content)
    - [User Features](#user-features)
    </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#information-architecture">Information Architecture</a></summary>

    <ul>
    <li><details>
    <summary><a href="#database-structure">Database Structure</a></summary>

    - [Details](#details)
    </details></li>    

    <li><details>
    <summary><a href="#data-models">Data Models</a></summary>

    - [Users](#users)
    - [Stories](#stories)
    </details></li>
    </ul>
</details>

4. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Packages](#packages)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
</details>

5. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#methods">Methods</a></summary>

    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>

    <li><details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
</details>

6. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    <ul>
    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary>

    - [Local Preparation](#local-preparation)
    - [Local Instructions](#local-instructions)
    </details></li>

    <li><details>
    <summary><a href="#heroku-deployment">Heroku Deployment</a></summary>

    - [Heroku Preparation](#heroku-preparation)
    - [Heroku Instructions](#heroku-instructions)
    </details></li>
    </ul>
</details>

7. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>

    - [Content](#content)
    - [Media](#media)
    - [Contact](#contact)
</details>

----

# UX
## Goals
### Visitor Goals
The target audience for Corona Tales is:
- People who want to share their experience publicly.
- People who are interested in reading other people's experiences.
- People that want  a simpler kind of social network.
- People that want to search for a particular idea or theme.
- People that want to create a log of their own stories.

User goals are:
- Express my sentiments on the site.
- Create an account securely to save my stories.
- View other people's stories from around the world.
- Search through the stories available.
- See the most interesting stories first.

Corona Tales fills these needs by:
- Creating a system similar to social feeds with likes, infinite scroll and tags, for people to feel familiar posting.
- Allow user to both post anonymously and with an account.
- Displaying stories from around the world, with he most interesting featured first.
- Providing a search function to browse through the site.

### Project Goals
The Project Goals of Corona Tales are:
- Create an interesting place to to explore other people's experiences.
- Have people relate to others through reading new experiences.
- Create a database where people's stories are stored securely.
- Allow people to create a secure account.
- Allow people to post their own thoughts.

### User Stories
1. As a user interested in writing, I expect to be able to write stories on the site.
0. As a user interested in the pandemic, I expect to be able to read varied experiences.
0. As a user interested in social networks, I expect to be able to scroll through the stories.
0. As a user interested in reading, I expect to see many stories to read.
0. I expect to be able to use likes to save stories.
0. As a user enjoying the stories, I expect to be able to see them on my account.
0. I expect to be able to post a story easily.
0. I expect to create an account to save my story history.
0. I expect to be able to customise my story appearance with different fonts and colors.
0. I expect to be able to use tags to categories my story.
0. I expect to be able to use tags to search through other stories.
0. I expect to see a fully functioning search.
0. As a user who has made an account, I expect to be able to delete my account or change my password.
0. I expect to be able to delete my content, or delete my account but leave my content anonymous.
0. As a user who has made an account, I expect my information to be saved.

## Visual Design

### Wireframes
Wireframes: https://drive.google.com/open?id=1qIyntbCbm1Q0vOoC849uHAyfC5QICYAL

### Fonts
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92395862-55dec180-f124-11ea-927e-665258e480a5.png" alt="Fonts">
</div>

- The primary font, [Eczar](https://fonts.google.com/specimen/Eczar) was chosen because it has an appearance similar to fonts used in books, magazines and printed text, however is not too distracting or stylised. It is serif, so it is has some flair but remains clear and simple. It was chosen also to compliment the secondary font which is a very stylised serif font.
- The secondary font, [IM Fell English SC](https://fonts.google.com/specimen/IM+Fell+English+SC) was chosen because it is reminiscent of a typewriter or classic printed text. It gives a sense of reading a book or the feeling of touching paper. It is stylised quite a bit as a serif font, so it stands out from the other text, perfect for a heading.

<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92396141-cf76af80-f124-11ea-8cda-5d5abfe71ba7.png" alt="Post Fonts">
</div>

- When writing a post, [CKEditor5](https://ckeditor.com/ckeditor-5/) is used to provide a choice of different fonts to type with.
- These are a selection of common fonts with different styles to add variety to the posts.

### Icons
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92397986-039f9f80-f128-11ea-8431-ab9b01c4dd69.png" alt="Icons">
</div>

- Icons are taken from the [Material Design Icons](https://material.io/resources/icons/?style=baseline) library and and are utilised as classes in the `<i>` tag.
- As they are utilised as classes, they can easily be styled using other classes or IDs in the same tag. I often used Bootstrap classes to style them uniformly.
- The icons are used for the 'like' button, next to forms as indicators and in the floating menu button.
- If an item is liked, the icons are swapped out on the fly after a successful ajax response to indicate the change.


### Colors
#### Main Palette
![Main Palette](https://user-images.githubusercontent.com/44118951/81061325-7081ff00-8ed4-11ea-94d9-5e01ace77669.png)

#### Story Cards
![Story Card 1](https://user-images.githubusercontent.com/44118951/81062707-c2c41f80-8ed6-11ea-86b0-355dd042702c.png)
![Story Card 2](https://user-images.githubusercontent.com/44118951/81062698-c061c580-8ed6-11ea-843c-78bd4eb94521.png)

- Colors were chosen from the Materialize CSS palette for ease of use with classes in dynamic content.I mainly targeted bright, bubbly colors to give life to what is essentially a slow, patient content. 
- The main background color and the nav color are utilised to give a sense of clam.
- The main menu button colors are used to represent certain ideas throughout the entire site, so you'll find them reused in forms and menus. For example, posting is purple, home/profile is teal, the main theme color, search is blue, etc.
- The cards have a set palette of colors to choose from. I chose a subset that was a balance between impact, boldness and readability.
- The colors allow each person to give a bit more character to their story card.
- The colors are kept simple and clean and the use of dark tones is avoided, reserved for text. Shadows are used appropriately to give a sense of depth.

### Styling
- For this project I have utilised - [Materialize](https://materializecss.com/) as the style framework.
- The above palette has been used in toasts, messages, error warnings as well.
- Responsive text sizing has also been utilised on certain elements.
- Shadows give an impression of depth.
- Smooth animations and tooltips are utilised throughout for cleanliness.
- The menu nav button is made evident the first time you visit the site with a large circle drawing attention to it.
- Everything has nice universal icons so the meaning can be conveyed through symbols.
- Tooltips are utilised throughout for clarity.
**Note** WHile SASS was considered for this project, I faced a large amount of issues with Materialize CSS and so opted not to attempt using SASS.

## Seamless Design
### Preloader
- A simple, style-consistent, preloader is used when loading pages.
- The Preloader is placed under the Navbar and the floating menu, so access to menu options will always be available to the user for a better navigation experience. It also maintains the brand logo front and centre.
- The use of the preloader under the Navbar gives the impression of a persistent webpage despite loading new pages.
- The preloader is also underneath toasts, so it won't block them.

### AJAX
- AJAX forms are used throughout the site, as this is a basic modern expectation of users when browsing a site, otherwise there would be serious flow and UX issues.
- If logged in, an ajax like button will be present.
- The Like button utilizes AJAX to encourage easy interaction.
- On click the icon will send the form in the background to register a like in the database.
- On success change and deliver a short recognition sound. 
- The button's default image is decided on whether the like is attached to your account in the database or not.

### Infinite Scroll
- Infinite Scroll has been implemented to the site using [Infinite Scroll](https://infinite-scroll.com/).
- Infinite Scroll is applied to story pages to create a social media-like feed.
- The same preloader icon is used for loading new items.
- On append re-initialising functions are fire by Infinite Scroll in order to ensure all features work correctly.
- Initialising features have been grouped into two functions, based on whether they are required for all appended stories, or only stories on the profile page that require editing functions. If a new function needs to be created, it can easily be slipped into one of the two grouped functions, and it will easily function correctly on all pages.
- [Flask-Paginate](https://pythonhosted.org/Flask-paginate/) automatically provides the page list for the next set of items.

----

# Features
## Page Elements
### All Pages
#### Navbar
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92401356-c9d19780-f12d-11ea-8dd5-1e2b4b5ad2d3.png" alt="Medium Header"><br>
  <img src="https://user-images.githubusercontent.com/44118951/92401432-eb328380-f12d-11ea-8236-5d954f26e6da.png" alt="Small Header">
</div>

- The Navbar is persistent across the site along with the Floating Action Button, as a footer has been foregone in favour of the infinite scroll.
- The Logo is always highlighted, central and bold, on all screen sizes.
- Keeping with the theme, no imagery has been used for the logo.
- Contains more informational links than interactive links. This is to try and maintain user engagement with the Floating Action button,
- Authorisation functions switch depending on whether or not the user is logged in. Signup, login, profile and logout are always highlighted no matter the page.
- Authorisation functions have a different color to remain highlighted.
- The mobile nav button has been placed to the right that opens a SideNav on the right for ease of use with one hand.

#### Floating Action Button
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92397986-039f9f80-f128-11ea-8431-ab9b01c4dd69.png" alt="Icons">
</div>

- On the very first load of each session, an alert will pop out from the floating menu to alert the user of its presence.
- I'm utilising this menu as the main point of interaction and navigation for the site.
- All pages on the site can be accessed through this menu and some features are exclusive to it. On desktop it opens on hover, on mobile with a tap, positioned bottom-right for easy right-hand access.
- It hovers above the preloader to maintain importance to the same degree of the nav.
- It uses a bright and colorful palette to catch the eye. 
- This is to encourage interaction with these functions in particular, as well as create preference for, and push users towards, the colorful, eye-catching floating menu button, where the key site functions are, while simultaneously diminishing the importance of the basic navbar items.
- The menu items are tool-tipped and color coordinated for clarity.
- The green button  changes on context between signup/login/profile/home.
- Each button opens a modal except the button for the aforementioned green button.
- All forms in the modals have helper text and validation where necessary for user feedback.

#### Post Modal
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92402839-93494c00-f130-11ea-8696-0a0fcd94547d.png" alt="Post Modal">
</div>

- Active on every page so you can create a post from anywhere.
- Uses icons, hints on form fields and live validation because the form is a bit longer than the most basic social media forms.
- If a user is signed in, the form will auto fill with your info if it is saved to the account.
- The Post a story option allows people to preview a color by holding down on it before posting.
- Utilises [CKEditor5](https://ckeditor.com/ckeditor-5/) for the message field, allowing a range of customisability options to make your post stand out.
- The editor has been rebuilt and customised to include coloring fonts, amongst other additional features.
- Provides a tag field so you can categorize your stories.
- Tag field has an autocomplete function that pulls the tags from other stories to be reused.
- Tag field will automatically cut out any hash symbols added to the tags in the backend, as they are not recognised as the same.
- Text limit of 40,000 characters
- Card colors can be previewed on the select dropdown by hover, or holding on mobile

#### Search Modal
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92403613-16b76d00-f132-11ea-91d8-a2bca9319daf.png" alt="Search Modal">
</div>

- Utilises the same icons from the Post Modal for coherence.
- All fields are optional, even for the range fields.
- The search function is thorough enough to filter through each field sent and return results based.
- Combines a full text search with integers and timestamps, working through each singly to return results.
- Text search is weighted in the DB, valuing tags higher than other text.
- Some fields function more explicitly like filters, such as language, rather than a text search, removing stories in other languages.
- Indexes for times, dates and ages have been included, ensuring that in search both full days are included.
- The database makes use of arrays, integers, booleans and embedded documents to fully utilise the search abilities.
- The text index has been tested to include all string info, and excludes common text word searches.

#### Sign up and Log in Modal
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92404377-b1fd1200-f133-11ea-8e90-2a3a070fb5a5.png" alt="Login Modal">
</div>

- Log In and SIgnup are available on the same modal as different tabs.
- Log In is default tab.
- Has a functional "Remember Me" option.
- Form validation is used for the Sign Up form.
- Gives instead validation feedback.
- Provides helper text for every field.
- Email is not necessary to sign up. I have used sites such as typing.com where it isn't requested. I liked this in particular and chose to follow suit.
- Log in functions utilise [Flask-Login](https://flask-login.readthedocs.io/en/latest/) to manage the process.
- A User Class was created for a blueprint
- Users can securely create an account with a hashed password
- Patterns are required for both usernames and passwords

#### Toasts
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92400430-38155a80-f12c-11ea-88f9-eb84682e008a.png" alt="Toasts">
</div>

- Materialize Toasts are used to notify users of their actions on the site.
- A toast will show with a response to the user action, it may be a success message or an error message.
- Colors change depending on the message type, the class is passed
- This gives users immediate feedback, for instance, if an error occurred logging it, they will be notified immediately.
- Toasts have a higher z-index than the preloader so they can be seen even while a page is loading.

### Home Page
#### Quote Box
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92404983-f3da8800-f134-11ea-912c-993b370c9459.png" alt="Quote Box">
</div>

- A different random quote on the topic of sharing is pulled from a hand-picked selection will be displayed as the Home page central graphic.
- I hope will help set the tone by having visitors reflect before reacting.
- Quotes are pulled from `project/static/js/quotes.json`. It is a custom file I built for to choose quotes.
- New quotes can be easily added by inputting a few small details into this file.
- I wanted to utilise an API, but the ability to select quotes myself always required paid commitment.
- I previously had a chart with information on the virus, but the further I developed the site, the less it was in theme. Something written felt much more coherent.

#### Story Feed
- Featured stories display at the top of the feed before other stories.
- Feature stories are automatically set at 21 likes, but for the purpose of this project I have manually set some for display purposes.
- Under this all other stories are displayed.
- The stories in each section are ordered reverse chronologically, most recent first.
- The story list from the database will pull 100 stories maximum, featured and non-featured inclusive.
- Infinite Scroll is used to avoid pagination and create the social media-like feed.
- The scroll has a loading icon for feedback, gives an alert when the content has ended and when there are connection issues.
- It is possible to post stories both logged in and anonymously.
- Creating an account will save the stories to your account.

#### Story Card
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92406658-defff380-f138-11ea-9f1e-c21aa22e17f2.png" alt="Story Card">
</div>

- Each story has a card as a basic design, with a user-selected color from a set palette, allowing for personalisation but maintaining a coherent style.
- Each card is has its content truncated at 180px to maintain a consistent size and give a preview of the story. The story can then be opened to full height with a smooth animation.
- Each card displays basic info about the writer and allows the main content to have stylised text formatting.
- Tags are always on display so the viewer can get an idea of the theme.
- Each one is a link to a search page on that tag.
- The search uses a text index and does not filter posts by tag.
- This was a choice as to also include content which may have the keywords but not list the tag, however the tags carry a higher importance weight in the index, so they will always be prioritised. 
- If logged in, a 'like' button will be displayed.
- The button uses ajax for seamless experience and registered the like to the database on click.
- Likes are deliberately obfuscated until clicked, at which point they are shown briefly by a tooltip.
- Simple card format, all evenly sized for uniformity when scrolling
- I give everything one like as a thanks for posting

### Profile Page
#### User Feed
- The profile page is made of two tabs. A user story feed and a user settings section.
- The user story feed functions similarly to the main feed but with a drew differences.
- All stories are filtered to only user-created stories. 
- Each story has an edit button instead of a like button.
- The edit button has a different color to differentiate it from the main menu and will sit just to the right of the main menu button on small screens.
- It displays a menu perpendicular to the main menu, to not have menu tooltips clip.
- It has two color-coordinated options, edit and delete.
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92407617-60f11c00-f13b-11ea-9106-ad698e345441.png" alt="Edit Menu">
</div>

- Both options pull up modals, the edit story modal will open pre-filled with the story info.
- Each time an edit modal is closed, the CKEditor instance is disposed and then recreated to not overload the page and refresh the story text info.

#### User Settings
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92408190-0c4ea080-f13d-11ea-8e90-1dda5d06923b.png" alt="Edit Menu">
</div>

- The layout is standard with the rest of the site with buttons sitting on the right.
- All forms have validation and helper text.
- Sections have dividers for clarity and the delete buttons are centered for clarity.
- User can opt to input basic data that will pre-fill their data when posting a story, if any info is saved, a button to delete the info is shown.
- Users can also change their password securely here.
- Alternatively it is possible to delete the account and stories separately. A choice made as it is possible to post stories both logged in and anonymously.
- Delete options all have confirmation modals.

### Other Pages
#### Search Page
- The page is essentially the homepage feed, with all the same features but with filtered results.
- The  search page returns results either sorted by text-score if text was entered, or within the range requested in the search form.
- Shows a message if no results are found.
- A specific per-tag search was tried but I preferred the weighted text search.

#### Contact Page
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/) is used to process and format the emails.
- A simple form with validations, helpers and icons.

#### About
- A simple page explaining the site.

## Additional Features
### App Structure
- The app has been designed as a module, utilising an __init__.py file for configuration of the app.
- The site utilises blueprints that are imported into the main app creation, one for the majority of views, and the other for views requiring secure authorisation/
- Extensions.py has been utilised, along with blueprint, to avoid circular imports.
- config.py has been created for environment variable storage.
- models.py has been utilised to create a User Class for flask-login.
- The other details follow standard practice for a flask app.
- A .gitgnore file is included.
- the procfile utilises gunicorn for initialisation

### Security
- Environment variables have never been written in the app, let alone committed.
- Flask login is used to manage users.
- Passwords are hashed securely on signup and the hash is checked on login.
- People are blocked from accessing each others' profiles.
- All user-created data can be securely deleted.

## Features Not Yet Implemented
### Basic
- Toasts fire when a post is liked/unliked.
- Change to Bootstrap / Foundation CSS
- Implement alternative tagging system - Materialize Chips is buggy
- Work on mobile font-size formatting (I don't currently have access to enough phones for this)
- More testing on views and debugging 
- Italian language site
- Optimize Edit Modal creation on user page.

### Content 
- Share button for each card
- Tag-specific more restricted search
- More quotes for index
- More freedom in card color choice

### User Features
- More interaction between users, such as the ability to follow/friend.
- A public profile page with liked items, bought items if desired, etc.
- Login using social accounts.
- Email entry for password recovery using flask-mail
- A tab that displays like stories
- A friend / follow system
- edit and like buttons for users on their own cards on all pages

----

# Information Architecture
## Database Structure
### Details
- I have utilised a **NoSQL** database, [MongoDB](https://www.mongodb.com/) throughout the entire project development.
- I have tried to use different field types for the documents to experiment with the database.
- I have used tried to manipilate the data using different command in Python views to explore their use.

## Data models
### Users
| Field Name | Field Type | Info |
 --- | --- | ---
 username | string | Mostly used for display purposes.
 user_id | string | The username in capitals to prevent capitilisation having an effect on login and account creation.
 password | string | the protected password hash.
 prefill | object | Used to prefill forms. Keys: name, age, country, story_language. Type: String.
 liked | array | Contains the doc IDs of each liked story. Used to remember liked stories.

### Stories
| Field Name | Field Type | Info |
 --- | --- | ---
user_id | string | Attaches the story to a particular user. Optional.
name | string | Displays the writer's name.
age | int | Displays the user's age.
country | string | Lists the country they are in. Used as a filter in search.
story_language | string | Lists the story language. Used as a filter in search.
color | string | Saves the story card color. Must be an appropriate HTML class.
title | string | Title of the stories.
text | string | The text of the story. Saved as a HTML string.
time | int64 | Javascript timestamp in seconds.
featured | boolean | Places the story in the featured section if true.
likes | int32 | Number of likes the story has received. Featured changes to true at 21 likes.
tags | array | A list of tags associated with the story.
edit_time | int64 | If the story has been edited it saves the timestamp in seconds.

# Technologies Used
## Languages
- [Python](https://www.python.org/)
    * Using Django and other plugins to develop the app.
- [HTML](w3.org/standards/webdesign/htmlcss)
    * Page markup.
- [CSS](w3.org/standards/webdesign/htmlcss)
    * Styling.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    * Running functions for interactive components, AJAX, etc.
- [JQuery](https://jquery.com/)
        * Animations and click functions

## Frameworks
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The main app technology for the views
- [Materialize](https://materializecss.com/)
    * Used for basic styles and outline

## Libraries
- [JQuery](https://jquery.com/)
    * Animations and click functions.
- [Google Fonts](https://fonts.google.com)
    * Font Styles.
- [Material Design Icons](https://material.io/resources/icons/?style=baseline)
    * Used for icons.

## Packages
- [Pymongo, Flask-Pymongo](https://pymongo.readthedocs.io/en/stable/)
    * Used for database manipulation
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
    * User authentication and functions based on this
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
    * The contact page
- [Flask-Paginate](https://pythonhosted.org/Flask-paginate/)
    * Paginates content with my settings, allowing Infinite Scroll to append items and recognise page limits 
- [Gunicorn](https://gunicorn.org/)
    * Server deployment on heroku

## Platforms
- [Github](https://github.com/)
    * Storing code remotely.
- [Gitpod](https://gitpod.io/)
    * IDE for project development.
- [Heroku](https://www.heroku.com/)
    * Platform for production deployement.
- [Travis CI](https://travis-ci.org/)
    * For CI testing and automatic deployment.

## Other Tools
- [Balsamiq](https://balsamiq.com/)
    * To create wireframes.
- [DBeaver](https://dbeaver.io/)
    * Generate Diagrams for the database.
- [Mockup Generator](https://techsini.com/multi-mockup/index.php)
    * For device mockup images.
- [CKEditor5](https://ckeditor.com/ckeditor-5/)
    * More complex text editing in the stories
- [Infinite Scroll](https://infinite-scroll.com/)
    * Used for infinite scroll on feed pages

# Testing
## Methods
### Validation
- HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/).
- CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/).
- Links checked with [W3C Link Checker](https://validator.w3.org/checklink).
- Each javascript file was tested on the site for errors and functionality using the console and with [JSHint](https://jshint.com/).
- gitignore file has been included to prevent system file commits
- requirements.txt updated

### General Testing
- Each feature was developed and tested in its own branch before being merged with master. Branches were subsequently deleted.
- The views have been thoroughly manually tested and refined over time, utilising  python features to create documents in the database in a useful, flexible structure.
- The documents in the database have been examined and structured in a manner so that the information is well defined, checking how the views effect documents.
- Some tests were performed on views and were tested manually throuroughly. For example, every possible combination on search was tested.
- Each time a feature was added, all the functions were tested to see if there was an impact.
- The python module structure has been tested and implemented, adding config.py, setup.py and some tests.
- The site was sent to friends for feedback and testing.
- All forms have validation and will not submit without the proper information.
- .gitignore file has been included to prevent system file commits.
- The image loading blur has been thoroughly tested and gone through numerous iterations to optimise the smoothness of the transition on different devices and internet speeds.
- Backup Map functions have been tested in a local deployment.
- Email error functions have been tested offline as well.
- External links open in a new tab.
- I regret that, due to the amount of troubleshooting I had to do with the CSS, I was unable to fully utilise pythons's unittest framework. I made some simple views, but the CSS troubleshooting slowed down my app development to the point where I had to move forward with features to make the deadline. More testing is necessary in this area.

### Mobile Testing
- I tested the site personally on my Android device, going through the entire process, checking buttons, functions, checking out, etc. I was personally unable to test on iOS.
- I have tested the site and its layout on multiple android devices, different sizes, on multiple browsers. I was unable to test on iOS. It is fully responsive with a clean layout on each device.
- The site was sent to friends and relatives for them to follow the same process. They have tested on their devices, including iOS.
- Chrome was utilised to inspect the site in mobile format, going through the pages and functions.

### Desktop Testing
- The site was developed on a Chromebook and, as such, the majority of testing occurred on Chrome.
- The site was tested by friends and relatives on numerous desktop devices.
- The site was marginally tested on other browsers, such as Firefox and Edge.
- Internet Explorer was not tested and the site was not developed with it in mind as support for the browser is gradually being dropped.

## Bugs
### Known Bugs
- On android devices, when writing incredibly long stories, the CKEditor formatting bar gets stuck at the top of the screen even after scrolling.
- It seems there a certain combination of characters in certain stories that act as a wildcard for the text search index in the database, with the story being in the results for each search. Needs further investigation.

### Fixed Bugs
**Note: Throughout development I found my largest issues were caused by difficulties with Materialize CSS components. I sincerely regret using it, as I spent a lot of time debugging the CSS instead of developing features or creating test views. Bootstrap and Foundation are both more complex and therefore more flexible, perhaps more study is required to utilise them well, but that suits me. The simplicity of Materialize may suit some developers, but I found it to be a hinderance.

#### Materialize CSS
- The tags feature in Materialize "Chips" was something I implemented early on as the tag system, only to find out that when I began testing using real devices as opposed to developer mode, that it had [unfixable bugs](https://github.com/Dogfalo/materialize/issues/5722) on android. To enter a tag, you must use the "Enter" key, however on android, within a form, the enter button becomes a "Tab" button. I edited the Materialize.js to allow using spaces, including keys for space on android, but it still would not register. This has been a known issue since 2018 In the end I found a workaround by implementing the Chips outside of the form, pulling the data from the tags and reinserting it as a list, key by key, into the form. This was just one of many issues I found and still have with the Materialize CSS.
- Many of the components are inflexible, functioning well while used singly but buggy and requiring a lot of specific code editing when used in conjunction with one another
- Tabs within a modal, for example, didn't have the active tab selected properly so I had to reinitiate it with specific settings.
- Tooltips weren't fixed on the page for the action buttons, scrolling upwards on mobile devices, I simply had to create my own.
- Z-indexes have a bizzare order, placing less relevant components under or over others, seemingly randomly. The action buttons themselves had z-indexes above the Nav, as well as modals, so scrolling on the user page left buttons clipping, I had to edit z-indexes.
- Bullet points removed by default in styles
- Some form components recognise "required" attribute, other do not, validation only functions on some of fields, requiring custom code. The list goes on.
- Documentation was missing, ouright incorrect, or messy in many parts. There were classes that didn not function as described, and examples that weren't connected to the information.

#### Others
- Troubleshooting database issues was relatively easy. As this is my first project utilising the database, a little bit of study in the dcumentation to learn syntax was usually enough.
- I came accross issues with cirular imports when writing the app, and found that the best solution was to scale the app up a little from a single app.py, to a module. This allowed me to avoid circular imports, keep the the app information organised and make the app nicely distributable.
- I began trying out creating an app-factory but found it was overkill for my purposes.
- The search function had a number of iterations before it was fully functional. The main issue was the presence or lack of variables in the search. The main way to resolve it was to declare all the variables as `None` and only change them if present in the form.

----
   
# Deployment
## Local Deployment
### Local Preparation
**Requirements:**
- An IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3](https://www.python.org/downloads/release/python-385/)
- [pip](https://github.com/pypa/pip)
- [Git](https://git-scm.com/
- A MongoDB database set up.

### Local Instructions
#### Standard
1. Download a copy of the project repository [here](https://github.com/Ri-Dearg/corona-share/archive/master.zip) and extract the zip file to your base folder. Or you can clone the repository with:
    ```
    git clone https://github.com/Ri-Dearg/corona-share/
    ```
2. Open your IDE and choose the base directory.
3. I recommend running the program Python's virtual environment with:
    ```
    python3 -m .venv venv
    ```
    - Setting up a virtual environment can differ from system to system, please see [python documentation](https://docs.python.org/3/library/venv.html) for more info. The site can also be run without setting up a virtual environment.
4. Run the virtual environment.
    ```
    .venv\Scripts\activate
    ```
5. Install project requirements with:
    ```
    pip3 -r requirements.txt.
    ```
6. Set up the necessary environment variables in your IDE.
    The necessary variables are as follows:
    ```
    'ADMINS', <key>
    'DATABASE_URL', <key>
    'MAIL_PASSWORD', <key>
    'MAIL_USERNAME', <key>
    'MONGO_URI', <key>
    'SECRET_KEY', <key>
    'IP', <key>
    'PORT', <key>
    ```
    - Certain variables may not be necessary based on your setup, but the some files will need to be modified accordingly.
    - The `DEBUG` variable can be added if in development.

9. Run the local server:
    ```
    flask run
    ```
    This command may need to be altered depending on your setup, for example I use:
    ```
    flask run -h localhost -p 8080
    ```
    This runs it on a local server on port 8080.

10. The site should now run and be accessible. Login to the admin area and create some models to see the site features.

#### Setup.py
1. A setup.py file has been created for easy deployment.
0. At a python terminal you can run `python setup.py sdist` to create a source distributable
0. This can then be unpacked, and the module be installed by running python `setup.py install` from its directory.
0. This will install the package for modification.
0. This will allow you to run the program locally, if you wish
0. The steps from 6 onwards from the above instructions will still have to be followed.

## Heroku Deployment
### Heroku Preparation
- It is possible to copy or clone the repository to directly deploy it to Heroku without any changes, only adding environment variables. If you wish to customise the repo please check the details below.
**Requirements:**
- A `requirements.txt` file created with `pip freeze > requirements.txt`.
- A `Procfile` with the command `web: gunicorn config.wsgi:application`.

### Heroku Instructions
1. Copy or clone the repository.
2. `git add`, `git commit` and `git push` to a GitHub repository.
3. Create an app on [Heroku](https://www.heroku.com/), selecting a name and region.
4. Click on 'Deploy' in the menu, and select the Github repository from the menu. Confirm that you are linking the correct repository. Do not yet deploy it.
5. Go to the 'Settings' section and click on 'Reveal Config Vars'.
6. Input the same environment variables as listed in step 6. of [Local Instruction](#local-instructions).
7. Continue on to follow steps 7 and 8 in your IDE. You can also create add product models, etc during this step if you wish. Repeat step 7.
8. Return to the 'Deploy' section and manually deploy the repository.
9. Click the 'View App' button and everything should be up and running!

## Credit and Contact

### Content
- Stories provided by actual people.
- Infinite Scroll is utilised under its Open Source license for personal projects.
- Any code utilised from another programmer is documented and credited within the code.

### Media
- Sound:
    - Title: Blop
        Uploaded: 03.27.13
        License: Attribution 3.0
        Recorded by Mark DiAngelo
    - Title: Pop Cork
        Uploaded: 06.09.09
        License: Attribution 3.0
        Recorded by Mike Koenig

### Contact
Please feel free to contact me at `sheridan.rp@gmail.com`