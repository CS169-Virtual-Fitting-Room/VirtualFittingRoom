from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
import json

def detail(request, category, product):
	db = dataBaseModel()
	item = db.getDetail(product)
	

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
	