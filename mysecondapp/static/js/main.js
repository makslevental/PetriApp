$(document).ready(function () {
    //toggle `popup` / `inline` mode
    $.fn.editable.defaults.mode = 'inline';


//init editables
    $('.myeditable').editable({
        url: '/post' //this url will not be used for creating new user, it is only for update
    });

//make username required
    $('#required_firstname').editable('option', 'validate', function (v) {
        if (!v) return 'Required field!';
    });
    //make username required
    $('#required_lastname').editable('option', 'validate', function (v) {
        if (!v) return 'Required field!';
    });
    //make username required
    $('#required_phonenumber').editable('option', 'validate', function (v) {
        if (!v) return 'Required field!';
    });

//automatically show next editable
    $('.myeditable').on('save.newuser', function () {
        var that = this;
        setTimeout(function () {
            $(that).closest('tr').next().find('.myeditable').editable('show');
        }, 200);
    });

    //reset
    $('#reset-btn').click(function () {
        $('.myeditable').editable('setValue', null)
            .editable('option', 'pk', null)
            .removeClass('editable-unsaved');

        $('#save-btn').show();
        $('#msg').hide();
    });



    $('#save-btn').click(function () {
        $('.myeditable').editable('submit', {
            url: '/newuser',
            ajaxOptions: {
                dataType: 'json' //assuming json response
            },
            success: function (data, config) {
                if (data && data.id) {  //record created, response like {"id": 2}
                    //set pk
                    $(this).editable('option', 'pk', data.id);
                    //remove unsaved class
                    $(this).removeClass('editable-unsaved');
                    //show messages
                    var msg = 'New user created! Now editables submit individually.';
                    $('#msg').addClass('alert-success').removeClass('alert-error').html(msg).show();
                    $('#save-btn').hide();
                    $(this).off('save.newuser');
                } else if (data && data.errors) {
                    //server-side validation error, response like {"errors": {"username": "username already exist"} }
                    config.error.call(this, data.errors);
                }
            },
            error: function (errors) {
                var msg = '';
                if (errors && errors.responseText) { //ajax error, errors = xhr object
                    msg = errors.responseText;
                } else { //validation error (client-side or server-side)
                    $.each(errors, function (k, v) {
                        msg += k + ": " + v + "<br>";
                    });
                }
                $('#msg').removeClass('alert-success').addClass('alert-error').html(msg).show();
            }
        });
    });












    //make username editable
//    $('#firstname1').editable();
//    $('#lastname1').editable();
//    $('#phonenumber1').editable();
    //make status editable
    $('#status').editable({
        type: 'select',
        title: 'Select status',
        placement: 'right',
        value: 2,
        source: [
            {value: 1, text: 'status 1'},
            {value: 2, text: 'status 2'},
            {value: 3, text: 'status 3'}
        ]
        /*
         //uncomment these lines to send data on server
         ,pk: 1
         ,url: '/post'
         */
    });
});
