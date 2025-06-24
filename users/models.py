from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  address = models.TextField(blank=True)
  phone = models.CharField(max_length=20, blank=True)
  is_subscribed = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class DefaultShippingInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=200)
  phone = models.CharField(max_length=15)
  city = models.CharField(max_length=100)
  postal_code = models.CharField(max_length=20)
  address = models.TextField()

  def __str__(self):
      return f"Shipping Info for {self.user.username}"