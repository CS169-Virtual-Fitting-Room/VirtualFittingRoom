from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout as google_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from main.dataBaseModel import dataBaseModel
from main.ImageRW import ImageRW
import json

def listProduct(request, category):
    db = dataBaseModel()
    result = db.getProducts(category.lower())
    if (result[1] != dataBaseModel.SUCCESS): # fail to get products
        failData = {'category_name': '', 'image': [], 'item_name' : [], 'price' : []}
        return HttpResponse(json.dumps(failData), content_type='applicatoin/json')
    items = result[0]
    
    # json raw data
    image = []
    item_name = []
    price = []
    
    for item in items:
        item_name.append(item.name)
        price.append(item.price)
        image.append(ImageRW.readImage(item.photo))
        
    data = {'category_name': category, 'image' : image, 'item_name' : item_name, 'price' : price}
    return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')
    
def listCategory(request):
    #a = lineproduct
    return render(request, "main/category_list.html")
    



def item(request):
    return render(request, "main/item.html")
