$(document).ready(function(){
	$(".contain-page").load("mainpage");
	$(".header-wrap").load("top_menu");
	$("#home").click(function(){
		$(".contain-page").load("mainpage");
	});
}); 
function rendermainpage(){
	$(".contain-page").load("mainpage");
}
function rendertopmenu(){
	$(".header-wrap").load("top_menu");
}
function homeclick(){
	$("#home").click(function(){
		$(".contain-page").load("mainpage");
	});
}
