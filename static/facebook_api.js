// Boilerplate facebook api SDK
// Downloads and initializes FB
// https://developers.facebook.com/docs/javascript/examples

var app_id = '';

(function () {
    window.fbAsyncInit = function() {
	FB.init({
	    appId      : app_id,
	    xfbml      : true,
	    version    : 'v2.6'
	});
    };
    
    (function(d, s, id){
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) {return;}
	js = d.createElement(s); js.id = id;
	js.src = "https://connect.facebook.net/en_US/sdk.js";
	fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
}())
