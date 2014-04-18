//load image resource specified url by the fitlist and create overlays from the resource
function loadOverlay(url,category) {
    url = "http://virtualfittingroom.herokuapp.com"+url;
    console.log("loading overlay image for url: "+url);
    var resource = gapi.hangout.av.effects.createImageResource(url);
    resource.onLoad.add( function(event) {
        if ( !event.isLoaded ) {
            console.log('cannot loaded overlay image for url: '+url);
        } else {
            console.log('loaded overlay image for url: '+url);
        }
    });
    var params;
    if (category == 1) {
      params = hatOverlayPreset;
    } else if (category == 2) {
      params = glassesOverlayPreset;
    } else {
      params = hpOverlayPreset;
    }
    overlay = resource.createFaceTrackingOverlay(params);
    overlay.setVisible(false);
    return overlay;
}

function loadPreview(data,category) {
  var url = "http://virtualfittingroom.herokuapp.com/static/temp/" + data + "ol.png";
  console.log("loading preview image for url"+url);
  var resource = gapi.hangout.av.effects.createImageResource(url);
  resource.onLoad.add( function(event) {
        if ( !event.isLoaded ) {
            console.log('cannot loaded preview image for url: '+url);
        } else {
            console.log('loaded preview image for url: '+url);
        }
    });
  var params;
  if (category == "hats") {
      params = hatOverlayPreset;
    } else if (category == "glasses") {
      params = glassesOverlayPreset;
    } else {
      params = hpOverlayPreset;
    }
  vCanvas.setVisible(true);
  overlay = resource.createFaceTrackingOverlay(params);
  overlay.setVisible(true);
  previewOverlay = overlay;
  $("#previewSliders").show();
}

function addElementToContainer(name,category,index,picUrl) {
  var container = document.getElementsByClassName('container-inner');
  var productButton = document.createElement('input');
  var type = 'image';
  var bClass = 'picButton';
  var bid = category+'button'+index;
  var src = "http://virtualfittingroom.herokuapp.com"+picUrl;
  var bOnClick;
  if (category == 1) {
    bOnClick = 'hatChange1('+index+')';
  } else if (category == 2) {
    bOnClick = 'glassChange1('+index+')';
  } else {
    bOnClick = 'hpChange1('+index+')';
  }
  var width = "50";
  var height = "50";
  productButton.setAttribute('type',type);
  productButton.setAttribute('class',bClass);
  productButton.setAttribute('src',src);
  productButton.setAttribute('onClick',bOnClick);
  productButton.setAttribute('width',width);
  productButton.setAttribute('height',height);
  productButton.setAttribute('id',bid);
  container[0].appendChild(productButton);
}

//function to compute width of a html text
$.fn.textWidth = function(){
  var html_org = $(this).html();
  var html_calc = '<span>' + html_org + '</span>';
  $(this).html(html_calc);
  var width = $(this).find('span:first').width();
  $(this).html(html_org);
  return width;
}

//save down fitlist
function saveData(response) {
  if (response.length == 0) {
      $("#loadingMessage").text("No accessories found");
      return false;
  }
  var container_width = 65 * response.length;
  $(".container-inner").css("width", container_width);
  for (var i = 0; i < response.length; i++) {
    if (response[i]["category"] == "hats") {
      hats.push(response[i]);
    } else if (response[i]["category"] == "glasses") {
      glasses.push(response[i]);
    } else if (response[i]["category"] == "headphones") {
      headphones.push(response[i])
    } else {
      console.log("Cannot load product with id "+response[i]["product_id"]+" unrecognized Category");
    }
  }
  return true;
}

//create overlay items from the fitlist and save it in the arrays for future adjustment
function createOverlays() {
  for (var i = 0; i < hats.length; i++) {
    hatsOverlay.push(loadOverlay(hats[i]["overlay"],1));
    //$("#hatList").append('<option value='+(i+1)+'>'+hats[i]["item_name"]+'</option>');
    addElementToContainer(hats[i]["item_name"],1,i+1,hats[i]["image"]);
  }
  for (var i = 0; i < glasses.length; i++) {
    glassesOverlay.push(loadOverlay(glasses[i]["overlay"],2));
    //$("#glassesList").append('<option value='+(i+1)+'>'+glasses[i]["item_name"]+'</option>');
    addElementToContainer(glasses[i]["item_name"],2,i+1,glasses[i]["image"]);
  }
  for (var i = 0; i < headphones.length; i++) {
    hpOverlay.push(loadOverlay(headphones[i]["overlay"],3));
    //$("#hpList").append('<option value='+(i+1)+'>'+headphones[i]["item_name"]+'</option>');
    addElementToContainer(headphones[i]["item_name"],3,i+1,headphones[i]["image"]);
  }
  $("#loadingMessage").text("All accessories loaded, select them below");
  $("#loadingMessage").offset({top:$("#loadingMessage").offset().top,left: wWidth/2-($("#loadingMessage").textWidth()/2)});
  //$("#selectors").show();
  $('#sliders').show();
  vCanvas.setVisible(true);

}

