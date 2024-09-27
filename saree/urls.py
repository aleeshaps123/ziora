from django.shortcuts import render,redirect
from django.urls import path, include
from . import views
from .views import CustomPasswordResetView, index, products, user_register, user_login,admin_add, adminpage, edit_product, delete_product, add_to_cart, decrease_to_cart, cart, checkout_view
from django.contrib.auth import views as auth_views
from .views import register_seller, seller_dashboard
from django.contrib import admin
from .views import seller_list, delete_seller, edit_seller
from .views import create_purchase_order
from .views import purchase_order_list
from .views import product_comments



urlpatterns = [
    path('',views.index,name='index'),
    path('products/', products, name='products'),
    path('user_login/', views.user_login, name='user_login'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('user_register/',views.user_register,name='user_register'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'), 
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('dec_from_cart/<int:product_id>/', views.decrease_to_cart, name='decrease_quantity'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('admin_add/', views.admin_add, name='admin_add'),
    path('adminpageorder/', views.admin_order_view, name='adminorders'),
    path('order_view/', views.user_order_view, name='user_order'),

    path('adminordersiteam/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('order_list_and_detail/', views.order_list_and_detail, name='order_list_and_detail'),
    path('order_list_and_detail/', views.order_list_and_detail, name='order_list_and_detail'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('order_summary/', views.order_summary_view, name='order_summary'),
    path('search/', views.search, name='search'),
    path('update_status/<int:order_id>/', views.update_status, name='update_status'),
    path('stock',views.stock,name='stock'),
    path('about/', views.about_us, name='about'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    

    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_to_wishlist/<int:product_id>/', views.remove_to_wishlist, name='remove_to_wishlist'),
    path('view_to_wishlist/', views.view_to_wishlist, name='view_to_wishlist'),
    
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
    path('suppliers/edit/<int:supplier_id>/', views.edit_supplier, name='edit_supplier'),
    path('suppliers/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
    path('supplier_login/',views.supplier_login,name='supplier_login'),
    path('supplier_dashboard/',views.supplier_dashboard,name='supplier_dashboard'),


    
    path('register/', register_seller, name='register_seller'),
    path('dashboard/', seller_dashboard, name='seller_dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sellers/', seller_list, name='seller_list'),
    path('sellers/delete/<int:pk>/', delete_seller, name='delete_seller'),
    path('sellers/edit/<int:pk>/', edit_seller, name='edit_seller'),
    path('create_purchase_order/<int:product_id>/', create_purchase_order, name='create_purchase_order'),
    path('purchase_orders/', purchase_order_list, name='purchase_order_list'),
    path('update_purchase_order/<int:order_id>/', views.update_purchase_order, name='update_purchase_order'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('product/<int:product_id>/comments/', product_comments, name='product_comments'),
    path('sentiment/', views.sentiment_analysis, name='sentiment'),
    path('monthly_sales/',views.monthly_sales_report,name='monthly_sales'),
    path('contact/',views.contact,name='contact'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),



]
