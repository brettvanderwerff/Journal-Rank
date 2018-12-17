
// Datatable logic

$(document).ready(function() {
    $('#example').DataTable( {
        "order": [[ 3, "desc" ]],
        "processing": true,
        "serverSide": true,
        "ajax": {
        url : "/table_result",
        data: function ( args ) {
          return { "args": JSON.stringify( args ) };
    }
        },
    } );
} );


// Dynamic Review Submission Stars Logic

$(document).ready(function(){
//  Check Radio-box
    $(".rating input:radio").attr("checked", false);
    $('.rating input').click(function () {
        $(".rating span").removeClass('checked');
        $(this).parent().addClass('checked');
    });
});