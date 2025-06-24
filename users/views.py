from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, DefaultShippingInfo
from orders.models import Order
from django.contrib.auth import login
from cart.models import Cart, CartItem


def adopt_guest_cart(request, user):
  session_key = request.session.session_key
  if not session_key:
    return
  try:
    guest_cart = Cart.objects.get(session_key=session_key, user__isnull=True)
  except Cart.DoesNotExist:
    return

  user_cart, _ = Cart.objects.get_or_create(user=user)

  for item in guest_cart.items.all():
    existing = CartItem.objects.filter(cart=user_cart, variant=item.variant).first()
    if existing:
      existing.quantity += item.quantity
      existing.save()
    else:
      item.cart = user_cart
      item.save()

  guest_cart.delete()


def register(request):
  if request.method == 'POST':
    firstname =  request.POST.get('firstname', '').strip()
    lastname =  request.POST.get('lastname', '').strip()
    email =  request.POST.get('email', '').strip()
    phone =  request.POST.get('phone', '').strip()
    password1 =  request.POST.get('password1', '').strip()
    password2 =  request.POST.get('password2', '').strip()
    subs = request.POST.get('email_updates') == 'on'

    if password1 != password2:
      messages.error(request, "Passwords don't match")
      return redirect('register')
    
    if User.objects.filter(username=email).exists():
      messages.error(request, 'Email already registered')
      return redirect('register')
    
    user =User.objects.create_user(username=email, email=email, password=password1)
    user.is_staff = False
    user.is_superuser = False
    user.save()
    userProfile = UserProfile.objects.create(
      user = user,
      firstname=firstname,
      lastname=lastname,
      address='',
      phone=phone,
      is_subscribed=subs,
    )
    userProfile.save()
    adopt_guest_cart(request, user)
    login(request, user)
    return redirect('home')

  return render(request, 'loginsignup.html')

@login_required
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    orders = Order.objects.filter(user=user).order_by('-created_at')
    shipping = DefaultShippingInfo.objects.filter(user=user).first()

    if request.method == 'POST':
        if 'save_profile' in request.POST:
            profile.firstname = request.POST.get('firstname', '')
            profile.lastname = request.POST.get('lastname', '')
            profile.phone = request.POST.get('phone', '')
            profile.address = request.POST.get('address', '')
            profile.is_subscribed = request.POST.get('is_subscribed') == 'on'
            profile.save()
            return redirect('profile')

        elif 'save_shipping' in request.POST:
            if not shipping:
                shipping = DefaultShippingInfo(user=user)
            shipping.full_name = request.POST.get('full_name', '')
            shipping.phone = request.POST.get('shipping_phone', '')
            shipping.city = request.POST.get('city', '')
            shipping.postal_code = request.POST.get('postal_code', '')
            shipping.address = request.POST.get('shipping_address', '')
            shipping.save()
            return redirect('profile')

    return render(request, 'profile.html', {
        'user': user,
        'profile': profile,
        'orders': orders,
        'default_shipping': shipping,
    })

@login_required
def orders(request):
  user = request.user
  orders = Order.objects.filter(user=user).order_by('-created_at')
  return render(request, 'orders.html', {'orders': orders})