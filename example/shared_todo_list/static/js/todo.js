function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {

        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Insert code here to run when the DOM is ready
$(document).ready( function() {

	$('.delete-btn').on('click', function(e) {
		var id = $(e.currentTarget).data('item-id');
		alert('removing: ' + id);

		$(e.currentTarget).parent().remove();
	});

	/* Adding csrf to post reqs */
	$(function() {
	    /* adds csrftoke to every ajax request we send */
	    $.ajaxSetup({
	        crossDomain: false, // obviates need for sameOrigin test
	        beforeSend: function(xhr, settings) {
	            if (!csrfSafeMethod(settings.type)) {
	                var token = getCookie('csrftoken');
	                xhr.setRequestHeader("X-CSRFToken", token);
	            }
	        }
	    });
	});

	/* Easily reloading the page */
	// setTimeout(function(){
	// 	Stub.render_list_reload()
	// }, 10000);

	setTimeout(function(){
		Stub.render_list_json(function(input) {
			console.log(input);
		})
	}, 3000);

	$('#add-item').on('submit', function(e) {
		e.preventDefault();
		$.ajax({
          type: "POST",
          url: $(e.target).attr('action'),
          data: $(e.target).serialize(),
          // converters: "text json",
          complete: function(data) {
            /* html_render_item is autogenerated method that returns 
               the html string from server side */
            Stub.render_list_reload()
           
          }
        });

        e.target.reset();
	});

});
