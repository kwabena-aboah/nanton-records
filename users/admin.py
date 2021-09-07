from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'is_active', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'image', 'fb_profile',
        'twitter_profile', 'linkedin_profile', 'website',
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

