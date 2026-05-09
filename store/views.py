from django.shortcuts import render, redirect
from .models import Product, Artisan
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# def home(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})
# -------------------------------------------------------
def home(request):
    products = Product.objects.all()
    slider_products = Product.objects.all()[:3]
    artisans = Artisan.objects.all()

    return render(request, 'index.html', {
        'products': products,
        'slider_products': slider_products,
        'artisans': artisans
    })

def products_page(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# ---------------------------------------------------------------------------

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)  # auto login after register
        return redirect('home')

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')

# ===========================================
# ADD TO CART
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart

    messages.success(request, "Item added to cart successfully!!")
    return redirect(request.META.get('HTTP_REFERER', 'home'))

#  VIEW CART
def cart_page(request):
    cart = request.session.get('cart', {})
    items = []

    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    return render(request, 'cart.html', {'items': items, 'total': total})
# ======================================================================================

# + INCREASE
def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1

    request.session['cart'] = cart
    return redirect('cart')


# - DECREASE
def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] -= 1

        if cart[str(product_id)] <= 0:
            del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')


#  x REMOVE ITEM
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')

#  Product detail page
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

#  buy now option
def buy_now(request, product_id):
    cart = {}
    cart[str(product_id)] = 1
    request.session['cart'] = cart

    return redirect('cart')  # later → checkout page

#  ARTISAN
def artisan_detail(request, artisan_id):
    artisan = Artisan.objects.get(id=artisan_id)

    products = Product.objects.filter(artisan=artisan)

    return render(request, 'artisan_detail.html', {
        'artisan': artisan,
        'products': products
    })