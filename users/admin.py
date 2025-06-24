from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, DefaultShippingInfo

# Inline for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Inline for DefaultShippingInfo
class ShippingInfoInline(admin.StackedInline):
    model = DefaultShippingInfo
    can_delete = False

# Extend the User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline, ShippingInfoInline]

# Unregister and reregister
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
