from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.models import User


def profile_view(request, myid):
    item = User.objects.get(id=myid)
    context = {
        'item':item,
    }
    return render(request, "profile.html", context=context)


def home(request):
    sort_by = request.GET.get('sort', 'default')
    
    if sort_by == 'price_desc':
        items = Product.objects.all().order_by('-price')
    elif sort_by == 'price_asc':
        items = Product.objects.all().order_by('price')
    elif sort_by == 'name_asc':
        items = Product.objects.all().order_by('name')
    elif sort_by == 'name_desc':
        items = Product.objects.all().order_by('-name')
    elif sort_by == 'in_stock':
        items = Product.objects.filter(in_stock=True)
    else:
        items = Product.objects.all()

    query = request.GET.get('q')
    if query:
        items = Product.objects.filter(name__icontains=query)
    else:
        items = Product.objects.all()

    context = {
        'items': items,
        'sort_by': sort_by,
        'query': query,
    }
    return render(request, "home.html", context=context)

def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "detail.html", context=context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../', permanent=True)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




# Create your views here.
