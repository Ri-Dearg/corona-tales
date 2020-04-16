document.addEventListener('DOMContentLoaded', function() {
    M.AutoInit();

    $("select[required]").css({position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0});
})

function initTags(tagCreate) {
    document.addEventListener('DOMContentLoaded', function() {
        var chips = document.querySelectorAll('.chips');
        
        var instances = M.Chips.init(chips, {
            limit: 15,
            placeholder: 'Enter a Tag', 
            secondaryPlaceholder: '+Tag',
            autocompleteOptions: {
                data: tagCreate,
                limit: 8,
            }
        });

        function addTags(length, array) {
            for (i=0; i < length; i++) {
                console.log(array[i].tag);
                $("#create-story").append(`<input type="hidden" name="tags" value="${array[i].tag}">`);
            }
        }
        
        $("#create-story").on('submit', function(event) {
            var tagDict = M.Chips.getInstance($('.chips')).chipsData
            var tagDictLength = Object.keys((M.Chips.getInstance($('.chips')).chipsData)).length

            addTags(tagDictLength, tagDict)
    });
    })
};