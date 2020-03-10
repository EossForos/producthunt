from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['icon'] and request.POST['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('https://'):
        else:
            return render(request, 'products/create.html', {'error':'All fields are required.'})
    else:
        return render(request, 'products/create.html')
