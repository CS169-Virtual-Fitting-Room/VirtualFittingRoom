from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth import logout as google_logout
#from django.contrib.auth.decorators import login_required
#from django.http import HttpResponseRedirect
from main.dataBaseModel import dataBaseModel
#from main.ImageRW import ImageRW
from django.templatetags.static import static
import json

def category_list(request, category):
    return render(request, 'main/category_list.html', {'category': category.title()})

def listProduct(request, category):
    db = dataBaseModel()
    result = db.getProducts(category.lower())
    if (result[1] != dataBaseModel.SUCCESS): # fail to get products
        failData = {'category_name': '', 'image': [], 'item_name' : [], 'price' : []}
        return HttpResponse(json.dumps(failData), content_type='application/json')
    items = result[0]
    
    # json raw data
    id = []
    image = []
    item_name = []
    price = []
    
    for item in items:
        id.append(item.pk)
        item_name.append(item.name.title())
        price.append(item.price)
        image.append(static("products/" + item.photo))
        
    data = {'category_name': category, 'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
    return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')

