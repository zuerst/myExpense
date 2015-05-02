// Add bootstrap model popup listener. For login in PopUp in mainPage
$('#loginPopup').on('shown.bs.modal', function () {
  $('#myInput').focus()
})