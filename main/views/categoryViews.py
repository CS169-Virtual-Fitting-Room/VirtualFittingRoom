from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout as google_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def category_list(request):
    return render("main/client_list.html")
