from main.dataBaseModel import dataBaseModel
from django.http import HttpResponse
import json
from django.templatetags.static import static
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from main.ImageRW import ImageRW
from main.CustomProductForm import CustomProductForm
import string
import random

@csrf_exempt
def addProfilePic(request):
    # verify first
    if not (request.method == 'POST' and request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    
    file = request.FILES["profile"]
    token = token_generator()
    token += str(request.user.id)
    profilePicFileName = token + ".jpg"
    
    if ImageRW.writeImage(file, True , profilePicFileName, True) == "":
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_ADD_PROFILE_PIC}), content_type='application/json')
    
    db = dataBaseModel()
    db.addProfilePic(request.user.id, profilePicFileName)
    return HttpResponse(json.dumps({'errCode' : dataBaseModel.SUCCESS, 'token' : token}), content_type='application/json')

def getProfilePic(request):
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    
    url = db.getProfilePic(request.user.id)
    if url != "":
        url = static('profile/' + url)
    return HttpResponse(json.dumps({'image_url' : url}), content_type='application/json')

def getUserInfo(request):
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    user = db.getUserInfo(request.user.id)
    numAdded = db.getNumAdded(request.user.id)
    if user == "":
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_GET_USER_INFO}), content_type='application/json')
    data = {'num_of_custom_products' : numAdded, 'email' : user.email, 'first' : user.first_name, 'last' : user.last_name, 'last_login' : str(user.last_login), 'date_joined': str(user.date_joined)}
    return HttpResponse(json.dumps(data), content_type='application/json')
 
def getCustomItem(request):
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    custom_list = db.getCustomProduct(request.user.id)
    data = []
    for product in custom_list:
        temp = {'category': product.category.name, 'item_name':product.name, 'brand':product.brand ,'price': product.price, 'url': product.url, 'image': static('products/' + product.photo),'description': product.description}
        data.append(temp)
    
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def removeCustomItem(request, id):
    if not (request.user.is_authenticated() and request.method == 'POST'):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    errCode = db.removeCustomProduct(request.user.id, id)
    
    return HttpResponse(json.dumps({'errCode' : errCode}), content_type='application/json')

@csrf_exempt
def editCustomItem(request, id):
    db = dataBaseModel()

    if not (request.user.is_authenticated() and request.method == 'POST' and db.checkIfOwnCustomProduct(request.user.id, id) == True):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')

    temppath = db.removeTempProduct(request.user.id) # try remove temp product
        
    # remove temp image
    if temppath != []:
        for path in temppath:
            ImageRW.removeImage(path, False)
            ImageRW.removeImage(path.replace('.png', '.jpg'), False)
        
    try:
        filename = token_generator()
        filename += str(request.user.id)
        filename += '.jpg'
        overlayfilename = filename.replace('.jpg', 'ol.jpg')
        imagefilename = ImageRW.writeImage(request.FILES['overlay'], True, filename) # write image
        ImageRW.writeImage(request.FILES['overlay'], True, overlayfilename) # write image
        #check here
        overlayfilename = ImageRW.Process(overlayfilename, True, request.POST["category"]) # convert it to transparent, return the new ol file name
        #check here
        ImageRW.removeImage(overlayfilename.replace('.png', '.jpg'), True)
        form = CustomProductForm(request.POST)
        
        if form.is_valid():
            pcategory = form.cleaned_data['category'].lower()
            pname = form.cleaned_data['itemname'].lower()
            pbrand = form.cleaned_data['brand']
            purl = form.cleaned_data['url']
            pprice = float(form.cleaned_data['price'])
            pdescription = form.cleaned_data['description']
            
            if db.editProduct(request.user.id, imagefilename, overlayfilename, pcategory, pbrand, pname, purl, pprice, pdescription, id) != dataBaseModel.SUCCESS:
                return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_EDIT_CUSTOM_PRODUCT}), content_type='application/json')
            data = {'errCode' : dataBaseModel.SUCCESS}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            raise Exception("")
    except:
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_EDIT_CUSTOM_PRODUCT}), content_type='application/json')
        
# helper method to generate random token
def token_generator(size=32, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))