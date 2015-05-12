$(document).ready(function() {

    $('#delete').on('shown.bs.modal', function (e) {
        var transId = $(e.relatedTarget).data('trans-id')
        var element = document.getElementById('confirmDelete')
        element.onclick = function () {
            deleteEntry(transId)
        }
        console.log('Delete')
    })

    // add dynamic to short History table.
    $('#shortHistory').dataTable({
        // Remove search, page, info functions since this is only short table.
        'bFilter': false,
        "paging":   false,
        "info":     false,
        // Setup to add toolbar.
        "dom": '<"toolbar">frtip',
        // Disable sorting for EDIT and DELETE columns
        "aoColumnDefs" : [{
            'bSortable' : false,
            'aTargets' : [ 6,7 ]
        }]
    });

    // Add toolbar to the Table.
    $("div .toolbar").html('<b>This table only shows most recent 7 Transactions</b>');

    // Bind when edit popup is shown grab the values from each table column.
    $('#edit').on('shown.bs.modal', function (e) {
        var transId = $(e.relatedTarget).data('trans-id');
        var title = document.getElementById('tit-'+transId).innerText;
        var description = document.getElementById('desc-'+transId).innerText;
        var transType = document.getElementById('trans-'+transId).innerText;
        var amount = document.getElementById('amount-'+transId).innerText;
        var date = document.getElementById('date-'+transId).innerText;
        var catName = document.getElementById('cat-'+transId).innerText;
        date = date.replace (",", "");
        mdy = date.split(" ");

        var month = mdy[0].toLowerCase();
        var monthNamesShort = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
        month = String(monthNamesShort.indexOf(month));

        if (month[1] == null) {
            month = "0"+String(month)
        }

        year = mdy[2]
        day = mdy[1]
        var fullDate = mdy[2]+"-"+month+"-"+mdy[1]

        document.getElementById("eTitle").value = title;
        document.getElementById("eDescription").value = description;
        document.getElementById("eAmount").value = amount;
        document.getElementById("eDate").value = fullDate;

        catOptions = document.getElementById("catNumSelection").options

        for (var i=0; i < catOptions.length; i++) {
            if (catName == catOptions[i].innerText) {
                catOptions.selected = true;
                break;
            }
        }

        if (transType == "+") {
            resetRadioButtons();
            document.getElementsByName("transactionPlus")[0].className += " active";
            document.getElementById("eTransTypePlus").checked = true;
        } else if (transType == "-") {
            resetRadioButtons();
            document.getElementsByName("transactionMinus")[0].className += " active";
            document.getElementById("eTransTypeMinus").checked = true;
        }

        var element = document.getElementById('confirmEdit')
        element.onclick = function () {
            editEntry(transId, transType)
        }
        console.log('Edit')
    })
})

function resetRadioButtons() {
    document.getElementsByName("transactionPlus")[0].className = "btn btn-default";
    document.getElementsByName("transactionMinus")[0].className = "btn btn-default";
    document.getElementById("eTransTypePlus").checked = false;
    document.getElementById("eTransTypeMinus").checked = false;
}

function selectCategory(catName, catColor) {
    document.getElementById("category").value = catName;
    document.getElementById("color").value = catColor;
}

function editCategory(catNum) {
    document.getElementById("catNum").value = catNum;
}

function showSelectCategory() {
    $('#selCatPopup').modal('show');
}

function deleteEntry(transId) {
    csrfmiddlewaretoken = '{{ csrf_token }}'
    $.ajax({
        url : "/profile/transControl",
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

function editEntry(transId, eTransType) {
    var eTitle = document.getElementById("eTitle").value;
    var eDescription = document.getElementById("eDescription").value;
    var eAmount = document.getElementById("eAmount").value;
    var eDate = document.getElementById("eDate").value;
    var catNumSelect = document.getElementById("catNumSelection");
    catNum = catNumSelect.options[catNumSelect.selectedIndex].value;

    console.log(catNum)

    csrfmiddlewaretoken = '{{ csrf_token }}'
    $.ajax({
        url : "/profile/transControl",
        type : "POST",
        data : { method : "edit", transID : transId, title : eTitle, description : eDescription, 
                transType : eTransType, amount : eAmount, date : eDate, newCatId : catNum},
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

