// Add bootstrap model popup listener. For login in PopUp in mainPage
$('#loginPopup').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

function selectCategory(catName, catColor) {
    document.getElementById("category").value = catName;
    document.getElementById("color").value = catColor;
    $('#selCatPopup').modal('hide');
}

function showSelectCategory() {
    $('#selCatPopup').modal('show');
}

function deleteEntry(x) {
    var item = x.closest("tr");
    var test = x.closest('tr').attr('id');
    console.log(item);
    alert("Row index is: " + test);
}


