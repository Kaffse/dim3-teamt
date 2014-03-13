$(document).ready(function() {
   alert("jQuery functioning");

   $('#new-list-dialog').dialog({
      autoOpen: false,
      title: 'Basic Dialog'
   });
   $('#new-list-button').click(function() {
      $(this).dialog('open');
      return false;
   });
 });
