

$(document).ready(function(){
    $('#submitbutton').click(function(event){
        $.ajax({
            url: "processnote",
            data: {'note': $('#noteentry').val()},
            type: "GET",
            dataType: "json",
            success: function(data) {
                $('#thestream').append("<br/><br/>Tags:");
                for(var i=1; i<data.length;i++){
                    $('#thestream').append(' '+data[i]);
                }
                $('#thestream').append(".<br/>"+data[0]);
                $('#thestream').stop().animate({
                    scrollTop: $('#thestream')[0].scrollHeight
                }, 800);
                $('#noteentry').val("");
            }
        });
    });
});
