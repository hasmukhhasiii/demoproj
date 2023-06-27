from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("todo.html")
    return HttpResponse(template.render())

def index1(request):
    return HttpResponse("helllooo haiiii")
