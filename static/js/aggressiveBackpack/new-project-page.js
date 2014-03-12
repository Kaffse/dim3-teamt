$(document).ready(function() {

  $('#new-list-dialog').dialog({
    autoOpen: false,
    title: 'Basic Dialog'
  });

  $('#new-list-button').click(function() {
    $('#wrapper').dialog('open');
    return false;
  });
});
