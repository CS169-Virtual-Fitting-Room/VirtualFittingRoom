function getItemFromCustomListAndStartRender(){
	//Need a way to know what item user is added
	$.ajax({
		url:"/getcustompage",
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			rendercustomlist(data);
		},
		error:
		function(data){
			alert("failure");
		}
	});
}	

function rendercustomlist(data){
	/*if($.type(data)!="array"){
		return false;
	}*/
	var len = data.length;
	$("table#customlisttable").html('');
	if(len ==0){
		
		$("#empty_customlist").html("Note: You didn't upload any item yet.");
	}
	console.log(data);
	for(var i=0; i<len; i++){
		var desc = data[i].description;
		var image = data[i].image;
		var brand = data[i].brand;
		var name = data[i].item_name;
		var price = data[i].price;
		var id = data[i].product_id;
		var category = data[i].category;
		rendercustomlistelement(desc, image, name, price, id, category, brand);
	}
	customlistclickbuttonEvent();
	return true;
}

function rendercustomlistelement(desc, image, name, price, id, category, brand){
	/*if(jQuery.type(desc)!="string" || jQuery.type(image)!="string" || jQuery.type(name)!="string" || jQuery.type(price)!="number"||jQuery.type(id)!="number"||jQuery.type(category)!="string"){
		return false;
	}*/
	var item = '<tr> <th scope="col" class="description">Product</th><th align="right" scope="col" class="brand">Brand</th><th align="right" scope="col" class="price">Price</th><tr><td style="padding-bottom: 40px" align="left" valign="top" class="description"><a href="/'+category+'/'+name+'_'+id+'"><img src='+image+' width="115" height="115" alt="'+name+'" class = "left"></a><p><a href="/'+category+'/'+name+'_'+id+'">'+name+'</a><br>'+desc+' <div class = "customlistremove"> <button class = "customlistremove" id = "'+category+'_'+name+'_'+id+'"> Remove </button></div> <div class = "customlistedit"> <button class = "customlistedit" id = "edit_'+category+'_'+name+'_'+id+'_'+desc+'_'+image+'_'+brand+'_'+price+'"> Edit </button></div> <td align="right" valign="top" class="brand">'+brand+'</td></td><td align="right" valign="top" class="price">'+price+'</td><td><button id = "'+category+'_'+name+'_'+id+'" class="customlistcontinue">Add Item to Fitting Room</button></td></tr>';
	var table = $("table#customlisttable");
	console.log(table);
	if(!$.isEmptyObject(table)){
		$("table#customlisttable").append(item);
	}
	return true;
	
}

function customlistclickbuttonEvent(){
	$("button").click(function(event){
		console.log(event.target.id);
		var id = event.target.id.split('_');
		var category = id[0];
		var name = id[1];
		var item_id = id[2];
		var commonpath = '/'+category+'/'+name+'_'+item_id;
		if(event.target.className=="customlistremove"){
			clickRemoveCustomListEvent(item_id);
		}else if(event.target.className=="customlistcontinue"){
			clickAddToFitListEvent(commonpath);
		}else if(event.target.className=="customlistedit"){
			clickEditCustomListEvent(id);
		}
	});
}

function clickRemoveCustomListEvent(id){
	/*if(jQuery.type(commonpath)!="string"){
		return false;
	}else if(commonpath.split('/').length<2){
		return false;
	}*/
	$.ajax({
		type:"post",
		url: '/deletecustompage/'+id,
		contentType:"application/json",
		dataType:"json",
		success:
		function(data){
			console.log(data);
			
			getItemFromCustomListAndStartRender();
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

function clickEditCustomListEvent(id){
	var url="/editcustomimage?"+id;
	window.location.href = url;
}