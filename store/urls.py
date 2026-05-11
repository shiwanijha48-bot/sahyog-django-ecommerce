# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_page),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('cart/', views.cart_page, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:product_id>/', views.increase_quantity),
    path('decrease/<int:product_id>/', views.decrease_quantity),
    path('remove/<int:product_id>/', views.remove_from_cart),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('artisan/<int:artisan_id>/', views.artisan_detail, name='artisan_detail'),
    path('apply-artisan/', views.apply_artisan, name='apply_artisan'),
    path('artisan-dashboard/', views.artisan_dashboard, name='artisan_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve-artisan/<int:id>/', views.approve_artisan, name='approve_artisan'),
    path('reject-artisan/<int:id>/', views.reject_artisan, name='reject_artisan'),
    path('checkout/', views.checkout, name='checkout'),
]