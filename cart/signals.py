from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart, CartItem

@receiver(user_logged_in)
def merge_carts(sender, request, user, **kwargs):
  session_key = request.session.session_key
  if not session_key:
    return
  try:
    guest_cart = Cart.objects.get(session_key=session_key, user__isnull=True)
  except Cart.DoesNotExist:
    return
  
  # Get or create user's cart
  user_cart, created = Cart.objects.get_or_create(user=user)
  
  for item in guest_cart.items.all():
    existing = CartItem.objects.filter(cart=user_cart, variant=item.variant).first()
    if existing:
      existing.quantity += item.quantity
      existing.save()
    else:
      item.cart = user_cart
      item.save()
  
  guest_cart.delete()
