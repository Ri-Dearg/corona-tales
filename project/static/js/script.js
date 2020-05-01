function initTags(tagCreate, id) {

        var chips = document.querySelector(`#chips-${id}`);

        var instances = M.Chips.init(chips, {
            limit: 15,
            placeholder: 'Add Tags',
            secondaryPlaceholder: '+Tag',
            autocompleteOptions: {
                data: tagCreate,
                limit: 8,
            }
        });
}

function initStoryModal(id, content, tagList) {
        
        modal = document.querySelector(`#modal-${id}`);
        instance = M.Modal.init(modal, {
            onOpenStart: function () {
                if (id !== 'search') {
                    ClassicEditor
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

                if (tagList !== undefined) {
                    var instance = M.Chips.getInstance(document.querySelector(`#chips-${id}`))
                    for (i = 0; i < tagList.length; i++) {
                        instance.addChip({
                            tag: tagList[i]
                        });
                    }
                }
            },
            onOpenEnd: function () {
                if (id !== 'search') {
                    if (content !== undefined) {
                        newEditor.setData(content)
                    }
                }
            },
            onCloseEnd: function () {
                if (id !== 'search') {
                    newEditor.destroy()
                }
            }
        });
}

function showDate(id, timeStamp) {
    var time = Number(timeStamp)
    var date = new Date(time)

    const options = { day: 'numeric', month: 'short', year: 'numeric'};
    var dateString = date.toLocaleDateString(undefined, options)

    document.querySelector(`#date-med-${id}`).textContent = dateString
    document.querySelector(`#date-small-${id}`).textContent = dateString
}

function initFab() {
        var sideFab = document.querySelectorAll('.horizontal-button');
        var indexFab = document.querySelector('#button-index');
        var indexTap = document.querySelector('.tap-target');

        if (sideFab != null) {
            var instanceUser = M.FloatingActionButton.init(sideFab, {
                direction: 'left',
            })
        };
        if (indexFab != null) {
            var instanceIndex = M.FloatingActionButton.init(indexFab, {})
        };
        if (indexTap != null && !sessionStorage.Shown) {
            var instancesFeature = M.TapTarget.init(indexTap, {});
                instancesFeature.open()
                setTimeout(function(){ instancesFeature.close(); }, 4000)
                sessionStorage.Shown = 1;
        }

}

function formValid(formId) {
    document.addEventListener('DOMContentLoaded', function () {

        $("select[required]").css({ position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0 });

        $(`#form-${formId}`).on('submit', function (event) {
            var tagDict = M.Chips.getInstance($(`#chips-${formId}`)).chipsData
            var tagDictLength = Object.keys((M.Chips.getInstance($(`#chips-${formId}`)).chipsData)).length
            if (formId !== 'search') {
                var editorData = newEditor.getData().length
                if (tagDictLength === 0 || editorData === 0) {
                    event.preventDefault();
                    alert('Please fill Tags and Stories');
                    return false
                }
            }

            addTags(formId, tagDictLength, tagDict)
        });
    });
}

function addTags(formId, arrayLength, array) {

    for (i = 0; i < arrayLength; i++) {
        $(`#form-${formId}`).append(`<input type="hidden" name="tags" value="${array[i].tag.toLowerCase()}">`);
    }
    return true
}

function likeUnlike(id, functionUrl) {

        function like(ev) {
        ev.preventDefault();
        $.ajax({
        method: 'POST',
        url: functionUrl,
        data: $(this).serialize(),
        datatype: 'json',
        success: function(data) {
            $(`#like-tip-${id}`).attr('data-tooltip', `${data.toString()} Likes`)
        }
        });
        }

        $(`#form-like-${id}`).on('submit', like)
}

function scrollInit(tagList) {

        var getUrl = window.location;
        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
        var reg = new RegExp(".*?", "g")
        var tagUrl = getUrl .protocol + "//" + getUrl.host + "/" + 'search_tags/' + reg


        var scroll = document.querySelector('.infiniscroll');
        if (scroll != undefined) {

            var infScroll = new InfiniteScroll(scroll, {
                // options
                path: function () {
                    if (window.location.href === baseUrl || window.location.href === tagUrl) {
                        pageNumber = this.loadCount + 2
                        return window.location.href + '?page=' + pageNumber
                    }
                    else {
                        pageNumber = this.loadCount + 2
                        return window.location.href + '&page=' + pageNumber
                    }
                },
                append: '.scroll-append',
                checkLastPage: '.scroll-append',
                history: false,
                status: '.page-load-status'
            });

                infScroll.on( 'append', function( response, path, items ) {
                for (i=0; i < items.length; i++) {
                    var info = items[i].children
                    var storyId = info[0].innerText
                    showDate(storyId, info[1].innerText)
                    
                    if (getUrl.pathname == '/profile') {
                    var tags = JSON.parse(info[2].innerText)
                    var content = $(items).find(`#content-${storyId}`).html()
                    initFab();
                    initTags(tagList, storyId)
                    initStoryModal(storyId, content, tags)
                    formValid(storyId);
                    }
                }
            }); 
        }
    }


document.addEventListener('DOMContentLoaded', function () {
    M.AutoInit();

    var sideNav = document.querySelectorAll('.sidenav');
    var nav = M.Sidenav.init(sideNav, {
        edge:'right'
    });

    var datepicker = document.querySelectorAll('.datepicker');
    var dateChoose = M.Datepicker.init(datepicker, {
        container: 'body'
    });

    var singupLogin = document.querySelector('#modal-signup-login');
    var modalTab = M.Modal.init(singupLogin, {
        onOpenEnd: function () {
            var formTabs = document.querySelector('#form-tabs')
            var instance = M.Tabs.init(formTabs, {})
        }
    });

    $('.password-create').on('submit', function (event) {
        var passFirst = document.querySelector('.passone').value
        var passSecond = document.querySelector('.passtwo').value

        if (passFirst != passSecond) {
            alert('Passwords do not match. Please Try again.')
            return false
        }
    })
})

