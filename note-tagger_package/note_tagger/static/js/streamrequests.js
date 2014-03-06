

$(document).ready(function(){
    $('#submitbutton').click(function(event){
        $.ajax({
            url: "processnote",
            data: {'note': $('#noteentry').val()},
            type: "GET",
            dataType: "json",
            success: function(data) {
                $('#thestream').append("<br/>");
                for(var i=0; i<data.length;i++){
                    $('#thestream').append(data[i]+' ');
                }
            }
        });
    });
});
