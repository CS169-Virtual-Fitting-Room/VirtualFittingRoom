$(document).ready(function(){
	$(".service-count1").click(function(){
		$(".contain-page").load("category_list.html", function() {
			//$("#test").append(" GLASSES");
		});
	});
	$(".service-count2").click(function(){
		$(".contain-page").load("category_list.html", function() {
			//$("#test").append(" HATS");
		});
	});
	$(".service-count3").click(function(){
		$(".contain-page").load("category_list.html", function() {
			//$("#test").append(" HEADPHONES");
		});
	});
	
}); 