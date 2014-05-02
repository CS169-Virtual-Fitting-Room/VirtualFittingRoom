function getItemFromWishListAndStartRender(){
	$.ajax({
		url:"/wishlist/get",
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			//setTimeout(renderwishlist(data), 1000);
			$("table#wishlisttable").html('');
			$("#empty_wishlist").hide();
			renderwishlist(data);
		},
		error:
		function(data){
			alert("failure");
		}
	});
}	


function renderwishlistelement(desc, image, name, price, id, category){
	if(jQuery.type(desc)!="string" || jQuery.type(image)!="string" || jQuery.type(name)!="string" || jQuery.type(price)!="number"||jQuery.type(id)!="number"||jQuery.type(category)!="string"){
		return false;
	}
	var item = '<tr> <th scope="col" class="description">Product</th><th align="right" scope="col" class="price">Price</th><tr><td style="padding-bottom: 40px" align="left" valign="top" class="description"><a href="/'+category+'/'+name+'_'+id+'"><img src='+image+' width="115" height="115" alt="'+name+'" class = "left"></a><p><a href="/'+category+'/'+name+'_'+id+'">'+name+'</a><br>'+desc+' <div > <button class = "wishlistremove" id = "'+category+'_'+name+'_'+id+'"> Remove </button></div> </td><td align="right" valign="top" class="price">'+price+'</td><td><button id = "'+category+'_'+name+'_'+id+'" class="wishlistcontinue">Add Item to Fitting Room</button></td></tr>';
	$("table#wishlisttable").append(item);
	return true;
	
}

function renderwishlist(data){
	if(jQuery.type(data)!="array"){
		return false;
	}
	var len = data.length;
	if(len ==0){
		$("#empty_wishlist").show();
		$("#empty_wishlist").html("Note: Please add items to Wish List. You can add items from product details.");
	}
	for(var i=0; i<len; i++){
		var desc = data[i].description;
		var image = data[i].image;
		var name = data[i].item_name;
		var price = data[i].price;
		var id = data[i].product_id;
		var category = data[i].category;
		renderwishlistelement(desc, image, name, price, id, category);
	}
	wishlistclickbuttonEvent();
	return true;
}

function wishlistclickbuttonEvent(){
	$("button").click(function(event){
		var id = event.target.id.split('_');
		var category = id[0];
		var name = id[1];
		var item_id = id[2];
		var commonpath = '/'+category+'/'+name+'_'+item_id;
		if(event.target.className=="wishlistremove"){
			clickRemoveWishListEvent(commonpath);
		}else if(event.target.className=="wishlistcontinue"){
			clickAddToFitListEvent(commonpath);
		}
	});
}


function clickAddToFitListEvent(commonpath){ //add to fit list
	if(jQuery.type(commonpath)!="string"){
		return false;
	}else if(commonpath.split('/').length<2){
		return false;
	}
	$.ajax({
		type:"POST",
		url:commonpath+"/fitlist/add",
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
				if(typeof getItemFromFitListAndStartRender !=='undefined' && $.isFunction(getItemFromFitListAndStartRender)){
					getItemFromFitListAndStartRender();
				}
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

function clickRemoveWishListEvent(commonpath){
	if(jQuery.type(commonpath)!="string"){
		return false;
	}else if(commonpath.split('/').length<2){
		return false;
	}
	$.ajax({
		type:"post",
		url: commonpath+'/wishlist/remove',
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			console.log(data);
			getItemFromWishListAndStartRender();
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
