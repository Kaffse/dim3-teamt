//When you click on add task button then it will pass the current list to the form.
$(document).on("click", ".add-task-button", function () {
     var cur_list = $(this).data('current-list');
    $("#list-id").val(cur_list);
});

//When you click on task it passes the details of the current task to modal.
$(document).on("click", ".btn btn-default btn-lg btn-block", function() {
    var cur_task = $(this).data('current-task');
    $("#task-id").val(cur_task);
});
