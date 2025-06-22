from django.urls import path
from . import views

urlpatterns =[
  path('', views.home, name='home'),
  path('browse/', views.browse, name='browse'),
  path('new_arrival/', views.newArrival, name='newArrival'),
  path('browse/', views.browse, name='browse'),
  path('about/', views.about, name='about'),
]