from ngopikuy.models import Product
from django.shortcuts import render


def HomePage(request):
    favmenu = Product.objects.filter(tags__name__in=["FAV"])
    context = {'favs':favmenu}
    return render (request, 'index.html',context)

def ContactPage(request):
    context ={}
    return render (request, 'page/contact.html',context)

def AboutPage(request):
    context ={}
    return render (request, 'page/about.html',context)   

