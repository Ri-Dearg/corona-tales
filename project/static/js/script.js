/**
 * Changes the timestamp from milliseconds to a readable format and places it within the story card
 * @param {string} id - a unique id for that story which can be used to identify the correct div
 * @param {string} timeStamp - a string passed from python that is the date in milliseconds
 */
function showDate(id, timeStamp) {
    var time = Number(timeStamp)
    var date = new Date(time)

    const options = { day: 'numeric', month: 'short', year: 'numeric' };  // Sets format for dates
    var dateString = date.toLocaleDateString(undefined, options)

    document.querySelector(`#date-med-${id}`).textContent = dateString  // Places the dates on the cards
    document.querySelector(`#date-small-${id}`).textContent = dateString
}


/**
 * Initiates Materialize's floating action buttons.
 * Initiates the alert that draws attention to the menu on the first page viewing.
 */
function initFab() {
    var indexFab = document.querySelector('#button-index');  // Selects the FAB that is on every page
    var indexTap = document.querySelector('.tap-target');  // The one-time alert

    var instanceIndex = M.FloatingActionButton.init(indexFab, {});

    if (indexTap != null && !sessionStorage.Shown) {  // Runs only if it hasn't been run before
        var instancesFeature = M.TapTarget.init(indexTap, {});  // Creates the alert
        instancesFeature.open()
        setTimeout(function () { instancesFeature.close(); }, 5000);
        sessionStorage.Shown = 1;  // Saves value after it is run once for this session
    }
}


/**
 * Initializes the edit button fab on the profile page. Does each seperately so intiated buttons
 * do not reinitiate when new content is added to the page.
 */
function initEditFab(id) {
    var sideFab = document.querySelector(`#button-${id}`);  // Selects the edit story button
    if (sideFab != null) { // Initiates only if it is present
        var instanceUser = M.FloatingActionButton.init(sideFab, { 
            direction: 'left',
        });
    }
}


/**
 * Initiates the select drop downs on the appended edit modals for the profile page
 */
function initSelect() {
    var select = document.querySelectorAll('select');
    var selectEdits = M.FormSelect.init(select, {});
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

    modal = document.querySelector(`#modal-${id}`);  // Selects a story modal div
    instance = M.Modal.init(modal, {  // initiates modal on that div
        onOpenStart: function () {  // Creates a CKeditor instance on the modal textarea when opened
            if (id !== 'search') {  // as long as the modal isn't the search modal
                ClassicEditor
                    .create(document.querySelector(`#editor-${id}`), {  // removes unused plugins
                        removePlugins: ['Image', 'EasyImage', 'ImageUpload', 'Link', 'MediaEmbed', 'Heading']
                    })
                    .then(editor => {
                        newEditor = editor;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            }
            if (storyTags !== undefined) {  // Checks to see if tag data has been passed for that story
                                          // and populates the chips tagdata with it
                var instance = M.Chips.getInstance(document.querySelector(`#chips-${id}`))
                for (i = 0; i < storyTags.length; i++) {
                    instance.addChip({
                        tag: storyTags[i]
                    });
                }
            }
        },
        onOpenEnd: function () {
            if (id !== 'search') {
                if (content !== undefined) {  // Sets the CKEditor content to the story content
                    newEditor.setData(content)
                }
            }
        },
        onCloseEnd: function () {
            if (id !== 'search') {  // Destoys the CKEditor instance on close so there will only
                                    // ever be one instance
                newEditor.destroy()
            }
        }
    });
}


/**
 * Appends the tags as hidden input in the forms before it is sent off with the form
 * @param {string} id - a unique id for that story which can be used to send those specific tags and form
 * @param {int} tagDictLength - Length of tag array
 * @param {Object[]} tagDict - the list of tags
 */
function addTags(id, tagDictLength, tagDict) {
    for (i = 0; i < tagDictLength; i++) {  // Cycles through each dictionary pair and appends the tag as a value
        $(`#form-${id}`).append(`<input type="hidden" name="tags" value="${tagDict[i].tag.toLowerCase()}">`);
    }
    return true
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
        var tagDict = M.Chips.getInstance($(`#chips-${id}`)).chipsData  // Gets entered tag data
        var tagDictLength = Object.keys((M.Chips.getInstance($(`#chips-${id}`)).chipsData)).length
        
        if (id !== 'search') {
            var editorData = newEditor.getData().length
            if (tagDictLength === 0 || editorData === 0) { // Checks to see if either the tags or textarea have no content
                event.preventDefault();
                alert('Please fill Tags and Stories');
                return false
            }
        }
        addTags(id, tagDictLength, tagDict)  // Adds tags to be submitted to form
    });
}


