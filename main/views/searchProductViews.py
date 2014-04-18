from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
from django.templatetags.static import static
import json


def search_list(request, searchProduct):
    print request
    return render(request, 'main/searchResult.html')


def searchProducts(request, searchProduct = "ad"):
    print request
    db = dataBaseModel()
    categoryList = ["hats", "headPhones", "glasses"]
    id = []
    image = []
    item_name = []
    price = []
    for elem in categoryList:
        response = db.getProducts(elem)
        if response[1] == dataBaseModel.SUCCESS :
            for item in response[0]:
                if searchProduct.lower() in item.name.lower():
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






