function initTags(tagCreate, id) {
    document.addEventListener('DOMContentLoaded', function () {

        var chips = document.querySelectorAll(`#chips-${id}`);

        var instances = M.Chips.init(chips, {
            limit: 15,
            placeholder: 'Add Tags',
            secondaryPlaceholder: '+Tag',
            autocompleteOptions: {
                data: tagCreate,
                limit: 8,
            }
        });
    });
}

function initStoryModal(id, content, tagList) {
    document.addEventListener('DOMContentLoaded', function () {
        var modals = document.querySelector(`#modal-${id}`);
        var instances = M.Modal.init(modals, {
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
    document.addEventListener('DOMContentLoaded', function () {
        var sideFab = document.querySelectorAll('.horizontal-button');
        var indexFab = document.querySelector('#button-index');
        var indexTap = document.querySelector('.tap-target');

        if (sideFab != null) {
            var instanceUser = M.FloatingActionButton.init(sideFab, {
                direction: 'left',
                hoverEnabled: false
            })
        };
        if (indexFab != null) {
            var instanceIndex = M.FloatingActionButton.init(indexFab, {
                hoverEnabled: false
            })
        };
        if (indexTap != null && !sessionStorage.Shown) {
            var instancesFeature = M.TapTarget.init(indexTap, {});
                instancesFeature.open()
                setTimeout(function(){ instancesFeature.close(); }, 4000)
                sessionStorage.Shown = 1;
        }
    });
}

function formValid(formId) {
    document.addEventListener('DOMContentLoaded', function () {

        $("select[required]").css({ position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0 });

        $(`#form-${formId}`).on('submit', function (event) {
            var tagDict = M.Chips.getInstance($(`#chips-${formId}`)).chipsData
            var tagDictLength = Object.keys((M.Chips.getInstance($(`#chips-${formId}`)).chipsData)).length
            var editorData = newEditor.getData().length
                            
            if (fromId !== 'search') {
                if (tagDictLength === 0 || editorData === 0) {
                    event.preventDefault();
                    alert('Please fill Tags and Stories');
                    return false
                }
            }

            else {
                addTags(formId, tagDictLength, tagDict)
            }
        });
    });
}

function addTags(formId, arrayLength, array) {

    for (i = 0; i < arrayLength; i++) {
        $(`#form-${formId}`).append(`<input type="hidden" name="tags" value="${array[i].tag}">`);
    }
    return true
}

document.addEventListener('DOMContentLoaded', function () {
    M.AutoInit();

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

