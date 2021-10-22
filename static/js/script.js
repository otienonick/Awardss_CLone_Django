$(document).ready(function(){
    $('#modal-btn').click(function(){
        $('.ui.modal')
        .modal('show')
        ;
    })

})


$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;