(function ($) {
    M.AutoInit();// end of document ready
})(jQuery); // end of jQuery name space

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {});

});
