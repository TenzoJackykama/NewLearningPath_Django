from datetime import datetime as dt
from time import strftime
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context

def home_page(request):
    response = "Ciao coco, <br> cuma la va in coo"
    return HttpResponse(response)

def hello_template(request):
    ctx = { "title" : "Hello Template", "lista" : new_func()}
    return render(request, template_name="home.html", context=ctx)

def new_func():
    return [dt.now(), dt.today().strftime('%A')]
