from django.contrib import admin

# Register your models here.

from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'email', 'eventpoint', 'star', 'coin', 'avatar_url', 'created_at', 'updated_at']
    list_editable = ['name', 'email', 'eventpoint', 'star', 'coin', 'avatar_url']


admin.site.register(UserAccount, UserAccountAdmin)