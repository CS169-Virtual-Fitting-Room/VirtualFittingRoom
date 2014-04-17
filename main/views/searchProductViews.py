from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
from django.templatetags.static import static
import json


def searchProduts(request, searchName):
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
                if item.name in searchName:
                    id.append(item.pk)
                    item_name.append(item.name)
                    price.append(item.price)
                    image.append(static("products/" + item.photo))

    data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
    return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')














