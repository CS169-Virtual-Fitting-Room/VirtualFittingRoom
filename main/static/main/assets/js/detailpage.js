
	function rendercomments(data){
		if(jQuery.type(data)!="array"){
			return false;
		}
		var len = data.length;
		for(var i=0; i<len; i++){
			var content = data[i].content;
			var name = data[i].name;
			var time = data[i].time;
			rendercomment(content, name, time);
		}
		return true;
	}

	function rendercomment(content, name, time){
		if(jQuery.type(content)!="string" || jQuery.type(name)!="string" ||jQuery.type(time)!="string"){
			return false;
		}
		var url = '/static/main/assets/img/anonymous-user.png';
		var comment = '<li class="cmmnt"><div class="avatar"><a href="javascript:void(0);"><img src='+url+' width="55" height="55" alt="'+name+'"></a></div><div class="cmmnt-content"><header><a href="javascript:void(0);" class="userlink">'+name+'</a> - <span class="pubdate">posted '+time+'</span></header><p>'+content+'</p></div></li>';
		$("#comment-list").append(comment);
		return true;
	}


