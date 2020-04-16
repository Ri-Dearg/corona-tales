document.addEventListener('DOMContentLoaded', function() {
    M.AutoInit();

    $("select[required]").css({position: 'absolute', display: 'inline', height: 0, padding: 0, width: 0});
})

function initTags(tagCreate) {
    var chips = document.querySelectorAll('.chips');
    var instances = M.Chips.init(chips, {
    limit: 15,
    placeholder: 'Enter a Tag', 
    secondaryPlaceholder: '+Tag',
    onChipAdd: function() {
        console.log(M.Chips.getInstance($('.chips')).chipsData[0].tag)
        console.log(Object.keys((M.Chips.getInstance($('.chips')).chipsData)).length)
    },
    autocompleteOptions: {
        data: tagCreate,
        limit: 8,
    }

});
}

/*
    var tagDict = M.Chips.getInstance($('.chips')).chipsData
    var tagDictLength = Object.keys((M.Chips.getInstance($('.chips')).chipsData)).length

    function addTags(length, array) {
        for (i=0; i < length; i++) {
            console.log(array[i].tag);
            $("#create-story").append(`<input type="hidden" name="tags" value="${array[i].tag}">`);
            return true;
        }
    }


    $("#post-story").on('submit', function(event) {
        addTags(tagDictLength, tagDict)
        event.preventDefault
    });
});
*/
