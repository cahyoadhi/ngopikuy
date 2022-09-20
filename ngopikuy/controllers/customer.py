import uuid
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required
from ngopikuy.models import Product, Order, Cart, Profile
import json


@login_required(login_url='login')
def CustomerPage(request):
    if request.method=='POST':
        return redirect('checkout')
    name = request.user
    profile = Profile.objects.get(user=name)
    coffee = Product.objects.filter(tags__name__in=["COFFEE"]).order_by('name')
    blend = Product.objects.filter(tags__name__in=["BLEND"]).order_by('name')
    tea = Product.objects.filter(tags__name__in=["TEA"]).order_by('name')
    chocolate = Product.objects.filter(tags__name__in=["CHOCOLATE"]).order_by('name')
    juice = Product.objects.filter(tags__name__in=["JUICE"]).order_by('name')
    context = {'coffees':coffee, 'blends':blend, 'teas':tea, 'chocolates':chocolate,'juices':juice,'name':name,'profiles':profile}
    return render (request, 'page/customer/customer.html',context)

def ChekcoutPage(request):
    name = request.user
    cart = Cart.objects.filter(user=name)
    if request.method=='POST':
        cart = Cart.objects.filter(user=name)
        total_price = 0
        order_user = []
        for items in cart.all():
            total_price = total_price + items.product.price * items.quantity
            data ={'product': items.product.name,'qty':items.quantity}
            order_user.append(data)
        list_order_json = json.dumps({'user':str(name) ,'order_list':order_user}, default=tuple)

        neworder = Order()
        neworder.user = name
        neworder.customer = request.POST.get('name')
        neworder.address = request.POST.get('address')
        neworder.payment = request.POST.get('payment-method')
        trackno = 'NGPKUY'+str(uuid.uuid4().fields[-1])[:10]
        while Order.objects.filter(tracking_no = trackno) is None:
            trackno = 'NGPKUY'+str(uuid.uuid4().fields[-1])[:10]
        neworder.tracking_no = trackno
        neworder.total_price = int(total_price) 
        neworder.list_order_json = list_order_json
        if neworder.total_price > 0:    
            messages.success(request, "Your order success")
            neworder.save() 
        else:
            pass
        cart.delete()

    total = 0
    for item in cart:
        total = total + item.quantity * item.product.price

    grand_total = '{:20,.2f}'.format(total)
    context = {'cart':cart, 'total':grand_total}
        
    return render (request, 'page/customer/checkout.html', context)