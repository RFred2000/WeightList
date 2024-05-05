from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from store.models import Item
from store.forms import ItemForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("info:about")
    else:
        form = RegisterForm
    return render(request, "accounts/register.html", {"form": form})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = auth_login(request, user)
            return redirect("info:about")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {"form": form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("info:about")
    
@login_required
def dashboard(request):
    userItems = Item.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', { "itemList": userItems })