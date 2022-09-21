from ngopikuy.models import Product
from django.shortcuts import render
from .employee import *
from .customer import *
from .blogs import *
from .authentication import *
from django.template import RequestContext


def HomePage(request):
    product = Product.objects.all()
    favmenu = Product.objects.filter(tags__name__in=["FAV"])
    context = {'favs':favmenu, 'product':product}
    return render (request, 'index.html',context)

def ContactPage(request):
    context ={}
    return render (request, 'page/contact.html',context)

def AboutPage(request):
    context ={}
    return render (request, 'page/about.html',context)   

