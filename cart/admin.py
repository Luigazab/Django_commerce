from django.contrib import admin
from .models import Cart, CartItem
from products.models import ProductVariant, ProductImage
from django.utils.html import format_html

class CartItemInline(admin.TabularInline):
  model = CartItem
  extra = 0
  readonly_fields = ['image_preview', 'variant', 'quantity', 'created_at']
  can_delete = False 

  def created_at(self, obj):
    return obj.cart.created_at
  
  def image_preview(self, obj):
    main_image = obj.variant.product.images.filter(is_main=True).first()
    if main_image:
      return format_html('<img src="{}" style="max-height: 50px;" />', main_image.image.url)
    return "(No image)"
  image_preview.short_description = 'Product Image'
  

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  list_display = [ 'user', 'session_key', 'created_at']
  inlines = [CartItemInline]
