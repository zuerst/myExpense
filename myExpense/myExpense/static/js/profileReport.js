// Func this when page is loaded.
$(document).ready(function() {
    // add dynamic to report table.
    $('#reportTable').dataTable();

    // Create Date range picker
    $('#daterange span').html(moment().subtract(29, 'days').format('MMMM D, YYYY') + ' - ' + moment().format('MMMM D, YYYY'));
    $('#daterange').daterangepicker({
        format: 'YYYY-MM-DD',
        startDate: '2013-01-01',
        endDate: '2013-12-31',
        ranges: {
            'Today': [moment(), moment()],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')],
            'This Year': [moment().startOf('year'), moment().endOf('year')]
        },
        opens: 'left'
        },
        function(start, end, label) {
            $('#daterange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
            getSelectedData(start.format("YYYY-MM-DD"), end.format("YYYY-MM-DD"));
    });
});

// render new graph with given data
function renderGraph(json) {
    // Stub
}

// render new table with given data
function renderTable(json) {
    monthNamesShort = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
    var tableHTML = ''
    $('#reportTable').empty();
    tableHTML += '<table id="reportTable" class="table table-striped table-bordered">'
    tableHTML +=         '<thead>'
    tableHTML +=         '<tr>'
    tableHTML +=             '<th>#</th>'
    tableHTML +=             '<th>Date</th>'
    tableHTML +=             '<th>Title</th>'
    tableHTML +=             '<th>Description</th>'
    tableHTML +=             '<th>Trans Type</th>'
    tableHTML +=             '<th>Amount</th>'
    tableHTML +=             '<th>Category</th>'
    tableHTML +=             '<th>User</th>'
    tableHTML +=         '</tr>'
    tableHTML +=         '</thead>'
    for (var i = 0; i < json.length; i++) {
        id = json[i]['pk']
        amount = json[i].fields['amount']
        category = json[i].fields['category']
        date = new Date(json[i].fields['date'])
        reportDate = monthNamesShort[date.getMonth()] + ' ' + date.getDate() + ', ' + date.getFullYear()
        description = json[i].fields['description']
        title = json[i].fields['title']
        transType = json[i].fields['transType']
        user = json[i].fields['user']

        tableHTML += '<tr>'
        tableHTML +=        '<td>'+ id + '</td>'
        tableHTML +=        '<td>' + reportDate + '</td>'
        tableHTML +=        '<td>' + title + '</td>'
        tableHTML +=        '<td>' + description +'</td>'
        tableHTML +=        '<td>' + transType + '</td>'
        tableHTML +=        '<td>' + amount + '</td>'
        tableHTML +=        '<td>' + category + '</td>'
        tableHTML +=        '<td>' + user +'</td>'
        tableHTML +=    '</tr>'
    }
    tableHTML += '</tbody> </table>'

    $('#reportTable').html(tableHTML);
    // add dynamic to report table.
    $('#reportTable').dataTable({
        "bDestroy": true
    });
}

// Get data for new StartDate and endDate use it to render graph and table.
function getSelectedData(start, end) {
    $.ajax({
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }},
        url : "/profile/report",
        type : "POST",
        dataType: "json",
        data : { method : "load", startDate : start, endDate: end},
        success : function(response) {
            renderTable(response)
            console.log("success")
        }
    })
}