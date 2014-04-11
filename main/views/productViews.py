from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
#from main.ImageRW import ImageRW
from django.templatetags.static import static
from main.ImageRW import ImageRW
import json

def detailpage(request, category, product, id):
    return render(request, 'main/detailpage.html')

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


def addProduct(request):
    #authenticate
    #delete the item from temp list
    #add the product
    db = dataBaseModel()
    temppath = db.removeTempProduct(request.user.id) # try remove temp product
    
    # remove temp image
    if temppath != "":
        ImageRW.readImage(temppath)
        
    path = ImageRW.writeImage(request.FILES['image']) # write image
    ImageRW.convertToTransparent(path) # convert it to transparent
    db.addProduct()

def previewProduct(request):
    #authenticate
    #convert image to transparent background, save it to temp folder and let hangout api retrieve it
    path = ImageRW.writeImage(request.FILES['image']) # change 'image' later
    ImageRW.convertToTransparent(path)
    #now save it to temp table
    db = dataBaseModel()
    token = "" # generate a random token here
    db.addTempProduct(request.user.id, token)	