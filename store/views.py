from django.shortcuts import render, redirect
from .models import Item, CartItem
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

################
# Item CRUD API
################

def storeFront(request):
    itemList = Item.objects.all()
    return render(request, 'store/main.html', { "itemList": itemList })

def itemDetail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'store/detail.html', { "item": item })

@login_required
def createItem(request):
    if request.method == "POST":
        itemForm = ItemForm(request.POST, request.FILES)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('store:main')
    else:
        itemForm = ItemForm()
    return render(request, 'store/sell.html', {"form": itemForm})

@login_required
def deleteItem(request, item_id):
    Item.objects.filter(pk=item_id).delete()
    return redirect('accounts:dashboard')

@login_required
def updateItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        itemForm = ItemForm(request.POST, request.FILES, instance=item)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('accounts:dashboard')
    else:
        itemForm = ItemForm(instance=item)
    return render(request, 'store/edit.html', {"form": itemForm, "item": item})

#####################
# Cart Item CRUD API
#####################

@login_required
def view_cart(request):
    cartItems = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', { "cartItems": cartItems })

@login_required    
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    user = request.user
    criteria1 = CartItem.objects.filter(item=item)
    criteria2 = criteria1.filter(user=user)
    if criteria2.count() == 0:
        CartItem.objects.create(item=item, user=user, quantity=1)
    return redirect('store:view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    CartItem.objects.filter(pk=cart_item_id).delete()
    return redirect('store:view_cart')