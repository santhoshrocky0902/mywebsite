$(document).ready(function() {

    /* minimum screen width size 400*/
    //  if (screen.width < 400) {
    //    var mvp = document.getElementById('webviewport');
    //    mvp.setAttribute('content', 'width=400, initial-scale=1.0');
    //  }

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-12460194-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'https://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();

    $('#subscribe').submit(function(e) {
        e.preventDefault();
        $(".message").empty();
        if (!valid_email_address($("#email").val())) {
            $(".message").html('Please make sure you enter a valid email address.');
        } else {
            $.ajax({
                url: 'check.php',
                data: $('#subscribe').serialize(),
                type: 'POST',
                dataType: 'JSON',
                beforeSend: function() {
                    $("#subscription_loading").show();
                },
                success: function(msg) {
                    $("#subscription_loading").hide();
                    if (msg.status == "success") {
                        $("#email").val("");
                        $(".message").html('<span style="color:green;">Please check your email for a message asking you to confirm your subscription.</span>').fadeIn("slow").fadeOut(8000);

                    } else {
                        $(".message").html('Please make sure you enter a valid email address.');
                    }
                },
                error: function(xhr, status, error) {
                    $("#subscription_loading").hide();
                    $(".message").html('<span style="color:#76ca8f;">' + xhr.responseText + '</span>').fadeIn("slow").fadeOut(8000);
                }
            });
        }
        return false;
    });

    function valid_email_address(email) {
        var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
        return pattern.test(email);
    }
    if ($('.dept_common').length > 0) {
        fadeinleft('.dept_common .common_box_wrap .row > div:first-of-type', '.dept_common');
        fadeinright('.dept_common .common_box_wrap .row > div:last-of-type', '.dept_common');
    }


    var n = 1;

    $('.item').each(function() {
        $(this).attr('dataindex', n++);
    });


});