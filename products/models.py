from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(unique=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name
  
class ProductVariant(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
  color = models.CharField(max_length=50)
  size = models.CharField(max_length=10)
  sku = models.CharField(max_length=50, unique=True, blank=True)
  stock = models.PositiveIntegerField()
  is_available = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.product.name}"
  
  def save(self, *args, **kwargs):
    if not self.sku:
      # Start with a base SKU format
      base = f"{self.product.name}-{self.color}-{self.size}"
      base_slug = slugify(base).upper()
      sku_candidate = base_slug

      # Ensure uniqueness by appending random part if needed
      while ProductVariant.objects.filter(sku=sku_candidate).exists():
        suffix = uuid.uuid4().hex[:4].upper()  # short random unique part
        sku_candidate = f"{base_slug}-{suffix}"

      self.sku = sku_candidate

    super().save(*args, **kwargs)

class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to='product_images/')
  alt_text = models.CharField(max_length=255, blank=True)
  is_main = models.BooleanField(default=False)

  def __str__(self):
    return f"Image for {self.product.name}"