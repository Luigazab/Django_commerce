from django.contrib import admin
from .models import Order, OrderItem, ShippingInfo

# Inline for Order Items (shown within Order admin)
class OrderItemInline(admin.TabularInline):
  model = OrderItem
  extra = 0
  readonly_fields = ('variant', 'quantity', 'price')
  can_delete = False

# Inline for Shipping Info (1:1 with Order)
class ShippingInfoInline(admin.StackedInline):
  model = ShippingInfo
  extra = 0
  max_num = 1
  can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('order_number', 'user_or_guest', 'status', 'is_paid', 'total_price', 'created_at')
  list_filter = ('status', 'is_paid', 'created_at')
  search_fields = ('order_number', 'user__username', 'guest_email')
  readonly_fields = ('order_number', 'total_price', 'payment_id', 'created_at')
  inlines = [OrderItemInline, ShippingInfoInline]
  date_hierarchy = 'created_at'
  ordering = ('-created_at',)

  def user_or_guest(self, obj):
      return obj.user.username if obj.user else obj.guest_email
  user_or_guest.short_description = "Customer"

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
  list_display = ('order', 'variant', 'quantity', 'price')
  list_filter = ('variant__product',)
  search_fields = ('order__order_number', 'variant__sku')

@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
  list_display = ('order', 'full_name', 'city', 'postal_code', 'phone')
  search_fields = ('order__order_number', 'full_name', 'address', 'city')
  readonly_fields = ('order',)
