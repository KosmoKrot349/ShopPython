from django.shortcuts import render
from . import models as m
from . import forms as f
import datetime

def Index(request):
    goods = m.Product.objects.all()
    return render(request,'Index.html',{'goods':goods})

def Buy(request,ProductId):
    if request.method == 'POST':
        order  = m.Order()
        order.productId=request.POST.get('productId')
        order.userEmail = request.user.email
        order.status=0
        order.quantity=request.POST.get('selectedQuantity')
        order.date=datetime.datetime.now()
        order.save()

        goods = m.Product.objects.all()
        return render(request, 'Index.html', {'goods': goods})
    else:
        product=m.Product.objects.get(id=ProductId)
        form = f.BuyForm(initial={'productId':product.id})
        return render(request, 'Buy.html', {'product': product, 'form':form})

