from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pagesapp/index.html')

def about(request):
    return render(request,'pagesapp/about.html')

def contact(request):
    return render(request,'pagesapp/contact.html')