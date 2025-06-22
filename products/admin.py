from django.contrib import admin
from .models import Category, Product, ProductVariant, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'is_available']
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProductVariant)
admin.site.register(ProductImage)

