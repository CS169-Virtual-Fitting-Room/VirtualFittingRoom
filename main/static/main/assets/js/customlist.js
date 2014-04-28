function getItemFromCustomListAndStartRender(){
	//Need a way to know what item user is added
	/*
	$.ajax({
		url:"/customlist/get",
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
	*/
	rendercustomlist(true);
}	

function rendercustomlist(data){
	/*if($.type(data)!="array"){
		return false;
	}*/
	//var len = data.length;
	var len =0;
	if(len ==0){
		console.log($("#empty_customlist"));
		$("#empty_customlist").html("Note: You didn't upload any item yet.");
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