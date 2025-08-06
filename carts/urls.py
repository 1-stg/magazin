from django.urls import path
from carts import views


app_name = 'carts'

urlpatterns = [
<<<<<<< HEAD
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
=======
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>/', views.cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
>>>>>>> e1ded3d2c89a029f73d0bda48b593df9743132a2
]
