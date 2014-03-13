from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout as google_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='/')
def members(request):
    return render(request, 'main/members.html')

def logout(request):
    google_logout(request)
    return HttpResponseRedirect('/')

def mainpage(request):
    return render(request, 'main/mainpage.html')

def top_menu(request):
    return render(request, "main/top_menu.html")