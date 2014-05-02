from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
from django.templatetags.static import static
import json


def search_list(request):
    value = request.GET.get("searchName")
    print value
    return render(request, 'main/searchResult.html', {"searchName" : value} )



def searchProducts(request):
    searchProduct = request.GET.get("searchName")
    searchNum = int(request.GET.get("sth"))
    pageNum = int(request.GET.get("page"))
    print "searchNum is ", searchNum
    print "searchProduct is ",searchProduct
    print "pageNum is", pageNum
    id = []
    image = []
    item_name = []
    price = []
    db = dataBaseModel()
    userId = db.getUserInfo(request.user.id)
    print "userId is ",userId
    if "wishlist" in searchProduct.lower():
        query = db.getWishList(userId)
        print query
    elif "fitlist" in searchProduct.lower():
        query = db.getFitList(userId)
    elif searchProduct.lower() in "hats":
        query = db.getProducts("hats")
    elif searchProduct.lower() in "headphones":
        query = db.getProducts("headphones")
    elif searchProduct.lower() in "glasses":
        query = db.getProducts("glasses")
    else:
        query = db.searchProducts(searchProduct)

    if (query[1] != dataBaseModel.SUCCESS):
        failData  = data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price}
        return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')
    else:
        items = query[0]
        if searchNum != 0:
            productNum = len(items)
            print "productNum is ",productNum
            endValue = pageNum * productNum / searchNum
        i = 0
        for item in items:
            if searchNum == 0 or  ( (pageNum -1)*searchNum <= i < (pageNum-1) * searchNum + searchNum ) :
                id.append(item.pk)
                item_name.append(item.name)
                price.append(item.price)
                image.append(static("products/" + item.photo))
            i = i + 1
        if searchNum == 0:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page':1}
        elif productNum % searchNum == 0:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page': productNum / searchNum}
        else:
            data = {'id': id, 'image' : image, 'item_name' : item_name, 'price' : price, 'page':  productNum / searchNum + 1}

        return HttpResponse(json.dumps(data ,encoding='latin-1'), content_type='application/json')


