from django.urls import path
from . import views

urlpatterns = [
  path('paypal-success/', views.paypal_success, name='paypal_success'),
  path('payment/success/', views.payment_success, name='payment_success'),
  path('create-order/', views.create_order_view, name='create_order'),
  path('checkout/<str:order_number>/', views.checkout_view, name='checkout'),
]
