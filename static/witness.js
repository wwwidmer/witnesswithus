/**
 * Created by william on 9/12/15.
 */
$("button").on('click', function(){
    var url = $(".url").val();
    var split = url.replace(/.*?:\/\//g, "");
    var host = split.split('/')[0];
    host = $.trim(host);
    var re = /\d+/;
    var vid = re.exec(split);
    var newurl = window.location.href+"counter?host="+host+"&vid="+vid;
    $("#newurl").html("<a href='"+newurl+"'>"+newurl+"</a>");
});