//respond for the change of slider and change the offset of the corresponding item
function adjustOffset(item, adjustX, value) {
  if (item == 1) {
    if (showingHat != 0) {
      var offset = hatsOverlay[showingHat-1].getOffset();
      if (adjustX) {
        offset['x'] = -parseFloat(value);
      } else {
        offset['y'] = -parseFloat(value);
      }
      console.log(offset);
      hatsOverlay[showingHat-1].setOffset(offset);
    }
  } else if (item == 2) {
    if (showingGlasses != 0) {
      var offset = glassesOverlay[showingGlasses-1].getOffset();
      if (adjustX) {
        offset['x'] = -parseFloat(value);
      } else {
        offset['y'] = -parseFloat(value);
      }
      glassesOverlay[showingGlasses-1].setOffset(offset);
    }
  } else if (item == 3) {
    if (showingHP != 0) {
      var offset = hpOverlay[showingHP-1].getOffset();
      if (adjustX) {
        offset['x'] = -parseFloat(value);
      } else {
        offset['y'] = -parseFloat(value);
      }
      hpOverlay[showingHP-1].setOffset(offset);
    }
  } else {
     var offset = previewOverlay.getOffset();
      if (adjustX) {
        offset['x'] = -parseFloat(value);
      } else {
        offset['y'] = -parseFloat(value);
      }
      previewOverlay.setOffset(offset);
  }
}

function adjustScale(item, value) {
  if (item == 4) {
    previewOverlay.setScale(parseFloat(value));
  }
}


//request for the fitlist
function vrfRequest(url, suc ,err) {

  $.ajax({
        type: 'GET',
        url: url,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        xhrFields: {
                withCredentials: true
            },
        success: suc,
        error: err
    });
}

//Get the fitlist from the backend
function getFitlist() {
  try {
    vrfRequest("http://virtualfittingroom.herokuapp.com/fitlist/get/", function(data) { return proccessResponse(data); }, function(err) {return displayError(); });
  } catch (err) {
     displayError(); 
  }
}


//Display the error message to notify user when error occur
function displayError() {
  $("#loadingMessage").text("Cannot load accessories");
  $("#loadingMessage").offset({top:$("#loadingMessage").offset().top,left: wWidth/2-($("#loadingMessage").textWidth()/2)});

}

//Process the fitlist response
function proccessResponse(response) {
    //Inject a fake fitlist to test if image loading and overlaying works fine
    // var response = 
    // [{"category": "hats", "product_id": 3, "overlay": "/static/products/addidasol.jpg", "item_name": "adidas cap", "price": 56.9, "description": "adidas cap!"}, 
    // {"category": "glasses", "product_id": 2, "overlay": "/static/products/", "item_name": "nike glasses", "price": 99.9, "description": "sporty nike"}, 
    // {"category": "headphones", "product_id": 5, "overlay": "/static/products/beatsol.jpg", "item_name": "beats headphones", "price": 256.9, "description": "stylish headphones!"}]
    console.log("Fitlist:");
    console.log(response);
    if (saveData(response)) {
      createOverlays();
    }
}



//update offset for a better adjusting experience(for future iteration)
function updateOffset(category,offset) {

}

//responses for items selection
function hatChange(){
  var list = $("#hatList");
  console.log("hat "+list.val()+" selected");
  //if there is already showing hat, hide it
  if (showingHat != 0) {
    hatsOverlay[showingHat-1].setVisible(false);
  }
  //if user choose to display a hat(not to hide all hats), set the corresponding overlay to visible
  if (list.val() != 0) {
    hatsOverlay[list.val()-1].setVisible(true);
    updateOffset(1,hatsOverlay[list.val()-1].getOffset());
  } else {
    updateOffset(1,sliderDefault);
  }
  showingHat = list.val();
}

function hatChange1(val){
  var list = $("#hatList");
  console.log("hat "+val+" selected");
  //if there is already showing hat, hide it
  if (showingHat != 0) {
    hatsOverlay[showingHat-1].setVisible(false);
  }
  //if user choose to display a hat(not to hide all hats), set the corresponding overlay to visible
  if (val != showingHat) {
    $('#'+'1'+'button'+val).css('outline','blue solid thick');
    hatsOverlay[val-1].setVisible(true);
    updateOffset(1,hatsOverlay[val-1].getOffset());
    showingHat = val;
  } else {
    $('#'+'1'+'button'+val).css('outline','0');
    updateOffset(1,sliderDefault);
    showingHat = 0;
  }
  
}


function glassChange() {
  var list = $("#glassesList");
  console.log("glasses "+list.val()+" selected");
  if (showingGlasses != 0) {
    glassesOverlay[showingGlasses-1].setVisible(false);
  }
  if (list.val() != 0) {
    glassesOverlay[list.val()-1].setVisible(true);
    updateOffset(2,glassesOverlay[list.val()-1].getOffset());
  } else {
    updateOffset(2,sliderDefault);
  }
  showingGlasses = list.val();
}

