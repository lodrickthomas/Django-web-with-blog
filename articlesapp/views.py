from django.shortcuts import render
from articlesapp.models import Article
from django.http import HttpResponse
# Create your views here.


def articleslist(request):

    articles = Article.objects.all().order_by('date')

    return render(request,'articlesapp/articleslist.html',{'articles':articles})


def articlesdetails(request, slug):
    

    article = Article.objects.get(slug=slug)

    return render(request,'articlesapp/articlesdetails.html',{'article':article})

    