/**
 * Fades the preloader once content is loaded.
 */
function fadePreload() {
    $('.preloader').fadeOut(1800);
}


/**
 * Changes the timestamp from milliseconds to a readable format and places it within the story card
 * @param {string} id - a unique id for that story which can be used to identify the correct div
 * @param {string} timeStamp - a string passed from python that is the date in milliseconds
 */
function showDate(id, timeStamp) {
    var time = Number(timeStamp);
    var date = new Date(time);

    // Sets format for dates
    const options = { day: 'numeric', month: 'short', year: 'numeric' };
    var dateString = date.toLocaleDateString(undefined, options);

    // Places the dates on the cards
    document.querySelector(`#date-med-${id}`).textContent = dateString;
    document.querySelector(`#date-small-${id}`).textContent = dateString;
}



/**
 * Applies the relevant classes to long stories that reqire truncating, so that the story is cut
 * It also places the button to read more. On other stories, while the div is present, it cannot
 * be clicked.
 * @param {string} id - a unique id for that story which can be used to identify the correct div
 */
function truncate(id) {
    var truncate = $(`#truncate-${id}`);
    var readButton = $(`#show-${id}`);
    if (truncate.height() > 180) {
        truncate.addClass('hide-content')
        readButton.html('<a>Read More</a>')
    }
}

/**
 * Animates the change from truncated content to fully displayed content
 *  code adapted from https://stackoverflow.com/questions/5003220/animate-element-to-auto-height-with-jquery
 * @param {string} id - a unique id for that story which can be used to identify the correct div
 */
function clickToShow(id) {
    $(`#show-${id}.click-to-show`).on('click', function () {
        var truncate = $(`#truncate-${id}`);
        // The 'toggled' class is added after the content is opened, so if it is toggled it closes to the same height.
        if ($(`#show-${id}`).hasClass('toggled')) {
            $(`#show-${id}`).removeClass('toggled').html('<a>Read More</a>');
            truncate.stop().animate({
                height: '180px'
            }, 1200);
        // Otherwise it opens the content to the correct height by setting content to auto before animation
        } else {
            $(`#show-${id}`).addClass('toggled').html('<a>Close</a>');
            var previewHeight = truncate.height();
            var contentHeight = truncate.css('height', 'auto').height();
            truncate.height(previewHeight);
            truncate.stop().animate({
                height: contentHeight
            }, 1200);
        }
    });
}


/**
 * Initiates Materialize's floating action buttons.
 * Initiates the alert that draws attention to the menu on the first page viewing.
 */
function initFab() {
    // Selects the FAB that is on every page  
    var indexFab = document.querySelector('#button-index');
    // The one-time alert
    var indexTap = document.querySelector('.tap-target'); 

    var instanceIndex = M.FloatingActionButton.init(indexFab, {});

    // Runs only if it hasn't been run before
    if (indexTap != null && !sessionStorage.Shown) { 
        // Creates the alert
        var instancesFeature = M.TapTarget.init(indexTap, {});  
        instancesFeature.open();
        setTimeout(function () { instancesFeature.close(); }, 5000);
        // Saves value after it is run once for this session
        sessionStorage.Shown = 1;  
    }
}


/**
 * Initializes the edit button fab on the profile page. Does each seperately so intiated buttons
 * do not reinitiate when new content is added to the page.
 */
function initEditFab(id) {
    // Selects the edit story button
    var sideFab = document.querySelector(`#button-${id}`);  
    // Initiates only if it is present
    if (sideFab != null) { 
        var instanceUser = M.FloatingActionButton.init(sideFab, {
            direction: 'left',
        });
    }
}


/**
 * ANimates the tooltips on open and close using classes from Materialize CSS
 */
function tipAnim() {
    $('.fixed-action-btn').hover(
        function () {
            // Tooltip becomes visible
            $('.mobile-fab-tip').addClass('scale-in');
        },
        function () {
            // Tooltip disappears
            $('.mobile-fab-tip').removeClass('scale-in');
        });
}


/**
 * Initiates the select drop downs on the appended edit modals for the profile page
 */
function initSelect() {
    var select = document.querySelectorAll('select');
    var selectEdits = M.FormSelect.init(select, {});
}


/**
 * Changes background color of the select menu color select dropdown
 */
