/**
 * Created by Jack on 2016/10/14.
 */

function toggle(targetid) {
    if (document.getElementById(targetid)){
        target=document.getElementById(targetid);
        if(target.style.display=="block"){
            target.style.display="none";
        } else {
            target.style.display="block";
        }
    }
}

jQuery(function ($) {
    function show_reply_form(event) {
        var $this = $(this);
        var comment_id = $this.data("comment-id");

        $('#id_parent').val(comment_id);
        $('#form-comment').insertAfter($this.closest('.comment'));
    }

    function cancel_reply_form(event) {
        $('#id_comment').val('');
        $('#id_parent').val('');
        $('#form-comment').appendTo($('#wrap-form-comment'));
    }

    $.fn.ready(function () {
        $('.comment_reply_link').click(show_reply_form);
        $('#cancel_reply').click(cancel_reply_form);
    });

});

function setAuthenticatedUser() {
    $('#div_id_name').hide();
    $('#div_id_email').hide();
    $('#div_id_url').hide();
}
