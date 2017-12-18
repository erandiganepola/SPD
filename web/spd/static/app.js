$(document).ready(function () {
    $(".alert").hide();
});

function compareDocs() {
    $(".alert").hide();

    var doc1 = $("#doc1").val();
    var doc2 = $("#doc2").val();
    if (!doc1 || !doc2 || doc1.length === 0 || doc2.length === 0) {
        showError("Please insert two documents to compare");
        return;
    }

    console.log("comparing documents ...");

    $.ajax({
        url: "/spd/compare",
        method: 'post',
        data: {
            doc1: doc1,
            doc2: doc2
        }
    }).done(function (data) {
        console.log(data);
        sim = data.similarities;
        text = "<ul>";
        for (var i in sim) {
            for (var j in sim[i]) {
                text += "<li> Doc " + i + " and Doc " + j + " -> " + sim[i][j].toFixed(2) + "</li>"
            }
        }
        text += "</ul>";

        showSuccess(text);
    }).fail(function (err) {
        console.log(err);
        showError("Error occurred when processing documents");
    });
}

function showError(msg) {
    console.log("Error - %s", msg);
    $('#errorMsg').text(msg);
    $('#errorBox').show();
}

function showSuccess(msg) {
    console.log("Success - %s", msg);
    $('#successBox').html(msg);
    $('#successBox').show();
}