function colorChange() {
    $("span:contains('Red')").hover(function () {
        $(this).addClass('red-sel');
    }, function () {
        $(this).removeClass('red-sel');
    });
    $("span:contains('Deep-Orange')").hover(function () {
        $(this).addClass('dorange-sel');
    }, function () {
        $(this).removeClass('dorange-sel');
    });
    $("span:contains('Orange')").hover(function () {
        $(this).addClass('orange-sel');
    }, function () {
        $(this).removeClass('orange-sel');
    });
    $("span:contains('Amber')").hover(function () {
        $(this).addClass('amber-sel');
    }, function () {
        $(this).removeClass('amber-sel');
    });
    $("span:contains('Yellow')").hover(function () {
        $(this).addClass('yellow-sel');
    }, function () {
        $(this).removeClass('yellow-sel');
    });
    $("span:contains('Lime')").hover(function () {
        $(this).addClass('lime-sel');
    }, function () {
        $(this).removeClass('lime-sel');
    });
    $("span:contains('Light-Green')").hover(function () {
        $(this).addClass('lgreen-sel');
    }, function () {
        $(this).removeClass('lgreen-sel');
    });
    $("span:contains('Green')").hover(function () {
        $(this).addClass('green-sel');
    }, function () {
        $(this).removeClass('green-sel');
    });
    $("span:contains('Teal')").hover(function () {
        $(this).addClass('teal-sel');
    }, function () {
        $(this).removeClass('teal-sel');
    });
    $("span:contains('Cyan')").hover(function () {
        $(this).addClass('cyan-sel');
    }, function () {
        $(this).removeClass('cyan-sel');
    });
    $("span:contains('Light-Blue')").hover(function () {
        $(this).addClass('lblue-sel');
    }, function () {
        $(this).removeClass('lblue-sel');
    });
    $("span:contains('Blue')").hover(function () {
        $(this).addClass('blue-sel');
    }, function () {
        $(this).removeClass('blue-sel');
    });
    $("span:contains('Indigo')").hover(function () {
        $(this).addClass('indigo-sel');
    }, function () {
        $(this).removeClass('indigo-sel');
    });
    $("span:contains('Deep-Purple')").hover(function () {
        $(this).addClass('dpurple-sel');
    }, function () {
        $(this).removeClass('dpurple-sel');
    });
    $("span:contains('Purple')").hover(function () {
        $(this).addClass('purple-sel');
    }, function () {
        $(this).removeClass('purple-sel');
    });
    $("span:contains('Pink')").hover(function () {
        $(this).addClass('pink-sel');
    }, function () {
        $(this).removeClass('pink-sel');
    });
}


/** Initiates the materialize 'chips' component
 * @param {Object<string, null>} tagList - takes a dictionary of tags to fill the autocomplete for that chips instance
 * @param {string} id - a unique id for that story which can be used to create that chips instance
 */
function initTags(tagList, id) {

    var chips = document.querySelector(`#chips-${id}`);  // identifies a place for a necessary chips instance

    var instances = M.Chips.init(chips, {
        limit: 15,
        placeholder: 'Add Tags',
        secondaryPlaceholder: 'Press Enter',
        autocompleteOptions: {
            data: tagList, // Uses tag object for autofill info
            limit: 8,
        }
    });
}


/** Initiates the modal used for creating and editing stories
 * @param {string} id - a unique id for that story which can be used to create that modal instance
 * @param {string} [content] - retrieves info for a written story and populates CKeditor with that info
 * @param {Object[]} [storyTags] - an array containing the tags used in a given story
 */
