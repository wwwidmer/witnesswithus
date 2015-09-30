/**
 * Created by william on 9/12/15.
 */
$("button").on('click', function(){
    var url = $(".url").val();
    var split = url.replace(/.*?:\/\//g, "");
    split = split.replace('www.', '');
    var host = split.split('/')[0];
    host = $.trim(host);
    if(host == 'meerkatapp.co'){
        var vid = split.split('/')[2];
    } else {
        var re = /\d+/;
        var vid = re.exec(split);
    }
    if(!vid){
        vid = split.split('/')[1]
    }
    var newurl = window.location.href+"counter?host="+host+"&vid="+vid;
    $("#newurl").html("<a href='"+newurl+"'>"+newurl+"</a>");
});
