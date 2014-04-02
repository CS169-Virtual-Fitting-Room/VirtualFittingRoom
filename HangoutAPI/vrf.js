//load image resource specified url by the fitlist and create overlays from the resource
function loadOverlay(uri,category) {
    uri = "http://virtualfittingroom.herokuapp.com"+uri;
    console.log("loading overlay image for uri: "+uri);
    resource = gapi.hangout.av.effects.createImageResource(uri);
    resource.onLoad.add( function(event) {
        if ( !event.isLoaded ) {
            console.log('cannot loaded overlay image for uri: '+uri);
        } else {
            console.log('loaded overlay image for uri: '+uri);
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
    $("#hatList").append('<option value='+(i+1)+'>'+hats[i]["item_name"]+'</option>');
  }
  for (var i = 0; i < glasses.length; i++) {
    glassesOverlay.push(loadOverlay(glasses[i]["overlay"],2));
    $("#glassesList").append('<option value='+(i+1)+'>'+glasses[i]["item_name"]+'</option>');
  }
  for (var i = 0; i < headphones.length; i++) {
    hpOverlay.push(loadOverlay(headphones[i]["overlay"],3));
    $("#hpList").append('<option value='+(i+1)+'>'+headphones[i]["item_name"]+'</option>');
  }
  $("#loadingMessage").text("All Accessories Loaded");
  $("#selectors").show();
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
  } else {
    if (showingHP != 0) {
      var offset = hpOverlay[showingHP-1].getOffset();
      if (adjustX) {
        offset['x'] = -parseFloat(value);
      } else {
        offset['y'] = -parseFloat(value);
      }
      hpOverlay[showingHP-1].setOffset(offset);
    }
  }
}

//request for the fitlist
function fitlistRequest(url, suc ,err) {

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
    fitlistRequest("http://virtualfittingroom.herokuapp.com/fitlist/get/", function(data) { return proccessResponse(data); }, function(err) {return displayError(); });
  } catch (err) {
     displayError(); 
  }
}

//Display the error message to notify user when error occur
function displayError() {
  $("#loadingMessage").text("Cannot load accessories");
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
      $("#loadingMessage").text("Accessories loaded");
  }
}

//responses for items selection
$('#hatList').on('change', function() {
  console.log("hat "+this.value+" selected");
  //if there is already showing hat, hide it
  if (showingHat != 0) {
    hatsOverlay[showingHat-1].setVisible(false);
  }
  //if user choose to display a hat(not to hide all hats), set the corresponding overlay to visible
  if (this.value != 0) {
    hatsOverlay[this.value-1].setVisible(true);
    updateOffset(1,hatsOverlay[this.value-1].getOffset());
  } else {
    updateOffset(1,sliderDefault);
  }
  showingHat = this.value;
});

$('#glassesList').on('change', function() {
  console.log("glasses "+this.value+" selected");
  if (showingGlasses != 0) {
    glassesOverlay[showingGlasses-1].setVisible(false);
  }
  if (this.value != 0) {
    glassesOverlay[this.value-1].setVisible(true);
    updateOffset(2,glassesOverlay[this.value-1].getOffset());
  } else {
    updateOffset(2,sliderDefault);
  }
  showingGlasses = this.value;
});

$('#hpList').on('change', function() {
  console.log("headphone "+this.value+" selected");
  if (showingHP != 0) {
    hpOverlay[showingHP-1].setVisible(false);
  }
  if (this.value != 0) {
    hpOverlay[this.value-1].setVisible(true);
    updateOffset(3,hpOverlay[this.value-1].getOffset());
  } else {
    updateOffset(3,sliderDefault);
  }
  showingHP = this.value;
});


//init function for the hangout app
function init() {
  gapi.hangout.onApiReady.add(function(eventObj) {

    //Set video canvas properties and show
    var vCanvas = gapi.hangout.layout.getVideoCanvas();
    var wHeight = $(window).height();
    var wWidth = $(window).width();
    var newSize = vCanvas.setHeight(380);
    var cHeight = newSize["height"];
    var cWidth = newSize["width"];
    //center all the things
    vCanvas.setPosition(wWidth/2-(cWidth/2),0);
    $("#loadingMessage").offset({top:cHeight+20,left: wWidth/2-($("#loadingMessage").textWidth()/2)});
    $("#selectors").offset({top:cHeight+20+20,left: $('#selectors').offset().left});
    $("#selectors").hide();
    $("#sliders").hide();
    //get startData
    var vrfInfo = gapi.hangout.getStartData();
    console.log("startData: "+vrfInfo);

    getFitlist();
  });
}

var vrfInfo;
var hats = new Array();
var headphones = new Array();
var glasses = new Array();

var hatsOverlay = new Array();
var hpOverlay = new Array();
var glassesOverlay = new Array();

var showingHat = 0;
var showingGlasses = 0;
var showingHP = 0;

var sliderDefault = {'x': 0, 'y': 0};


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
gadgets.util.registerOnLoadHandler(init);
