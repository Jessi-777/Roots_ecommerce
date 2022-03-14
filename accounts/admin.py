from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


class AccountAdmin(UserAdmin):

    ordering = ('-date_joined',)

    readonly_fields = ('date_joined', 'last_login')

    list_display_links = ('email', 'first_name', 'last_name')
    list_display = ('date_joined', 'first_name', 'last_name', 'email', 'is_active', 'username', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)