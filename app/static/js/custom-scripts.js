
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

// Redirect user to edit a post

function redirect(button_id, target, current_endpoint) {
    let current_url = window.location.href
    console.log(current_url)

    let url_prefix = current_url.split(current_endpoint)[0]
    let new_endpoint = url_prefix + target + '/' + button_id
    window.location.replace(new_endpoint)
}