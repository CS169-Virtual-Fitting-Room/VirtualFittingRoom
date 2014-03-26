from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
from main.views.mainViews import index
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def addComment(request, category, product, id):   ## userID, productID, content
	if request.method == 'POST' and 'application/json' in request.META['CONTENT_TYPE'] and request.user.is_authenticated():
		content = json.loads(request.body)
		dbModel = dataBaseModel()
		response = dbModel.addComment(request.user.id, product, id, content['content'], timezone.now())        	
		return HttpResponse(json.dumps({'errCode' : response}), content_type = 'application/json')
	return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_USER}), content_type = 'application/json')


def getComments(request, category, product, id):
	dbModel = dataBaseModel()
	result = dbModel.getComments(product, id)
	if result[1] != dataBaseModel.SUCCESS:
		data = []
		return HttpResponse(json.dumps(data), content_type='application/json')
	data = []
	for comment in result[0]:
		map = {'name' : comment.owner.first_name, 'content' : comment.content, 'time' : str(comment.time)}
		data.append(map)
		
	return HttpResponse(json.dumps(data), content_type='application/json')
	
	