/**
 * Receives the like button press, prevents the page reload and runs the funxtion that
 * passes the info to Python.When it receives the data it swaps the icon on the heart 
 * to indicate liked/not liked.
 * @param {string} id - a unique id for that story which identifies the correct like button
 */
function likeUnlike(id) {
    function like(ev) {
        ev.preventDefault();
        $.ajax({
            method: 'POST',
            url: '/like',
            data: $(this).serialize(),
            datatype: 'json',
            success: function (data) {
                if ($(`#heart-${id}`).text() === 'favorite') {
                    $(`#heart-${id}`).text('favorite_border');
                }
                else {
                    $(`#heart-${id}`).text('favorite');
                }
                $(`#like-info-${id}`).attr('data-tooltip', `${data.toString()} likes`);
                $(`#like-tip-${id}`).text(`${data.toString()} likes`);
                $(`#like-tip-${id}`).fadeIn(600, function () {
                    setTimeout(function () {
                        $(`#like-tip-${id}`).fadeOut(600);
                    }, 2000);
                });
            }
        });
    }
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
        path: function () {  // correctly chooses pagination url depending on page
            if (getUrl.href === baseUrl || getUrl.pathname.split('/')[1] === "search_tags") {
                var pageNumber = this.loadCount + 2
                return getUrl.href + '?page=' + pageNumber
            } else if (getUrl.hash == '#user-settings') {  // necessary for url recognition as flask can redirect to this tab
                var pageNumber = this.loadCount + 2
                return getUrl.pathname + '?page=' + pageNumber
            } else {
                var pageNumber = this.loadCount + 2
                return getUrl.href + '&page=' + pageNumber
            }
        },
        append: '.scroll-append',  // appends story cards to the section
        checkLastPage: '.scroll-append',
        history: false,
        status: '.page-load-status',
    });

    infScroll.on('append', function (response, path, items) {  // Fires funtions when items are appended
        for (i = 0; i < items.length; i++) {
            var info = items[i].children
            var storyId = info[0].innerText
            initBaseStory(storyId, info[1].innerText)  // reinitiates functions for new dynamic content

            if (getUrl.pathname == '/profile') {  // reinitiates materialize components for the profile page edit button
                var storyTags = JSON.parse(info[2].innerText)
                var content = $(items).find(`#content-${storyId}`).html()
                initEditStory(tagList, storyId, content, storyTags)
                initSelect();
            }
        }
    });
    return infScroll
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
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];

    var scroll = document.querySelector('.infiniscroll');

    if (scroll != undefined && getUrl.hash !== '#user-settings') {  // will not fire on user settings
        infScroll = new createScroll(getUrl, baseUrl, scroll, tagList);
    }
    
    $('#tab-settings').on('click', function() { 
        infScroll.destroy();
    });

    $('#tab-user-stories').on('click', function() {
        infScroll = new createScroll(getUrl, baseUrl, scroll)
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
 * Initiates the dates and the like system for the stories on the index and the search page.
 * @param {string} id - a unique id for that story which identifies the correct like button
 * @param {string} timestamp - a string passed from python that is the date in milliseconds
 */
function initBaseStory(id, timestamp) {
    showDate(id, timestamp);
    likeUnlike(id)
}


/**
 * Initiates functions for story editing on the user's profile page
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
    M.AutoInit();  // Initiates all auto-initiated Materialize components


    var sideNav = document.querySelectorAll('.sidenav');  // initiates the sidenav on the right side
    var nav = M.Sidenav.init(sideNav, {
        edge: 'right'
    });


    var datepicker = document.querySelectorAll('.datepicker');  // initiates the datepicker
    var dateChoose = M.Datepicker.init(datepicker, {
        container: 'body'
    });


    var singupLogin = document.querySelector('#modal-signup-login');  // Initiates the modal for signup / login
    var modalTab = M.Modal.init(singupLogin, {  // necesarry as there is a bug when you use tabs within a modal
        onOpenEnd: function () {
            var formTabs = document.querySelector('#form-tabs')  // initiates the tabs
            var instance = M.Tabs.init(formTabs, {})
        }
    });

    $('.password-create').on('submit', function (event) { // confirms that the two entered passwords are the same.
        var passFirst = document.querySelector('.passone').value
        var passSecond = document.querySelector('.passtwo').value

        if (passFirst != passSecond) {  // Prevents form entry of they are not
            alert('Passwords do not match. Please Try again.');
            return false
        }
    });
});

