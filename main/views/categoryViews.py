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
    pageOption= int(request.GET.get("pageOption"))
    pageNum = int(request.GET.get("page"))
    print "pageOption is ", pageOption
    print "pageNum is", pageNum
    id = []
    image = []
    item_name = []
    price = []
    result = db.getProducts(category.lower())
    if (result[1] != dataBaseModel.SUCCESS): # fail to get products
        failData = {'category_name': '', 'image': [], 'item_name' : [], 'price' : []}
        return HttpResponse(json.dumps(failData), content_type='application/json')
    else:
        items = result[0]
        if pageOption != 0:
            productNum = len(items)
            print "productNum is ",productNum
            endValue = pageNum * productNum / pageOption
        i = 0
        for item in items:
            if pageOption == 0 or  ( (pageNum -1)*pageOption <= i < (pageNum-1) * pageOption + pageOption ) :
                id.append(item.pk)
                item_name.append(item.name)
                price.append(item.price)
                image.append(static("products/" + item.photo))
            i = i + 1
        if pageOption == 0:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page':1}
        elif productNum % pageOption == 0:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page': productNum / pageOption}
        else:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page':  productNum / pageOption + 1}
        print "data[id] is ",data
        return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')
