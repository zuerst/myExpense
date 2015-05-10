// Add bootstrap model popup listener. For login in PopUp in mainPage
$('#loginPopup').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

function selectCategory(catName, catColor) {
    document.getElementById("category").value = catName;
    document.getElementById("color").value = catColor;
    $('#selCatPopup').modal('hide');
}

