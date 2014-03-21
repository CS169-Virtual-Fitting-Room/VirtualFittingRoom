function rendermainpage(){
	$(".contain-page").load("/mainpage");
}
function rendertopmenu(){
	$(".header-wrap").load("/top_menu");
}
function homeclick(){
	$("#home").click(function(){
		$(".contain-page").load("/mainpage");
	});
}
function rendergrids(num_of_items, images, item_names, prices){
		if(jQuery.type(num_of_items)!="number" || jQuery.type(images)!="array" || jQuery.type(item_names)!="array"|| jQuery.type(prices)!="array"){
			return false;
		}
		for ( var i = 0; i < num_of_items; i++ ) {
			var item = '<li> <a href="'+item_names[i]+'" id="item-img'+i+'"></a> <a href="'+item_names[i]+'" class="title">'+item_names[i]+'</a><strong>&dollar;'+prices[i]+'</strong></li>'
			$("#items").append(item);
			b64imgData = btoa(images[i]);
			$("a#item-img"+i).html("<img src='data:image/jpeg;base64,"+b64imgData+"'/>");
		}
		return true;
}
function capitaliseFirstLetter(string)
{
	if(string ==""){
		return "";
	}
    return string.charAt(0).toUpperCase() + string.slice(1);
}
function renderpage(desp, image, item_name, price){
	if(jQuery.type(desp)!="string" || jQuery.type(image)!="string" || jQuery.type(item_name)!="string"|| jQuery.type(price)!="number"){
		return false;
	}
	$("#price").html("&dollar;"+price);
	var current_category = capitaliseFirstLetter(window.location.pathname.split('/')[1]);
	$("#breadcrumb").html('<a href="/'+current_category+'">'+current_category+'</a> > '+item_name );
	$("h1#item_name").html(item_name );
	$("p#desp").html("Description: "+desp);
	b64imgData = btoa(image);
	$("div#images").html("<a href='data:image/jpeg;base64,"+b64imgData+"'><img src='data:image/jpeg;base64,"+b64imgData+"'/>");
	return true;
}