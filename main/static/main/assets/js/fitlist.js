function getItemFromFitListAndStartRender(){
	$.ajax({
		url:"/fitlist/get",
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			renderfitlist(data);
		},
		error:
		function(data){
			alert("failure");
		}
	});
}	

function renderfitlist(data){
	/*if($.type(data)!="array"){
		return false;
	}*/
	var len = data.length;
	if(len ==0){
		$("#empty_fitlist").html("Note: Please add items to Fitting Room. You can add items from product details or Wish List.");
	}
	/*
	for(var i=0; i<len; i++){
		var desc = data[i].description;
		var image = data[i].image;
		var name = data[i].item_name;
		var price = data[i].price;
		var id = data[i].product_id;
		var category = data[i].category;
		renderwishlistelement(desc, image, name, price, id, category);
	}
	clickbuttonEvent();*/
	return true;
}