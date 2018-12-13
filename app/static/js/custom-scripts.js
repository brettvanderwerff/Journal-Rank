$(document).ready(function() {
    $('#example').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
        url : "/table_result",
        data: function ( args ) {
          return { "args": JSON.stringify( args ) };
    }
        }
    } );
} );