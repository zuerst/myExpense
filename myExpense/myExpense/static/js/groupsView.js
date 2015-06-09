$(document).ready(function() {
    $('#addGroupPopUp').on('shown.bs.modal', function () {
        $('#groupname').focus()
    })

    $( "#autocomplete" ).autocomplete({
        source: function( request, response ) {
        $.ajax({
            url: '/profile/friends/' + document.getElementById("autocomplete").value,
            type : 'GET',
            dataType: "json",
            success: function(data) {
                response( $.map( data, function(item) {
                    return {"label" : item, "value" : item};
                }));
            },
            error: function(data) {
                $('input.suggest-user').removeClass('ui-autocomplete-loading');  
            }
        });
      },

      minLength: 2,

      open: function() {

      },
      close: function() {

      },
      focus:function(event, ui) {

      },
      select: function(event, ui) {

      }
    });
})

function addGroup() {
    var groupnameValue = document.getElementById("groupname").value;
    var descriptionValue = document.getElementById("description").value; 

    csrfmiddlewaretoken = '{{ csrf_token }}'

    $.ajax({
        url : "/profile/groups/",
        type : "POST",
        data : { method : "add", groupname : groupnameValue, description : descriptionValue},
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