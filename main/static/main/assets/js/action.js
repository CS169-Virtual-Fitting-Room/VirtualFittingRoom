//$("div.contain-page").get("mainpage.html", function(data){
//    $(this).html(data);
//});
{% load staticfiles }
$(document).ready(function(){
	//$(".contain-page").append("<p>Test</p>");
	$(".contain-page").load('{% static "main/mainpage.html" %}');
	$("#home").click(function(){
		$(".contain-page").load('{% static "main/mainpage.html" %}');
	});
}); 