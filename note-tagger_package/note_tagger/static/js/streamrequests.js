

$(document).ready(function(){
    $('#submitbutton').click(function(event){
        $.ajax({
            url: "processnote",
            data: {'note': $('#noteentry').val()},
            type: "GET",
            dataType: "text",
            success: function(data) {
                $('#thestream').append("<br/><br/>"+data);
            }
        });
    });
});
