from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid

# Create your models here.
class Order(models.Model):
  STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ('returned', 'Returned'),
    ('refunded', 'Refunded'),
  ]

  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  guest_email = models.EmailField(null=True, blank=True)
  order_number = models.CharField(max_length=30, unique=True, default=uuid.uuid4)
  created_at = models.DateTimeField(auto_now_add=True)
  is_paid = models.BooleanField(default=False)
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  payment_method = models.CharField(max_length=50, blank=True)  # e.g., 'PayPal', 'Stripe'
  payment_id = models.CharField(max_length=100, blank=True)  # Transaction ID from gateway

  def __str__(self):
    return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  quantity = models.PositiveIntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)  # At time of purchase

class ShippingInfo(models.Model):
  order = models.OneToOneField(Order, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=200)
  address = models.TextField()
  phone = models.CharField(max_length=15)
  city = models.CharField(max_length=100)
  postal_code = models.CharField(max_length=20)