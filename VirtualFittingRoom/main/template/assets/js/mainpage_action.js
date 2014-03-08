$(document).ready(function(){
	$(".service-count1").click(function(){
		$(".contain-page").load("category_list.html", function() {
			
			$("#items").load("item.html", function(data){
				for ( var i = 0; i < 24; i++ ) {
					$(this).append(data);
				}
				$("a#item-img").html('<img src="assets/img/glasses_demo.jpg" alt="Elegant evening Dress"/>');
				$("a.title").html('Awesome glasses');
			});
			
		});
	});
	$(".service-count2").click(function(){
		$(".contain-page").load("category_list.html", function() {
			$("#items").load("item.html", function(data){
				for ( var i = 0; i < 24; i++ ) {
					$(this).append(data);
				}
				$("a#item-img").html('<img src="assets/img/hat_demo.png" alt="Elegant evening Dress"/>');
				$("a.title").html('Spectacular Hat');
			});
		});
	});
	$(".service-count3").click(function(){
		$(".contain-page").load("category_list.html", function() {
			$("#items").load("item.html", function(data){
				for ( var i = 0; i < 24; i++ ) {
					$(this).append(data);
				}
				$("a#item-img").html('<img src="assets/img/headphone_demo.png" alt="Elegant evening Dress"/>');
				$("a.title").html('Fantastic Headphone');
			});
		});
	});
	
}); 