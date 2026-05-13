from django.shortcuts import render, redirect
from .models import Product, Artisan
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import ArtisanApplication

from django.contrib.auth.decorators import login_required
from .forms import ProductForm

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Order

# Create your views here.

def home(request):

    products = Product.objects.all()
    slider_products = Product.objects.all()[:6]
    artisans = Artisan.objects.all()

    is_artisan = False

    if request.user.is_authenticated:
        is_artisan = Artisan.objects.filter(
            user=request.user
        ).exists()

    return render(request, 'index.html', {
        'products': products,
        'slider_products': slider_products,
        'artisans': artisans,
        'is_artisan': is_artisan
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

# ------- ARTISAN APPLICATION ------

@login_required
def apply_artisan(request):
    if request.method == 'POST':
        ArtisanApplication.objects.create(
            user=request.user,   # IMPORTANT
            name=request.POST['name'],
            village=request.POST['village'],
            state=request.POST['state'],
            craft=request.POST['craft'],
            story=request.POST['story'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            image=request.FILES['image'],
        )
        messages.success(request, "Application submitted successfully!")
        return redirect('/')
    return render(request, 'apply_artisan.html')


# --------- ARTISAN- DASHBOARD -------------
@login_required
def artisan_dashboard(request):
    artisan = Artisan.objects.get(user=request.user)
    products = Product.objects.filter(artisan=artisan)
    return render(request, 'artisan_dashboard.html', {
        'artisan': artisan,
        'products': products
    })

# -------------- ADD PRODUCT BY ARTISAN ------
@login_required
def add_product(request):
    artisan = Artisan.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            # attach artisan automatically
            product.artisan = artisan
            product.save()
            return redirect('artisan_dashboard')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


# ------------ ADMIN DASHBOARD --------
@staff_member_required
def admin_dashboard(request):
    pending_artisans = ArtisanApplication.objects.filter(
        approved=False,
        rejected=False)
    approved_artisans = Artisan.objects.all()
    rejected_artisans = ArtisanApplication.objects.filter(
        rejected=True)
    approved_products = Product.objects.all()
    return render(request, 'admin_dashboard.html', {
        'pending_artisans': pending_artisans,
        'approved_artisans': approved_artisans,
        'rejected_artisans': rejected_artisans,
        'approved_products': approved_products,
    })


@staff_member_required
def approve_artisan(request, id):

    application = ArtisanApplication.objects.get(id=id)

    Artisan.objects.create(
        user=application.user,
        name=application.name,
        village=application.village,
        craft=application.craft,
        story=application.story,
        image=application.image,
    )

    application.approved = True
    application.save()

    return redirect('admin_dashboard')


@staff_member_required
def reject_artisan(request, id):

    artisan = ArtisanApplication.objects.get(id=id)

    artisan.rejected = True
    artisan.save()

    return redirect('admin_dashboard')


# --------  CART- VIEW TO BUY  ------------
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity
    if request.method == 'POST':
        Order.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            total_amount=total,
        )
        # clear cart after order
        request.session['cart'] = {}
        messages.success(
            request,
            "Order placed successfully!"
        )
        return redirect('/')
    return render(request, 'checkout.html', {
        'total': total
    })

# ----- My Orders --------
from .models import Order

@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })