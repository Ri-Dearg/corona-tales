document.addEventListener('DOMContentLoaded', function () {
    ClassicEditor
        .create(document.querySelector('#editor'), {
            removePlugins: ['Image', 'EasyImage', 'ImageUpload', 'Link', 'MediaEmbed']
        })
        .then(newEditor => {
            editor = newEditor;
        })
        .catch(error => {
            console.error(error);
        });

    /*document.querySelector( '#submit' ).addEventListener( 'click', () => {
        const editorData = editor.getData().length;
        if( !messageLength ) {
            alert( 'Please enter a message' );
            e.preventDefault();
        }});*/
});