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
    // add dynamic to report table.
    $('#reportTable').dataTable();

$('#delete').on('shown.bs.modal', function (e) {
  var transId = $(e.relatedTarget).data('trans-id')
  var element = document.getElementById('confirmDelete')
  element.onclick = function () {
      deleteEntry(transId)
  }
  console.log('Delete')
})
})

$(document).ready(function() {
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
  var months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
  month = String(months.indexOf(month));

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

// Add bootstrap model popup listener. For login in PopUp in mainPage
$(document).ready(function() {
	$('#loginPopup').on('shown.bs.modal', function () {
		$('#myInput').focus()
	})

	$('#registerPopup').on('shown.bs.modal', function () {
		$('#myInput').focus()
	})

	$('#loginFromRegPopup').click(function() {
		$('#loginPopup').modal('show')
		$('#registerPopup').modal('hide')
	})
})

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

