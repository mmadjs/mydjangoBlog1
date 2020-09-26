from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('love programmer very very very very match')
    return render(request,'about.html')

def mjs(request):
    return HttpResponse('me is good boy')

def home(request):
    #return HttpResponse('home')
    return render(request,'Home.html')
