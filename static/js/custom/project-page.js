$(document).on("click", ".add-task-button", function () {
     var myBookId = $(this).data('current-list');
    $("#list-id").val(myBookId);
});
