# Horizon Photography

The site is desgined as a text-base story sharing platform based around the coronavirus epidemic. Its goal is to allow people to post, share and search experiences and opinions on the site. The inspiration came from the various ways people have begun to use social networking during the epidemic, in manners not sen before. I wanted to create a site which is based more on thoughtful exploration rather than instant gratification, such as Instagram or Facebook, but still allow for personalisation. Certain design choices which would be out of line with similar systems were made deliberately and will be explained.

Link to deployed project [here](https://corona-tales.herokuapp.com/).

## UX

### Outline

#### Home Page

##### Initial Viewing
The home page is desgined as a feed, with infinite scrolling, much like many social networks. A page preloader with a slow fade is placed covering content on all pages, the z-index has been placed under the navbar, so the nav persists from one page to the next. A different random quote on the topic of sharing is pulled from a hand-picked selection will be displayed as the Home page central graphic. I previously had a chart with information on the virus, but the further I developed the site, the less it was in theme. So, I chose a random quote, which I hope will help set the tone by having visitors reflect before reacting. On the very first load of each session, an alert will pop out from the floating menu to alert the user of its presence.

##### Story Section
Under this there is a "Featured" story section that is displayed first, followed by an non-featured story section. Feature stories are automatically set at 21 likes, but for the purpose of this project I have manually set some for display purposes. The stories in each section are ordered reverse chronologically, most recent first. The story list from the database will pull 100 stories maximum, featured and non-featured inclusive. Each story has a card as a basic design, with a user-selected color from a set pallet, allowing for personalisation but maintaining a coherent style. Each card is has its content truncated at 180px to maintain a consistent size and give a preview of the story. 
.

Images used are of full quality as I felt it necessary for a photographer's website that the best quality is always utilised. Loading blur is used where appropriate to ensure that the images will be loaded at full quality without disruption to the user experience.

#### Layouts, Colours and Styles
The layout utilised is simple, a sticky nav helps to navigate after scrolling down. The navbar collapses below medium devices as the spacing in the fonts becomes squahed on smaller devices. The logo shifts from the center on larger devices to the left side on smaller devices so it is always visible. The nav features only two obvious options for simplicity and a focus on what's important: the gallery. The footer contains basic options: newsletter, social links, contact. The gallery has a map with markers which, when clicked, open a gallery coressponding to the country. An infowindow opens, the map shifts to focus on it and after a few seconds the page automatically scrolls down to the images. Once the page shifts down an arrow appears that scrolls you back up to the map. The gallery is responsive and opens a large modal on an image click to highlight the photo, modal background is darkened significantly to highlight the photo. Contact page is simple and clean, with photographer info stacked on top of the form.

The main color used is black, to keep the design clean and to contrast with the colors of the photos so that they remain the focus. Secondary colors used are a silver-grey or white to continue the clean look. A deep green is used as an accent to add color and create a thematic connection with nature. The dark colors highlight the colors of the photographs much better than a lighter color. This theme is continued throughout the site to retain a minimalistic, clean design with a focus on the photographer's work.

The fonts are sans-serif in keeping with the clean, minimal design elements. An uppercase font is used to emphasise all headings. 

### User Stories
As a user interested in photography, I expect to see a varied photography portfolio.

As a user interested in travel, I expect to be able to explore locations through photography.

As a user interested in project work, I can use the contact form to reach the photographer.

### Wireframes
Wireframe: https://drive.google.com/open?id=17ZBPFFBDwHyMecXJiWNz-r5LhEaP79as

## Features

### Features implemented

- Map styled consistently with website
- Map zooms differently based on device size
- A map that is populated with markers featuring drop animation on load, bounce animation on selection
- Marker information pulled from REST Countries API
- Backup marker array so the map and gallery can still be populated if the API fails
- The function skips the infowindow as it would not be able to be populated
- Map has infowindow that auto-populates with content pulled from the API
- Map features a fully responsive gallery within an iframe
- Gallery auto-scrolls down after 2 seconds to iframe heading after selecting a marker
- An arrow that scrolls back to the map appears after scrolling down
- Iframe images, heading and blurb swap country on marker selection
- Iframe height auto adjust on window resize and iframe images loading
- All images use loading blur and thumbnail placeholders until they are fully loaded
- An image popup modal appears when an image is clicked to highlight it
- Form Validation
- The newsletter allows people to sign up to receive the blog posts to the their inbox.
- Modal with success/error response on filling in forms ons the site

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
- The image loading blur has been thoroughly tested and gone through numerous iterations to optimise the smoothness of the transition on different devices and internet speeds.
- Changes in the UI occur depending on size, such as map zoom level, navbar logo position, iframe height, modal size, image styling.
- In case the REST Countries API fails, I have implemented a secondary backup array which will populate the map markers and provide enough info to change the images in the iframe.
- Iframe adjusts height based on the content within and window size, as switching images often left images cut.
- Animation length has been adjusted to aid in smoothing the transition
- All forms have validation and will not submit without the proper information.
- Different functions are provided for the newsletter and contact form.
- Forms will clear their field upon successful submission and the page will not reload.
- A modal will clarify the success or the failure of the form submission and provide error codes.
- An auto-reply to the form submission has been implemented.
- For ease of use, the gallery automatically scrolls down to the iframe with the images amd an arrow is provided that scrolls back to the top.
- The fixed navabar covered the heading, so I created an offset div to scroll down to.
- External links open in a new tab.
- Images sytematically organised for iframe image switching functions.
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
