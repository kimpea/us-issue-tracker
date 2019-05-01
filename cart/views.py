from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.models import Feature
from features.forms import RequestFeatureForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from features.views import feature_detail

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Add a feature upvote to the cart"""
    quantity = 1
    
    feature = get_object_or_404(Feature, id=id)
    feature.save()

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    cart[id] = quantity
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """Removes a feature upvote from the cart page"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))