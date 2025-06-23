from django.contrib import admin
from .models import Category, Product, ProductVariant, ProductImage
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class ProductVariantInline(admin.TabularInline):  # or admin.StackedInline if you prefer
  model = ProductVariant
  extra = 1  
  min_num = 1
  exclude = ['sku']

class ProductImageInline(admin.TabularInline):  # or admin.StackedInline if you prefer
  model = ProductImage
  extra = 1  
  min_num = 1
  readonly_fields = ['image_preview']

  def image_preview(self, obj):
    if obj.image:
      return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
    return "-"
  image_preview.short_description = 'Preview'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'is_available']
  prepopulated_fields = {'slug': ('name',)}
  inlines = [ProductVariantInline, ProductImageInline]

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
  readonly_fields = ['sku']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
  readonly_fields = ['image_preview']

  def image_preview(self, obj):
    if obj.image:
      return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
    return "-"
  image_preview.short_description = 'Preview'