function initStoryModal(id, content, storyTags) {
    // Selects a story modal div
    modal = document.querySelector(`#modal-${id}`);  
    // initiates modal on that div
    instance = M.Modal.init(modal, { 
        // Creates a CKeditor instance on the modal textarea when opened
        onOpenStart: function () { 
            // as long as the modal isn't the search modal
            if (id !== 'search') {  
                ClassicEditor
                    // removes unused plugins
                    .create(document.querySelector(`#editor-${id}`), {  
                        removePlugins: ['Image', 'EasyImage', 'ImageUpload', 'Link', 'MediaEmbed', 'Heading']
                    })
                    .then(editor => {
                        newEditor = editor;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            }
            // Checks to see if tag data has been passed for that story
            if (storyTags !== undefined) {  
                // and populates the chips tagdata with it
                var instance = M.Chips.getInstance(document.querySelector(`#chips-${id}`));
                for (i = 0; i < storyTags.length; i++) {
                    instance.addChip({
                        tag: storyTags[i]
                    });
                }
            }
        },
        onOpenEnd: function () {
            if (id !== 'search') {
                // Sets the CKEditor content to the story content
                if (content !== undefined) {  
                    newEditor.setData(content);
                }
            }
        },
        onCloseEnd: function () {
            // Destoys the CKEditor instance on close so there will only
            if (id !== 'search') {  
                // ever be one instance
                newEditor.destroy();
            }
        }
    });
    deleteModal = document.querySelector(`#delete-${id}`);
    deleteInstance = M.Modal.init(deleteModal, {});
}


/**
 * Appends the tags as hidden input in the forms before it is sent off with the form
 * @param {string} id - a unique id for that story which can be used to send those specific tags and form
 * @param {int} tagDictLength - Length of tag array
 * @param {Object[]} tagDict - the list of tags
 */
function addTags(id, tagDictLength, tagDict) {
    // Cycles through each dictionary pair and appends the tag as a value
    for (i = 0; i < tagDictLength; i++) {  
        $(`#form-${id}`).append(`<input type="hidden" name="tags" value="${tagDict[i].tag.toLowerCase()}">`);
    }
    return true;
}


/**
 * Validates fields in submitted forms that do not accept the 'required' HTML attribute
 * Passes Tag information from chips, back into the form to be sent away as chips
 * does not automatically send data in forms.
 * @param {string} id - a unique id for that form used to identify the correct story and tag content
 */
function formValid(id) {

    // Validates select fields on forms as Materialize does not natively support this.
    $("select[required]").css({ position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0 });

    $(`#form-${id}`).on('submit', function (event) {
        // Gets entered tag data
        var tagDict = M.Chips.getInstance($(`#chips-${id}`)).chipsData;  
        var tagDictLength = Object.keys((M.Chips.getInstance($(`#chips-${id}`)).chipsData)).length;

        if (id !== 'search') {
            var editorData = newEditor.getData().length;
            // Checks to see if either the tags or textarea have no content
            if (tagDictLength === 0 || editorData === 0) { 
                event.preventDefault();
                alert('Please fill Tags and Stories');
                return false;
            }
        }
        // Adds tags to be submitted to form
        addTags(id, tagDictLength, tagDict);  
    });
}


/**
 * Receives the like button press, prevents the page reload and runs the funxtion that
 * passes the info to Python.When it receives the data it swaps the icon on the heart 
 * to indicate liked/not liked.
 * @param {string} id - a unique id for that story which identifies the correct like button
 */
function likeUnlike(id) {

    /**
     * Runs the form to like the post through an ajax function.
     */
    function like(ev) {
        // stops form from sending
        ev.preventDefault();
        // Sends form to flask view
        $.ajax({
            method: 'POST',
            url: '/like',
            data: $(this).serialize(),
            datatype: 'json',
            success: function (data) {
                // If content is already liked, swaps the icon and plays the unlike sound on successful response
                if ($(`#heart-${id}`).text() === 'favorite') {
                    var unlikeAudio = new Audio('/static/audio/pop-cork.wav');
                    unlikeAudio.play();
                    $(`#heart-${id}`).text('favorite_border');
                }
                // Otherwise it likes it and plays the corresponding sound
                else {
                    var likeAudio = new Audio('/static/audio/blop.wav');
                    likeAudio.play();
                    $(`#heart-${id}`).text('favorite');
                }
                // Displays the number of strings and animates the fade-in and out
                $(`#like-info-${id}`).attr('data-tooltip', `${data.toString()} likes`);
                $(`#like-tip-${id}`).text(`${data.toString()} likes`);
                $(`#like-tip-${id}`).fadeIn(600, function () {
                    setTimeout(function () {
                        $(`#like-tip-${id}`).fadeOut(600);
                    }, 3000);
                });
            }
        });
    }
    // Waits for the like button press before firing off the function
    $(`#form-like-${id}`).on('submit', like);
}


/**
 * Creates infinite scroll instances and runs the functions to reinitiate
 * Materialize components for dynamically created content. Without this the components will not
 * function
 * @param {string} getUrl - identifies current full url so it can load pagination correctly 
 * @param {string} baseUrl - The url to the base pathname
 * @param {Object} elem - the element to attach the scroll to
 * @param {Object[]} tagList - An array of tags to use for chips autocomplete
 */
function createScroll(getUrl, baseUrl, elem, tagList) {
    var infScroll = new InfiniteScroll(elem, {
        // correctly chooses pagination url depending on page
        path: function () { 
            var pageNumber = this.loadCount + 2;
            if (getUrl.href === baseUrl || getUrl.pathname.split('/')[1] === "search_tags") {
                return getUrl.href + '?page=' + pageNumber;
            // necessary for url recognition as flask can redirect to this tab
            } else if (getUrl.hash == '#user-settings') {  
                return getUrl.pathname + '?page=' + pageNumber;
            } else {
                return getUrl.href + '&page=' + pageNumber;
            }
        },
        // appends story cards to the section
        append: '.scroll-append',  
        checkLastPage: '.scroll-append',
        history: false,
        status: '.page-load-status',
    });

    // Fires funtions when items are appended
    infScroll.on('append', function (response, path, items) {  
        for (i = 0; i < items.length; i++) {
            var info = items[i].children;
            var storyId = info[0].innerText;
            // reinitiates functions for new dynamic content
            initBaseStory(storyId, info[1].innerText);

            // reinitiates materialize components for the profile page edit button
            if (getUrl.pathname == '/profile') {  
                var storyTags = JSON.parse(info[2].innerText);
                var content = $(items).find(`#truncate-${storyId}`).html();
                initEditStory(tagList, storyId, content, storyTags);
                initSelect();
                colorChange();
                tipAnim();
            }
        }
    });
    return infScroll;
}


/**
 * Initiates the infinite scroll in different ways depending on the circumstances.
 * Checks for the existence of a section to append to before initializing
 * Will not initialize if the url is set to the user's tab as it will incorrectly load
 * and try to append stories when reaching the bottom of the user settings tab.
 * To rectify this it isn't initialised on redirect to that page, additionally, on switching
 * to that tab, the instance is destoyed, so it won't fire at the bottom of that page.
 * it is recreated when switching to the user story feed, so it can append on the correct tab only.
 * @param {Object<string, null>} tagList - An array of tags to use for chips autocomplete
 */
function initScroll(tagList) {
    // Declares locations for URLs so Infinite Scroll can correctly append stories from paginated content
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
    var scroll = document.querySelector('.infiniscroll');

    // will not fire on user settings
    if (scroll != undefined && getUrl.hash !== '#user-settings') {  
        infScroll = new createScroll(getUrl, baseUrl, scroll, tagList);
    }

    $('#tab-settings').on('click', function () {
        infScroll.destroy();
    });

    
    $('#tab-user-stories').on('click', function () {
        infScroll = new createScroll(getUrl, baseUrl, scroll);
    });

}

/**
 * Initiates the modals used for searching and posring stories on every page
 * @param {Object<string, null>} tagList - An array of tags to use for chips autocomplete
 * @param {string} id - a unique id for that story which identifies the correct like button
 */
function initMenu(tagList, id) {
    initTags(tagList, id);
    initStoryModal(id);
    formValid(id);
}


/**
 * Initiates the dates, color and the like system for the stories on the index and the search page.
 * If a function is necessary for every story, it can be added here.
 * @param {string} id - a unique id for that story which identifies the correct like button
 * @param {string} timestamp - a string passed from python that is the date in milliseconds
 */
function initBaseStory(id, timestamp) {
    showDate(id, timestamp);
    likeUnlike(id);
    truncate(id);
    clickToShow(id);
}


/**
 * Initiates functions for story editing on the user's profile page.
 * If a function is necessary only for editing stories, it can be added here.
 * @param {Object<string, null>} tagList - An array of tags to use for chips autocomplete
 * @param {string} id - a unique id for that story which identifies the correct like button
 * @param {string} [content] - retrieves info for a written story and populates CKeditor with that info
 * @param {Object[]} [storyTags] - an array containing the tags used in a given story
 */
function initEditStory(tagList, id, content, storyTags) {
    initEditFab(id);
    initTags(tagList, id);
    initStoryModal(id, content, storyTags);
    formValid(id);
}


/**
 * Functions to fire off on page load. Mostly initiating Materialize components.
 * Also used for password verification
 */
document.addEventListener('DOMContentLoaded', function () {

    // Runs the fade for the preloader once content has loaded.
    window.addEventListener('load', fadePreload());

    // Initiates all auto-initiated Materialize components
    M.AutoInit();  

    // ANimates the tooltips on menues
    tipAnim();

    // Colors change while hovering over select menus.
    colorChange();

    // initiates the sidenav on the right side
    var sideNav = document.querySelectorAll('.sidenav');
    var nav = M.Sidenav.init(sideNav, {
        edge: 'right'
    });

    // initiates the datepicker
    var datepicker = document.querySelectorAll('.datepicker');  
    var dateChoose = M.Datepicker.init(datepicker, {
        container: 'body'
    });


    // Initiates the modal for signup / login
    var singupLogin = document.querySelector('#modal-signup-login');
    // necesarry as there is a bug when you use tabs within a modal  
    var modalTab = M.Modal.init(singupLogin, {  
        onOpenEnd: function () {
            // initiates the tabs
            var formTabs = document.querySelector('#form-tabs');  
            var instance = M.Tabs.init(formTabs, {});
        }
    });

    // confirms that the two entered passwords are the same.
    $('.password-create').on('submit', function (event) { 
        var passFirst = document.querySelector('.passone').value;
        var passSecond = document.querySelector('.passtwo').value;

        // Prevents form entry of they are not identical
        if (passFirst != passSecond) {  
            alert('Passwords do not match. Please Try again.');
            return false;
        }
    });

    /**
     * If we are on the index page, this runs to select a random quote from the JSON file to place on the main site page.
     */
    if (window.location.pathname == '/') {
        $.getJSON('static/js/quotes.json', function (data) {
            var quoteLength = data.length;
            i = Math.floor(Math.random() * quoteLength);
            $('#splash-text').text(data[i].text);
            $('#splash-author').text(`- ${data[i].author}`);
        });
    }
});