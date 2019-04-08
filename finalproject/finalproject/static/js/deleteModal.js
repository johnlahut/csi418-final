$(".passingID").click(function () {
    var ids = $(this).attr('data-id');
    $("#idkl").val( ids );
    $('#myModal').modal('show');
});

function deleteButton(questionID, url){
    console.log(questionID);
    console.log(url);
    var ids = $(this).attr('data-id');
    $("idkl").val( ids );
    $('#myModal').modal('show');
    $('#finalDelete').attr('href', url.replace('0', questionID));



};