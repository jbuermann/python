from django.shortcuts import render

from .models import *

def index(request):
    return render(request,"blog/home.html",{'hello' : "Howdy Blogger"})

def articles(request):
    p = post.objects.filter(type=1)
    params = [];
    for i in p:
        params.append({'title' : i.title,'url' : i.id})
    return render(request,"blog/articles.html",{'data' : params})