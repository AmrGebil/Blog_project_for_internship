from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username','last_login','data_joined','is_active',)
    list_display_links = ('email','username')
    readonly_fields = ('last_login','data_joined',)
    ordering = ('-data_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account,AccountAdmin)

# admin.site.register(Profile)