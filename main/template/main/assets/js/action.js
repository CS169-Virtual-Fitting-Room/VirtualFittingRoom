//$("div.contain-page").get("mainpage.html", function(data){
//    $(this).html(data);
//});
$(document).ready(function(){
	//$(".contain-page").append("<p>Test</p>");
	$(".contain-page").load("mainpage.html");
	$("#home").click(function(){
		$(".contain-page").load("mainpage.html");
	});
}); 