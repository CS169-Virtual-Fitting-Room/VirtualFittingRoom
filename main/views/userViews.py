from main.dataBaseModel import dataBaseModel
from django.http import HttpResponse
import json
from django.templatetags.static import static
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from main.ImageRW import ImageRW
import string
import random

@csrf_exempt
def addProfilePic(request):
    # verify first
    if not (request.method == 'POST' and request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    
    file = request.FILES["profile"]
    token = token_generator()
    token += str(request.user.id)
    profilePicFileName = token + ".jpg"
    
    if ImageRW.writeImage(file, True , profilePicFileName, True) == "":
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_UNABLE_TO_ADD_PROFILE_PIC}), content_type='application/json')
    
    db = dataBaseModel()
    db.addProfilePic(request.user.id, profilePicFileName)
    return HttpResponse(json.dumps({'errCode' : dataBaseModel.SUCCESS, 'token' : token}), content_type='application/json')
    
    
# helper method to generate random token
def token_generator(size=32, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))