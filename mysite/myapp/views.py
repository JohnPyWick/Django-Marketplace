from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm,UserRegistrationForm
from django.contrib.auth.views import LogoutView

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/detail.html', {'product': product})

def addProduct(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()
            return redirect('index')

    product_form = ProductForm()
    return render(request, 'myapp/addProduct.html', {'product_form': product_form})

def editProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('index')

    product_form = ProductForm(instance=product)
    return render(request, 'myapp/editProduct.html', {'product_form': product_form, 'product': product})

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'myapp/deleteProduct.html', {'product': product})

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'myapp/dashboard.html',{'products': products})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return redirect('index')
        else:
            print(user_form.errors)
    user_form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'user_form': user_form})

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']