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
                response($.map( data, function(item) {
                    return {"label" : item.username, "value" : item.username};
                }));
            },

            error: function(data) {
            }});
        },

        minLength: 2,

        open: function() {

        },
        
        close: function() {

        },
        
        focus:function(event, ui) {

        },
        
        select: function(event, ui) {
            $('input#autocomplete').before("<div class=\"label label-primary user-search-label\" id=user-block>" + ui.item.value + "</div>")
        }
    });
})

function addGroup() {
    var groupnameValue = document.getElementById("groupname").value;
    var descriptionValue = document.getElementById("description").value; 

    var usersValue = ""

    $('div#user-block').each(function() {
        usersValue += ($(this ).text());
        usersValue += ";"
        console.log(usersValue)
    });

    dataValues = { method : "add", groupname : groupnameValue, description : descriptionValue};
    if (usersValue.length > 0){
        dataValues = { method : "add", groupname : groupnameValue, description : descriptionValue, users : usersValue.slice(0,-1)};
    }


    csrfmiddlewaretoken = '{{ csrf_token }}'

    $.ajax({
        url : "/profile/groups/create",
        type : "POST",
        data : dataValues,
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
        success : function(json) {
            console.log(json);
            location.reload();
        }
    })
}