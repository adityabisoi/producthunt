from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone

def home(request):
    products = Products.objects
    return render(request, 'products/home.html',{'products':products})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            products = Products()
            products.title = request.POST['title']
            products.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                products.url = request.POST['url']
            else:
                products.url = 'http://' + request.POST['url']
            products.icon = request.FILES['icon']
            products.image = request.FILES['image']
            products.date = timezone.datetime.now()
            products.hunter = request.user
            products.votes = 1
            products.save()
            return redirect('/products/' + str(products.id))
        else:
            return render(request, 'products/create.html', {'error': 'Please fill all fields'})
    else:
        return render(request, 'products/create.html')

def details(request, products_id):
    product = get_object_or_404(Products, pk = products_id)
    return render(request, 'products/details.html', {'products':product})

@login_required
def upvote(request, products_id):
    if request.method == 'POST':
        products = get_object_or_404(Products, pk = products_id)
        products.votes += 1
        products.save()
        return redirect('/products/' + str(products.id))