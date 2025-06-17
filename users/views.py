from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login

# Create your views here.
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
    login(request, user)
    return redirect('home')

  return render(request, 'loginsignup.html')

def profile(request):
  return render(request, 'profile.html')

def orders(request):
  return render(request, 'orders.html')