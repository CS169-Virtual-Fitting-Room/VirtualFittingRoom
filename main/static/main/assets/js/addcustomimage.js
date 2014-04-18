function checkValidImageType(image){
	if(image=="" || jQuery.type(image)!="string"){
		return false;
	}
	var arr = image.split('.');
	if(arr.length!=2){
		return false;
	}else if(!(arr[1]=="jpg" || arr[1]=="jpeg")){
		return false;
	}
	return true;
}
function checkEmptyInput(map){
	var string = "";
	$.map(map,function(value, key){
		if(value==""){
			if (string ==""){
				string = string+" "+key;
			}else{
				string = string+", "+key;
			}
		}
	});
	return string;
}
function checkValidPrice(price){
	if(price == ""){
		return false;
	}
	var arr = price.split('.');
	if(arr.length>2){
		return false;
	}else if(arr.length==1){
		var s = arr[0];
		return checkValidInteger(s);
	}else if(arr.length==2){
		var integer = arr[0];
		var fractional = arr[1];
		return checkValidInteger(integer) && checkValidInteger(fractional);
	}
}
function checkValidInteger(s){
	for(var i=0; i<s.length; i++){
		if(!(s[i]>='0'&& s[i]<='9')){
			return false;
		}
	}
	return true;
}