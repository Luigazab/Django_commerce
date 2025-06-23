from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import ProductVariant
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def get_cart(request):
  if request.user.is_authenticated:
    cart, created = Cart.objects.get_or_create(user=request.user)
  else:
    session_key = request.session.session_key or request.session.save()
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
  return cart

def cart_view(request):
  cart = get_cart(request)
  items = cart.items.select_related('variant__product').all()
  total = sum(item.variant.product.price * item.quantity for item in items)
  return render(request, 'cart.html', {
    'cart': cart,
    'items': items,
    'total': total,
  })

def add_to_cart(request, variant_id):
  variant = get_object_or_404(ProductVariant, id=variant_id)
  cart = get_cart(request)
  item, created = CartItem.objects.get_or_create(cart=cart, variant=variant)
  if not created:
    item.quantity += 1
  item.save()
  return redirect('cart_view')

def remove_from_cart(request, item_id):
  item = get_object_or_404(CartItem, id=item_id)
  item.delete()
  return redirect('cart_view')

def update_quantity(request, item_id):
  item = get_object_or_404(CartItem, id=item_id)
  if request.method == "POST":
    qty = int(request.POST.get("quantity", 1))
    item.quantity = max(qty, 1)
    item.save()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
      return JsonResponse({
        'success': True,
        'quantity': item.quantity,
        'subtotal': float(item.variant.product.price) * item.quantity,
      })
  return redirect('cart_view')
