from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout as google_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json

def listProduct(request, category):
    pass
    
def listCategory(request):
    return render(request, "main/category_list.html")
    

def top_menu(request):
    return render(request, "main/top_menu.html")

def item(request):
    return render(request, "main/item.html")
