from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from cart.utils import adopt_guest_cart

@receiver(user_logged_in)
def transfer_guest_cart(sender, request, user, **kwargs):
  adopt_guest_cart(request, user)