function glassChange1(val) {
  console.log("glasses "+val+" selected");
  if (showingGlasses != 0) {
    glassesOverlay[showingGlasses-1].setVisible(false);
  }
  if (val != showingGlasses) {
    $('#'+'2'+'button'+val).css('outline','blue solid thick');
    glassesOverlay[val-1].setVisible(true);
    updateOffset(2,glassesOverlay[val-1].getOffset());
    showingGlasses = val;
  } else {
    $('#'+'2'+'button'+val).css('outline','0');
    updateOffset(2,sliderDefault);
    showingGlasses = 0;
  }
  
}

function hpChange() {
  var list = $("#hpList");
  console.log("headphone "+list.val()+" selected");
  if (showingHP != 0) {
    hpOverlay[showingHP-1].setVisible(false);
  }
  if (list.value != 0) {
    hpOverlay[list.val()-1].setVisible(true);
    updateOffset(3,hpOverlay[list.val()-1].getOffset());
  } else {
    updateOffset(3,sliderDefault);
  }
  showingHP = list.val();
}

function hpChange1() {
  console.log("headphone "+list.val()+" selected");
  if (showingHP != 0) {
    hpOverlay[showingHP-1].setVisible(false);
  }
  if (val != 0) {
    $('#'+'3'+'button'+val).css('outline','blue solid thick');
    hpOverlay[list.val()-1].setVisible(true);
    updateOffset(3,hpOverlay[val-1].getOffset());
    showingHP = val;
  } else {
    $('#'+'3'+'button'+val).css('outline','0');
    updateOffset(3,sliderDefault);
    showingHP = 0;
  }
  
}

//init function for the hangout app
function init() {
  gapi.hangout.onApiReady.add(function(eventObj) {

    //Set video canvas properties and show
    vCanvas = gapi.hangout.layout.getVideoCanvas();
    wHeight = $(window).height();
    wWidth = $(window).width();
    var newSize = vCanvas.setHeight(380);
    var cHeight = newSize["height"];
    var cWidth = newSize["width"];
    //center all the things
    vCanvas.setPosition(wWidth/2-(cWidth/2),0);
    $("#loadingMessage").offset({top:cHeight+120,left: wWidth/2-($("#loadingMessage").textWidth()/2)});
    $('.container-outer').offset({top:cHeight+135,left: wWidth/2-($('.container-outer').width()/2)});
    $("#sliders").hide();
    $("#previewSliders").hide();
    //get startData
    var previewData = gapi.hangout.getStartData();
    console.log("Preview Data: "+previewData);
    if (previewData != null) {
      preview = true;
      var previewParam = previewData.split("&"); 
      loadPreview(previewParam[0],previewParam[1]);
    } else {
      getFitlist();
    }
  });
}

window.onresize = function(event) {
    vCanvas = gapi.hangout.layout.getVideoCanvas();
    wHeight = $(window).height();
    wWidth = $(window).width();
    var newSize = vCanvas.setHeight(380);
    var cHeight = newSize["height"];
    var cWidth = newSize["width"];
    vCanvas.setPosition(wWidth/2-(cWidth/2),0);
    $("#loadingMessage").offset({top:$("#loadingMessage").offset().top,left: wWidth/2-($("#loadingMessage").textWidth()/2)});
    $('.container-outer').offset({top:$(".container-outer").offset().top,left: wWidth/2-($('.container-outer').width()/2)});
};

var vCanvas;
var vrfInfo;
var hats = new Array();
var headphones = new Array();
var glasses = new Array();

var wHeight;
var wWidth;

var hatsOverlay = new Array();
var hpOverlay = new Array();
var glassesOverlay = new Array();

var showingHat = 0;
var showingGlasses = 0;
var showingHP = 0;
var previewOverlay;

var sliderDefault = {'x': 0, 'y': 0};

var preview = false;


//overlay settings for different categories
var hatOverlayPreset = {
  'trackingFeature': gapi.hangout.av.effects.FaceTrackingFeature.NOSE_ROOT,
         'scaleWithFace': true,
         'rotateWithFace': true,
         'scale': 1,
         'scaleWithFace' : true,
         'offset' : {'x' : 0, 'y' : -0.58}
}

var glassesOverlayPreset = {
  'trackingFeature': gapi.hangout.av.effects.FaceTrackingFeature.NOSE_ROOT,
         'scaleWithFace': true,
         'rotateWithFace': true,
         'scale': 1,
         'scaleWithFace' : true,
         'offset' : {'x' : 0, 'y' : 0}
}

var hpOverlayPreset = {
  'trackingFeature': gapi.hangout.av.effects.FaceTrackingFeature.NOSE_ROOT,
         'scaleWithFace': true,
         'rotateWithFace': true,
         'scale': 1,
         'scaleWithFace' : true,
         'offset' : {'x' : 0, 'y' : -0.15}
}

var defaultPreset = {
  'trackingFeature': gapi.hangout.av.effects.FaceTrackingFeature.NOSE_ROOT,
         'scaleWithFace': true,
         'rotateWithFace': true,
         'scale': 1,
         'scaleWithFace' : true,
         'offset' : {'x' : 0, 'y' : 0}
}
gadgets.util.registerOnLoadHandler(init);
