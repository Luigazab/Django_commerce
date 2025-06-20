from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariant

# Create your models here.
class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  session_key = models.CharField(max_length=100, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
  variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
