from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
from django.templatetags.static import static
import json


def search_list(request, searchProduct):
    return render(request, 'main/searchResult.html')


def searchProducts(request, searchProduct):
    db = dataBaseModel()
    categoryList = ["hats", "headPhones", "glasses"]
    id = []
    image = []
    item_name = []
    price = []
    print "I have been here"
    for elem in categoryList:
        response = db.getProducts(elem)
        if response[1] == dataBaseModel.SUCCESS :
            for item in response[0]:
                if item.name.lower() in searchProduct.lower():
                    print item.name
                    id.append(item.pk)
                    item_name.append(item.name)
                    price.append(item.price)
                    image.append(static("products/" + item.photo))

    data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
    return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')







# def searchProducts(request, searchProduct):
#     id = []
#     image = []
#     item_name = []
#     price = []
#     db = dataBaseModel()
#     query = db.searchProducts(searchProduct)
#     if (query[1] != dataBaseModel.SUCCESS):
#         failData  = data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
#         return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')
#     else:
#         items = query[0]
#         for item in items:
#             id.append(item.pk)
#             item_name.append(item.name)
#             price.append(item.price)
#             image.append(static("products/" + item.photo))
#         data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
#         return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')






