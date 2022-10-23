/*! jQuery v3.6.0 | (c) OpenJS Foundation and other contributors | jquery.org/license */
$( document ).on ('click', id='#ajax-btn', function(event) {
    console.log('step1');

    $.ajax({
            url: '/user/update-token-ajax/',
            success: function (data) {
                        console.log(data);
                        $('#token').html(data.key);
                        }

    });


});