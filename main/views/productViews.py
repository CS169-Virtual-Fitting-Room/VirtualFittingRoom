from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
#from main.ImageRW import ImageRW
from django.templatetags.static import static
from main.ImageRW import ImageRW
import json
from main.CustomProductForm import CustomProductForm
from django.views.decorators.csrf import csrf_exempt

def detailpage(request, category, product, id):
    return render(request, 'main/detailpage.html')

def addcustomimage(request):
    return render(request, 'main/addcustomimage.html')

def detail(request, category, product, id):
    db = dataBaseModel()
    item = db.getDetail(product, id)
    if item[1] != dataBaseModel.SUCCESS:
        failData = {'image' : '', 'item_name': '', 'price' : -1, 'description' : ''}
        return HttpResponse(json.dumps(failData), content_type='application/json')
    item = item[0]
    image = static("products/" + item.photo)
    data = {'image' : image, 'item_name': item.name, 'price' : item.price, 'description' : item.description}
    
    return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')

@csrf_exempt
def addProduct(request):
    #authenticate
    if (not request.user.is_authenticated()) or request.method != "POST":
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    #delete the item from temp list
    #add the product
      
    db = dataBaseModel()
    temppath = db.removeTempProduct(request.user.id) # try remove temp product
        
    # remove temp image
    if temppath != []:
        for path in temppath:
            ImageRW.removeImage(path, False)
            ImageRW.removeImage(path.replace('.png', '.jpg'), False)
        
    try:
        # helper method to generate random token
        import string
        import random
        def token_generator(size=32, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        filename = token_generator()
        filename += str(request.user.id)
        filename += '.jpg'
        overlayfilename = filename.replace('.jpg', 'ol.jpg')
        imagefilename = ImageRW.writeImage(request.FILES['display'], True, filename) # write image
        ImageRW.writeImage(request.FILES['overlay'], True, overlayfilename) # write image
        #check here
        overlayfilename = ImageRW.convertToTransparent(overlayfilename, True) # convert it to transparent, return the new ol file name
        #check here
        ImageRW.removeImage(overlayfilename.replace('.png', '.jpg'), True)
        form = CustomProductForm(request.POST)
        
        if form.is_valid():
            pcategory = form.cleaned_data['category'].lower()
            pname = form.cleaned_data['itemname']
            pbrand = form.cleaned_data['brand']
            purl = form.cleaned_data['url']
            pprice = float(form.cleaned_data['price'])
            pdescription = form.cleaned_data['description']
            
            if db.addProduct(request.user.id, imagefilename, overlayfilename, pcategory, pbrand, pname, purl, pprice, pdescription) != dataBaseModel.SUCCESS:
                return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_ADD_PRODUCT}), content_type='application/json')
            data = {'errCode' : dataBaseModel.SUCCESS}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            raise Exception("")
    except:
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_ADD_PRODUCT}), content_type='application/json')
@csrf_exempt
def previewProduct(request):
    #authenticate
    if (not request.user.is_authenticated()) or request.method != "POST":
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    #convert image to transparent background, save it to temp folder and let hangout api retrieve it
    try:
        # helper method to generate random token
        import string
        import random
        def token_generator(size=32, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        
        token = token_generator() # generate a random token here
        token += str(request.user.id)
        filename = token +'ol.jpg'

        if ImageRW.writeImage(request.FILES['overlay'], False, filename) == "":
            return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_PREVIEW_PRODUCT}), content_type='application/json')

        overlay = ImageRW.convertToTransparent(filename, False)

        
        
        #now save it to temp table
        db = dataBaseModel()

        db.addTempProduct(request.user.id, token, overlay, request.POST["category"])
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.SUCCESS, 'token' : token}), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_PREVIEW_PRODUCT}), content_type='application/json')
