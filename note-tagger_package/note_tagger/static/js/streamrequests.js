

$(document).ready(function(){
    $('#submitbutton').click(function(event){
        $.ajax({
            url: "processnote",
            data: $(this).siblings('#noteentry').val(),
            type: "POST",
            dataType: "json",
            success: function(data) {
                $('#thestream').append("<br/>");
                for(var i=0; i<=data.length;i++){
                    $('#thestream').append(data[i]);
                }
            }
        });
    });
});
