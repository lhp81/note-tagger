

$(document).ready(function(){
    $('#submitbutton').click(function(event){
        $.ajax({
            url: "processnote",
            data: $(this).siblings('#noteentry').text(),
            type: "POST",
            dataType: "text",
            success: function(data) {
                $('#thestream').append("<br/><br/>"+data);
            }
        });
    });
});
