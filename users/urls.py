from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import EmailLoginForm
from . import views

urlpatterns =[
  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='loginsignup.html', authentication_form=EmailLoginForm), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]