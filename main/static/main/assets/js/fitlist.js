function getItemFromFitListAndStartRender(){
	$.ajax({
		url:"/fitlist/get",
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			$("table#fitlisttable").html('');
			renderfitlist(data);
			console.log(data);
		},
		error:
		function(data){
			alert("failure");
		}
	});
}	

function renderfitlistelement(desc, image, name, price, id, category){
	if(jQuery.type(desc)!="string" || jQuery.type(image)!="string" || jQuery.type(name)!="string" || jQuery.type(price)!="number"||jQuery.type(id)!="number"||jQuery.type(category)!="string"){
		return false;
	}
	var item = '<tr> <th scope="col" class="description">Product</th><th align="right" scope="col" class="price">Price</th><tr><td style="padding-bottom: 40px" align="left" valign="top" class="description"><a href="/'+category+'/'+name+'_'+id+'"><img src='+image+' width="115" height="115" alt="'+name+'" class = "left"></a><p><a href="/'+category+'/'+name+'_'+id+'">'+name+'</a><br>'+desc+' <div > <button class = "fitlistremove" id = "'+category+'_'+name+'_'+id+'"> Remove </button></div> </td><td align="right" valign="top" class="price">'+price+'</td><td><button id = "'+category+'_'+name+'_'+id+'" class="fitlistcontinue">Add Item to WishList</button></td></tr>';
	var table = $("table#fitlisttable");
	if(!$.isEmptyObject(table)){
		$("table#fitlisttable").append(item);
	}
	return true;
	
}

function renderfitlist(data){
	/*if($.type(data)!="array"){
		return false;
	}*/
	var len = data.length;
	if(len ==0){
		$("#empty_fitlist").show();
		$("#empty_fitlist").html("Note: Please add items to Fitting Room. You can add items from product details or Wish List.");
	}
	
	for(var i=0; i<len; i++){
		var desc = data[i].description;
		var image = data[i].image;
		var name = data[i].item_name;
		var price = data[i].price;
		var id = data[i].product_id;
		var category = data[i].category;
		renderfitlistelement(desc, image, name, price, id, category);
	}
	fitlistclickbuttonEvent();
	return true;
}

function fitlistclickbuttonEvent(){
	$("button").click(function(event){
		var id = event.target.id.split('_');
		var category = id[0];
		var name = id[1];
		var item_id = id[2];
		var commonpath = '/'+category+'/'+name+'_'+item_id;
		if(event.target.className=="fitlistremove"){
			clickRemoveFitListEvent(commonpath);
		}else if(event.target.className=="fitlistcontinue"){
			clickAddToWishListEvent(commonpath);
		}
	});
}

function clickRemoveFitListEvent(commonpath){
	if(jQuery.type(commonpath)!="string"){
		return false;
	}else if(commonpath.split('/').length<2){
		return false;
	}
	$.ajax({
		type:"post",
		url: commonpath+'/fitlist/remove',
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			console.log(data);
			
			getItemFromFitListAndStartRender();
			return true;
		},
		error:
		function(data){
			alert("failure");
			return false;
		}
	});
	return false;
}


function clickAddToWishListEvent(commonpath){ //add to fit list
	if(jQuery.type(commonpath)!="string"){
		return false;
	}else if(commonpath.split('/').length<2){
		return false;
	}
	$.ajax({
		type:"POST",
		url:commonpath+"/wishlist/add",
		contentType:"application/json",
		dataType: "json",
		success:
		function(data){
			console.log("success");
			if(data.errCode<0){
				//alert("");
				//$("#failure_dialog").html("<p>Error! Fail to verify user info. Please log in first! OR Item is already added in Fitting Room!</p>");
				if(data.errCode == -8) {
					$("#failure_dialog").html("<p>Fail to verify user info. Please log in first!</p>");
				}
				else if(data.errCode == -7) {
					$("#failure_dialog").html("<p>Item is already in Fitting Room!</p>");
				}
				else {
					$("#failure_dialog").html("<p>Failed to add to Fitting Room!</p>");
				}
				$("#failure_dialog").dialog();
				
			}else{
				//alert("");
				$("#success_dialog").html("<p>Item is successfully added.</p>");
				$("#success_dialog").dialog();
				getItemFromWishListAndStartRender();
			}
			return true;
		},
		error:
		function(){
			alert("failure");
			return false;
		}
	});
	return false;
}