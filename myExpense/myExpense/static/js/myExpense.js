// using jQuery
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

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function() {
    $('#delete').on('shown.bs.modal', function (e) {
        var transId = $(e.relatedTarget).data('trans-id')
        var element = document.getElementById('confirmDelete')
        element.onclick = function () {
            deleteEntry(transId)
        }
        console.log('Delete')
    })
})

function selectCategory(catName, catColor) {
    document.getElementById("category").value = catName;
    document.getElementById("color").value = catColor;
}

function showSelectCategory() {
    $('#selCatPopup').modal('show');
}

function deleteEntry(transId) {
    csrfmiddlewaretoken = '{{ csrf_token }}'
    $.ajax({
        url : "/profile/add-expense",
        type : "POST",
        data : { method : "delete", transID : transId },
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
        success : function(json) {
            console.log("success");
            location.reload();
        }
    })
}

