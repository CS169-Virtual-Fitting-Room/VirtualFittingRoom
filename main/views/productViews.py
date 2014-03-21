from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
#from main.ImageRW import ImageRW
from django.templatetags.static import static
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

# we might want to move to wishlistViews
def addToWishList(request):
	if request.method == 'POST' and request.META['CONTENT_TYPE'] != 'application/json':
		content = json.loads(request.body)
		dataUser = dataBaseModel()
		response = dataUser.addToWishList(content['owner'], content['product'])

        ##if response[0] == UsersModel.SUCCESS: # success
		outcome = json.dumps({'errCode' : response[0]})
		return HttpResponse(outcome, content_type = 'application/json')


def getComment(request):
	if request.method == 'POST' and request.META['CONTENT_TYPE'] != 'application/json':
		content = json.loads(request.body)
		dataUser = dataBaseModel()
		response = dataUser.getComment(content['owner'], content['productCommented'])
		commentList = response[0]
		outcome = json.dumps({'commentList':commentList, 'errCode' : response[0]})
		return HttpResponse(outcome, content_type = 'application/json')
	