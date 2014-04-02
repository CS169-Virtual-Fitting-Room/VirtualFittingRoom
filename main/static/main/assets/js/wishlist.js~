function getItemFromWishListAndStartRender(){
	$.ajax({
		url:"get",
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			//console.log(data);
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
	var item = '<tr> <th scope="col" class="description">Product</th><th align="right" scope="col" class="price">Price</th></tr><tr><td align="left" valign="top" class="description"><a href="/'+category+'/'+name+'_'+id+'"><img src='+image+' width="115" height="115" alt="'+name+'" class = "left"></a><p><a href="/'+category+'/'+name+'_'+id+'">'+name+'</a><br>'+desc+' <div > <button class = "remove" id = "'+category+'_'+name+'_'+id+'"> Remove </button></div> </td><td align="right" valign="top" class="price">'+price+'</td><td><button id = "'+category+'_'+name+'_'+id+'" class="continue">Add Item to Fitting Room</button></td></tr>';
	$("table").append(item);
	return true;
	
}

function renderwishlist(data){
	if(jQuery.type(data)!="array"){
		return false;
	}
	var len = data.length;
	for(var i=0; i<len; i++){
		var desc = data[i].description;
		var image = data[i].image;
		var name = data[i].item_name;
		var price = data[i].price;
		var id = data[i].product_id;
		var category = data[i].category;
		renderwishlistelement(desc, image, name, price, id, category);
	}
	clickbuttonEvent();
	return true;
}

function clickbuttonEvent(){
	$("button").click(function(event){
		var id = event.target.id.split('_');
		var category = id[0];
		var name = id[1];
		var item_id = id[2];
		var commonpath = '/'+category+'/'+name+'_'+item_id;
		if(event.target.className=="remove"){
			clickRemoveEvent(commonpath);
		}else if(event.target.className=="continue"){
			clickContinueEvent(commonpath);
		}
	});
}


function clickContinueEvent(commonpath){ //add to fit list
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
				alert("Error! Fail to verify user info. Please log in first! OR Item is already added in Fitting Room!");
			}else{
				alert("Item is successfully added.");
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

function clickRemoveEvent(commonpath){
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
			$("table").html('');
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
