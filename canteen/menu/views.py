from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Item
from food_cart.forms import CartAddProductForm
from food_cart.cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here
@login_required(login_url='main_home')
def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = Item.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'items': items
    }
    return render(request, 'menu/list.html', context)

@login_required(login_url='main_home')
def item_detail(request, id, slug):
    q=0
    item = get_object_or_404(Item, id=id, slug=slug, available=True)
    cart = Cart(request)
    for i in cart:
        if i['product']==item:
            q=i['quantity']
            break
    cart_product_form=CartAddProductForm(initial={'quantity':q})
    return render(request, 'menu/detail.html', {'item': item,'cart_product_form':cart_product_form})
