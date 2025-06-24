from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from products.models import ProductVariant
from cart.models import Cart, CartItem
from .models import Order, OrderItem, ShippingInfo
import json

# Create order from cart

def create_order_view(request):
    cart = get_object_or_404(Cart, user=request.user) if request.user.is_authenticated else get_object_or_404(Cart, session_key=request.session.session_key)
    items = CartItem.objects.filter(cart=cart).select_related('variant__product')
    if not items:
        return redirect('cart_view')

    order = Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        guest_email=None if request.user.is_authenticated else request.session.get('guest_email'),
        total_price=sum(item.variant.product.price * item.quantity for item in items)
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            variant=item.variant,
            quantity=item.quantity,
            price=item.variant.product.price * item.quantity
        )

    return redirect('checkout', order_number=order.order_number)

# Checkout page

def checkout_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    items = order.orderitem_set.select_related('variant__product')
    return render(request, 'checkout.html', {
        'order': order,
        'order_items': items,
    })


def paypal_success(request):
  data = json.loads(request.body)
  order_number = data.get('orderNumber')

  try:
    order = Order.objects.get(order_number=order_number)
    order.is_paid = True
    order.status = 'processing'
    order.payment_method = 'PayPal'
    order.payment_id = data.get('orderID')
    order.save()

    # Save shipping info
    shipping = data.get('shipping', {})
    ShippingInfo.objects.create(
      order=order,
      full_name=shipping.get('full_name'),
      address=shipping.get('address'),
      city=shipping.get('city'),
      postal_code=shipping.get('postal_code'),
      phone=shipping.get('phone'),
    )

    if order.user:
      cart = Cart.objects.filter(user=order.user).first()
    else:
      session_key = request.session.session_key
      cart = Cart.objects.filter(session_key=session_key).first()

    if cart:
      cart.items.all().delete()

    return JsonResponse({'status': 'success'})

  except Order.DoesNotExist:
    return JsonResponse({'status': 'error'}, status=404)

# Payment success redirect

def payment_success(request):
  order_number = request.GET.get('order')
  return render(request, 'payment_success.html', {'order_number': order_number})

