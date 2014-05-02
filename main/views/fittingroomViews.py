from django.http import HttpResponse
from django.shortcuts import render
from main.dataBaseModel import dataBaseModel
#from main.ImageRW import ImageRW
from django.templatetags.static import static
from main.ImageRW import ImageRW
import json
from main.CustomProductForm import CustomProductForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def setConfig(request, token):
    if not (request.method == 'POST' and 'application/json' in request.META['CONTENT_TYPE'] and request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type = 'application/json')
    
    try:
        db = dataBaseModel()
        content = json.loads(request.body)
        db.setPositionalConfig(token, content['xoffset'], content['yoffset'], content['scale'], content['rotation'])
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.SUCCESS}), content_type = 'application/json')
        
    except:
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_SET_POSITIONAL_CONFIG}), content_type = 'application/json')