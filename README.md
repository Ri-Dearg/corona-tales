# Horizon Photography

The site is desgined as a text-base story sharing platform based around the coronavirus epidemic. Its goal is to allow people to post, share and search experiences and opinions on the site. The inspiration came from the various ways people have begun to use social networking during the epidemic, in manners not sen before. I wanted to create a site which is based more on thoughtful exploration rather than instant gratification, such as Instagram or Facebook, but still allow for personalisation. Certain design choices which would be out of line with similar systems were made deliberately and will be explained.

Link to deployed project [here](https://corona-tales.herokuapp.com/).

## UX

### Home Page

#### First Impression

##### Initial Viewing
The home page is desgined as a feed, with infinite scrolling, much like many social networks. A page preloader with a slow fade is placed covering content on all pages, the z-index has been placed under the navbar and mneu button, so they persists from one page to the next.
A different random quote on the topic of sharing is pulled from a hand-picked selection will be displayed as the Home page central graphic. I previously had a chart with information on the virus, but the further I developed the site, the less it was in theme. So, I chose a random quote, which I hope will help set the tone by having visitors reflect before reacting.
The style is simplicistic, minimalist and clean to create clear focus rather than busy distration.
On the very first load of each session, an alert will pop out from the floating menu to alert the user of its presence.
Many actions will pop up a flashed color coded messeage for confirmation and user feedback.

#### Navigation

##### Navbar
The navbaar is simple and clean. Kepping in theme with the idea of text, no imagery has been used for the logo. The authourisation functions switch depending one whether or not the user is logged in. Signup, login, profile and logout are always highlighted no matter the page. This is to encourage interaction with these functions in particular, as well as create preference for, and push users towards, the colorful, eye-catching floating menu button, where the key site functions are, while simultaneously diminishing the importance of the basic navbar items.
The mobile and side nav have been placed to the right for ease of use with one hand, favouring the right-handed majority.

##### Floating Fixed Menu
I'm utillising this menu as the main point of interaction and navigation for the site. All pages on the site can be accessed through this menu and some features are exclusive to it. On desktop it opens on hover, on mobile with a tap, positioned bottom-right for the same reaason as before. It hovers above the preloader to maintain importance to the same degree of the nav.
It uses a bright and colorful pallet to catch the eye. The menu items are tooltipped and color coordinated for clarity. The green button also changes on context between signup/login/profile/home. Each button opens a modal except the button for the aformentioned green button.
All forms in the modals have helper text and validation where necessary for user feedback. The signup login form uses tabs to offer both options. The Post a story option allows people to preview a color by holding down on it before posting.

#### Feed

##### Story Section
Under this there is a "Featured" story section that is displayed first, followed by an non-featured story section. Feature stories are automatically set at 21 likes, but for the purpose of this project I have manually set some for display purposes.
The stories in each section are ordered reverse chronologically, most recent first. The story list from the database will pull 100 stories maximum, featured and non-featured inclusive.
Infinite Scroll is used to avoid pagination and create the social media-like feed. The scroll has a loading icon for feedback, gives an alert when the content has ended and when there are connection issues.

##### Story Cards
Each story has a card as a basic design, with a user-selected color from a set pallet, allowing for personalisation but maintaining a coherent style. Each card is has its content truncated at 180px to maintain a consistent size and give a preview of the story. The story can then be opened to full height.
Each card displays basic info about the writer and allows the main content to have stylised text formatting.
If logged in, a like button will be present, which uses ajax to perform form submission in the background. On click the icon will change and deliver a short recognition sound. Likes are only displayed after a user clicks the like button, and only temporarily. This is a deliberate choice to deliver a familiar system but diminish its importance. The reason being to like something if it interests you, and not solely because it is popular. While it is possible to like and unlike something to see the number, it requires extra effort that will likely dissuade the average user.
Tags are always on display so the viewer can get an idea of the theme. Each one is a link to a search page on that tag. The search uses a text index and does not filter posts by tag. This was a choice as to also include content which may have the keywords but not list the tag, however the tags carry a higher importance weight in the index, so they will always be prioritised. A specific per-tag search was tried but I preferred the weighted text search.

### Profile Page

#### User Feed

##### Edit Menu
The profile page is made of two tabs. A user story feed and a user settings section. The user story feed has functions the same as the main feed but with two main differences. Firstly, all stories are filtered to only user-created stories. Secondly, each story has an edit button instead of a like button.
The edit button opens has a differerent color to differentiate it from the main menu and will sit just to the right of the main menu button on small screens, displaying a menu perpendicular to the main meu, to not have menu tooltips clip.
It has two color-coordinated options, edit and delete. Both pull up modals, the edit story being pre-filled with the story info.

#### User Settings

##### Layout
The layout is standard with the rest of the site with buttons sitting on the right. Sections have dividers for clarity and the delete buttons are centered for clarity.
User can opt to input basic data that will prefill their for data when posting a story, if any info is saved, a button to delete the info is shown.
All forms have helper text. The delete options have modals that require password input to confirm the decision.

### Search, About, Contact

#### Search
The searchpage returns results either sorted by tectscore if text was entered, or within the range requested in the search form. The page is essentially the homepage, with all features bt with filtered results.

#### About
A simple page explaining the site.

#### Contact
Another simple form field that uses flask-mail for email.

### Fonts, Colours

#### Fonts
THe font choices were based on the idea of reading a book, sp a styles fitting the theme were picked. However, when writing a story, users may choose their own fonts in the story content.

#### Colours
Colors were chosen from the Materialize CSS palette for ease of use with classes in dynamic content. I mainly targeted bright, bubbly colors to give life to what is essentially a slow, patient content. 
THe main background color anf the nav color are utilised to give a sense of clam.
The main menu button colors are used to represent certain ideas throughout the entire site, so you'll find them reused in forms and menus. The cards have a set pallete of colors to choose from. I chose a subset that was a balance between impact, boldness and readability. The colors allow each person to give a bit more character to their story card. The colors are kept simple and clean and the use of dark tones is avoided, reserved for text. Shadows are used appropriately to give a sense of depth.

### User Stories
As a user interested in reading stories, I expect to see a many different perspectives..

As a user interested in writing, I expect to be able to share my stories.

### Wireframes
Wireframe: https://drive.google.com/open?id=17ZBPFFBDwHyMecXJiWNz-r5LhEaP79as


## Features

### Features implemented

- Content
    - Story Creation
        - Edit text using a custom-built CKEditor for font styles, colors, sizes and other features.
        - Post anonymously without logging in, but cannot like stories
        - Choose from a range of colors for the post
        - Text limit of 40,000 characters
    - Story Display
        - Featured stories displayed above others after passing a set number of likes
        - Stories are ordered chronologically by a millisecond timestamp, and converted to a readable date
        - Trucated text that can be expanded
        - Like stories asynchronously, with sound and notification for the action
        - Simple card format, all evenly sized for uniformity when scrolling
    - Search
        - Form requires data which is then used to search through stories
        - Add tags, which are linked to search facility
        - Tags are weighted heavier in the search index and mixed with content for a full text search
        - Date and age ranges for search
        - All search field are optional, mix any details
        - Country and language search filter the results
- Users
    - Authentication
        - flask-login manages users
        - A USer Class was created for a blueprint
        - Users can securely create an account with a hashed password
        - Patterns are required for both usernames and passwords
        - User can signup using only a username and password. I recently used typing.com and was refreshed to find they required no email. I decided to follow suit.
        - Can use the "Remember me" function to stay logged in
        - Can change password securely
        - Can delete all users stories while keeping the account
        - Can delete account while leaving posted stories, user information is stripped from the story
    - Content
        - Registered users can like stories
        - Ragistered users have their stories saved to their account.
        - Users can edit or delete any created stories
        - Users can fill in autofill info to use when posting a story.
        - Users can delete their autofill info
- General
    - Utility
        - Infinite Scroll has been applied to all feeds.
        - Preloader placed over content but under menus
        - Nav and menus placed on the right for one-handed use
        - Menus utilise tooltips for clarity        
        - Nav options change depending on location and authentication.
        - Flashed messages pop up for user feedback
        - flask-mail is used for the contact page
    - Colors
        - Site is color co-ordinated for cheerfullness.
        - Buttons and themes are color co-ordinated to give for clearer, more uniform recognition of function
    - Other 
        - Random quote on site index
        - Utilises Material Design to give a sense of depth
        - Flashed messages have styled categories
        - Clean, minimal and colorful

### To Explore / Do

- Content 
    - Share button for each card
    - Tag-specific more restricted search
    - More quotes for index
- Users
    - Email entry for password recovery using flask-mail
    - A tab that displays like stories
    - A friend / follow system
- General
    - Change to Bootstrap / Foundation CSS
    - Implement alternative tagging system - Materialize Chips is buggy
    - Work on mobile font-size formatting (I don't currently have access to enough phones for this)
    - More testing on views and debugging 
    - Italian language site
    - Optimize Edit Modal creation on user page

## Technologies Used
- Languages
    - [HTML](w3.org/standards/webdesign/htmlcss)
        * Page markup
    - [CSS](w3.org/standards/webdesign/htmlcss)
        * Styling
    - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
        * Map, iframe, response windows
    - [JQuery](https://jquery.com/)
        * Map, iframe, response windows
- Framework
    - [Bootstrap](https://getbootstrap.com/)
        * Used for basic styles and outline
- Resources
    - [Fontawesome](https://fontawesome.com/)
        * Used for icons
    - [Google Fonts](https://fonts.google.com)
        * Font Styles
    - [Favicon Generator](https://www.favicon-generator.org/)
        * Favicons
    - [Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial)
        * Map
    - [REST Countries API](https://restcountries.eu/)
        * Statistics for infowindow, marker information

## Testing
- I have tested the site and its layout on multiple android devices, different sizes, on multiple browsers. I was unable to test on iOS. Mainly developed and tested using chrome developer mode. It is fully responsive with a clean layout on each device.
- All forms have validation and will not submit without the proper information.
- Links checked with [W3C Link Checker](https://validator.w3.org/checklink)
- HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/)
- CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/)
- Each javascript file was tested on the site for errors and fucntionality using the console and with [JSHint](https://jshint.com/).
- gitignore file has been included to prevent system file commits
- Each feature was developed and tested in its own branch before being pushed to master.

## Deployment
1. Set up a git hub repository for deployment and set up an SSH key.
0. Push the master branch to the Github Repository. The site will update automatically from the master branch.
0. Go to the settings of the repository and select the Github pages section.
0. Validate and test HTML, CSS and Javascript.
0. Published the site from the master branch, ensure index.html is the landing page.

### User Deployment
1. Download Master Branch.
0. Unzip contents into a folder.
0. Open up index.html in a web browser. Site will function offline.

To run locally, you can clone this repository by clicking the clone button on the repository or by typing ```git clone https://github.com/Ri-Dearg/horizon-photo``` into your terminal. To disconnect from this repository, type ```git remote rm origin``` into the terminal.

## Credits

### Content
All text content was generated by GPT-2 and lighlty edited at [Talk to Transformer](https://talktotransformer.com/).  
Any code utilised from a site is documented and credited within the code.

### Media
All photographs, authors, license rights, copyright, etc. used in this project can be found [here.]( https://unsplash.com/collections/8825126/used-in-horizon-photo)  
All other media used is my own.
