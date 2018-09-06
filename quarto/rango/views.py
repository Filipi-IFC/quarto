from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<!DOCTYPE html>"
                        "<html>"
                        "<head>rango</head>"
                        "<br></br>"
                        "<a href='/rango/about'>About</a>"
                        "</html>")

def about(request):
    return HttpResponse("<head>aqui e o about</head><a href='/rango/'>rango</a>")