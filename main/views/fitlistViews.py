from main.dataBaseModel import dataBaseModel
from django.http import HttpResponse
import json
from django.templatetags.static import static
from django.shortcuts import redirect
from main.views.mainViews import index
from django.views.decorators.csrf import csrf_exempt


def getFitlist(request):
    if request.user.is_authenticated() == False:
        return HttpResponse(json.dumps([]), content_type='application/json')
    db = dataBaseModel()
    result = db.getFitList(request.user.id)
    data = []
    if result[1] != dataBaseModel.SUCCESS:       
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    for wish in result[0]:
        map = {'item_name': wish.product.name.title(), 
               'overlay' : static('products/' + wish.product.overlay),
               'image' : static('products/' + wish.product.photo), 
               'price' : wish.product.price, 
               'description' : wish.product.description,
               'category' : wish.product.category.name,
               'product_id' : wish.product.pk,
               'xoffset' : wish.product.xoffset,
               'yoffset' : wish.product.yoffset,
               'scale' : wish.product.scale,
               'rotation' : wish.product.rotation}
        data.append(map)
    return HttpResponse(json.dumps(data), content_type='application/json')
        
@csrf_exempt
def addToFitlist(request, category, product, id):
    if not (request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    result = db.addToFitList(request.user.id, product.lower(), id)
    return HttpResponse(json.dumps({'errCode' : result}), content_type='application/json')
    
@csrf_exempt
def removeFromFitlist(request, category, product, id):
    if not (request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    result = db.removeFromFitList(request.user.id, product.lower(), id)
    return HttpResponse(json.dumps({'errCode' : result}), content_type='application/json')

#csrf_exempt
def getPreviewItem(request, token):
    if not (request.user.is_authenticated()):
        print "run"
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    product = db.getTempProduct(request.user.id, token)
    if product[1] != dataBaseModel.SUCCESS:
        return HttpResponse(json.dumps({'errCode' : product[1]}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'errCode' : product[1], 'overlay' : static('temp/' + product[0].overlay), 'category' : product[0].category.name}), content_type='application/json')
