$(document).ready(function() {
    $('#addGroupPopUp').on('shown.bs.modal', function () {
        $('#groupname').focus()
    })
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