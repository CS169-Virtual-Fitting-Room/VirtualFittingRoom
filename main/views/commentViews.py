from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
import dataBaseModel
import json

@csrf_exempt
def addComment(request):   ## userID, productID, content
	if request.method == 'POST' && request.META['CONTENT_TYPE'] != 'application/json'::
		content = json.loads(request.body)
		dataUser = dataBaseModel()
		response = dataUser.addComment(content['owner'], content['productCommented'], content['content'])
        ##if response[0] == UsersModel.SUCCESS: # success
		outcome = json.dumps({'errCode' : response[0]})
		return HttpResponse(outcome, content_type = 'application/json')


def getComment(request):
	if request.method == 'POST' && request.META['CONTENT_TYPE'] != 'application/json'::
		content = json.loads(request.body)
		dataUser = dataBaseModel()
		response = dataUser.getComment(content['owner'], content['productCommented'])
		commentList = response[0]
		outcome = json.dumps({'commentList':commentList, 'errCode' : response[0]})
		return HttpResponse(outcome, content_type = 'application/json')
	