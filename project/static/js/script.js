function initTags(tagCreate, id) {
    document.addEventListener('DOMContentLoaded', function () {

        var chips = document.querySelectorAll(`#chips${id}`);

        var instances = M.Chips.init(chips, {
            limit: 15,
            placeholder: 'Tags (Press Enter)',
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
        var modals = document.querySelector(`#modal${id}`);
        var instances = M.Modal.init(modals, {
            onOpenStart: function () {
                ClassicEditor
                    .create(document.querySelector(`#editor${id}`), {
                        removePlugins: ['Image', 'EasyImage', 'ImageUpload', 'Link', 'MediaEmbed', 'Heading']
                    })
                    .then(editor => {
                        newEditor = editor;
                    })
                    .catch(error => {
                        console.error(error);
                    });

                if (tagList !== undefined) {
                    var instance = M.Chips.getInstance(document.querySelector(`#chips${id}`))
                    for (i = 0; i < tagList.length; i++) {
                        console.log(instance)
                        instance.addChip({
                            tag: tagList[i]
                        });
                    }
                }
            },
            onOpenEnd: function () {
                if (content !== undefined) {
                    newEditor.setData(content[0])
                }
            },
            onCloseEnd: function () {
                newEditor.destroy()
            }
        });
    });
}

function initFab() {
    document.addEventListener('DOMContentLoaded', function () {
        var sideFab = document.querySelectorAll('.horizontal-button');
        var indexFab = document.querySelector('#buttonindex');
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
        if (indexTap != null) {
            var instancesFeature = M.TapTarget.init(indexTap, {});
                instancesFeature.open()
                setTimeout(function(){ instancesFeature.close(); }, 4000)
        }
    });
}

function formValid(formId) {
    document.addEventListener('DOMContentLoaded', function () {

        $("select[required]").css({ position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0 });

        $(`#form${formId}`).on('submit', function (event) {
            var tagDict = M.Chips.getInstance($('.chips')).chipsData
            var tagDictLength = Object.keys((M.Chips.getInstance($('.chips')).chipsData)).length
            var editorData = newEditor.getData().length;

            if (tagDictLength === 0 || editorData === 0) {
                event.preventDefault();
                alert('Please fill all fields');
                return false
            }

            else {
                addTags(formId, tagDictLength, tagDict)
            }
        });
    });
}

function addTags(formId, arrayLength, array) {

    for (i = 0; i < arrayLength; i++) {
        $(`#form${formId}`).append(`<input type="hidden" name="tags" value="${array[i].tag}">`);
    }
    return true
}

document.addEventListener('DOMContentLoaded', function () {
    M.AutoInit();

})
